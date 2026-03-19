# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: PageCounter.py
# Compiled at: 2007-04-27 10:00:47
import twc, twc.dsmarshal as dsm, twccommon.Log, wxscan

def estWeatherBulletinPages(params):
    global dsm
    charPerLine = 40
    linesPerPage = 8
    try:
        attribs = wxscan.getAttribs(params)
        key = 'headline.%s' % attribs.zone
        headlines = dsm.get(key)
    except:
        return 0

    if len(headlines) == 0:
        return 0
    totLines = len(headlines) - 1
    for hl in headlines:
        totLines = totLines + len(hl) / charPerLine + 1

    numPages = totLines / linesPerPage + 1
    twccommon.Log.info('Number of pages estimated: %d' % numPages)
    return numPages
    return

