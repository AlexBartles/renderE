# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: radarSatellite.py
# Compiled at: 2007-01-12 11:33:37
import os, twccommon.Log, string, glob, twc, twc.dsmarshal
dsm = twc.dsmarshal

def init(config):
    global _config
    _config = config
    return


def uninit():
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
        if not os.path.exists(mapName):
            err = 'Map cut is not present for %s. Skipping imagecut.' % finalName
            twccommon.Log.warning(err)
            continue
        cmd = NICE_VALUE
        cmd += _config.imageCutTool
        cmd += ' -M -i %s -o %s -l%d,%d -w%d -h%d -p%d,%d -S%d,%d                 -a0,0,0:20,20,20 -r -f%d,%d' % (iname, dataName, x, y, w, h, offsetX, offsetY, fw, fh, 512, 512)
        twccommon.Log.debug('Cutting %s' % cmd)
        rc = os.system(cmd)
        if rc != 0:
            err = 'Image failed to cut for %s.' % dataName
            twccommon.Log.error(err)
            raise RuntimeError(err)
        os.rename(dataName, finalName)

    return


NICE_VALUE = 'nice -20 '
_config = None
