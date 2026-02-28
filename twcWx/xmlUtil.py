# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: xmlUtil.py
# Compiled at: 2005-12-01 07:18:53
import twccommon, twccommon.Log, xml.sax
OPTIONAL = 0
REQUIRED = 1

class LookupSAXHandler(twccommon.SAXHandler):

    def __init__(self, subHandlerClass):
        self.msghandler = subHandlerClass(self)
        return

    def startRootNode(self, attrs):
        self.msghandler.begin()
        return

    def endRootNode(self):
        self.msghandler.done()
        return

    def dataDictionary(self):
        return self.msghandler.dataDictionary()
        return


class LookupSubHandler(twccommon.SubHandler):

    def __init__(self, container):
        twccommon.SubHandler.__init__(self, container)
        self._dataDict = {}
        return

    def _parseAttributes(self, attrs, elements):
        d = twccommon.Data()
        for (tag, ctype, required) in elements:
            try:
                value = attrs.getValueByQName(tag)
            except Exception as e:
                value = None
                if required:
                    raise e

            if value != None:
                value = ctype(value)
            setattr(d, tag, value)

        return d
        return

    def dataDictionary(self):
        return self._dataDict
        return


def parseXML(path, subHandlerClass):
    f = open(path)
    parser = xml.sax.make_parser()
    handler = LookupSAXHandler(subHandlerClass)
    parser.setContentHandler(handler)
    parser.parse(f)
    f.close()
    return handler.dataDictionary()
    return


