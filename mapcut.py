import nethandler as nh
from PIL import Image
Image.MAX_IMAGE_PIXELS = None #these images are too HUGE
import twc.dsmarshal as dsm
import os

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

if __name__ == "__main__":
    process('Config.1.Local_RadarSatelliteComposite')