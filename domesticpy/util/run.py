# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: run.py
# Compiled at: 2007-01-12 11:33:37
import os.path, getopt, time, sys
from omniORB import CORBA
import twc, twc.DataStoreInterface, twc.corba, twccommon, twccommon.corba
from domestic import wxdata
ds = twc.DataStoreInterface

def main():
    orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
    twccommon.corba.setOrb(orb)
    twccommon.Log.setIdent(os.path.basename(sys.argv[0]))
    ds.init()
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
    d = twccommon.Data()
    d.id = id
    d.time = stime
    d.frame = frame
    wxdata.runData(prodType, d)
    ds.uninit()
    return 0
    return


if __name__ == '__main__':
    sys.exit(main())
