
import os
import Config

TWCDIR     = os.environ['TWCDIR']
TWCCLIDIR  = os.environ['TWCCLIDIR']
TWCPERSDIR = os.environ['TWCPERSDIR']

Config.setProductDirectory(TWCPERSDIR + '/Products')
Config.setTempDirectory(TWCPERSDIR + '/data/volatile/bullman/rsc')
Config.setChannel('SystemEventChannel')
Config.setRotationSize(3)
Config.setPidFileDirectory(TWCPERSDIR + '/data/pid')
Config.setAppName('bullman')

