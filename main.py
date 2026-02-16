import rendereglobals as rg
import math
from PIL import Image
from io import BytesIO
from twc.embedded.renderd.RenderScript import *
import twc.embedded.renderd.renderUtil as renderUtil
import twc.psp
import domestic.renderTools as renderTools
import twc
import twc.products
import twccommon.Log
import socket
import os
import threading as th
rl = rg.rl

screensize = (720, 480)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("localhost", 7245))

def loadtif(filename):
    im = Image.open(filename)
    arr = BytesIO()
    im.save(arr, format="PNG")
    arr = arr.getvalue()
    im2 = rl.load_image_from_memory('.png', arr, len(arr))
    return (rl.load_texture_from_image(im2), im2.width, im2.height)

e = os.popen("fortune disclaimer")
rl.init_window(screensize[0], screensize[1], f"RenderE - {e.read()}")
e.close()

fov = 25

camera = rl.Camera3D(
    rl.Vector3(0, 0, 0),
    rl.Vector3(0, 0, -10),
    rl.Vector3(0, 1, 0),
    fov,
    rl.CameraProjection.CAMERA_PERSPECTIVE
)

planem = rl.gen_mesh_plane(1, 1, 1, 1)

rl.set_target_fps(30)

def frustum_size_at_z(z, fov_y_deg, aspect_ratio):
    fov_y = math.radians(fov_y_deg)
    height = z * math.tan(fov_y / 2)
    width = height * aspect_ratio
    return width, height

zzz = rg.zzz

xxx, yyy = frustum_size_at_z(zzz, fov, screensize[0]/screensize[1])
# xxx = 2.6
# yyy = 1.72

plane = rl.load_model_from_mesh(planem)

defaulttex = plane.materials[0].maps.texture

rl.rl_disable_backface_culling()

ee = 0

def sockethandle():
    sock.listen()
    while True:
        conn, addr = sock.accept()
        while True:
            data = conn.recv(1024).decode().strip()
            if not data:
                # if data is not received break
                break
            args = data.split(" ")
            if args[0] == "loadrs":
                print("loadrs", args)
            if args[0] == "loadprod":
                print("loadprod", args)
                loadprod(args[1], twccommon.Data(prodName="prodName", product="product"))
        conn.close()

tth = th.Thread(target=sockethandle, daemon=True)
tth.start()

layers = rg.layers

prodloader = twc.products.ProductLoader()
def loadprod(path, params):
    prodloader.loadProductFile(path, params)

def fsplash():
    l = Layer()
    p = Page()
    l.addPage(p)

    gr = Box()
    gr.setSize(720,480)
    r,g,b,a = renderUtil.rgbaConvert(235,235,235)
    gr.setColor(r,g,b,a)
    p.addItem(gr)

    quad2 = TIFF_Image("/rsrc/images/renderELogo")
    quad2.setSize(360, 240)
    quad2.setPosition(180, 120)

    Rotate(quad2, .9, xr=1)
    Rotate(quad2, .8, yr=1)
    Rotate(quad2, .7, zr=1)

    gr = Box()
    gr.setSize(720, 110)
    r, g, b, a = renderUtil.rgbaConvert(20, 20, 20)
    gr.setColor(r, g, b, a)
    p.addItem(gr)

    # gr = TIFF_Image()
    # gr.setSize(720, 110)
    # r, g, b, a = renderUtil.rgbaConvert(20, 20, 20)
    # gr.setColor(r, g, b, a)
    # p.addItem(gr)

    p.addItem(quad2)

    f = TTFont("/rsrc/fonts/Frutiger_Bold", 16, shadow = 0)
    r,g,b,a = renderUtil.rgbaConvert(255, 212,  14)
    gr = Text(f, 'headend Id: 322737')
    gr.setPosition(70,92)
    gr.setColor(r,g,b,a)
    p.addItem(gr)
    gr = Text(f, 'serial number: N/A')
    gr.setPosition(70,76)
    gr.setColor(r,g,b,a)
    p.addItem(gr)
    gr = Text(f, 'location name: Minneapolis')
    gr.setPosition(70,60)
    gr.setColor(r,g,b,a)
    p.addItem(gr)
    gr = Text(f, 'affiliate name: XFINITY TV')
    gr.setPosition(70,44)
    gr.setColor(r,g,b,a)
    p.addItem(gr)
    
    #cr = CompositeRenderable()

    filename = "/rsrc/logos/twcLogo"
    gr = TIFF_Image(filename)
    gr.setPosition(600, 62)
    p.addItem(gr)
    #cr.addItem(gr)
    filename = "/rsrc/logos/wxScanLogo"
    gr = TIFF_Image(filename)
    gr.setPosition(490, 44)
    p.addItem(gr)
    #cr.addItem(gr)
    
    #p.addItem(cr)
    
    # gr = renderUtil.getBevelBox(200, 200)
    # gr.setPosition(0, 0)
    # p.addItem(gr)

    #name, layer, time, frameOffset, depth, repeat, x, y, w, h, sx, sy, tx, ty
    layers.append(["Foreground", l, 0, 0, 10, 0, 0, 0, 720, 480, 1, 1, 0, 0])

