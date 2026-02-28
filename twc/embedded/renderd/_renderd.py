import rendereglobals as rg
from PIL import Image
from io import BytesIO
import os
import glob
import nethandler
import libmv
rl = rg.rl
pg = rg.pg

def parsePath(path : str):
    if path.startswith("/rsrc"):
        return path.replace("/rsrc", os.environ["RENDERERSRC"], 1)
    if path.startswith("/media"):
        return path.replace("/media", os.environ["RENDEREMEDIA"], 1)
    return path

def createImage(self, name, evict=0, x1=0, y1=0, x2=1, y2=1):
    ogname = name+""
    pname = parsePath(name)
    possible = glob.glob(pname+".*")
    print(possible)
    if len(possible) > 0:
        name = possible[0]
    else:
        name = nethandler.requestNetAsset(name, "gfx")
    if not name:
        print(f"No suitable image found for {ogname}!")
        exit(1)
    
    im = Image.open(name)
    arr = BytesIO()
    im.save(arr, format="PNG")
    arr = arr.getvalue()
    self.im2 = rl.load_image_from_memory('.png', arr, len(arr))
    self.texture = None
    self._size = (self.im2.width, self.im2.height)

def createIcon(self, name, evict=0):
    ogname = name+""
    pname = parsePath(name)
    possible = glob.glob(pname+".mv")
    print(possible)
    if len(possible) > 0:
        name = possible[0]
    else:
        name = nethandler.requestNetAssetExt(name, "mv")
    if not name:
        print(f"No suitable icon found for {ogname}!")
        exit(1)
    
    with open(name, "rb") as f:
        data = f.read()
    
    print("loading mv ", name)
    self._frames = libmv.loadmv(data)
    
    im = self._frames[0]
    arr = BytesIO()
    im.save(arr, format="PNG")
    self._rframes = [rl.ffi.new('char []', fr.tobytes()) for fr in self._frames]
    self.idx = 0
    self.framect = len(self._rframes)
    arr = arr.getvalue()
    self._kickstart = rl.load_image_from_memory('.png', arr, len(arr))
    self.texture = None
    self._size = (self._kickstart.width, self._kickstart.height)

def createTTFont(self, name, pointSize, shadow, sr=0.08, sg=0.08, sb=0.08, sa=1.0, sx=1, sy=2, t=0, l=None, evict=0):
    ogname = name+""
    pname = parsePath(name)
    possible = glob.glob(pname+".*")
    if len(possible) > 0:
        name = possible[0]
    else:
        name = nethandler.requestNetAsset(name, "font")
    if not name:
        print(f"No suitable font found for {ogname}!")
        exit(1)
    self.pxSize = round(pointSize * 0.95)
    
    self.font = pg.Font(name, self.pxSize)
    self.scol = (sr, sg, sb, sa)
    self.ascent = self.font.get_ascent()
    self.descent = self.font.get_descent()
    self.cachedtex = None

def createAudio(self):
    return

def createAudioClip(self, name, evict=0, duration_limit=0, loop_limit=1):
    ogname = name+""
    pname = parsePath(name)
    if os.path.exists(pname):
        name = ogname
    else:
        name = nethandler.requestNetAssetExt(name)
    if not name:
        print(f"No suitable sound found for {ogname}!")
        exit(1)
    self.name = name
    self.file = rg.pg.Sound(name)
    self.chan = None
    self.evict = evict
    self.duration_limit = duration_limit
    self.time_played = 0
    self.loop_limit = loop_limit
    self.level = 1
    self.mix = 1
    self.single_play = 0