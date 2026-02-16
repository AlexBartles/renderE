
background = CompositeRenderable()
# Big bad black box background (Bx5)
bb = Box()
bb.setSize(720,74)
bb.setPosition(0,0)
r,g,b,a = renderUtil.rgbaConvert(20,20,20,255)
bb.setColor(r,g,b,a)
background.addItem(bb)

boxPos = 0
def getBox(w, h, colors):
    # Used to help build crazy glint line at top
    global boxPos
    poly = Polygon()
    r,g,b = colors[0]
    r,g,b,a = renderUtil.rgbaConvert(r,g,b)
    poly.addVertex(0, 0, r,g,b,a)
    r,g,b = colors[1]
    r,g,b,a = renderUtil.rgbaConvert(r,g,b)
    poly.addVertex(w, 0, r,g,b,a)
    poly.addVertex(w, h, r,g,b,a)
    r,g,b = colors[0]
    r,g,b,a = renderUtil.rgbaConvert(r,g,b)
    poly.addVertex(0, h, r,g,b,a)
    poly.setPosition(boxPos, 0)
    boxPos = boxPos + w
    return poly

# Crazy glint line at top of LDL
cr = CompositeRenderable()
cr.addItem(getBox(65,2, [[58,58,58], [157,157,157]]))
cr.addItem(getBox(43,2, [[157,157,157], [66,66,66]]))
cr.addItem(getBox(43,2, [[66,66,66], [101,101,101]]))
cr.addItem(getBox(187,2, [[101,101,101], [206,206,206]]))
cr.addItem(getBox(137,2, [[206,206,206], [103,103,103]]))
cr.addItem(getBox(39,2, [[103,103,103],[165,165,165]]))
cr.addItem(getBox(34,2, [[165,165,165], [105,105,105]]))
cr.addItem(getBox(172,2, [[105,105,105], [105,105,105]]))
cr.setPosition(0, 74)
background.addItem(cr)


m = TIFF_Image('/rsrc/logos/weatherDotComLogo')
m.setPosition(547,37)
background.addItem(m)


p.addItem(background)