def producttest():
    l = Layer()
    p = Page()
    l.addPage(p)
    pduration = 100
    
    bkg1 = twc.findRsrc("/backgrounds/%s" % ("domestic"), "tif", 1)
    background = TIFF_Image(bkg1)
    background.setTransitionable(0)
    background.setSize(720, 480)
    p.addItem(background)


    def center(areaStart, areaWidth, elemWidth):
        return areaStart + areaWidth/2 - elemWidth/2

    ru = renderUtil   # abbreviation
    
    title = ("current", "conditions")
    dur = 100

    titleX = 52
    titleY = 479 - 74
    
    def resolveOverrides(name, defaultVal):
        return defaultVal

    text1Color       = resolveOverrides('text1Color', (212, 212, 212, 255))
    text2Color       = resolveOverrides('text2Color', (20, 20, 20, 255))
    text1ShadowColor = resolveOverrides('text1ShadowColor', (20, 20, 20, 255))
    text2ShadowColor = resolveOverrides('text2ShadowColor', (212, 212, 212, 255))
    text1BkgColor    = resolveOverrides('text1BkgColor', (0, 0, 0, 0))
    text2BkgColor    = resolveOverrides('text2BkgColor', (212, 212, 212, 255))
    fadeIn           = resolveOverrides('titleFadeInDuration', 5)
    fadeOut          = resolveOverrides('titleFadeOutDuration', 5)


    #Create the title bar elements
    crBev, crTxt = renderTools.createTitleBar(
        title[0],              title[1],
        text1BkgColor,    text2BkgColor,
        text1Color,       text2Color,
        text1ShadowColor, text2ShadowColor)

    #First add the title bevel
    crBev.setPosition(titleX, titleY)
    p.addItem(crBev)

    #Now add the title text (and background gradient)
    crTxt.setPosition(titleX, titleY)
    p.addItem(crTxt)

    if ((fadeIn > 0) or ( fadeOut > 0)):
        renderUtil.fadeInOut(p, crTxt, dur, fadeIn, fadeOut)

    ww = 215
    hh = 282
    xpos =  52
    ypos = 370
    baseline = 89

    locBox   = CompositeRenderable()
    iconBox  = CompositeRenderable()
    tabBox   = CompositeRenderable()
    dataBox  = CompositeRenderable()
        
    # location name with bevel box    
    wwbb = 616
    locBox.addItem(ru.getBevelBox(wwbb, 30))
        
    r,g,b,a = ru.rgbaConvert(212,212,50)
    ff = TTFont('/rsrc/fonts/Interstate-Bold', 24, t=50)
    tt = Text(ff, "WINNERS DON'T USE DRUGS")
    tt.setPosition(11, 8)
    tt.setColor(r,g,b,a)
    locBox.addItem(tt)
        
    # position the compsite renderable
    locBox.setPosition(xpos, ypos)

    # left and right bevel boxes with icon and temp data
    bb = ru.getBevelBox(ww,hh)
    bb.setPosition(0, 0)
    iconBox.addItem(bb)

    bb = ru.getBevelBox(wwbb-ww, hh)
    bb.setPosition(0, 0)
    tabBox.addItem(bb)
    
    iconBox.setPosition(52, baseline)
    tabBox.setPosition(267, baseline)
    dataBox.setPosition(453, baseline)
        
    # transitions
    # add the locBox, iconBox, and tabBox into one Composite Renderable to slide off screen
    slideCR = CompositeRenderable()        
    slideCR.addItem(locBox)
    slideCR.addItem(iconBox)
    slideCR.addItem(tabBox)
    p.addItem(slideCR)
    p.addItem(dataBox)    

    # begin loc box
    es = EffectSequencer(slideCR)
    es.addEffect(NullEffect(None), pduration - 10)
    es.addEffect(Slider(None, -72, 0), 10)
    p.addItem(es)

    # begin right side data area
    #TODO: Make Clipper work on text!    
    # add clipper for 'reveal' effect    
    #c = Clipper(None, bottom=100)
    #c.clip(Clipper.CP_BOTTOM, pos=hh, step=-10)
        
    es = EffectSequencer(dataBox)
    #es.addEffect(NullEffect(None), 5)
    #es.addEffect(c, 60)
    es.addEffect(NullEffect(None), pduration - 10)
    es.addEffect(Slider(None, -72, 0), 10)
    p.addItem(es)

    renderTools.dataNotAvailable(page=p, displayDuration=pduration)
    
    layers.append(["Foreground", l, 0, 0, 10, 0, 0, 0, 720, 480, 1, 1, 0, 0])
