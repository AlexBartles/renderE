# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: setBulletin.py
# Compiled at: 2007-01-12 11:33:37
import sys, time, types, getopt
import twc, twc.DataStoreInterface, twccommon.corba, domestic.wxdata
ds = twc.DataStoreInterface
now = str(int(time.time()))
p30 = str(int(time.time()) + 30)
p90 = str(int(time.time()) + 90)
LOPTS = [('ugc', 1, '   ', None, 'GAC067'), ('pil', 1, '   ', None, 'TOR'), ('pilExt', 0, '001', '001', ''), ('dispExpir', 0, 'i+30', p30, 'sec from issue, or sec since epoch'), ('expir', 0, 'i+90', p90, 'sec from issue, or sec since epoch'), ('text', 0, 'txt', 'txt', 'A Big Bad Tornado is coming'), ('qatext', 0, '   ', None, 'test case XYZ, issued at 2:13PM'), ('issueTime', 0, 'now', now, 'or sec from now, or sec-since-epoch')]
SOPTS = [('verbose', 'v', 'verbose - show the values set in this invocation')]

def getopts():
    lnameList = []
    optionDo = twc.Data()
    for (lname, required, eg, deflt, comment) in LOPTS:
        lnameList.append(lname + '=')
        setattr(optionDo, lname, deflt)

    snameStr = ''
    snameDict = {}
    for (sname, sletter, comment) in SOPTS:
        snameStr += sletter
        snameDict[sletter] = sname
        setattr(optionDo, sname, None)

    (opts, args) = getopt.getopt(sys.argv[1:], snameStr, lnameList)
    for (oname, val) in opts:
        if oname[0:2] == '--':
            setattr(optionDo, oname[2:], val)
        else:
            setattr(optionDo, snameDict[oname[1]], 1)

    for (lname, required, eg, deflt, comment) in LOPTS:
        if required == 1 and getattr(optionDo, lname) == None:
            print('\nYou forgot --%s%s' % (lname, '!'))
            printUsage()
            sys.exit()

    return (optionDo, args)
    return


def makeUtc(sec):
    s = int(sec)
    if s < 100000:
        s = int(time.time()) + s
    return s
    return


def exTm(utc):
    """Explain a time_t in a triplet suitable for printing out"""
    fmtStr = time.strftime('%H:%M:%S', time.localtime(utc))
    secFromNow = utc - time.time() + 1
    return (utc, fmtStr, secFromNow)
    return


def printUsage():
    print('')
    print('usage:        name      dflt         example')
    print('          ___________   ____     _______________________')
    for (lname, req, eg, deflt, cm) in LOPTS:
        print('\t %12s  %5s \t%s' % ('--' + lname, eg, cm))

    for (name, letter, cm) in SOPTS:
        print('\t\t%s\t\t%s' % ('-' + letter, cm))

    print("\t(all '--name' options require an arg, and '-x' options don't)")
    print('')
    sys.exit()
    return


def printValues(bull):
    print('pil and pilExt: ', bull.pil, bull.pilExt)
    print('bulletin text: ', bull.text)
    print('issue time: %d (%s, %2ds from now)' % exTm(bull.issueTime))
    print('disp expir: %d (%s, %2ds from now)' % exTm(bull.dispExpiration))
    print('expiration: %d (%s, %2ds from now)' % exTm(bull.expiration))
    return


def main():
    if len(sys.argv) == 1:
        printUsage()
    (opts, args) = getopts()
    bull = twc.Data()
    try:
        bull.pil = opts.pil
        bull.pilExt = opts.pilExt
        bull.text = opts.text
        bull.issueTime = int(opts.issueTime)
        bull.expiration = makeUtc(opts.expir)
        bull.dispExpiration = makeUtc(opts.dispExpir)
    except AttributeError:
        print('A required argument is missing')
        sys.exit()

    try:
        bull.qatext = opts.qatext
    except AttributeError:
        pass

    if opts.verbose:
        printValues(bull)
    ds.init()
    counties = domestic.wxdata.getBulletinInterestList(opts.ugc)
    for county in counties:
        domestic.wxdata.setBulletin(county, bull, bull.expiration)

    ds.uninit()
    return 0
    return


if __name__ == '__main__':
    sys.exit(main())
