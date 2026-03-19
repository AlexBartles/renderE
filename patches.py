import string
import time
import nethandler
import os
import rendereglobals as rg
import loadtools
string.__dict__["letters"] = string.ascii_letters
string.__dict__["find"] = (lambda s, f : s.find(f))
string.__dict__["upper"] = (lambda s : str(s).upper())
string.__dict__["lower"] = (lambda s : str(s).lower())
def rfix(s, o, n, count=-1):
    return s.replace(o, n, count)

def sfix(s, sep, maxsplit=-1):
    return s.split(sep, maxsplit)
string.__dict__["replace"] = rfix
string.__dict__["split"] = sfix
oldtime = time.struct_time

def unprint(stuff):
    lines = stuff.split("\n")
    finallines = []
    for l in lines:
        if l.strip().startswith("print"):
            continue
        finallines.append(l)
    return "\n".join(finallines)

from functools import reduce

oldmktime = time.mktime
def newmktime(struc):
    if type(struc) == list:
        return oldmktime(tuple(struc))
    return oldmktime(struc)
time.mktime = newmktime

def apply(func, args, kwargs=None):
    return func(*args) if kwargs is None else func(*args, **kwargs)

def newaccess(path, mode):
    if not os.path.exists(path):
        newpath = nethandler.requestNetAssetExt(path)
        if newpath:
            return True
        else:
            return False
    else:
        return os.access(path, mode)

def newstat(path):
    if path.startswith(os.path.join(os.path.dirname(os.path.abspath(__file__)), "net").replace("\\", "/")):
        return os.stat(path)
    if not os.access(path, os.R_OK):
        newpath = nethandler.requestNetAssetExt(path)
        if newpath:
            return os.stat(newpath)
        else:
            return os.stat(path)
    else:
        return os.stat(path)

rg.newaccess = newaccess
rg.newstat = newstat

def runrs(filename):
    crs = loadtools.compilers(filename)
    print(type(crs))
    ns = {"apply": apply, "newaccess": newaccess, "newstat": newstat}
    exec(crs.replace("os.stat", "newstat").replace("os.access", "newaccess"), ns, ns)

def runrsc(filename):
    dat = "global layerProps\n"
    with open(filename, "r") as f:
        dat += f.read()
    ns = {"apply": apply, "newaccess": newaccess, "newstat": newstat, "reduce": reduce}
    exec(compile(unprint(dat).replace("os.stat", "newstat").replace("os.access", "newaccess"), filename, "exec"), ns, ns)

rg.runrsfunction = runrs
rg.runrscfunction = runrsc

#i've said it before but THIS is my most cursed python code
def yes_i_am_real_struct_time(seq=None, tm_year=0, tm_mon=0, tm_mday=0, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=0, tm_isdst=0):
    if seq:
        return oldtime(seq)
    return oldtime((tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst))
time.__dict__["struct_time"] = yes_i_am_real_struct_time