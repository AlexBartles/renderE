import os
import re
import rendereglobals as rg

def _fix_if(m):
    return f" (({m.group(1)} if {m.group(1)} is not None else -1) {m.group(2)} ({m.group(3)} if {m.group(3)} is not None else -1))"

ifpattern = r"\s([A-Za-z0-9_]+)\s*(<|>|>=|<=)\s*([A-Za-z0-9_]+)"
def fix(rs):
    rs = rs.replace("as =", "aseq =")
    rs = rs.replace("(as,", "(aseq,")
    rs = rs.replace("(as.", "(aseq.")
    rs = rs.replace("for as ", "for aseq ")
    rs = rs.replace("(as)", "(aseq)")
    rs = rs.replace(" as.", " aseq.")
    rs = rs.replace("-as.", "-aseq.")
    rs = rs.replace(" as,", " aseq,")
    rs = rs.replace("Exception, e", "Exception as e")
    rs = rs.replace("/twc/data/map.cuts", rg.newjoin(os.environ["RENDEREROOT"], "map.cuts"))
    rs = rs.replace("os.path.join", "newjoin")
    rs = re.sub(ifpattern, _fix_if, rs)
    return rs

def fix_if(rs):
    fixed = re.sub(ifpattern, _fix_if, rs).replace("Exception, e", "Exception as e")
    return fixed