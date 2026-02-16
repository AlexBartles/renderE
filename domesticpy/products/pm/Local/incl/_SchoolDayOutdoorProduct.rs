<%!
import twc
import time

data     = prod.getData()
fcstTime = data.fcstTime
labels = []

# figure out whether lablel is for forecast or obs
if fcstTime != None:
    # Must be in format hour am Weekday. The hour uses a different 
    # font than the text so this gets the label in a format usable
    # for RichText
    h     = time.strftime('%I', time.localtime(fcstTime))
    dow   = time.strftime('%A', time.localtime(fcstTime))
    am_pm = time.strftime('%p', time.localtime(fcstTime))

    labels.append(str(int(h)) + ' ')
    labels.append('%s %s' % (am_pm.lower(), dow.title()))
else:
    labels.append('Currently')

%>

<%@'_Background.rs'%>

data     = <%-prod.getData()%>
duration  = <%-prod.getDuration()%>
art       = twc.findRsrc(data.art, 'tif', 0)
validData = data.valid

# Page Constants
leftMargin = 52

# Tombstone coordinates
recBevelY = (479 - 391)
recBevelW = 442
recBevelH = 312
recBevelStartX = -recBevelW
recBevelFinalX = leftMargin
recBevelStartY = recBevelY
recBevelFinalY = recBevelY

# Animation effect timing
flyInDuration = 10
artFadeInDuration = 10

flyOutDuration = 10
artFadeOutDuration = 10
    
# Next add the appropriate (data dependent) background art
if art:
    gr = TIFF_Image(art)
    # right justify the image in the upper right corner as image sizes vary
    w,h = gr.size()
    xpos = renderUtil.justifyGR(w, 720, renderUtil.RIGHT)
    ypos = 480 - h
    gr.setPosition(xpos, ypos)
    p.addItem(gr)
    fade = EffectSequencer(gr)
    fade.addEffect(Fader(None, 0, 1, artFadeInDuration), artFadeInDuration)
    fade.addEffect(NullEffect(None),
                   duration - (artFadeInDuration + artFadeOutDuration))
    fade.addEffect(Fader(None, 1, 0, artFadeOutDuration), artFadeOutDuration)
    p.addItem(fade)
    
# Title needs to be added after the background image above for layering reasons
<%@'_Title.rs'%>

# Add the main bevel and record text
timeLabel  = <%-labels%>
r, g, b, a = renderUtil.rgbaConvert(212, 212, 212, 255)

# For obs, just need Currently label. For fcst, need the time and day label in different fonts
if len(timeLabel) == 1:
    f = TTFont("/rsrc/fonts/Interstate-Bold", 30, t=150)
    strList = [(timeLabel[0], f, (r,g,b,a))]
elif len(timeLabel) == 2:
    timeFont = TTFont("/rsrc/fonts/Interstate-Black", 30, t=150)
    dayFont  = TTFont("/rsrc/fonts/Interstate-Bold", 30, t=150)
    strList = [(timeLabel[0], timeFont, (r,g,b,a)),
               (timeLabel[1], dayFont, (r,g,b,a))]
else:
    strList = None

crRecBevel = renderUtil.getBevelBox(recBevelW, recBevelH)
# place elements - ALL POSITIONS RELATIVE TO COMPOSITE RENDERABLE POSITION
# place time phrase
if strList != None:
    gr = RichText(strList)
    xpos = renderUtil.justifyGR(gr.size()[0], recBevelW, renderUtil.CENTER)
    gr.setPosition(xpos, 366-recBevelY)
    crRecBevel.addItem(gr)