producttest()
whiteimg = rl.gen_image_color(1, 1, rl.WHITE)
white = rl.load_texture_from_image(whiteimg)
once = True

def updateseq(seq : EffectSequencer):
    seq.timer += 1
    al = []
    al.append(seq.effects[0][1])
    if len(seq.effects) > 0:
        for i in seq.effects[1:]:
            al.append(al[-1]+i[1])
    
    ea = 0
    for i in range(len(seq.effects)):
        ea += 1
        if seq.timer < al[i]:
            break
    if len(seq.activeeffects) < ea:
        seq.activeeffects.append(seq.effects[ea-1][0])
    for i in range(ea-1):
        seq.activeeffects[i].frozen = True
    if seq.timer >= seq.total:
        if seq.repeat:
            seq.timer = 0
            for ef in seq.effects:
                ef[0].timer = 0
                ef[0].frame = 0
                ef[0].frozen = False
            seq.activeeffects = [seq.effects[0][0]]
        else:
            for ef in seq.effects:
                ef[0].frozen = True

def draw_quad(quad : TIFF_Image, tex=white, debug=False):
    effects = quad.effects
    plane.materials[0].maps.texture = tex
    qqx, qqy = quad.position
    if isinstance(quad, Text):
        test = "qypgj"
        descending = False
        for c in test:
            if c in quad.s:
                descending = True
        if descending or True:
            qqy += quad.descent
        if quad.fnt.shadow:
            qqx += quad.fnt.sx
            #qqy -= quad.fnt.sy
    qx, qy = qqx*1, qqy*1
    xxw = (-qx-quad._size[0]/2)/720*(xxx*2)
    yyw = (-qy-quad._size[1]/2)/480*(yyy*2)
    xw = quad._size[0]/720*(xxx*2)
    yw = quad._size[1]/480*(yyy*2)
    
    mat = rl.matrix_rotate_xyz((math.radians(90), 0, math.radians(0)))
    mat = rl.matrix_multiply(mat, rl.matrix_scale(xw, yw, 1))
    fader = 1
    def applyeffect(effect : GraphicEffect):
        nonlocal mat, xxw, yyw, fader
        if type(effect) == Rotate:
            if effect.xr:
                mat = rl.matrix_multiply(mat, rl.matrix_rotate_x(math.radians(effect.angle*effect.frame)))
            if effect.yr:
                mat = rl.matrix_multiply(mat, rl.matrix_rotate_y(math.radians(effect.angle*effect.frame)))
            if effect.zr:
                mat = rl.matrix_multiply(mat, rl.matrix_rotate_z(math.radians(effect.angle*effect.frame)))
        elif type(effect) == Slider:
            xxw -= (effect.dx*effect.frame/720*(xxx*2))
            yyw -= (effect.dy*effect.frame/480*(yyy*2))
        elif type(effect) == Fader:
            dist = (effect.frame/effect.frames)
            dist = min(dist, 1)
            fader = effect.startAlpha*(1-dist) + effect.endAlpha*dist
        elif type(effect) == SetPosition:
            quad.position = (effect.x, effect.y)
        elif type(effect) == SetSize:
            quad.size = (effect.w, effect.h)
        elif type(effect) == SetText:
            if isinstance(quad, Text):
                quad.s = effect.s
        elif type(effect) == SetVisibility:
            if not effect.fired:
                quad.visible = effect.visible
                effect.fired = True
        if hasattr(effect, "frame"):
            if not effect.frozen:
                effect.frame += 1
        
    def loopover(eflist):
        for effect in eflist:
            if type(effect) == EffectSequencer:
                updateseq(effect)
                loopover(effect.activeeffects)
            else:
                applyeffect(effect)
    loopover(effects)
    mat = rl.matrix_multiply(mat, rl.matrix_translate(-xxx, -yyy, 0))
    plane.transform = mat
    col = rl.Color(round(quad._color[0]*255), round(quad._color[1]*255), round(quad._color[2]*255), round(quad._color[3]*fader*255))
    if isinstance(quad, Text):
        col = rl.Color(255, 255, 255, int(255*fader))
    if quad.visible:
        rl.draw_model_ex(plane, rl.Vector3(-xxw, -yyw, -zzz), rl.Vector3(0, 0, 0), 0, rl.Vector3(1, 1, 1), col)

