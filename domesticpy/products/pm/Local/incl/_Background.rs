
## BACKGROUND
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

bkgImage = resolveOverrides('bkgImage', (None, None))

# if bkgFade not defined, set (1, 1) as default
# so that bkg2 will fade in and fade out
bkgFade  = resolveOverrides('bkgFade', (1, 1))

%>

bkg1, bkg2 = <%-bkgImage%>
fadeIn, fadeOut = <%-bkgFade%>

if bkg1:
    bkg1 = twc.findRsrc("/backgrounds/%s" % (bkg1), 'tif', 1)
    background = TIFF_Image(bkg1)
    background.setTransitionable(0)
    background.setSize(720,480)
    p.addItem(background)

if bkg2:
    ## Some products need a second background to fade in
    bkg2 = twc.findRsrc("/backgrounds/%s" % (bkg2), 'tif', 0)
    background = TIFF_Image(bkg2)
    background.setSize(720,480)
    p.addItem(background)

    bkgFade = EffectSequencer(background)
    p.addItem(bkgFade)

    if fadeIn:
        bkgFade.addEffect(Fader(None, 0, 1, 5), 5)
    else:
        bkgFade.addEffect(NullEffect(None), 5)
    
    if fadeOut:
        bkgFade.addEffect(NullEffect(None), <%-prod.getDuration()%>-10)
        bkgFade.addEffect(Fader(None, 1, 0, 5), 5)
    
