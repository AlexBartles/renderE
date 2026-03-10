import re

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
    rs = re.sub(ifpattern, _fix_if, rs)
    return rs

def fix_if(rs):
    fixed = re.sub(ifpattern, _fix_if, rs)
    return fixed