class DummyQuad():
    def __init__(self, x, y, w, h, effects=[]):
        self.position = (x, y)
        self._size = (w, h)
        self.effects = effects
        self._color = (1, 1, 1, 1)
        self.visible = True
    def size(self):
        return self._size

def draw_poly(quad : TIFF_Image, tex=white):
    effects = quad.effects
    plane.materials[0].maps.texture = tex
    qqx, qqy = quad.position
    qx, qy = qqx*1, qqy*1
    xxw = (-qx)/720*(xxx*2)
    yyw = (-qy)/480*(yyy*2)
    xw = (xxx*2)/720
    yw = (yyy*2)/480
    
    mat = rl.matrix_scale(xw, yw, 1)
    fader = 1
    def applyeffect(effect : GraphicEffect):
        nonlocal mat, xxw, yyw, fader
        if type(effect) == Rotate:
            if effect.xr:
                mat = rl.matrix_multiply(mat, rl.matrix_rotate_x(math.radians(effect.angle*effect.frame)))
            if effect.yr:
                mat = rl.matrix_multiply(mat, rl.matrix_rotate_y(math.radians(effect.angle*effect.frame)))
            if effect.zr:
                mat = rl.matrix_multiply(mat, rl.matrix_rotate_z(math.radians(effect.angle*effect.frame)))
        elif type(effect) == Slider:
            xxw -= (effect.dx*effect.frame/720*(xxx*2))
            yyw -= (effect.dy*effect.frame/480*(yyy*2))
        elif type(effect) == Fader:
            dist = (effect.frame/effect.frames)
            dist = min(dist, 1)
            fader = effect.startAlpha*(1-dist) + effect.endAlpha*dist
        if hasattr(effect, "frame"):
            if not effect.frozen:
                effect.frame += 1
        
    def loopover(eflist):
        for effect in eflist:
            if type(effect) == EffectSequencer:
                updateseq(effect)
                loopover(effect.activeeffects)
            else:
                applyeffect(effect)
    loopover(effects)
    mat = rl.matrix_multiply(mat, rl.matrix_translate(-xxx, -yyy, 0))
    
    mat = rl.matrix_multiply(mat, rl.matrix_translate(-xxw, -yyw, 0))
    
    pts2 = quad.vertices
    pts = []
    
    for p in pts2:
        pts.append((rl.vector3_transform(p[0], mat), p[1], p[2], p[3], p[4]))
    #pts = pts2
    
    if len(pts) == 4:
        rl.rl_begin(rl.RL_QUADS)
        rl.rl_color4f(pts[0][1], pts[0][2], pts[0][3], pts[0][4]*fader)
        rl.rl_vertex3f(pts[0][0].x, pts[0][0].y, pts[0][0].z)
        
        rl.rl_color4f(pts[1][1], pts[1][2], pts[1][3], pts[1][4]*fader)
        rl.rl_vertex3f(pts[1][0].x, pts[1][0].y, pts[1][0].z)
        
        rl.rl_color4f(pts[2][1], pts[2][2], pts[2][3], pts[2][4]*fader)
        rl.rl_vertex3f(pts[2][0].x, pts[2][0].y, pts[2][0].z)
        
        rl.rl_color4f(pts[3][1], pts[3][2], pts[3][3], pts[3][4]*fader)
        rl.rl_vertex3f(pts[3][0].x, pts[3][0].y, pts[3][0].z)
    else:
        rl.rl_begin(rl.RL_TRIANGLES)
        for i in range(1, len(pts) - 1):
            # Triangle 1: Vertex 0, i, i+1
            # Setting color per vertex
            rl.rl_color4f(pts[0][1], pts[0][2], pts[0][3], pts[0][4]*fader)
            rl.rl_vertex3f(pts[0][0].x, pts[0][0].y, pts[0][0].z)
            
            rl.rl_color4f(pts[i][1], pts[i][2], pts[i][3], pts[i][4]*fader)
            rl.rl_vertex3f(pts[i][0].x, pts[i][0].y, pts[i][0].z)
            
            rl.rl_color4f(pts[i+1][1], pts[i+1][2], pts[i+1][3], pts[i+1][4]*fader)
            rl.rl_vertex3f(pts[i+1][0].x, pts[i+1][0].y, pts[i+1][0].z)
        rl.rl_end()

