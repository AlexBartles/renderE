
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
config.setAppName('receiverdPri')

config.setUDPDatagramTimeout(20);
config.setTimeDriftThreshold(200);  # 200 milli-seconds

config.addPortListener('localPri', '127.0.0.1', 7003)

ipAddr = twc.getStaticValue('receiverdPriIpAddr', '224.1.1.77')
ipPort = twc.getStaticValue('receiverdPriIpPort', 7778)
config.addMulticastPortListener('hostPri', ipAddr, ipPort)


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

