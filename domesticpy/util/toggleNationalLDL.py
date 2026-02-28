# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: toggleNationalLDL.py
# Compiled at: 2007-01-12 11:33:37
import os.path, sys
#import twc, twc.DataStoreInterface, twc.corba, twccommon.corba
import socket
#from domestic import wxdata
import json
ds = twc.DataStoreInterface

def apply(func, args, kwargs=None):
    return func(*args) if kwargs is None else func(*args, **kwargs)

def main():
    t = list(sys.argv[1:])
    #apply(wxdata.toggleNationalLDL, t)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 7245))
    sock.sendall(("togglenat", json.dumps(t)))
    return 0
    return


if __name__ == '__main__':
    sys.exit(main())
