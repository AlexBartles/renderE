# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: dataUtil.py
# Compiled at: 2005-12-01 07:18:53
import twccommon, twcWx.SkyCondMapping as sky, twcWx.TextFcstMapping as txt, twcWx.IncidentTypeMapping as inc
incidentTypeMap = inc.IncidentTypeMapping(1)

def getIncidentType(typeID, mappingFile, default=None):
    result = incidentTypeMap.get(typeID, mappingFile)
    if result == None:
        if default == None:
            result = twccommon.Data(group='', description='')
        else:
            result = default
    return result
    return


skyCondMap = sky.SkyCondMapping(1)

def formatSkyCondition(iconCode, locale='default', default=None):
    result = skyCondMap.get(iconCode, locale)
    if result == None:
        if default == None:
            result = twccommon.Data(iconFile='BlankIcon', textModifier='')
        else:
            result = default
    return result
    return


def skyConditionHasPrecip(iconCode):
    data = skyCondMap.get(iconCode, 'Observation')
    if data.precipitation == None:
        return 0
    return data.precipitation
    return


def getSkyCondGroup(iconCode):
    data = skyCondMap.get(iconCode, 'ExtendedForecast')
    if data.group == None:
        return 0
    return data.group
    return


textFcstMap = txt.TextFcstMapping(1)

def getTextMapping(code, mappingFile, default=None):
    result = textFcstMap.get(code, mappingFile)
    if result == None:
        if default == None:
            result = twccommon.Data(text='')
        else:
            result = default
    return result
    return


