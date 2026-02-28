# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: radar.py
# Compiled at: 2007-01-12 11:33:37
import os, twccommon.Log, string, glob, twc, twc.dsmarshal
dsm = twc.dsmarshal

def init(config):
    global _config
    _config = config
    return


def uninit():
    return


def genSmoothingCommandLine(inputFile, outputFile, miles):
    cmdString = ''
    if miles <= 120:
        radius = 8
        scale = 8
        round = 1.0
        dropShadow = 2
        gaussian = 0
    elif miles >= 121 and miles <= 180:
        radius = 6
        scale = 7
        round = 0.9
        dropShadow = 2
        gaussian = 0
    elif miles >= 181 and miles <= 250:
        radius = 4
        scale = 8
        round = 0.5
        dropShadow = 4
        gaussian = 0
    elif miles >= 251 and miles <= 370:
        radius = 2
        scale = 8
        round = 0.5
        dropShadow = 4
        gaussian = 0
    elif miles > 370:
        radius = 0
        scale = 14
        round = 0.5
        dropShadow = 2
        gaussian = 0
    else:
        radius = 0
        scale = 8
        round = 0.5
        dropShadow = 2
        gaussian = 0
    cmdString += ' -i %s -o %s -r %d -s %d -R %f -d %d -g %d' % (inputFile, outputFile, radius, scale, round, dropShadow, gaussian)
    return cmdString
    return


def process(ftype, loc, iname):
    bname = os.path.splitext(os.path.basename(iname))[0]
    rc = 0
    key = 'interestlist.%s.%s.cuts' % (ftype, loc)
    il = dsm.configGet(key)
    for prod in il:
        mapDataKey = prod + '.MapData'
        attribs = dsm.get(mapDataKey)
        mapName = '%s/%s.map.tif' % (_config.mapRoot, prod)
        dataName = '%s/%s/%s.cuts/%s.%s.data.tif' % (_config.imageRoot, ftype, loc, prod, bname)
        tempName = '%s/%s/%s.cuts/%s.%s.TEMP.tif' % (_config.imageRoot, ftype, loc, prod, bname)
        smoothName = '%s/%s/%s.cuts/%s.%s.SMOOTH.tif' % (_config.imageRoot, ftype, loc, prod, bname)
        finalName = '%s/%s/%s.cuts/%s.%s.tif' % (_config.imageRoot, ftype, loc, prod, bname)
        x = attribs.datacutCoordinate[0]
        y = attribs.datacutCoordinate[1]
        w = attribs.datacutSize[0]
        h = attribs.datacutSize[1]
        fw = attribs.dataFinalSize[0]
        fh = attribs.dataFinalSize[1]
        offsetX = attribs.dataOffset[0]
        offsetY = attribs.dataOffset[1]
        fw = int(fw * 512 / 720)
        fh = int(fh * 512 / 480)
        offsetX = int(offsetX * 512 / 720)
        offsetY = int(offsetY * 512 / 480)
        miles = attribs.mapMilesSize[0]
        if not os.path.exists(mapName):
            err = 'Map cut is not present for %s. Skipping imagecut.' % finalName
            twccommon.Log.warning(err)
            continue
        TWCPERSDIR = os.environ['TWCPERSDIR']
        configFile = TWCPERSDIR + '/conf/imagecut.py'
        smoothingApplication = '/usr/twc/smooth/bin/imageSmooth'
        version = dsm.defaultedConfigGet('version.twc_imagesmooth')
        if version == None:
            twccommon.Log.debug('Could not determine smoothing application version!')
        else:
            twccommon.Log.debug('Smoothing with imageSmooth v%s' % (version,))
        if _config.enableSmoothing:
            scalingAlgorithm = 'fixedPalette'
        else:
            scalingAlgorithm = 'colorAverage'
        cmd = NICE_VALUE
        cmd += _config.imageCutTool
        cmd += ' -i %s -o %s -l%d,%d -w%d -h%d -p%d,%d -S%d,%d                 -m%s -a0,0,0:20,20,20 -r -c %s -f%d,%d' % (iname, dataName, x, y, w, h, offsetX, offsetY, fw, fh, scalingAlgorithm, configFile, 512, 512)
        twccommon.Log.debug('Cutting %s' % cmd)
        rc = os.system(cmd)
        if rc != 0:
            err = 'Image failed to cut for %s.' % dataName
            twccommon.Log.error(err)
            raise RuntimeError(err)
        if _config.enableSmoothing:
            if os.path.exists(smoothingApplication):
                cmd = NICE_VALUE
                cmd += smoothingApplication
                cmd += genSmoothingCommandLine(dataName, smoothName, miles)
                twccommon.Log.debug('Smoothing %s' % cmd)
                rc = os.system(cmd)
                if rc != 0:
                    err = 'Image failed to smooth for %s.' % dataName
                    twccommon.Log.error(err)
                    raise RuntimeError(err)
                cmd = 'mv %s %s' % (smoothName, dataName)
                twccommon.Log.debug('Moving %s' % cmd)
                rc = os.system(cmd)
                if rc != 0:
                    err = 'Image failed to rename from %s to %s.' % (smoothName, dataName)
                    twccommon.Log.error(err)
                    raise RuntimeError(err)
            else:
                err = 'Application [%s] not found.' % smoothingApplication
                twccommon.Log.error(err)
                raise RuntimeError(err)
        else:
            print('_config.enableSmoothing NOT set')
        cmd = NICE_VALUE
        cmd += _config.imageCutTool
        cmd += ' -i %s -o %s -a0,0,0' % (dataName, tempName)
        twccommon.Log.debug('Adjusting %s' % cmd)
        rc = os.system(cmd)
        if rc != 0:
            err = 'Image failed to adjust for %s.' % finalName
            twccommon.Log.error(err)
            raise RuntimeError(err)
        os.unlink(dataName)
        os.rename(tempName, finalName)

    return


NICE_VALUE = 'nice -20 '
_config = None