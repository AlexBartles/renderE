# This section displays the map itself or a default map

import os
import string
import twccommon
TWCPERSDIR = os.environ['TWCPERSDIR']

# This SECTION handles "all-things mappable" and stuff!
import os
import os.path
import twccommon.Log
import twc

def buildObsKey(loc):
    key = 'obs.%s' % loc
    return key

def buildFcstKey(type, id, time):
    """Build 'daily', 'hourly', or 'text' fcst keys"""
    key = '%sFcst.%s.%d' % (type, id, time)
    return key

def fileExists(name, extension):

    exists = 0
    filename = name + extension
    exists = os.path.exists(filename)

    if not exists:
       twccommon.Log.error('Required file %s does not exist. Cannot render map product properly!' % (filename,))

    return exists

class mapElement:

    def __init__(self, data):
        self._type = 'unknown'
        self._data = data

        self._positionX = 0
        self._positionY = 0

        self._properties = []
        self._elements   = []
        self._skipDraw   = 0    # This will be set if there are problems creating the object
        self._outline    = 0

    def setProperties(self, props):
        self._properties = props

    def drawElements(self, elems):
        self._elements = elems

    #def skipDraw(self, skip):
    #    self._skipDraw = skip

    #def drawOutline(self, outline):
    #    self._outline = outline

    def process(self):
        for properties,elements in self._data:
            self.setProperties(properties)
            self.drawElements(elements)


class textString(mapElement):

    def __init__(self, data):

        # call parent/base
        mapElement.__init__(self, data)

        self._type = 'textString'


    def setProperties(self, props):
        # Set some defaults
        self._justification = 0
        self._layerMask = 1
        self._skipDraw = 0

        mapElement.setProperties(self, props)

        self._fontName     = props[0]
        self._fontSize     = props[1]
        self._fontColor    = props[2]
        self._fontShadow   = props[3]
        self._fontTracking = props[4]

        if(len(props) > 5):
            self._justification = props[5]

        if(len(props) > 6):
            self._fontOutlineColor = props[6]
        else:
            self._fontOutlineColor = None

        if(len(props) > 7):
            self._layerMask = props[7]

        # If the object is not on the current layer
        if not (self._layerMask & drawMask):
            self._skipDraw = 1

        self._fontInstance = None
        self._outlineFontInstance = None

        # If there are some basic problems with the properties (such as the font doesn't exist)
        # then set the _skipDraw flag.

    def my_drawElements(self, elems):

        # now that we have a font set, draw some stuff
        for xx in elems:

            position = xx[0]
            text     = xx[1]

            xPos = position[0]
            yPos = position[1]

            # If we define a color, then we want to draw the filled font.
            if (self._fontColor):
                textString = Text(self._fontInstance, text)
                xOffset    = renderUtil.justifyGR(self._fontInstance.stringWidth(text), 0,
                                                  self._justification)
                textString.setPosition(xPos + xOffset, yPos)

                r,g,b,a = renderUtil.rgbaConvert(self._fontColor[0],
                                                 self._fontColor[1],
                                                 self._fontColor[2],
                                                 self._fontColor[3])
                textString.setColor(r, g, b, a)
                baseObj.addItem(textString)

            # If we define a color, then we want to draw the outline.
            if(self._fontOutlineColor):
                # Now create the outline
                textString = Text(self._outlineFontInstance, text)
                xOffset    = renderUtil.justifyGR(self._outlineFontInstance.stringWidth(text), 0,
                                                  self._justification)
                textString.setPosition(xPos + xOffset, yPos)
                r,g,b,a = renderUtil.rgbaConvert(self._fontOutlineColor[0],
                                                 self._fontOutlineColor[1],
                                                 self._fontOutlineColor[2],
                                                 self._fontOutlineColor[3])
                textString.setColor(r, g, b, a)
                baseObj.addItem(textString)


    def drawElements(self, elems):

        if self._skipDraw:
            return

        mapElement.drawElements(self, elems)

        # sanity check
        fontName = '/rsrc/fonts/%s' % self._fontName
        if not fileExists(fontName, '.ttf'):
            return

        self._fontInstance = TTFont(fontName, self._fontSize, t=self._fontTracking,
                                    shadow=self._fontShadow)

        # If we defined an outline color, then we will need a TTOutlineFont object.
        if(self._fontOutlineColor):
            self._outlineFontInstance = TTOutlineFont(fontName, self._fontSize,
                                                      t=self._fontTracking,
                                                      thickness=1)
        self.my_drawElements(elems)


