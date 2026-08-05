import json
import twc.dsmarshal as dsm
import twccommon

with open("ds.json", "r") as f:
    data : dict = json.load(f)
listofkeys = list(data.keys())

for k in listofkeys:
    if k.endswith("._dsmarshal"):
        try:
            kn = ".".join(k.split(".")[:-1])
            data2 = dsm.get(kn)
        except:
            continue
        if isinstance(data2, twccommon.Data):
            if "bkgImage" in data2.__dict__ or "productTitle" in data2.__dict__ or "bkgFade" in data2.__dict__:
                data3 = twccommon.Data()
                for key in list(data2.__dict__.keys()):
                    if key not in ["bkgImage", "productTitle", "bkgFade"]:
                        data3.__dict__[key] = data2.__dict__[key]
                print(data2)
                print(data3)
                
                dsm.set(kn, data3, 0)

dsm.ds.commit()