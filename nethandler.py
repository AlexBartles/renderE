import requests as r
import os
import json
from pathlib import PurePath

servers = [
    "https://archive.lewolfyt.cc/PerrisLive/",
    "https://archive.lewolfyt.cc/FlatRockLive/",
#    "https://archive.lewolfyt.cc/WxScanLive/"
]

def newjoin(*args):
    pp = PurePath(*args).as_posix()
    jp = os.path.join(*args)
    if jp.endswith("/") or jp.endswith("\\") and not (pp.endswith("/")):
        pp = pp + "/"
    return pp

try:
    with open(newjoin(os.path.dirname(os.path.abspath(__file__)), "servers.json")) as f:
        servers = json.loads(f.read())[1:]
except:
    import traceback
    traceback.print_exc()
    pass

temp = newjoin(
    os.path.dirname(os.path.abspath(__file__)),
    "net"
)

def _socksend(sock, data):
    dlen = len(data).to_bytes(4)
    sock.sendall(dlen+data)

def e(a):
    return a.replace("https:\\a","https://a").replace("https:/a", "https://a")

def requestNetAsset(path : str, extensions, check=False):
    fonts = ["ttf", "otf"]
    gfx = ["tif", "jpg", "tiff", "jpeg", "png"]
    aud = ["wav", "mp3"]
    all = fonts + gfx + aud
    emap = {"font": fonts, "gfx": gfx, "audio": aud, "all": all}
    for ex in emap[extensions]:
        out = e(newjoin(temp, path.strip("/")))+"."+ex
        if e(os.path.exists(out)):
            return out
    if check:
        return
    for ex in emap[extensions]:
        out = e(os.path.join(temp, path.strip("/")))+"."+ex
        for server in servers:
            spath = e(os.path.join(server, path.strip("/")))+"."+ex
            print(spath)
            if r.head(spath).ok:
                os.makedirs(os.path.dirname(out), exist_ok=True)
                f = open(out, "wb")
                f.write(r.get(spath, allow_redirects=True).content)
                f.close()
                return out
    return None

def requestNetAssetExt(path : str, ext=None, check=False):
    out = e(newjoin(temp, path.strip("/")))+("."+ext if ext else "")
    if os.path.exists(out):
        return out
    if check:
        return
    for server in servers:
        spath = e(newjoin(server, path.strip("/")))+("."+ext if ext else "")
        print(spath)
        if r.head(spath).ok:
            os.makedirs(os.path.dirname(out), exist_ok=True)
            f = open(out, "wb")
            f.write(r.get(spath, allow_redirects=True).content)
            f.close()
            return out
    return None
