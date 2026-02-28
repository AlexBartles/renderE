# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: overPriority_v1.py
# Compiled at: 2007-01-12 11:33:37
import twccommon
from domestic.Heuristic import *
_heuristic = None

class OverHeuristic(Heuristic):

    def __init__(self, config):
        Heuristic.__init__(self, config)
        return

    def reduce(self, curDuration, srcList, runList, duration, dynPlist):
        self._srcList = srcList
        self.sortPriorityDisplay(runList)
        runList.reverse()
        self._runList = runList
        curDuration = self._reduceByStepping(curDuration, duration)
        if curDuration > duration:
            curDuration = self._reduceByRemovingProducts(curDuration, duration)
        return (curDuration, self._srcList, self._runList)
        return

    def _reduceByStepping(self, curDuration, duration):
        zeroDuration = 0
        while curDuration > duration:
            adjusted = 0
            curPri = -1
            for pe in self._runList:
                if pe[CUR_POS] - pe[STEP_POS] >= pe[MIN_POS] and pe[STEP_POS]:
                    if curPri == -1:
                        curPri = pe[PRI_POS]
                    if pe[PRI_POS] != curPri:
                        break
                    if curDuration <= duration:
                        break
                    pe[CUR_POS] -= pe[STEP_POS]
                    if pe[CUR_POS] == 0:
                        zeroDuration = 1
                    curDuration -= pe[STEP_POS]
                    adjusted = 1
                    self.debug(self._runList, 'runlist during reduce():')

            if adjusted == 0:
                break

        if zeroDuration:
            newRunList = []
            for pe in self._runList:
                if pe[CUR_POS]:
                    newRunList.append(pe)

            self._runList = newRunList
        return curDuration
        return

    def _reduceByRemovingProducts(self, curDuration, duration):
        while curDuration > duration:
            adjusted = 0
            runListLen = len(self._runList)
            if runListLen:
                pe = self._runList[0]
                curDuration -= pe[CUR_POS]
                adjusted = 1
                newRunList = self._runList[1:]
                self._runList = newRunList
                self.debug(self._runList, 'runlist during reduce():')
            else:
                break

        return curDuration
        return


def init(config):
    global _heuristic
    _heuristic = OverHeuristic(config)
    return


def heuristic():
    return _heuristic
    return


