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
