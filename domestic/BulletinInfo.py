# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: BulletinInfo.py
# Compiled at: 2007-01-12 11:33:26
import time, twc, twc.psp, twc.dsmarshal, twccommon, twccommon.Log, sys
dsm = twc.dsmarshal
Log = twccommon.Log
CAT_WARNING = 3
CAT_WATCH = 2
CAT_ADVISORY = 1
BLUE_BKG = 0
YELLOW_BKG = 1
ORANGE_BKG = 2
RED_BKG = 3

class InvalidBulletin(Exception):

    def __init__(self, args=None):
        self.args = args
        return


def getPILs():
    """Get a list of all known pil and pil exyentions.
    return:
        A list of 2-element tuples, each containg a pil and a pil extention.
        Ex. [('TOR', '001'), ...]
    """
    data = dsm.defaultedConfigGet('interestlist.pil')
    if data == None:
        data = []
    return data
    return


def getBulletinProperties(pil, pilExt):
    """Get the properties for the specified pil and pilExt.
    params:
        pil    - The pil.
        pilExt - The pil extention.
    return:
        A structure containing data about the pil/pilExt including
        headline, color, priority, group, etc.
    exceptions:
        KeyError if either the pil or the pilExt is unknown.
    """
    data = dsm.defaultedConfigGet('pil.%s%s' % (pil, pilExt))
    if data == None:
        ver = dsm.getConfigVersion()
        raise KeyError("Config.%s.pil '%s%s' not found" % (ver, pil, pilExt))
    return data
    return


def validateBulletin(bulletin):
    try:
        getattr(bulletin, 'pil')
        getattr(bulletin, 'pilExt')
        getattr(bulletin, 'expiration')
        getattr(bulletin, 'text')
        getattr(bulletin, 'issueTime')
        getattr(bulletin, 'dispExpiration')
    except AttributeError as e:
        raise InvalidBulletin(str(e))

    return


def loadBulletin(primaryCounty, county, group):
    key = 'bulletin.%s.%d' % (county, group)
    bulletin = dsm.get(key)
    return loadValidateBulletin(bulletin, primaryCounty, county)
    return


def loadValidateBulletin(bulletin, primaryCounty, county):
    validateBulletin(bulletin)
    bulletinInfo = getBulletinProperties(bulletin.pil, bulletin.pilExt)
    text = getattr(bulletinInfo, 'text', None)
    if text:
        ns = {}
        ns.update(sys.modules)
        ns['bulletin'] = bulletin
        bulletinInfo.text = twc.psp.evalPage(text, ns)
    bulletin.__dict__.update(bulletinInfo.__dict__)
    bulletin.county = county
    bulletin.primary = bulletin.county == primaryCounty
    maxDispTime = getattr(bulletin, 'maxDispTime', None)
    if maxDispTime != None:
        now = time.time()
        bulletin.dispExpiration = min(now + maxDispTime, bulletin.dispExpiration)
    if getattr(bulletin, 'crawlGroup', None) == None:
        bulletin.crawlGroup = None
    return bulletin
    return


def loadActiveBulletins(interestlist):
    grps = {}
    for (pil, pilExt) in getPILs():
        grps[getBulletinProperties(pil, pilExt).group] = 1

    groups = grps.keys()
    bullKeys = []
    for county in interestlist:
        for group in groups:
            bullKeys.append('bulletin.%s.%d' % (county, group))

    bulls = []
    try:
        bulls = dsm.multiGet(bullKeys)
    except:
        pass

    bulletins = {}
    for county in interestlist:
        for group in groups:
            try:
                bull = bulls[0]
                bulls = bulls[1:]
                if bull:
                    bulletins[(county, group)] = loadValidateBulletin(bull, interestlist[0], county)
            except InvalidBulletin as e:
                Log.warning('invalid bulletin found for %s.%d: %s' % (county, group, e))

    return bulletins
    return


