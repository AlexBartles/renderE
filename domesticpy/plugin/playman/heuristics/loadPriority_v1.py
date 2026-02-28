# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: loadPriority_v1.py
# Compiled at: 2007-01-12 11:33:37
import twccommon
from domestic.Heuristic import *
_heuristic = None

class LoadHeuristic(Heuristic):

    def __init__(self, config):
        Heuristic.__init__(self, config)
        return

    def load(self, srcList, duration, dynPlist):
        runList = []
        curDuration = 0
        self.sortPriorityDisplay(srcList)
        while 1:
            (prodDuration, srcList, runList) = self._loadProduct(duration, dynPlist, srcList, runList)
            curDuration += prodDuration
            if prodDuration == 0 or curDuration >= duration:
                break

        return (curDuration, srcList, runList)
        return

    def _loadProduct(self, duration, dynPlist, srcList, runList):
        found = 0
        prodDuration = 0
        newSrcList = []
        for pe in srcList:
            if found or self.isExclusiveInList(pe[EXCL_POS], runList):
                newSrcList.append(pe)
                continue
            prod = dynPlist.getProduct(pe[PRODNM_POS])
            if prod == None:
                twccommon.Log.info("unable to load product '%s'" % pe[PRODNM_POS])
                continue
            if not prod.isValid():
                twccommon.Log.info("product '%s' is not valid" % pe[PRODNM_POS])
                continue
            if pe[PRODPG_POS]:
                if pe[PROD_POS]:
                    prodDuration = pe[DES_POS]
                else:
                    tmpList = []
                    for entry in srcList:
                        if entry[PRODNM_POS] == pe[PRODNM_POS]:
                            tmpList.append((entry[PRODPG_POS], entry[OPT_POS], entry[MAX_POS], entry[MIN_POS]))

                    pages = prod.getDesiredPageDurations(duration, tmpList, dynPlist)
                    for entry in srcList:
                        if entry[PRODNM_POS] == pe[PRODNM_POS]:
                            entry[PROD_POS] = prod
                            entry[DES_POS] = pages[entry[PRODPG_POS] - 1]

                    prodDuration = pe[DES_POS]
            else:
                prodDuration = prod.getDesiredDuration(pe[OPT_POS], pe[MAX_POS], pe[MIN_POS], duration, dynPlist)
            if prodDuration:
                if prodDuration <= pe[MAX_POS] and prodDuration >= pe[MIN_POS]:
                    pe[PROD_POS] = prod
                    pe[CUR_POS] = prodDuration
                    pe[DES_POS] = prodDuration
                    runList.append(pe)
                    self.debug(runList, 'runlist during load():')
                    found = 1
                else:
                    twccommon.Log.info("invalid desired duration(%d) max(%d) min(%d) - product '%s'" % (prodDuration, pe[MAX_POS], pe[MIN_POS], pe[PRODNM_POS]))
            else:
                twccommon.Log.info("zero desired duration - product '%s'" % pe[PRODNM_POS])

        return (prodDuration, newSrcList, runList)
        return


def init(config):
    global _heuristic
    _heuristic = LoadHeuristic(config)
    return


def heuristic():
    return _heuristic
    return

