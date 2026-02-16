
<%@'_init.rs'%>

layerProps  = <%-params.layerProps%>
preroll     = <%-params.preroll%>
lnameBack   = layerProps.name + 'Background'
lnameExpire = layerProps.name + 'Expire'
lexpire     = <%-params.layerProps.expire%> 
squeezeBack = <%-getattr(params, "squeezeBack", 0)%>


def createNamedLayer(name, depth, autoDestroy):
    RenderControl.createNamedLayer(
        name, depth, repeat=0, autoDestroy=autoDestroy)
    RenderControl.queueCommand(
        SetNamedLayerViewPortCmd(
            name, layerProps.x, layerProps.y, 
            layerProps.w, layerProps.h, 
            layerProps.sx, layerProps.sy, 
            layerProps.tx, layerProps.ty))


RenderControl.destroyNamedLayer(layerProps.name)
createNamedLayer(layerProps.name, layerProps.depth, 0)
RenderControl.destroyNamedLayer(lnameBack)
createNamedLayer(lnameBack, VIDEO_DEPTH+1, 1)

# Begin Expire Named Layer Logic
# This layer exists to remove the real layer(s) if they are loaded and never run.
RenderControl.destroyNamedLayer(lnameExpire)
createNamedLayer(lnameExpire, layerProps.depth-1, 1)
l = Layer()
p = Page(lexpire)
p.addOnFrameCommand(DestroyNamedLayerCmd(layerProps.name), lexpire -1)
p.addOnFrameCommand(DestroyNamedLayerCmd(lnameBack), lexpire -1)
l.addPage(p)
RenderControl.setLayer(lnameExpire, l)
RenderControl.activateLayer(lnameExpire)
# End Expire Named Layer Logic


# create a layer and page for the local-background
totDur = 0
prodSchedule = <%-params.prodSchedule%>
for rs, dur in prodSchedule:
    totDur += dur 
 
l = Layer()
p = Page(totDur)
l.addPage(p)

# create a second page (1 frame duration) to remove main layer
# this way the main layer won't autodestroy if a product doesn't
# render in time
p1 = Page(1)
p1.addItem(RemoveLayer(0, layerProps.name))
l.addPage(p1)

# put up a black box as a background for duration of local if not in squeeze
# back
#squeezeBack = 1
#if not squeezeBack:
#    gr = Box()
#    gr.setSize(layerProps.w, layerProps.h)
#    r,g,b,a = renderUtil.rgbaConvert(20,20,20)
#    gr.setColor(r,g,b,a)
#    p.addItem(gr)


# go ahead and load 1st product now so it 
# will be ready when run comes 
rs, dur = prodSchedule[0]
RenderControl.loadPresentation(rs)
prerollTotal = dur
fpos = dur - preroll
if dur < preroll:
    fpos = 0

# after preroll frames
# add page command to load each subsequent page 
# at preroll seconds before its time to play
for rs, dur in prodSchedule[1:]:
    pc = LoadPresentation(fpos, rs)
    p.addItem(pc)

    # keep loading products on frame zero until we have exceeded preroll
    if prerollTotal < preroll:
        fpos = 0
    else:
        fpos += dur 

    prerollTotal += dur 
 

p.addOnEndCommand(DestroyNamedLayerCmd(layerProps.name))
RenderControl.setLayer(lnameBack, l)


