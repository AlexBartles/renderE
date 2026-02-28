# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: LogInterfaceImpl.py
# Compiled at: 2006-04-03 09:02:55
import _twc, twccommon.Log

class InterfaceImpl:
    """Log using embedded C++ intrinsics so that log calls from 
    C++ code and embedded python interpreter are processed the same.
    (Avoids having 2 sets of log level functions, etc.)
    """

    def setIdent(self, ident):
        """ HAHAHAHA! """
        return

    def setLevel(self, level):
        _twc.setLogLevel(level)
        return

    def critical(self, msg):
        _twc.logItem(twccommon.Log.CRIT, msg)
        return

    def error(self, msg):
        _twc.logItem(twccommon.Log.ERR, msg)
        return

    def warning(self, msg):
        _twc.logItem(twccommon.Log.WARN, msg)
        return

    def info(self, msg):
        _twc.logItem(twccommon.Log.INFO, msg)
        return

    def debug(self, msg):
        _twc.logItem(twccommon.Log.DBG, msg)
        return


return
