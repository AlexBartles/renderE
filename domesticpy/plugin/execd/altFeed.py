# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: altFeed.py
# Compiled at: 2007-01-12 11:33:37
import domestic, time, os, subprocess, twc.DataStoreInterface, twccommon, twccommon.Log, twc.dsmarshal
ds = twc.DataStoreInterface
dsm = twc.dsmarshal

def init(config):
    global _config
    _config = twccommon.Data()
    _config.__dict__.update(config.__dict__)
    return


def channelChange(channel):
    channelChangeRequest(channel)
    irdIpAddress = dsm.defaultedConfigGet('irdIpAddress')
    if irdIpAddress == None:
        irdIpAddress = '10.100.102.13'
    irdChannelOid = dsm.defaultedConfigGet('irdChannelOid')
    if irdChannelOid == None:
        irdChannelOid = '1.3.6.1.4.1.1166.1.620.3.1.2.0'
    irdChannelList = dsm.defaultedConfigGet('irdChannelList')
    if irdChannelList == None:
        irdChannelList = ['100', '101']
    if channel not in irdChannelList:
        twccommon.Log.error('AltFeed: %s is not a valid channel; ignoring request' % (channel,))
    else:
        cmd = 'nice -20 snmpset -Le -v 2c -c private %s %s i %s' % (irdIpAddress, irdChannelOid, channel)
        time.sleep(6)
        twccommon.Log.debug('AltFeed: Cmd = "%s"' % (cmd,))
        (rc, outlines) = subprocess.getstatusoutput(cmd)
        if rc == 0:
            twccommon.Log.info('AltFeed: Successfully switched IRD channel to %s' % (channel,))
        else:
            twccommon.Log.error('AltFeed: Unable to switch IRD channel. Err: %d, %s!' % (rc, outlines))
        key = 'Config.' + dsm.getConfigVersion() + '.irdLastRequestedChannel'
        dsm.set(key, channel, 0)
        ds.commit()
    return


def channelChangeRequest(channel):
    key = 'Config.' + dsm.getConfigVersion() + '.irdChannelChangeRequest'
    dsm.set(key, channel, 0)
    ds.commit()
    return


def resetChannel(channel='100'):
    irdPresent = dsm.defaultedConfigGet('irdSlave')
    if irdPresent == None or irdPresent == '0':
        twccommon.Log.info('AltFeed: Resetting IRD back to the main feed (%s)' % (channel,))
        channelChange(channel)
    return


