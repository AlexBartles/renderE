
import os
import twc
import twc.DataStoreInterface
import twc.MiscCorbaInterface
import twc.embedded.receiverd
import twc.embedded.receiverd.config
import twc.dsmarshal
import twc.InterestList
import twccommon.Log
import domestic 
import domestic.wxdata


TWCPERSDIR = os.environ['TWCPERSDIR']
config = twc.embedded.receiverd.config.Config()

config.setPidFileDir(TWCPERSDIR + '/data/pid')
config.setAppName('receiverd')

config.setUDPDatagramTimeout(20);
config.setTimeDriftThreshold(200);  # 200 milli-seconds

# Begin writing files here as they arrive.  When they have
# completed, move them to their target locations.
config.setTmpDir('/usr/twc/domestic/data/volatile/receiverd');

#NOTE: The sysctl kern.ipc.maxsockbuf is configured for 4096K
# The setsockopt() for SO_RCVBUF gets passed the value specified below
# but really allocates 1 extra cluster for every 8 specified.
# 3640*9/8 = 4095 hence the value of 3640 below gives a 4MB buffer.
config.setRecvSize(3640*1024);

config.addPortListener('local', '127.0.0.1', 7001)

ipAddr = twc.getStaticValue('receiverdIpAddr', '224.1.1.77')
ipPort = twc.getStaticValue('receiverdIpPort', 7777)
config.addMulticastPortListener('host', ipAddr, ipPort)


# This is a bit wierd but necessary to avoid having the
# domestic.wxdata module import twc.embedded.receiverd.
# Doing so would make it where their can be no scripts, etc.
# that use the wxdata module.
domestic.wxdata._setTime = twc.embedded.receiverd.setTime


ns = {}
ns['abortMsg']       = twc.embedded.receiverd.abortMsg
ns['setMsgDesc']     = twc.embedded.receiverd.setMsgDesc
ns['assertValues']   = twc.embedded.receiverd.assertValues
ns['assertInterest'] = twc.embedded.receiverd.assertInterest
ns['setTime']        = twc.embedded.receiverd.setTime

ns['signalEvent']    = twc.MiscCorbaInterface.signalEvent
ns['isInterested']   = twc.InterestList.isInterested

ns['ds']           = twc.DataStoreInterface
ns['dsm']          = twc.dsmarshal
ns['twc']          = twc
ns['wxdata']       = domestic.wxdata
ns['system']       = domestic.wxdata.system

ns['Log']          = twccommon.Log

config.setPyCmdNamespace(ns)

twc.DataStoreInterface.init()