def draw_item(item, extra={"tex": None}):
    global once
    if type(item) == Layer:
        item.timer += 1
        al = []
        al.append(item.pages[0][1])
        if len(item.pages) > 0:
            for i in item.pages:
                al.append(al[-1]+i[1])
        
        ea = 0
        for i in range(len(item.pages)):
            ea += 1
            if item.pages[ea-1][1] == 0:
                break
            if item.timer < al[i]:
                break
        
        if len(item.pages) > 0:
            if not item.pages[0][0].started == True:
                item.pages[0][0].started = True
                #todo: add the hooks here
        if item.pa != (ea-1):
            item.pages[item.pa][0].ended = True
            #and here
            item.pa = (ea-1)
            item.pages[item.pa][0].started = True
            #...and here
        draw_item(item.pages[item.pa][0])
    elif type(item) == Page:
        for el in item._elements:
            draw_item(el)
    elif type(item) is TIFF_Image:
        #quad senior
        draw_quad(item, item.texture)
    elif type(item) is JPEG_Image:
        #quad junior
        draw_quad(item, item.texture)
    elif type(item) is Box:
        #quad, i am your father's brother's nephew's cousin's former roommate
        draw_quad(item)
    elif isinstance(item, DummyQuad):
        draw_quad(item)
    elif isinstance(item, Text):
        if (item._lastcol != item._color) and item.cachedtex is not None:
            rl.unload_texture(item.cachedtex)
            item.cachedtex = None
            item._lastcol = item._color
        elif (item.lasts != item.s) and item.cachedtex is not None:
            rl.unload_texture(item.cachedtex)
            item.cachedtex = None
            item.lasts = item.s
        if item.cachedtex is None:
            if item.fnt.shadow:
                newsurf = rg.pg.Surface((item._textsize[0]+abs(item.fnt.sx), item._textsize[1]+abs(item.fnt.sy)), rg.pg.SRCALPHA)
                newsurf.fill((0, 0, 0, 0))
                newsurf.blit(item.fnt.font.render(item.s, True, [c*255 for c in item.fnt.scol]), (max(0, item.fnt.sx), max(0, item.fnt.sy)))
                newsurf.blit(item.fnt.font.render(item.s, True, [c*255 for c in item._color]), (max(0, -item.fnt.sx), max(0, -item.fnt.sy)))
            else:
                #newsurf = rg.pg.Surface(item._textsize, rg.pg.SRCALPHA)
                newsurf = item.fnt.font.render(item.s, True, [c*255 for c in item._color])
            newsurf = rg.pg.transform.smoothscale_by(newsurf, (1, 0.98))
            item._size = newsurf.get_size()
            buf = BytesIO()
            rg.pg.image.save(newsurf, buf, ".bmp")
            cimg = rl.load_image_from_memory(".bmp", buf.getvalue(), len(buf.getvalue()))
            item.cachedtex = rl.load_texture_from_image(cimg)
            rl.export_image(cimg, "cimg.png")
        
        draw_quad(item, item.cachedtex)
    elif isinstance(item, CompositeRenderable):
        rl.end_mode_3d()
        rl.begin_texture_mode(item.rtex)
        rl.clear_background(rl.Color(0, 0, 0, 0))
        rl.begin_mode_3d(camera)
        
        
        for ch in item.items:
            if isinstance(ch, CompositeRenderable):
                draw_item(ch, extra={"tex": item.rtex})
                rl.begin_texture_mode(item.rtex)
                rl.begin_mode_3d(camera)
            elif isinstance(ch, Polygon):
                rl.rl_set_blend_mode(rl.BlendMode.BLEND_ALPHA_PREMULTIPLY)
                draw_item(ch)
                rl.rl_set_blend_mode(rl.BlendMode.BLEND_ALPHA)
            else:
                draw_item(ch)
        
        rl.end_mode_3d()
        rl.end_texture_mode()
        
        rl.begin_texture_mode(item.ftex)
        rl.clear_background(rl.Color(0, 0, 0, 0))
        rl.rl_set_blend_mode(rl.BlendMode.BLEND_ALPHA_PREMULTIPLY)
        rl.draw_texture(item.rtex.texture, 0, 0, rl.WHITE)
        rl.end_texture_mode()
        
        if not extra["tex"]:
            rl.begin_mode_3d(camera)
            rl.rl_set_blend_mode(rl.BlendMode.BLEND_ALPHA)
            draw_quad(DummyQuad(*item.position, 720, 480, effects=item.effects), item.ftex.texture)
        else:
            rl.rl_set_blend_mode(rl.BlendMode.BLEND_ALPHA_PREMULTIPLY)
            rl.begin_texture_mode(extra["tex"])
            rl.begin_mode_3d(camera)
            draw_quad(DummyQuad(*item.position, 720, 480, effects=item.effects), item.ftex.texture)
            rl.end_mode_3d()
            rl.rl_set_blend_mode(rl.BlendMode.BLEND_ALPHA)
        
        if item.debug:
            tex = rl.load_image_from_texture(item.rtex.texture)
            rl.export_image(tex, "image2.png")
        
    elif type(item) is Polygon:
        draw_poly(item)
    
while not rl.window_should_close():
    layers.sort(key=lambda x: x[4])
    ee += 1
    rl.begin_drawing()
    rl.clear_background(rl.BLACK)
    rl.begin_mode_3d(camera)
    rl.rl_disable_depth_test()
    rl.rl_disable_depth_mask()
    
    rl.rl_enable_smooth_lines()
    
    for l in layers:
        draw_item(l[1])

    rl.end_mode_3d()
    rl.end_drawing()
    if ee == 5:
        rl.take_screenshot("screenshot.png")