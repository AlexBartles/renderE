import os
import re
import rendereglobals as rg

def _fix_if(m):
    n1 = m.group(1)
    op = m.group(2)
    n2 = m.group(3)
    fn = "ehuehuehue_i_added_a_function"
    return f" {fn}({n1}) {op} {fn}({n2})"
    # add2 = ""
    # add1 =""
    # if n1.startswith("("):
    #     n1 = n1[1:]
    #     if n2.endswith(")"):
    #         n2 = n2[:-1]
    
    # do = False
    # try:
    #     n1 = float(n1)
    # except:
    #     do = True
    
    # try:
    #     n2 = float(n2)
    # except:
    #     do = True
    
    # if do:
    #     return add1+f" (({n1} if {n1} is not None else -1) {op} ({n2} if {n2} is not None else -1))"+add2
    # else:
    #     return f"{n1} {op} {n2}"

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