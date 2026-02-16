
import os
import config

TWCDIR     = os.environ['TWCDIR']
TWCCLIDIR  = os.environ['TWCCLIDIR']
TWCPERSDIR = os.environ['TWCPERSDIR']

config.set('sleepTime',      0.5)  # seconds
config.set('validDuration', 10)    # seconds
config.set('devTimeout',     1)    # seconds
config.set('dsKey',         'obs.SENSOR')
config.set('devFile',       '/dev/cuaa0')
config.set('appName',       'sensord')
config.set('pidFileName',   TWCPERSDIR + '/data/pid')

