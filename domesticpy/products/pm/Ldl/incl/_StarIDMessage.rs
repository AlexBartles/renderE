
<%!
data = prod.getData()
if len(data.bulletins) > 0:
    titleColor = (239,192,49,255)
else:
    titleColor = (121,186,242,255)

message = data.message
%>
import time

titleColor = <%-titleColor%>


cr = CompositeRenderable()
f = TTFont('/rsrc/fonts/Interstate-Bold', 25, shadow=0, t=80)
if <%-message%> != None:
    t = Text(f, <%-message%>)
    t.setPosition(55, 37)
    r,g,b,a = renderUtil.rgbaConvert(212,212,212,255)
    t.setColor(r,g,b,a)
    cr.addItem(t)
else:
    __skipPage = 1

cr.setPosition(0,0)

p.addItem(cr)

