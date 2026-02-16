# This section displays the map itself or a default map

import os
TWCPERSDIR = os.environ['TWCPERSDIR']

#
# handle the MAP display
#

# Init globals
mapAvailable = 0

# this is where maps live
mapPath   = TWCPERSDIR + '/data/map.cuts/'

mapFile = ''
mapFile += mapPath
mapFile += productString
mapFile += '.map'

if os.path.exists(mapFile + '.tif'):
    m = TIFF_Image(mapFile)
    mapAvailable = 1
else:
    m = TIFF_Image('/rsrc/maps/defaultMap')
    mapAvailable = 0

m.setSize(720,480)
m.setPosition(0,0)
p.addItem(m)
