# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: InterestList.py
# Compiled at: 2007-01-12 11:17:29
import types, twc.dsmarshal, twccommon.Log
dsm = twc.dsmarshal

def getInterestList(type, updateCache=0):
    global _interestList
    if not updateCache:
        try:
            return _interestList[type]
        except KeyError:
            pass

    try:
        key = 'interestlist.%s' % (type,)
        il = dsm.configGet(key)
        twccommon.Log.info('%s interest list loaded from data-store: %s' % (type, str(il)))
        _interestList[type] = il
        return il
    except KeyError:
        return []

    return


def isInterested(**kw):
    for (key, val) in kw.items():
        if not isInterestedItem(key, val):
            return 0

    return 1
    return


def isInterestedItem(ilType, value):
    if type(value) != types.ListType:
        value = [value]
    il = getInterestList(ilType)
    for val in value:
        if val not in il:
            return 0

    return 1
    return


_interestList = {}
