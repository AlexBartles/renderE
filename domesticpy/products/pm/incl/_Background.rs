
## BACKGROUND
<%!
params = prod.getParams()

# if bkgFade not defined, set (5, 5) as default
# so that bkg2 will fade in and fade out
bkgFade = getattr(params, 'bkgFade', (5,5))
%>

bkg1, bkg2 = <%-params.bkgImage%>
fadeIn, fadeOut = <%-bkgFade%>

bkg1 = twc.findRsrc("/backgrounds/%s" % (bkg1), "tif", 1)
background = TIFF_Image(bkg1)
background.setTransitionable(0)
background.setSize(<%-params.layerProps.w%>,<%-params.layerProps.h%>)
p.addItem(background)

if bkg2:
    ## Some products need a second background to fade in
    bkg2 = twc.findRsrc("/backgrounds/%s" % (bkg2), "tif", 1)
    background = TIFF_Image(bkg2)
    background.setSize(<%-params.layerProps.w%>,<%-params.layerProps.h%>)
    p.addItem(background)

    bkgFade = EffectSequencer(background)
    p.addItem(bkgFade)

    if fadeIn:
        bkgFade.addEffect(Fader(None, 0, 1, fadeIn), fadeIn)
    
    if fadeOut:
        bkgFade.addEffect(NullEffect(None), <%-prod.getDuration()%>-(fadeIn+fadeOut))
        bkgFade.addEffect(Fader(None, 1, 0, fadeOut), fadeOut)
    
