
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
loginfo           = twccommon.Data()
loginfo.time      = params.startTime
loginfo.frame     = params.startFrame
loginfo.duration  = params.duration
loginfo.configSet = dsm.getConfigVersion() 
loginfo.flavor    = params.flavor
loginfo.schedule  = params.prodSchedule
loginfo.starId    = dsm.defaultedConfigGet('starId', None)

runlogEvents.append(('local', loginfo))
%>

