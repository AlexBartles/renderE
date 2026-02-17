import os
import sys
import json
from itertools import batched

if len(sys.argv) < 2:
    print("usage: python loadi1datastore.py /path/to/ds/files/")
    print("remember to have both ds.dat and ds.stat in the folder!")
    print("on the i1, these are in /usr/twc/domestic/data/datastore/")
    sys.exit(1)

dsdict = {}

directory = sys.argv[1]
if not os.path.exists(directory):
    print("directory does not exist!")
    sys.exit(1)

datpath = os.path.join(directory, "ds.dat")
statpath = os.path.join(directory, "ds.stat")
if not os.path.exists(datpath):
    print("missing ds.dat!")

if not os.path.exists(statpath):
    print("missing ds.stat!")

if not (os.path.exists(datpath) and os.path.exists(statpath)):
    sys.exit(1)

def chunk_data(data, size):
    for i in range(0, len(data), size):
        yield data[i:i + size]

for file in [datpath, statpath]:
    with open(file) as f:
        data = f.read()

    filepos = 0
    while True:
        fs = "\x1c"
        nameix = data.find(fs, filepos)
        if nameix == -1:
            break
        name = data[filepos:nameix]
        filepos = nameix + 1
        
        valix = data.find(fs, filepos)
        if valix == -1:
            break
        
        val = data[filepos:valix]
        filepos = valix + 1
        
        expireix = data.find(fs, filepos)
        if expireix == -1:
            break
        
        expire = data[filepos:expireix]
        filepos = expireix + 1
        
        nextix = data.find("\n", filepos)
        filepos = nextix + 1
        
        dsdict[name] = val

with open("ds.json", "w") as f:
    f.write(json.dumps(dsdict, indent=4))
print("Success!")