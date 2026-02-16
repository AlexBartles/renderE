
import os
import twc
import twc.embedded.renderd.config
from twc.embedded.renderd import *


TWCPERSDIR = os.environ['TWCPERSDIR']
config = twc.embedded.renderd.config.Config()

config.setPidFileDir(TWCPERSDIR + '/data/pid')
config.setAppName('renderd')
config.activateTStormCard(0)
config.activateAsiOutput(0)

# Choose on of the following to set audio/video input port.
# OPTIONS ARE INPUT_LOCAL_NTSC, INPUT_NET_NTSC, INPUT_MPEGSPOOL,
# INPUT_LOCAL_SDI, and INPUT_NET_SDI (Default).
config.setTStormDefaultAVInput(twc.getStaticValue('avInput', INPUT_NET_SDI))

# Choose one of the following to set the analog audio output levels,
# -4, 0, 10, 4. Default is +4dBu
config.setAnalogAudioLevel(twc.getStaticValue('audioLevel', 4))

# Allow/Disable VBI passthrough.  Default is disabled
config.setVBIDisableFlag(twc.getStaticValue('vbiDisable', 0))
