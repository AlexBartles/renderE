import nethandler as nh
from PIL import Image, ImageDraw
Image.MAX_IMAGE_PIXELS = None #these images are too HUGE
import twc.dsmarshal as dsm
import os
import json
import pygame as pg

def vginfo(vgfile):
    extents = [1, 1]
    def setExtents(w, h):
        nonlocal extents
        extents = [w, h]
    polylines = []
    def addPolyline(pl, name):
        polylines.append(pl)
    with open(vgfile, "r") as f:
        exec(f.read(), {"setExtents": setExtents, "addPolyline": addPolyline})
    return extents, polylines

def process(mtype):
    print("MAPCUT")
    print(f"PROCESS {mtype}")
    md = dsm.get(mtype+".MapData")
    mapname = md.mapName
    print(mapname)
    mappath = nh.requestNetAssetExt(f"/rsrc/maps/{mapname}")
    if mapname.endswith(".bfg"):
        dt = os.path.join(os.environ["RENDEREROOT"], "temp", f"{mapname}.jpeg")
        if os.path.exists(dt):
            finalmapimg = Image.open(dt)
        else:
            print(f"Assembling {mapname} for the first time! This will be cached until you delete your temporary files again.")
            with open(mappath, "r") as f:
                mapdef = f.read().strip().split("\n")
            total = int(mapdef[0])
            cols = int(mapdef[1])
            rows = total//cols
            maps = mapdef[2:]
            mp = []
            for map in maps:
                mp.append(Image.open(nh.requestNetAssetExt(map)))
            finalmapimg = Image.new("RGB",
                (sum([m.width for m in mp[:cols]]),
                sum([m.height for m in mp[::rows]]))
            )
            
            xx = 0
            yy = 0
            for row in range(rows):
                for col in range(cols):
                    cmap = mp[col+row*cols]
                    finalmapimg.paste(cmap, (xx, yy))
                    xx += cmap.width
                xx = 0
                yy += mp[row*cols].height
            del maps #memory management!
            finalmapimg.save(os.path.join(os.environ["RENDEREROOT"], "temp", f"{mapname}.jpeg"))
    else:
        finalmapimg = Image.open(mappath).convert("RGB")
    
    #cut
    cx, cy = md.mapcutCoordinate
    cw, ch = md.mapcutSize
    cy = finalmapimg.height-cy
    crop = (cx, cy-ch, cx+cw, cy)
    intermediate = finalmapimg.crop(crop)
    print(crop, cw, ch)
    final = intermediate.resize(md.mapFinalSize, Image.Resampling.LANCZOS)
    os.makedirs(os.path.join(os.environ["TWCPERSDIR"], "data", "map.cuts"), exist_ok=True)
    final.save(os.path.join(os.environ["TWCPERSDIR"], "data", "map.cuts", f"{mtype}.map.tif"))
    
    #dcx, dcy1 = getattr(md, "datacutCoordinate", (0, 0))
    dcx = 0
    dcy1 = 0
    dcw, dch = getattr(md, "_datacutSize", (cw, ch))
    dcx += cx
    dcy1 = cy - dcy1
    
    fdcw, fdch = getattr(md, "_dataFinalSize", md.mapFinalSize)
    
    finalmapimg = None
    intermediate = None
    final = None
    
    for v in md.vectors:
        vx = v.split(".")[-2]
        ex, pl = vginfo(nh.requestNetAssetExt(f"/rsrc/maps/{v}"))
        dcy = ex[1] - dcy1
        
        left = dcx
        right = dcx+dcw
        top = dcy
        bottom = dcy+dch
        print("vstats", v, left, right, top, bottom, "full", ex)
        
        finalpl = []
        for pol in pl:
            poly_is_inside = False
            for pt in pol:
                ptx, pty = pt
                if (left <= ptx <= right) and (top <= pty <= bottom):
                    poly_is_inside = True
                    print("IT'S IN")
                    break
            
            if poly_is_inside:
                finalpl.append([((p[0]-dcx)*fdcw/dcw, (ex[1]-p[1]-(ex[1]-bottom))*fdch/dch) for p in pol])
        
        vectorCut = os.path.join(os.environ["TWCPERSDIR"], "data", "map.cuts", f'{mtype}.{vx}.vg')
        with open(vectorCut, "w") as f:
            f.write(json.dumps([fdcw, fdch, finalpl], indent=4))

if __name__ == "__main__":
    process('Config.1.Local_MetroDopplerRadar')