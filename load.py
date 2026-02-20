import domesticpy.plugin.playman.playCmd.pm as pm
import socket
import os
import sys

pm.init(os.path.join(os.environ["RENDEREROOT"], "domesticpy", "conf", "playman.py"))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("localhost", 7245))