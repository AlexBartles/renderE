# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: run.py
# Compiled at: 2007-01-12 11:33:37
import os.path, getopt, time, sys
import socket
import json

class Data:
    """An empty data structure.  Useful for data structures with dynamic
    member fields, i.e. adding new member variables at run time.
    """

    def __init__(self, other=None, **kw):
        self.update(other, **kw)
        return

    def __repr__(self):
        c = self.__class__
        s = '%s.%s(' % (c.__module__, c.__name__)
        for (k, v) in self.__dict__.items():
            s += '%s=%s, ' % (k, repr(v))

        s += ')'
        return s
        return

    def update(self, other=None, **kw):
        if other != None:
            self.__dict__.update(other.__dict__)
        self.__dict__.update(kw)
        return

    def clone(self):
        other = Data()
        other.update(self)
        return other
        return

def main():
    id = 0
    stime = 0
    frame = 0
    (opts, args_proper) = getopt.getopt(sys.argv[1:], '', ['id='])
    for (opt, val) in opts:
        if opt == '--id':
            id = int(val)

    prodType = args_proper[0]
    if len(args_proper) > 1:
        stime = int(args_proper[1])
        if len(args_proper) > 2:
            frame = int(args_proper[2])
    if stime == 0:
        stime = int(time.time())
    d = Data()
    d.id = id
    d.time = stime
    d.frame = frame
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 7245))
    sock.sendall(("jsonrun " + prodType + " "+json.dumps(d.__dict__)).encode())
    sock.close()
    return 0
    return


if __name__ == '__main__':
    sys.exit(main())
