# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: mapping.py
# Compiled at: 2005-12-01 07:18:53
import os.path, twccommon.Log
_refresh = []

def refreshAll():
    for m in _refresh:
        m.refresh()

    return


class Map:

    def __init__(self, refresh=0):
        self._myMaps = {}
        if refresh:
            _refresh.append(self)
        return

    def get(self, key, data):
        m = self._getMap(data)
        result = None
        if m:
            try:
                result = m[key]
            except KeyError:
                pass

        return result
        return

    def _load(self, data):
        return None
        return

    def load(self, data):
        lresult = self._load(data)
        if lresult:
            modTime = os.path.getmtime(lresult[1])
            self._myMaps[data] = (lresult[0], lresult[1], modTime)
            return lresult[0]
        else:
            twccommon.Log.error("Map couldn't load data file %s" % data)
            return None
        return

    def refresh(self):
        for key in self._myMaps:
            try:
                (map, path, modTime) = self._myMaps[key]
                curModTime = os.path.getmtime(path)
                if curModTime != modTime:
                    self.load(key)
            except:
                twccommon.Log.error('Error refreshing data file %s' % path)
                twccommon.Log.logCurrentException()

        return

    def _getMap(self, data):
        try:
            mdata = self._myMaps[data]
            return mdata[0]
        except KeyError:
            return self.load(data)

        return


