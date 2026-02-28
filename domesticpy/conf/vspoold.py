
import os
import twc.embedded.renderd.config
from twc.embedded.renderd import *

TWCPERSDIR = os.environ['TWCPERSDIR']
config = twc.embedded.renderd.config.Config()

config.setPidFileDir(TWCPERSDIR + '/data/pid')
config.setAppName('vspoold')
