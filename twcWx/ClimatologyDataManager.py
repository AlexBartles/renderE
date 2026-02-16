# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: ClimatologyDataManager.py
# Compiled at: 2005-12-01 07:18:53
import twccommon, twcWx.ClimoMapping as Climo
climo = Climo.ClimoMapping(0)

def getData(location, month, day, default=None):
    result = climo.get((month, day), location)
    if result == None:
        if default == None:
            result = twccommon.Data()
        else:
            result = default
    return result
    return


def processDataFile(interestList):
    """ Interface to store climatological data.
    """
    for location in interestList:
        try:
            climo.load(location)
        except Exception as e:
            twccommon.Log.error("ClimatologyDataManager couldn't load climatology data file %s: %s" % (location, e))

    return