class vector(mapElement):

    def __init__(self, data):

        # call parent/base
        mapElement.__init__(self, data)

        self._type = 'vector'

        self._lineThickness = 0
        self._lineColor     = ()
        # Set some defaults
        self._layerMask = 1
        self._skipDraw = 0

        # vectors are always placed at the origin
        # as a full screen image
        self._positionX = 0
        self._positionY = 0
        self._sizeX     = 720
        self._sizeY     = 480

    def setProperties(self, props):

        # an 'vector' has a line thickness and a color
        self._lineThickness = props[0]
        self._lineColor     = props[1]
        self._layerMask     = props[2]

    def drawElements(self, elems):

        if self._skipDraw:
            return

        for xx in elems:
            vectorType = xx[0]

            # If this vector is not on the overlay layer (bit 2)
            if not (self._layerMask & drawMask):
                #print 'Overlay Skipping vectorType %s' % vectorType
                continue

            xPos = 0
            yPos = 0

            # show the vector data:
            # for this product, show the state borders, the country/coastline borders,
            # and the interstates

            # build name
            vectorFile = vectorPathPrefix + vectorType

            # sanity check
            if not fileExists(vectorFile, '.vg'):
                continue

            vector = VectorImage(vectorFile, lineThickness=self._lineThickness)
            vector.setSize(self._sizeX,self._sizeY)
            vector.setPosition(self._positionX,self._positionY)

            r,g,b,a = renderUtil.rgbaConvert(self._lineColor[0],
                                             self._lineColor[1],
                                             self._lineColor[2],
                                             self._lineColor[3])
            vector.setColor(r,g,b,a)
            baseObj.addItem(vector)


class tiffImage(mapElement):

    def __init__(self, data):

        # call parent/base
        mapElement.__init__(self, data)

        self._type      = 'tiffImage'
        self._imageName = ''

        # list of graphic renderables
        self.imageList = [ ]

    def getImageSize(self, index):

        size  = None
        image = self.imageList[index]

        if image != None:
            size = image.size()

        return size

    def addGRImage(self, gr):
        self.imageList.append(gr)

    def setProperties(self, props):
        # Set some defaults
        self._justification = 0
        self._layerMask = 1
        self._needsClearing = 0
        self._skipDraw = 0

        # a 'tiffImage' has a name
        self._imageName = props[0]

        imageName = '/rsrc/images/%s' % self._imageName
        # sanity check
        if not fileExists(imageName, '.tif'):
            self._skipDraw = 1

        if(len(props) > 1):
            self._justification = props[1]

        if(len(props) > 2):
            self._layerMask = props[2]

        # If the object is not on the current layer
        if not (self._layerMask & drawMask):
            self._skipDraw = 1

        if(len(props) > 3):
            self._needsClearing = props[3]

    def drawElements(self, elems):

        if self._skipDraw:
            return

        for xx in elems:
            position = xx[0]

            xPos = position[0]
            yPos = position[1]

            if (self._needsClearing):
                imageName = '/rsrc/images/%s.25' % self._imageName
                # sanity check
                if fileExists(imageName, '.tif'):
                    grTiffImage = TIFF_Image(imageName)
                    xOffset = renderUtil.justifyGR(grTiffImage.size()[0], 0,
                                                   self._justification)
                    if (grTiffImage != None):
                        grTiffImage.setPosition(xPos + xOffset, yPos)
                        baseObj.addItem(grTiffImage)
                        baseObj.addItem(grTiffImage)
                        baseObj.addItem(grTiffImage)
                        baseObj.addItem(grTiffImage)

            # Now draw the image
            imageName = '/rsrc/images/%s' % self._imageName
            grTiffImage = TIFF_Image(imageName)
            if (grTiffImage != None):
                xOffset = renderUtil.justifyGR(grTiffImage.size()[0], 0,
                                               self._justification)
                grTiffImage.setPosition(xPos + xOffset, yPos)
                baseObj.addItem(grTiffImage)

                # track these
                self.addGRImage(grTiffImage)
            else:
                self.addGRImage(None) # add placeholder
                #continue

