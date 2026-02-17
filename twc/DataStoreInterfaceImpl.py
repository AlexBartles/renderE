# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: DataStoreInterfaceImpl.py
# Compiled at: 2007-01-12 11:17:29
"""
"""
import os
import rendereglobals as rg
import json
import twc

class InterfaceImpl:

    def __init__(self):
        self.data = rg.datastore
        self.sessiondata = {}
        self.sessiondelete = set()
        

    def get(self, keys, cachingEnabled=None):
        (rc, values, notfound) = self.internalGet(keys, cachingEnabled)
        return (rc, values)
        return

    def getAll(self, keys, cachingEnabled=None):
        (rc, values, notfound) = self.internalGet(keys, cachingEnabled)
        values.update(notfound)
        return (rc, values)
        return

    def internalGet(self, keys, cachingEnabled=None):
        """Internal get implementation for get/getAll to use"""
        notfound = {}
        rc = 1
        result = {}
        
        for key in keys:
            if key in self.data:
                res = self.data[key]
                result[key] = res
            else:
                notfound[key] = None

        return (rc, result, notfound)
        return

    def set(self, entries):
        rc = 1
        
        for (key, data, expir) in entries:
            self.sessiondelete.discard(key)
            self.sessiondata[key] = data

        return rc
        return

    def remove(self, keys):
        rc = 1
        for key in keys:
            if key in self.sessiondata:
                del self.sessiondata[key]
                self.sessiondelete.add(key)

        return rc
        return

    def commit(self):
        rc = 1
        
        for key in self.sessiondata:
            self.data[key] = self.sessiondata[key]
        
        datas = json.dumps(self.data, indent=4)
        
        try:
            with open("ds.json", "w") as f:
                f.write(datas)
        except:
            rc = 0

        return rc
        return

    def abort(self):
        rc = 1

        return rc
        return

    def enableCaching(self, cachingEnabled=1):
        self._cachingEnabled = cachingEnabled
        return

    def clearCache(self):
        self._cache = {}
        self._invalid = []
        return

    def _get(self, keys):
        """Perform a straight DataStoreSession.get, i.e. ignore local cache."""

        return self.get(keys)
        return
