# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: ldl.py
# Compiled at: 2007-01-12 11:33:37
import domestic, time, twccommon, twccommon.Log, twc.MiscCorbaInterface, twc.dsmarshal
from domestic import BulletinInfo
dsm = twc.dsmarshal

def init(config):
    global _activate
    global _config
    _activate = dsm.defaultedGet('sensorState')
    if _activate is not None:
        _activate = int(_activate)
    else:
        _activate = 0
    _config = twccommon.Data()
    _config.duration = 5400
    _config.expiration = 300
    _config.playlistId = 'NationalLDL'
    _config.defaultPlaylistName = 'Ldl.nationalDefaultUp'
    _config.downPlaylistName = 'Ldl.nationalDown'
    _config.__dict__.update(config.__dict__)
    return


def _ldlBulletins():
    counties = dsm.defaultedConfigGet('interestlist.county')
    if counties is not None:
        bulletins = BulletinInfo.loadActiveBulletins(counties)
    else:
        bulletins = {}
    for (key, val) in bulletins.copy().items():
        if val.ldl == 0:
            del bulletins[key]

    return bulletins
    return


def _getPlaylistName(ldlWarningMode):
    _dispMode = {'A': (twc.Data(playlistName='Ldl.nationalDefaultUp')), 'B': (twc.Data(playlistName='Ldl.nationalLongformUp'))}
    dispMode = dsm.defaultedGet('displayMode')
    if _dispMode.has_key(dispMode):
        playListName = _dispMode[dispMode].playlistName
    else:
        playListName = _config.defaultPlaylistName
    if playListName == 'Ldl.nationalDefaultUp':
        (y, m, d, H, M, S, dow, jd, dst) = time.localtime()
        if H >= 5 and H < 10:
            if ldlWarningMode == 0:
                playListName = 'Ldl.nationalMorningUp'
            else:
                playListName = 'Ldl.nationalMorningSevereUp'
    twccommon.Log.info('Playlist.%s chosen' % playListName)
    playlistOverride = dsm.defaultedConfigGet('LdlPlaylistOverride')
    if playlistOverride == 'nationalDbsUp':
        playListName = 'Ldl.%s' % playlistOverride
        _config.duration = 13800
    return playListName
    return

import domesticpy.plugin.playman.playCmd.pm as pcpm
def load(playlistId, playlistName, duration, bulletins):
    tmpLdlWarningMode = _getLdlWarningMode(bulletins)
    eventValue = repr((playlistId, duration, _config.expiration, "[DynamicSchedule('%s')]" % playlistName, twccommon.Data(ldlBulletins=bulletins, ldlWarningMode=tmpLdlWarningMode, nationalLdl=1)))
    #twc.MiscCorbaInterface.signalEvent('SystemEventChannel', 'playman.playCmd.pm.load', eventValue)
    pcpm.load(*eventValue)
    return


def toggleNationalLDL(id, activate, time=0, frame=0):
    global _activate
    id = int(id)
    time = int(time)
    frame = int(frame)
    activate = int(activate)
    if _activate == 0 and activate == 0:
        return
    _activate = activate
    bulletins = _ldlBulletins()
    ldlWarningMode = _getLdlWarningMode(bulletins)
    if activate == 0:
        load(_config.playlistId, _config.downPlaylistName, 1, bulletins)
        return
    playlistName = _getPlaylistName(ldlWarningMode)
    load(_config.playlistId, playlistName, _config.duration, bulletins)
    eventValue = repr((_config.playlistId, time, frame, twccommon.Data(nationalLdl=1)))
    #twc.MiscCorbaInterface.signalEvent('SystemEventChannel', 'playman.playCmd.pm.run', eventValue)
    pcpm.run(*eventValue)
    return


def _getLdlWarningMode(bulletins):
    hurricaneStatement = dsm.defaultedGet('hurricaneStatement')
    ldlWarningMode = 0
    if len(bulletins) > 0:
        ldlWarningMode = 1
    elif hurricaneStatement != None:
        ldlWarningMode = 1
    return ldlWarningMode
    return

