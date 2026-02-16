
<%@'_init.rs'%>

layerProps  = <%-params.layerProps%>
lname   = layerProps.name
ldepth  = layerProps.depth
nationalLdl = <%-getattr(params, "nationalLdl", 0)%>
bulletinActive = <%-getattr(params, "bulletinActive", 0)%>

# these flags tell you what to do depending on who is calling
# for the TimeTemp -- so they are mutually exclusive. Yes, you
# can have a bulletin playing at the same time as the National
# LDL, but you'll "never" have timeTemp called with BOTH of
# these flags set at the same time.
if nationalLdl:
    ldepth = ldepth - 20
if bulletinActive:
    ldepth = ldepth + 20

lnameDuration  = lname + 'Duration'


<%!
scriptFiles = []
lduration = 0
for fname,dur in params.prodSchedule:
    lduration += dur
    scriptFiles.append(fname)
%>

lduration = <%-lduration%>

if not nationalLdl:
    RenderControl.destroyNamedLayer(lnameDuration)
    RenderControl.createNamedLayer(lnameDuration, ldepth-1, repeat=0, autoDestroy=1)
    l = Layer()
    p = Page(lduration)
    p.addOnEndCommand(DestroyNamedLayerCmd(lname))
    l.addPage(p)
    RenderControl.setLayer(lnameDuration, l)

RenderControl.destroyNamedLayer(lname)
RenderControl.createNamedLayer(lname, ldepth, repeat=1, autoDestroy=1)
RenderControl.queueCommand(SetNamedLayerViewPortCmd(lname,
                                                    layerProps.x,
						    layerProps.y,
						    layerProps.w,
						    layerProps.h,
						    layerProps.sx,
						    layerProps.sy,
						    layerProps.tx,
						    layerProps.ty))

# Begin Expire Named Layer Logic
# This layer exists to remove the real layer(s) if they are loaded and never run.
lnameExpire = lname + 'Expire'
lexpire = layerProps.expire 
RenderControl.destroyNamedLayer(lnameExpire)
RenderControl.createNamedLayer(lnameExpire, ldepth-1, repeat=0, autoDestroy=1)
l = Layer()
p = Page(lexpire)
p.addOnFrameCommand(DestroyNamedLayerCmd(lname), lexpire -1)
if not nationalLdl:
    p.addOnFrameCommand(DestroyNamedLayerCmd(lnameDuration), lexpire -1)
l.addPage(p)
RenderControl.setLayer(lnameExpire, l)
RenderControl.activateLayer(lnameExpire)
# End Expire Named Layer Logic


twccommon.Log.info('loading TimeTemp %s render-script' % (lname))

l = Layer()

<%@scriptFiles%>

RenderControl.appendLayer(lname, l)

