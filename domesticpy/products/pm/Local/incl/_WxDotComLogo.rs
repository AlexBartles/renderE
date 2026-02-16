
# weather.com label:
m = TIFF_Image('/rsrc/logos/weatherDotComLogo')
m.setPosition(547,37)
r,g,b,a = renderUtil.rgbaConvert(0, 51, 153)
m.setColor(r,g,b)
p.addItem(m)

