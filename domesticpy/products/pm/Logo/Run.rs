
<%@'_init.rs'%>

lname      = <%-params.layerProps.name%>
lnameDuration = lname + 'Duration'
startTime  = 0
startFrame = <%-params.startFrame%>
nationalLdl = <%-getattr(params, "nationalLdl", 0)%>

twccommon.Log.info(
    '%s activation @ %d.%d' % (lname, startTime, startFrame))

# Begin Expire Named Layer Logic
# This layer exists to remove the real layer(s) if they are loaded and never run.
# since we are in the run, destroy it!
lnameExpire  = lname + 'Expire'
RenderControl.destroyNamedLayer(lnameExpire)
# End Expire Named Layer Logic

RenderControl.activateLayer(lname, time=startTime, frameOffset=startFrame)
if not nationalLdl:
    RenderControl.activateLayer(lnameDuration, time=startTime, frameOffset=startFrame)

