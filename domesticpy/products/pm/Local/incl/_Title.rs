
from domestic import renderTools
from twc.embedded.renderd import renderUtil



# TITLE
<%!
params = prod.getParams()
data = prod.getData()

# Note: name needs to be a string
def resolveOverrides(name, defaultVal):
    try:
        # The product will set data.{name} if it is trying to override params.{name}
        if (hasattr(data, name)):
            retVal = getattr(data, name)
        else: # use what is in params (if found) otherwise use the supplied default
            retVal = getattr(params, name, defaultVal)
        return retVal
    except:
        return defaultVal

text1Color       = resolveOverrides('text1Color', (212, 212, 212, 255))
text2Color       = resolveOverrides('text2Color', (20, 20, 20, 255))
text1ShadowColor = resolveOverrides('text1ShadowColor', (20, 20, 20, 255))
text2ShadowColor = resolveOverrides('text2ShadowColor', (212, 212, 212, 255))
text1BkgColor    = resolveOverrides('text1BkgColor', (0, 0, 0, 0))
text2BkgColor    = resolveOverrides('text2BkgColor', (212, 212, 212, 255))
fadeIn           = resolveOverrides('titleFadeInDuration', 5)
fadeOut          = resolveOverrides('titleFadeOutDuration', 5)

%>


#
# draw me some titles!
#
title = <%-params.productTitle%>
dur = <%-prod.getDuration()%>

titleX = 52
titleY = 479 - 74


#Create the title bar elements
crBev, crTxt = renderTools.createTitleBar(
    title[0],              title[1],
    <%-text1BkgColor%>,    <%-text2BkgColor%>,
    <%-text1Color%>,       <%-text2Color%>,
    <%-text1ShadowColor%>, <%-text2ShadowColor%>)

#First add the title bevel
crBev.setPosition(titleX, titleY)
p.addItem(crBev)

#Now add the title text (and background gradient)
crTxt.setPosition(titleX, titleY)
p.addItem(crTxt)

if ((<%-fadeIn%> > 0) or ( <%-fadeOut%> > 0)):
    renderUtil.fadeInOut(p, crTxt, dur, <%-fadeIn%>, <%-fadeOut%>)


