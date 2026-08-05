# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: __init__.py
# Compiled at: 2007-01-12 11:17:29
import types, twc.dsmarshal, twc.DataStoreInterface, twc.InterestList, twccommon.Log
from . import _receiverd
ds = twc.DataStoreInterface
dsm = twc.dsmarshal

def abortMsg():
    raise _AbortMsgException
    return


def noInterest():
    global _fd
    global _msgId
    _receiverd.decrementInterest(_fd, _msgId)
    abortMsg()


def setMsgDesc(desc):
    _receiverd.setMsgDesc(_fd, _msgId, desc)


def assertValues(**kw):
    keys = kw.keys()
    try:
        for key in keys:
            val = dsm.get(key)
            if not _deepCompare(val, kw[key]):
                noInterest()

    except KeyError:
        noInterest()


def assertInterest(**kw):
    for (key, val) in kw.items():
        if not twc.InterestList.isInterestedItem(key, val):
            noInterest()

    return


def setTime(sec, millisec):
    return _receiverd.setTime(sec, millisec)
    return


_cmdNamespace = {}
_namespaces = {}
_fd = None
_msgId = None

class _AbortMsgException(Exception):

    def __init__(self, args=None):
        self.args = args
        return


def _setPyCmdNamespace(ns):
    global _cmdNamespace
    _cmdNamespace = ns
    return


def _createMsgNamespace(fd, msgId):
    global _namespaces
    ns = {}
    ns.update(_cmdNamespace)
    _namespaces[(fd, msgId)] = ns
    return


def _destroyMsgNamespace(fd, msgId):
    ns = _namespaces[(fd, msgId)]
    ns.clear()
    del _namespaces[(fd, msgId)]
    return


def _runCmdString(fd, msgId, cmd):
    global _fd
    global _msgId
    _fd = fd
    _msgId = msgId
    try:
        ns = _namespaces[(fd, msgId)]
        exec(cmd, ns, ns)
    except _AbortMsgException:
        _receiverd.abortMsg(fd, msgId)

    _fd = None
    _msgId = None
    ds.abort()
    return


def _deepCompare(a, b):
    if hasattr(a, "__dict__") and hasattr(b, "__dict__"):
        return a.__class__ == b.__class__ and a.__dict__ == b.__dict__
    else:
        return a == b
    return

