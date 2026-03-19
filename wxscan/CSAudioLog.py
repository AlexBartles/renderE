# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: CSAudioLog.py
# Compiled at: 2007-04-27 10:00:47
import twc, twc.EventLog as EventLog
_csaudiolog = None

def init(path, expir=3600):
    global _csaudiolog
    _csaudiolog = twc.EventLog.EventLog(path, expir)
    return


def write(event):
    _exists()
    _csaudiolog.write(event)
    return


def csaudiolog():
    _exists()
    return _csaudiolog
    return


def _exists():
    if _csaudiolog is None:
        raise Exception('CSAudioLog has not yet been defined')
    return

