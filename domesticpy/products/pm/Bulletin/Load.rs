 
<%@'_init.rs'%>

# get layer properties
layerProps = <%-params.layerProps%>
lname = layerProps.name

firstLoad = <%-params.firstLoad%>
activate  = <%-params.activate%>
prodSchedule  = <%-params.prodSchedule%>

# is this the first time that the client has called load?
# if so, create the bulletin layer
if firstLoad:
    twccommon.Log.info('creating layer %s (initial one-time create)' % (lname, ))
    RenderControl.createNamedLayer(lname, layerProps.depth, repeat=1)

    # bind the layer to the viewport
    RenderControl.queueCommand(SetNamedLayerViewPortCmd(
        lname, layerProps.x, layerProps.y, 
        layerProps.w, layerProps.h, 
        layerProps.sx, layerProps.sy, 
        layerProps.tx, layerProps.ty))

if activate:
    RenderControl.activateLayer(lname)
    twccommon.Log.info('Layer %s activated!' % (lname))
else:
    RenderControl.deactivateLayer(lname)
    twccommon.Log.info('Layer %s deactivated!' % (lname))

# load the products (according to schedule)
# (in the bulletin case, there's only ONE product -> the bulletin product)
for rs, dur in prodSchedule:
    RenderControl.loadPresentation(rs)

# Okay, hack time - we're going to assume that if we're trying
# to load the Null product, it means that there's no bulletin
# data so just set an empty layer so any currently running
# bulletins are removed. 
firstProduct, duration = prodSchedule[0]
##if firstProduct == "Null":
if len(<%-params.bulletinCrawl%>) == 0:
    l = Layer()
    p = Page(duration)
    l.addPage(p)
    RenderControl.setLayer(lname, l)
