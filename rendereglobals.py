import pyray as rl
import pygame as pg
import os
import json
import sys

pg.font.init()

sys.path.insert(0, os.path.dirname(__file__))

zzz = 10

layers = []
datastore = {}
if os.path.exists("ds.json"):
    with open("ds.json", "r") as f:
        datastore = json.loads(f.read())

#optionally, specify your environment vars here
#make sure to modify them to the actual paths
#you're expected to have the i1 files already
#also, this is untested so it may not work

os.environ["RENDERERSRC"] = ""
os.environ["RENDEREMEDIA"] = ""
os.environ["RENDEREDOMESTIC"] = ""
os.environ["RENDEREROOT"] = os.path.dirname(os.path.abspath(__file__))
os.environ["TWCCLIDIR"] = ""
os.environ["TWCPERSDIR"] = os.path.join(os.environ["RENDEREROOT"], "domesticpy")

#os.environ["RENDEREROOT"] = "/path/to/renderE"
#os.environ["RENDERERSRC"] = "/usr/local/twc/rsrc"
#os.environ["RENDEREMEDIA"] = "/media"
#os.environ["RENDEREDOMESTIC"] = "/usr/twc/domestic"
#os.environ["TWCCLIDIR"] = "/usr/twc"
#os.environ["TWCPERSDIR"] = "/path/to/renderE/domesticpy"