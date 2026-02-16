
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

<%!
# this is an emergency hack to get event/run logs to log their start
# time and frame properly
for item in runlogEvents:
    type = item[0]
    if type == 'tag':
        event = item[1]
        event.time=params.startTime
        event.frame=params.startFrame
%>
