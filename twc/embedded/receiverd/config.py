# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: config.py
# Compiled at: 2007-01-12 11:17:29
import receivere, twc.embedded.receiverd
from twccommon.embedded import Configuration

class Config(Configuration.Config):

    def addPortListener(self, desc, devIP, port):
        return receivere.addPortListener(desc, devIP, port)
        return

    def addMulticastPortListener(self, desc, groupIP, port, devIP=''):
        return receivere.addMulticastPortListener(desc, groupIP, port, devIP)
        return

    def setUDPDatagramTimeout(self, timeout):
        return receivere.setUDPDatagramTimeout(timeout)
        return

    def setPyCmdNamespace(self, ns):
        twc.embedded.receiverd._setPyCmdNamespace(ns)
        return

    def setRecvSize(self, rs):
        receivere.setRecvSize(rs)
        return

    def setTimeDriftThreshold(self, val):
        receivere.setTimeDriftThreshold(val)
        return

    def setTmpDir(self, dirName):
        receivere.setTmpDir(dirName)
        return

