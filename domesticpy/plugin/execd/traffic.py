# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: traffic.py
# Compiled at: 2007-01-12 11:33:37
import domestic, domestic.dataUtil, time, os, twc.DataStoreInterface, twccommon, twccommon.Log, twc.dsmarshal, xml.sax
from functools import cmp_to_key
ds = twc.DataStoreInterface
dsm = twc.dsmarshal
REV = 0
INT_TYPE = 1
FLOAT_TYPE = 2
STRING_TYPE = 3
OPTIONAL = 0
REQUIRED = 1

def convertToInt(name, value):
    try:
        return int(value)
    except Exception as e:
        twccommon.Log.error("integer conversion error: tag '%s' value '%s'" % (name, value))
        raise e

    return


def convertToFloat(name, value):
    try:
        return float(value)
    except Exception as e:
        twccommon.Log.error("float conversion error: tag '%s' value '%s'" % (name, value))
        raise e

    return


def convertToString(name, value):
    try:
        return str(value)
    except Exception as e:
        twccommon.Log.error("string conversion error: tag '%s' value '%s'" % (name, value))
        raise e

    return


def convertAttributesToData(attrs, elementTable):
    d = twccommon.Data()
    for (tag, ctype, required) in elementTable:
        try:
            value = attrs.getValueByQName(tag)
        except Exception as e:
            value = None
            if required:
                msg = "required attribute missing error: tag '%s'" % tag
                twccommon.Log.error(msg)
                e = Exception(msg)
                raise e

        if value != None:
            if ctype == INT_TYPE:
                value = convertToInt(tag, value)
            elif ctype == FLOAT_TYPE:
                value = convertToFloat(tag, value)
            elif ctype == STRING_TYPE:
                value = convertToString(tag, value)
            else:
                msg = "unknown data type error: tag '%s' type %d" % (tag, ctype)
                twccommon.Log.error(msg)
                e = Exception(msg)
                raise e
        setattr(d, tag, value)

    return d
    return


def incidentOrder(lst1, lst2):
    return twccommon.compare(lst1[0], lst2[0])
    return


class TrafficSAXHandler(twccommon.SAXHandler):

    def __init__(self, subHandlerClass):
        self.msghandler = subHandlerClass(self)
        return

    def startRootNode(self, attrs):
        return

    def endRootNode(self):
        self.msghandler.finished()
        return


