# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: DataEventLog.py
# Compiled at: 2007-01-12 11:17:30
import twccommon, EventLog

class DataEventLog(EventLog.EventLog):

    def __init__(self, workfile, debug):
        self.debug = debug
        self.workFile = workfile
        self.__logMap = {}
        return

    def writeData(self, tag, event):
        if self.debug == 1:
            self._writeData(tag, event)
        return

    def _open(self):
        return open(self.workFile, 'w')
        return
