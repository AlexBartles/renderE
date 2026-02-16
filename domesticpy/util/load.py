# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: load.py
# Compiled at: 2007-01-12 11:33:37
import os.path, getopt, sys
import twc, twc.DataStoreInterface, twc.corba, twccommon.corba, twccommon
from domestic import wxdata
ds = twc.DataStoreInterface

def main():
    twccommon.Log.setIdent(os.path.basename(sys.argv[0]))
    ds.init()
    id = 0
    expire = 1200
    vbid = '000'
    logoId = None
    mediaNum = None
    flavor = None
    duration = 0
    durationFrames = 0
    (opts, args_proper) = getopt.getopt(sys.argv[1:], '', [6, 7, 8, 9, 10])
    for (opt, val) in opts:
        if opt == '--id':
            id = int(val)
        if opt == '--expire':
            expire = int(val)
        if opt == '--vbid':
            vbid = val
        if opt == '--logoId':
            logoId = val
        if opt == '--duration':
            duration = int(val)

    prodType = args_proper[0]
    d = twccommon.Data()
    d.id = id
    d.expire = expire
    if prodType == 'local':
        if len(args_proper) > 1:
            flavor = args_proper[1]
            if len(args_proper) > 2:
                if logoId == None:
                    logoId = args_proper[2]
        d.logoId = logoId
        d.flavor = flavor
        d.vbid = vbid
        if duration > 0:
            d.duration = duration * 30
    if prodType == 'tag':
        if len(args_proper) > 1:
            mediaNum = args_proper[1]
            if len(args_proper) > 2:
                duration = int(args_proper[2])
                if len(args_proper) > 3:
                    durationFrames = int(args_proper[3])
        d.mediaNum = mediaNum
        d.duration = duration
        d.durationFrames = durationFrames
    wxdata.loadData(prodType, d)
    ds.uninit()
    return 0
    return


if __name__ == '__main__':
    sys.exit(main())