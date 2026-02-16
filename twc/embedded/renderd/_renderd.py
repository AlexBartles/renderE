import rendereglobals as rg
from PIL import Image
from io import BytesIO
import os
import glob
rl = rg.rl
pg = rg.pg

def parsePath(path : str):
    if path.startswith("/rsrc"):
        return path.replace("/rsrc", os.environ["RENDERERSRC"], 1)
    return path

def createImage(self, name, evict=0, x1=0, y1=0, x2=1, y2=1):
    name = parsePath(name)
    possible = glob.glob(name+".*")
    print(possible)
    name = possible[0]
    
    im = Image.open(name)
    arr = BytesIO()
    im.save(arr, format="PNG")
    arr = arr.getvalue()
    im2 = rl.load_image_from_memory('.png', arr, len(arr))
    self.texture = rl.load_texture_from_image(im2)
    self._size = (im2.width, im2.height)

def createTTFont(self, name, pointSize, shadow, sr=0.08, sg=0.08, sb=0.08, sa=1.0, sx=1, sy=2, t=0, l=None, evict=0):
    name = parsePath(name)
    possible = glob.glob(name+".*")
    print(possible)
    name = possible[0]
    self.pxSize = round(pointSize * 0.95)
    
    self.font = pg.Font(name, self.pxSize)
    self.scol = (sr, sg, sb, sa)
    self.ascent = self.font.get_ascent()
    self.descent = self.font.get_descent()
    self.cachedtex = None