# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: underPriority_v1.py
# Compiled at: 2007-01-12 11:33:37
import twccommon
from domestic.Heuristic import *
_heuristic = None

class UnderHeuristic(Heuristic):

    def __init__(self, config):
        Heuristic.__init__(self, config)
        return

    def grow(self, curDuration, srcList, runList, duration, dynPlist):
        self.sortPriorityDisplay(srcList)
        self._srcList = srcList
        self.sortPriorityDisplay(runList)
        self._runList = runList
        curDuration = self._growByStepping(curDuration, duration)
        if curDuration < duration:
            curDuration = self._growByAddingProducts(curDuration, duration, dynPlist)
        return (curDuration, self._srcList, self._runList)
        return

    def _growByStepping(self, curDuration, duration):
        while curDuration < duration:
            adjusted = 0
            curPri = -1
            for pe in self._runList:
                if pe[CUR_POS] + pe[STEP_POS] <= pe[MAX_POS] and pe[STEP_POS]:
                    if curPri == -1:
                        curPri = pe[PRI_POS]
                    if pe[PRI_POS] != curPri:
                        break
                    if curDuration >= duration:
                        break
                    pe[CUR_POS] += pe[STEP_POS]
                    curDuration += pe[STEP_POS]
                    adjusted = 1
                    self.debug(self._runList, 'runlist during grow():')

            if adjusted == 0:
                break

        return curDuration
        return

    def _growByAddingProducts(self, curDuration, duration, dynPlist):
        while curDuration < duration:
            adjusted = 0
            newSrcList = []
            for pe in self._srcList:
                if adjusted or self.isExclusiveInList(pe[EXCL_POS], self._runList):
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
                        curDuration += prodDuration
                        self._runList.append(pe)
                        self.debug(self._runList, 'runlist during grow():')
                        adjusted = 1
                    else:
                        twccommon.Log.info("invalid desired duration(%d) max(%d) min(%d) - product '%s'" % (prodDuration, pe[MAX_POS], pe[MIN_POS], pe[PRODNM_POS]))
                else:
                    twccommon.Log.info("zero desired duration - product '%s'" % pe[PRODNM_POS])

            self._srcList = newSrcList
            if adjusted == 0:
                break

        return curDuration
        return


def init(config):
    global _heuristic
    _heuristic = UnderHeuristic(config)
    return


def heuristic():
    return _heuristic
    return

