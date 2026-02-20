import requests as r
import os

servers = [
    "https://archive.lewolfyt.cc/PerrisLive/",
    "https://archive.lewolfyt.cc/FlatRockLive/",
    "https://archive.lewolfyt.cc/WxScanLive/"
]
temp = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "net"
)
def requestNetAsset(path : str, extensions):
    fonts = ["ttf", "otf"]
    gfx = ["tif", "jpg", "tiff", "jpeg", "png"]
    aud = ["wav", "mp3"]
    all = fonts + gfx + aud
    emap = {"font": fonts, "gfx": gfx, "audio": aud, "all": all}
    for ex in emap[extensions]:
        out = os.path.join(temp, path.strip("/"))+"."+ex
        if os.path.exists(out):
            return out
    for ex in emap[extensions]:
        out = os.path.join(temp, path.strip("/"))+"."+ex
        for server in servers:
            spath = os.path.join(server, path.strip("/"))+"."+ex
            print(spath)
            if r.head(spath).ok:
                os.makedirs(os.path.dirname(out), exist_ok=True)
                f = open(out, "wb")
                f.write(r.get(spath, allow_redirects=True).content)
                f.close()
                return out
    return None

def requestNetAssetExt(path : str, ext=None):
    out = os.path.join(temp, path.strip("/"))+("."+ext if ext else "")
    if os.path.exists(out):
        return out
    out = os.path.join(temp, path.strip("/"))+("."+ext if ext else "")
    for server in servers:
        spath = os.path.join(server, path.strip("/"))+("."+ext if ext else "")
        print(spath)
        if r.head(spath).ok:
            os.makedirs(os.path.dirname(out), exist_ok=True)
            f = open(out, "wb")
            f.write(r.get(spath, allow_redirects=True).content)
            f.close()
            return out
    return None