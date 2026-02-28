# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: ClimoMapping.py
# Compiled at: 2005-12-01 07:18:53
import os, types, twc, twcWx.xmlUtil as xmlUtil, twcWx.mapping as mapping, twccommon, twccommon.Log, nethandler

class ClimoMappingHandler(xmlUtil.LookupSubHandler):

    def __init__(self, container):
        self._elements = [('loc', types.StringType, xmlUtil.REQUIRED), ('year', types.IntType, xmlUtil.REQUIRED), ('month', types.IntType, xmlUtil.REQUIRED), ('day', types.IntType, xmlUtil.REQUIRED), ('avgHigh', types.StringType, xmlUtil.OPTIONAL), ('avgLow', types.StringType, xmlUtil.OPTIONAL), ('recHigh', types.StringType, xmlUtil.OPTIONAL), ('recHighYear', types.StringType, xmlUtil.OPTIONAL), ('recLow', types.StringType, xmlUtil.OPTIONAL), ('recLowYear', types.StringType, xmlUtil.OPTIONAL)]
        xmlUtil.LookupSubHandler.__init__(self, container)
        return

    def startClimoRec(self, attrs):
        data = self._parseAttributes(attrs, self._elements)
        if data != None:
            key = (data.month, data.day)
            data = twc.DefaultedData(data)
            self._dataDict[key] = data
        return


TWCPERSDIR = os.environ['TWCPERSDIR']
filePath = '/usr/twc/data/climatology/'

class ClimoMapping(mapping.Map):

    def __init__(self, refresh=0):
        mapping.Map.__init__(self, refresh)
        return

    def _load(self, data):
        path = filePath + data + '.xml'
        if not os.path.exists(path):
            path = nethandler.requestNetAssetExt(filePath+data, "xml")
        map = xmlUtil.parseXML(path, ClimoMappingHandler)
        if map:
            return (map, path)
        else:
            return None
        return

