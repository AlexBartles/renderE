
<%@'_init.rs'%>

lname      = <%-params.layerProps.name%>
lnameBack  = lname + 'Background'
startTime  = 0
startFrame = <%-params.startFrame%>

twccommon.Log.info(
    '%s activation @ %d.%d' % (lname, startTime, startFrame))

# Begin Expire Named Layer Logic
# This layer exists to remove the real layer(s) if they are loaded and never run.
# since we are in the run, destroy it!
lnameExpire  = lname + 'Expire'
RenderControl.destroyNamedLayer(lnameExpire)
# End Expire Named Layer Logic

RenderControl.activateLayer(lname, time=startTime, frameOffset=startFrame)
RenderControl.activateLayer(lnameBack, time=startTime, frameOffset=startFrame)