class labeledTiffImage(tiffImage):

    def __init__(self, data):

        # call parent/base
        tiffImage.__init__(self, data)

        self._type         = 'labeledTiffImage'
        self._fontName     = ''
        self._fontSize     = 0
        self._fontColor    = ()
        self._fontShadow   = 1
        self._fontTracking = 1
        self._justification = 0

    def setProperties(self, props):
        tiffImage.setProperties(self, (props[0]))

        # a labeled tiff also has font properties
        self._fontName     = props[1]
        self._fontSize     = props[2]
        self._fontColor    = props[3]
        self._fontShadow   = props[4]
        self._fontTracking = props[5]
        #props[6] justification ignored
        #props[7] outline color ignored
        #props[8] layer mask ignored
        #props[9] erase bit ignored

    def drawElements(self, elems):

        if self._skipDraw:
            return

        # draw the tiff portion of the image
        tiffImage.drawElements(self, elems)

        # sanity check
        fontName = '/rsrc/fonts/%s' % self._fontName
        if not fileExists(fontName, '.ttf'):
            return

        labelFont = TTFont(fontName, self._fontSize, shadow=self._fontShadow,
                           t=self._fontTracking)

        for ii in range(len(elems)):
            xx = elems[ii]

            position = xx[0]

            xBasePos = position[0]
            yBasePos = position[1]
            
            label = xx[1]

            # NOTE: We use the same image for all the elements, so this should
            #       be the same for all elements.
            imageSize   = tiffImage.getImageSize(self, ii)

            # sanity check in case image failed to draw
            if imageSize == None:
                continue

            imageWidth  = imageSize[0]
            imageHeight = imageSize[1]

            labelWidth = labelFont.stringWidth(label)
            # calculate xPos plus a tweak factor of +0
            # Image is off center (to the right) by 1
            labelPosX  = xBasePos + (imageWidth + 1 - labelWidth)/2
            # calculate yPos plus a tweak factor of +3
            labelPosY  = yBasePos + (imageHeight - self._fontSize)/2 + 3
            
            grLabel = Text(labelFont, label)
            grLabel.setPosition(labelPosX, labelPosY)

            r,g,b,a = renderUtil.rgbaConvert(self._fontColor[0],
                                             self._fontColor[1],
                                             self._fontColor[2],
                                             self._fontColor[3])
            grLabel.setColor(r, g, b, a)
            baseObj.addItem(grLabel)


class obsValue(mapElement):

    def __init__(self, data):
        # call parent/base
        mapElement.__init__(self, data)
        
        self._type = 'obsValue'

        # an 'obsValue' has the following properties:
        self._fontName     = ''
        self._fontSize     = 0
        self._fontColor    = ()
        self._fontShadow   = 1
        self._fontTracking = 0
        self._valueType    = ''
        self._justification = 1 # Default to LEFT justification

    def setProperties(self, props):
        mapElement.setProperties(self, props)

        self._fontName     = props[0]
        self._fontSize     = props[1]
        self._fontColor    = props[2]
        self._fontShadow   = props[3]
        self._fontTracking = props[4]
        self._valueType    = props[5]

        if(len(props) > 6):
            self._justification = props[6]

        #props[7] outline color ignored
        #props[8] layer mask ignored
        #props[9] erase bit ignored

    def drawElements(self, elems):
        if self._skipDraw:
            return

        mapElement.drawElements(self, elems)

        # sanity check
        fontName = '/rsrc/fonts/%s' % self._fontName
        if not fileExists(fontName, '.ttf'):
            return

        obsValueFont = TTFont(fontName, self._fontSize, shadow=self._fontShadow,
                              t=self._fontTracking)

        for xx in elems:

            value      = xx[0]
            position   = xx[1]

            xPos = position[0]
            yPos = position[1]

            if value == None:
                continue

            data    = "%d" % int(value)
            grValue = Text(obsValueFont, data)
            xOffset = renderUtil.justifyGR(obsValueFont.stringWidth(data), 0,
                                           self._justification)
            grValue.setPosition(xPos + xOffset, yPos)

            r,g,b,a = renderUtil.rgbaConvert(self._fontColor[0],
                                             self._fontColor[1],
                                             self._fontColor[2],
                                             self._fontColor[3])
            grValue.setColor(r, g, b, a)
            baseObj.addItem(grValue)

