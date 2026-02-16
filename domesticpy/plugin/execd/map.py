# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: map.py
# Compiled at: 2007-01-12 11:33:37
import os, string, glob, twc, twc.dsmarshal, twc.DataStoreInterface, twccommon.Log, domestic.wxdata
ds = twc.DataStoreInterface
dsm = twc.dsmarshal
MAP_ACTIVE_KEY = 'mapcuts.active'
MAP_PENDING_KEY = 'mapcuts.pending'

def init(config):
    global _config
    _config = config
    mapCutList = []
    activeKey = MAP_ACTIVE_KEY
    try:
        mapActiveList = dsm.get(activeKey)
    except:
        mapActiveList = []

    try:
        mapPendingList = dsm.get(MAP_PENDING_KEY)
    except:
        mapPendingList = []

    if len(mapActiveList) != 0:
        mapCutList.extend(mapActiveList)
        mapActiveList = []
        dsm.set(activeKey, mapActiveList, 0)
        ds.commit()
    if len(mapPendingList) != 0:
        mapCutList.extend(mapPendingList)
    if len(mapCutList) > 0:
        twccommon.Log.info('Processing pending map/vector cuts:')
        for map in mapCutList:
            process(map)

    return


def uninit():
    return


def process(key):
    pendingKey = MAP_PENDING_KEY
    activeKey = MAP_ACTIVE_KEY
    mapPendingList = dsm.get(pendingKey)
    if mapPendingList.count(key):
        mapPendingList.remove(key)
        dsm.set(pendingKey, mapPendingList, 0)
        ds.commit()
    try:
        mapActiveList = dsm.get(activeKey)
    except KeyError:
        mapActiveList = []

    if mapActiveList.count(key) < 1:
        mapActiveList.append(key)
        dsm.set(activeKey, mapActiveList, 0)
        ds.commit()
    tempName = '%s/%s.TEMP.tif' % (_config.mapRoot, key)
    finalName = '%s/%s.map.tif' % (_config.mapRoot, key)
    if os.path.exists(finalName):
        os.unlink(finalName)
    mapDataKey = key + '.MapData'
    try:
        attribs = dsm.get(mapDataKey)
    except:
        twccommon.Log.error("map.process() Key %s doesn't exist in datastore, skipping map cut" % mapDataKey)
        mapActiveList = dsm.get(activeKey)
        mapActiveList.remove(key)
        dsm.set(activeKey, mapActiveList, 0)
        ds.commit()
        mapCutList = dsm.get(pendingKey)
        if len(mapCutList) == 0:
            twccommon.Log.info('COMPLETED Map Cutting.')
        return

    try:
        dataType = _buildKeyTuple(attribs.datacutType)
        oldImages = '%s/%s/%s.cuts/%s.*.tif' % (_config.imageRoot, dataType[0], dataType[1], key)
        images = glob.glob(oldImages)
        oldStatFiles = '%s/%s/%s.cuts/%s.*.stats' % (_config.imageRoot, dataType[0], dataType[1], key)
        files = glob.glob(oldStatFiles)
        deleteList = []
        deleteList.extend(images)
        deleteList.extend(files)
        for file in deleteList:
            os.unlink(file)

    except:
        pass

    try:
        x = attribs.mapcutCoordinate[0]
        y = attribs.mapcutCoordinate[1]
        w = attribs.mapcutSize[0]
        h = attribs.mapcutSize[1]
        fw = attribs.mapFinalSize[0]
        fh = attribs.mapFinalSize[1]
        validMapCoords = 1
    except:
        validMapCoords = 0

    try:
        vectors = attribs.vectors
    except:
        vectors = []

    for vector in vectors:
        keyTuple = _buildKeyTuple(vector)
        type = keyTuple[len(keyTuple) - 2]
        inName = '%s/maps/%s' % (_config.resourceRoot, vector)
        tmpName = '%s/%s.%s.TEMP.vg' % (_config.mapRoot, key, type)
        outName = '%s/%s.%s.vg' % (_config.mapRoot, key, type)
        if validMapCoords and os.path.exists(inName):
            cmd = NICE_VALUE
            cmd += _config.vectorCutTool
            cmd += ' %s %s %d,%d %d %d %d %d' % (inName, tmpName, x, y, w, h, fw, fh)
            twccommon.Log.info('Cutting %s' % cmd)
            rc = os.system(cmd)
            if rc != 0:
                err = 'Vector file(s) failed to cut for %s' % outName
                twccommon.Log.error(err)
                raise RuntimeError, err
            if os.path.exists(outName):
                os.unlink(outName)
            os.rename(tmpName, outName)
        else:
            twccommon.Log.error('Unable to cut vector file %s' % outName)
            if os.path.exists(outName):
                os.unlink(outName)

    if validMapCoords:
        cmd = NICE_VALUE
        cmd += _config.imageCutTool
        cmd += ' -i %s/maps/%s -o %s -l%d,%d -w%d -h%d -f%d,%d' % (_config.resourceRoot, attribs.mapName, tempName, x, y, w, h, fw, fh)
        twccommon.Log.info('Cutting %s' % cmd)
        rc = os.system(cmd)
        if rc != 0:
            err = 'Image file failed to cut for %s' % finalName
            twccommon.Log.error(err)
            raise RuntimeError, err
        os.rename(tempName, finalName)
        twccommon.Log.info('Completed map cut for %s' % finalName)
    else:
        twccommon.Log.error('Unable to complete map cut for %s' % finalName)
    mapActiveList = dsm.get(activeKey)
    mapActiveList.remove(key)
    dsm.set(activeKey, mapActiveList, 0)
    ds.commit()
    mapPendingList = dsm.get(pendingKey)
    if len(mapPendingList) == 0:
        twccommon.Log.info('COMPLETED Map Cutting.')
    elif mapPendingList.count(key):
        twccommon.Log.debug('Another map cut is pending for %s' % key)
        twccommon.Log.debug('mapPendingList = %s' % str(mapPendingList))
    return


RADAR_SMOOTH = '-s'
NICE_VALUE = 'nice -20 '
_config = None

def _buildKeyTuple(eventType):
    return tuple(eventType.split('.'))
    return


return
