# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: Heuristic.py
# Compiled at: 2007-01-12 11:33:26
import twccommon
DISP_POS = 0
PRI_POS = 1
PRODNM_POS = 2
PRODPG_POS = 3
PROD_POS = 4
CUR_POS = 5
DES_POS = 6
OPT_POS = 7
MAX_POS = 8
MIN_POS = 9
STEP_POS = 10
EXCL_POS = 11

def displayOrder(lst1, lst2):
    return twccommon.compare(lst1[DISP_POS], lst2[DISP_POS])
    return


def priorityDisplayOrder(lst1, lst2):
    result = twccommon.compare(lst1[PRI_POS], lst2[PRI_POS])
    if result:
        return result
    else:
        return twccommon.compare(lst1[DISP_POS], lst2[DISP_POS])
    return


class Heuristic:

    def __init__(self, config):
        self._config = config
        self._srcList = []
        self._runList = []
        return

    def debugProdEntry(self, pe):
        twccommon.Log.debug('%3d %3d %25s %4d %3d %3d %3d %3d %3d %3d %3d' % (pe[DISP_POS], pe[PRI_POS], pe[PRODNM_POS], pe[PRODPG_POS], pe[CUR_POS], pe[DES_POS], pe[OPT_POS], pe[MAX_POS], pe[MIN_POS], pe[STEP_POS], pe[EXCL_POS]))
        return

    def debug(self, list, msg=''):
        if len(msg):
            twccommon.Log.debug(msg)
        twccommon.Log.debug('DSP PRI          Product          Page CUR DES OPT MAX MIN STP EXC')
        for pe in list:
            self.debugProdEntry(pe)

        return

    def load(self, srcList, duration, dynamicPlaylist):
        raise Exception('load heuristic not implemented')
        return

    def reduce(self, curDuration, srcList, runList, duration, dynamicPlaylist):
        raise Exception('over heuristic not implemented')
        return

    def grow(self, curDuration, srcList, runList, duration, dynamicPlaylist):
        raise Exception('under heuristic not implemented')
        return

    def sortDisplay(self, list):
        list.sort(displayOrder)
        return

    def sortPriorityDisplay(self, list):
        list.sort(priorityDisplayOrder)
        return

    def isExclusiveInList(self, exclusive, list):
        result = 0
        if exclusive:
            for pe in list:
                if pe[EXCL_POS] == exclusive:
                    result = 1
                    break

        return result
        return