class fcstValue(mapElement):

    def __init__(self, data):

        # call parent/base
        mapElement.__init__(self, data)
        
        self._type = 'fcstValue'

        # an 'fcstValue' has the following properties:
        self._fontName     = ''
        self._fontSize     = 0
        self._fontColor    = ()
        self._fontShadow   = 1
        self._fontTracking = 0
        self._valueType    = ''
        self._justification = 1 # Default to LEFT justification

    def setProperties(self, props):
        # Set some defaults
        self._layerMask = 1
        self._skipDraw = 0

        mapElement.setProperties(self, props)

        self._fontName     = props[0]
        self._fontSize     = props[1]
        self._fontColor    = props[2]
        self._fontShadow   = props[3]
        self._fontTracking = props[4]
        self._valueType    = props[5]
        if(len(props) > 6):
            self._justification = props[6]

        #props[7] outline color ignored

        if(len(props) > 8):
            self._layerMask = props[8]

        #props[9] erase bit ignored

        # If the object is not on the current layer
        if not (self._layerMask & drawMask):
            self._skipDraw = 1
    def drawElements(self, elems):

        if self._skipDraw:
            return

        mapElement.drawElements(self, elems)

        # sanity check
        fontName = '/rsrc/fonts/%s' % self._fontName
        if not fileExists(fontName, '.ttf'):
            return

        fcstValueFont = TTFont(fontName, self._fontSize, shadow=self._fontShadow,
                               t=self._fontTracking)

        for xx in elems:
            value      = xx[0]
            position   = xx[1]

            xPos = position[0]
            yPos = position[1]

            if value == None:
                continue

            data    = "%d" % int(value)
            grValue = Text(fcstValueFont, data)
            xOffset = renderUtil.justifyGR(fcstValueFont.stringWidth(data), 0,
                                           self._justification)
            grValue.setPosition(xPos + xOffset, yPos)

            r,g,b,a = renderUtil.rgbaConvert(self._fontColor[0],
                                             self._fontColor[1],
                                             self._fontColor[2],
                                             self._fontColor[3])
            grValue.setColor(r, g, b, a)
            baseObj.addItem(grValue)


class mapIcon(mapElement):

    def __init__(self, data):

        # call parent/base
        mapElement.__init__(self, data)

        self._type = 'icon'
        self._justification = 1
        
    def setProperties(self, props):
        # Set some defaults
        self._layerMask = 1
        self._skipDraw = 0

        if(len(props) > 0):
            # an 'icon' has a justification property
            self._justification = props[0]

        if(len(props) > 1):
            self._layerMask = props[1]

        # If the object is not on the current layer
        if not (self._layerMask & drawMask):
            self._skipDraw = 1

    def drawElements(self, elems):

        if self._skipDraw:
            return

        for xx in elems:
            iconFile = xx[0]
            position = xx[1]

            xPos = position[0]
            yPos = position[1]

            if iconFile == None:
                continue

            # sanity check
            iconName = twc.findRsrc('/icons/map/%s' % iconFile, "mv")
            if not fileExists(iconName, '.mv'):
                continue

            grIcon = Icon(iconName)
            xOffset = renderUtil.justifyGR(grIcon.size()[0], 0,
                                           self._justification)
            grIcon.setPosition(xPos + xOffset,yPos)
            baseObj.addItem(grIcon)


class obsIcon(mapIcon):

    def __init__(self, data):

        # call parent/base
        mapIcon.__init__(self, data)

        self._type = 'obsIcon'

class fcstIcon(mapIcon):

    def __init__(self, data):

        # call parent/base
        mapIcon.__init__(self, data)

        self._type = 'fcstIcon'
        

def buildMapElement(type, value):

    # If we don't have a base map, don't create anything
    if not mapAvailable:
        return None

    elem = None

    # If we have data to display, create the object
    if not noDataAvailable:
        if type == 'textString':
            elem = textString(value)
        elif type == 'tiffImage':
            elem = tiffImage(value)
        elif type == 'labeledTiffImage':
            elem = labeledTiffImage(value)
        elif type == 'obsValue':
            elem = obsValue(value)
        elif type == 'fcstValue':
            elem = fcstValue(value)
        elif type == 'obsIcon':
            elem = obsIcon(value)
        elif type == 'fcstIcon':
            elem = fcstIcon(value)

    # Regardless of available data, draw the vectors
    if type == 'vector':
        elem = vector(value)

    return elem
 

# DO SOME MAP STUFF
#parameters = <%#params.__dict__%>
#resolvedData = <%#data.__dict__%>

#print 'resolvedData=', resolvedData

# THESE ARE LISTED IN DRAW ORDER!!
elementTypes = [ 'vector', 'tiffImage', 'labeledTiffImage', 'obsValue',
                 'fcstValue', 'obsIcon', 'fcstIcon', 'textString',]

#
# handle the MAP display
#

# this is where maps live
mapPath   = TWCPERSDIR + '/data/map.cuts/'

vectorPathPrefix = mapPath + productString + '.'

noDataAvailable = mapData.noDataAvailable

if baseObj == None:
    baseObj = CompositedImage()
    p.addItem(baseObj)

if drawMask == None:
    #print 'Setting drawMask to 1' #DEBUG
    drawMask = 1

# look for elements in draw order and if they exist, process them
for type in elementTypes:
    # look for data for each type
    data = mapData.__dict__.get(type, None)

    # If we were able to get "type" (data != None)
    # and it was not empty (data != [])
    if data :
        item = buildMapElement(type,data)
        if item != None:
            item.process()