# if we have valid data, place the data on the page otherwise Temporarily Unvavailable
if validData:
    # vars
    elemData   = data.data
    skyCond    = elemData.skyCondition
    iconLookup = data.iconLookup
    temp       = elemData.temp
    windSpeed  = elemData.windSpeed
    windDir    = elemData.windDir
    apTempLabel, apTemp = dataUtil.formatApparentTemp(elemData.windChill, elemData.heatIndex)
    tempIconCR = CompositeRenderable()
    # place temp
    tempW = -20
    if temp != None:
        f = TTFont("/rsrc/fonts/Interstate-Black", 70, t=20)
        gr = Text(f, str(temp))
        tempW = gr.size()[0]
        gr.setPosition(0, 27)
        gr.setColor(r,g,b,a)
        tempIconCR.addItem(gr)
    # place icon and wx text modifier
    if skyCond != None:
        skyCond = wxDataUtil.formatSkyCondition(elemData.skyCondition, iconLookup)
        # place the icon
        gr = Icon(twc.findRsrc("/icons/large/%s" % skyCond.iconFile, "mv"))
        gr.setPosition(tempW+20, 0)
        tempIconCR.addItem(gr)

        # place wx text modifier
        f = TTFont("/rsrc/fonts/Interstate-Bold", 24, t=20, l=18)
        skyTextList = skyCond.textModifier.split('*')
        y = 216-recBevelY
        for skyText in skyTextList:
            gr = Text(f, skyText)
            xpos = renderUtil.justifyGR(gr.size()[0], recBevelW, renderUtil.CENTER)
            gr.setPosition(xpos, y)
            gr.setColor(r,g,b,a)
            crRecBevel.addItem(gr)
            y -= 20

    if skyCond != None or temp != None:
        # position the temp and icon cr
        xPos = renderUtil.justifyGR(tempIconCR.size()[0], recBevelW, renderUtil.CENTER)
        tempIconCR.setPosition(xPos, 234-recBevelY)
        crRecBevel.addItem(tempIconCR)

    labelFont = TTFont("/rsrc/fonts/Interstate-Regular", 24, t=150)
    dataFont  = TTFont("/rsrc/fonts/Interstate-Bold", 38, t=20)
    # place wind direction and speed label and data
    if windSpeed != None and windDir != None:
        wind = dataUtil.formatWindText(windSpeed, windDir)
        gr = Text(labelFont, 'WIND')
        gr.setColor(r,g,b,a)
        gr.setPosition(102-recBevelFinalX, 139-recBevelFinalY)
        crRecBevel.addItem(gr)
        gr = Text(dataFont, wind)
        gr.setColor(r,g,b,a)
        gr.setPosition(297-recBevelFinalX, 139-recBevelFinalY)
        crRecBevel.addItem(gr)

    # place apparent temp data if needed
    if apTempLabel != None:
        gr = Text(labelFont, apTempLabel)
        gr.setColor(r,g,b,a)
        gr.setPosition(102-recBevelFinalX, 101-recBevelFinalY)
        crRecBevel.addItem(gr)
        gr = Text(dataFont, str(apTemp) + '\260')
        gr.setColor(r,g,b,a)
        gr.setPosition(297-recBevelFinalX, 101-recBevelFinalY)
        crRecBevel.addItem(gr)

else:
    r,g,b,a = renderUtil.rgbaConvert(212,212,50,255)
    f = TTFont("/rsrc/fonts/Interstate-Bold", 30, 30)
    gr = Text(f, data.noDataPhrase)
    xpos = renderUtil.justifyGR(gr.size()[0], recBevelW, renderUtil.CENTER)
    gr.setPosition(xpos, 222-recBevelFinalY)
    gr.setColor(r,g,b,a)
    crRecBevel.addItem(gr)

crRecBevel.setPosition(recBevelStartX, recBevelY)
p.addItem(crRecBevel)

# Setup the movement for the record bevel
es = EffectSequencer(crRecBevel)
es.addEffect(Slider(None,
                   (float(recBevelFinalX - recBevelStartX) / flyInDuration),
                    0),
             flyInDuration)
es.addEffect(NullEffect(None),
             duration - (flyInDuration + flyOutDuration))
es.addEffect(Slider(None,
                    -(float(recBevelFinalX - recBevelStartX) / flyOutDuration),
                    0),
             flyOutDuration)
p.addItem(es)
    

