# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: TextFcstMapping.py
# Compiled at: 2005-12-01 07:18:53
import types, twcWx.xmlUtil as xmlUtil, twcWx.mapping as mapping, twc, os, nethandler

class TextFcstMappingHandler(xmlUtil.LookupSubHandler):

    def __init__(self, container):
        self._elements = [('key', str, xmlUtil.REQUIRED), ('text', str, xmlUtil.REQUIRED)]
        xmlUtil.LookupSubHandler.__init__(self, container)
        return

    def startrecord(self, attrs):
        data = self._parseAttributes(attrs, self._elements)
        if data != None:
            key = data.key
            delattr(data, 'key')
            data = twc.DefaultedData(data)
            self._dataDict[key] = data
        return


filePath = os.path.join(os.environ["RENDEREMEDIA"], '/mappings/textForecast/')

class TextFcstMapping(mapping.Map):

    def __init__(self, refresh=0):
        mapping.Map.__init__(self, refresh)
        return

    def _load(self, data):
        path = filePath + data + '.xml'
        if not os.path.exists(path):
            path = nethandler.requestNetAssetExt(filePath+data, "xml")
        map = xmlUtil.parseXML(path, TextFcstMappingHandler)
        if map:
            return (map, path)
        else:
            return None
        return