class IncidentMsgHandler(twccommon.SubHandler):

    def __init__(self, container):
        self.metroId = None
        self.expireTime = None
        self.issueTime = None
        self.records = []
        self.elements = [('incId', INT_TYPE, REQUIRED), ('keyRteId', INT_TYPE, OPTIONAL), ('crit', INT_TYPE, REQUIRED), ('lat', FLOAT_TYPE, REQUIRED), ('long', FLOAT_TYPE, REQUIRED), ('iType', STRING_TYPE, REQUIRED), ('loc', STRING_TYPE, REQUIRED), ('rteName', STRING_TYPE, OPTIONAL), ('dir', STRING_TYPE, OPTIONAL), ('desc', STRING_TYPE, REQUIRED), ('descLocation', STRING_TYPE, REQUIRED), ('descDetails', STRING_TYPE, REQUIRED), ('descComments', STRING_TYPE, OPTIONAL), ('descEstDuration', STRING_TYPE, OPTIONAL), ('descDetour', STRING_TYPE, OPTIONAL), ('descAltRoute', STRING_TYPE, OPTIONAL), ('start', STRING_TYPE, OPTIONAL), ('end', STRING_TYPE, OPTIONAL)]
        twccommon.SubHandler.__init__(self, container)
        return

    def charactersmetroId(self, text):
        self.metroId = str(text)
        return

    def charactersissueTime(self, text):
        self.issueTime = int(text)
        return

    def charactersexpTime(self, text):
        self.expireTime = int(text)
        return

    def startincident(self, attrs):
        try:
            data = convertAttributesToData(attrs, self.elements)
            value = data.start
            if value:
                value = int(value)
            else:
                value = None
            setattr(data, 'start', value)
            value = data.end
            if value:
                value = int(value)
            else:
                value = None
            setattr(data, 'end', value)
            self.records.append((data.incId, 0, data))
        except Exception as e:
            twccommon.Log.error("Exception '%s'" % e)
            msg = 'conversion error discarding incident record: ('
            names = attrs.getQNames()
            for name in names:
                value = attrs.getValueByQName(name)
                msg += '%s="%s" ' % (name, value)

            msg += ')'
            twccommon.Log.error(msg)

        return

    def endincident(self):
        return

    def finished(self):
        if self.issueTime == None:
            msg = "missing required element 'issueTime'"
            twccommon.Log.error(msg)
            e = Exception(msg)
            raise e
        if self.expireTime == None:
            msg = "missing required element 'expireTime'"
            twccommon.Log.error(msg)
            e = Exception(msg)
            raise e
        if self.metroId == None:
            msg = "missing required element 'metroId'"
            twccommon.Log.error(msg)
            e = Exception(msg)
            raise e
        self.collapseIncidents()
        self.addIncidentsToDataStore()
        ds.commit()
        return

    def collapseIncidents(self):
        count = 0
        newRecords = []
        lastId = None
        record = None
        self.records.sort(key=cmp_to_key(incidentOrder))
        for (incId, cnt, data) in self.records:
            if incId != lastId:
                if lastId != None:
                    newRecords.append(record)
                lastId = incId
                keyRteIds = []
                keyRteIds.append(data.keyRteId)
                data.keyRteIds = keyRteIds
                delattr(data, 'keyRteId')
                rteNames = []
                rteNames.append(data.rteName)
                data.rteNames = rteNames
                delattr(data, 'rteName')
                count += 1
                record = (incId, count, data)
            else:
                routes = record[2].keyRteIds
                routes.append(data.keyRteId)
                record[2].keyRteIds = routes
                names = record[2].rteNames
                names.append(data.rteName)
                record[2].rteNames = names

        if record != None:
            newRecords.append(record)
        self.records = newRecords
        return

    def addIncidentsToDataStore(self):
        global REV
        count = 0
        cnt = 0
        for (incId, count, data) in self.records:
            data.issueTime = self.issueTime
            cnt += 1
            key = 'incident.' + self.metroId + '.' + str(REV) + '.' + str(count)
            dsm.set(key, data, self.expireTime)

        if count != cnt:
            msg = 'logic error - records counts do not match'
            twccommon.Log.error(msg)
            e = Exception(msg)
            raise e
        mstr = twccommon.Data()
        mstr.count = count
        mstr.rev = REV
        key = 'incidents.' + self.metroId
        dsm.set(key, mstr, self.expireTime)
        return


def init(config):
    global _config
    _config = twccommon.Data()
    _config.__dict__.update(config.__dict__)
    return


def parseXML(path, subHandlerClass):
    try:
        f = open(path)
        parser = xml.sax.make_parser()
        handler = TrafficSAXHandler(subHandlerClass)
        parser.setContentHandler(handler)
        parser.parse(f)
        f.close()
    except xml.sax.SAXParseException as e:
        ds.abort()
        eLine = e.getLineNumber()
        eCol = e.getColumnNumber()
        twccommon.Log.error('%s: XML Line %d, CharPosition %d' % (e.getMessage(), e.getLineNumber(), e.getColumnNumber()))
        twccommon.Log.error('XML path=%s' % (path,))
    except Exception as e:
        ds.abort()
        twccommon.Log.error('error processing %s: %s' % (path, str(e)))

    return


def processIncidents(path):
    global REV
    REV += 1
    if REV > 999:
        REV = 1
    twccommon.Log.info('Traffic: processIncidents("%s")' % (path,))
    parseXML(path, IncidentMsgHandler)
    return

