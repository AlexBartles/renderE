import os
import nethandler
import twc.psp
import twccommon

def compilers(rs):
    ns = {"params": twccommon.Data()}
    path = None
    if os.path.exists(rs):
        path = rs
    elif nethandler.requestNetAssetExt(rs):
        path = nethandler.requestNetAssetExt(rs)
    if not path:
        raise ValueError("rs file not found!")
    with open(path, "r") as f:
        data = f.read()
    return twc.psp.evalRenderScript(data, ns)