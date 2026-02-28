
import os
import config

TWCDIR     = os.environ['TWCDIR']
TWCCLIDIR  = os.environ['TWCCLIDIR']
TWCPERSDIR = os.environ['TWCPERSDIR']

config.set('appName',              'execd')
config.set('channel',              'SystemEventChannel')
config.set('pluginRoot',           TWCPERSDIR + '/plugin')
config.set('imageCutTool',         TWCCLIDIR + '/util/imagecut')
config.set('vectorCutTool',        TWCCLIDIR + '/util/vectorcut')
config.set('mapRoot',              TWCPERSDIR + '/data/map.cuts')
config.set('imageRoot',            TWCPERSDIR + '/data/volatile/images')
config.set('resourceRoot',         '/rsrc')
config.set('enableSmoothing',      1)
config.set('pidFileName',          TWCPERSDIR + '/data/pid')

