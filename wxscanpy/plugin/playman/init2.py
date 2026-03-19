# Source Generated with Decompyle++
# File: init.pyc (Python 2.2)

import domestic.HeatSafetyTipManager as domestic
import twcWx.ClimatologyDataManager as twcWx
import twc.dsmarshal as twc
import twccommon.Log as twccommon
dsm = twc.dsmarshal

def init(config):
    global _config
    _config = config
    _setClimIds(dsm.defaultedGet('interestlist.climId', []))
    setHeatSafetyDataFile(_config.heatSafetyDataFile)


def setClimIds(climIds):
    _setClimIds(climIds)


def setHeatSafetyDataFile(fname):
    twccommon.Log.info('using heat-safety-tips data: %s' % (fname,))
    domestic.HeatSafetyTipManager.init(fname)


def uninit():
    pass

_config = None

def _setClimIds(climIds):
    twccommon.Log.info('using climIds: %s' % (str(climIds),))
    twcWx.ClimatologyDataManager.processDataFile(climIds)

