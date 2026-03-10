# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: Configuration.py
# Compiled at: 2006-04-03 09:02:55
import os, twccommon.embedded, twccommon.Log, rendereglobals

def execfile(filename, globa, loca):
    with open(filename, "r", encoding="windows-1252") as f:
        exec(compile(f.read(), filename, 'exec'), globa, loca)

class Config:
    """Le Config Base Class"""
    localConfDepth = 0

    def __init__(self):
        twccommon.embedded.setconfclass(self)
        self.pidFileDir = None
        self.workDir = None
        self.systemDataDir = None
        self.appName = ""
        return

    def _finalize(self):
        rendereglobals.configs[self,]
        return

    def setPidFileDir(self, dir):
        self.pidFileDir = dir
        return

    def setWorkDir(self, dir):
        """Sets the work directory for the current process"""
        self.workDir = dir
        return

    def getWorkDir(self):
        """Returns the work directory for the current process"""
        return self.workDir

    def getSystemDataDir(self):
        """Gets the system data directory"""
        return self.systemDataDir

    def setLogLevel(self, level):
        """Sets the current logging level"""
        return

    def setLogDir(self, dir):
        """Sets directory to write application log"""
        return

    def setLogFlushAfterWrite(self, flushAfterWrite):
        """Set to non zero to cause the log to be flushed to disk after every
        write."""
        return

    def setChannel(self, channel):
        """Sets the name of the event channel to use (if appropriate)"""
        return

    def setChannelFactory(self, factory):
        """Sets the name of the event channel factory for creating new ones"""
        return

    def setAppName(self, name):
        """Sets the name of the application (in case default isnt good enuf"""
        twccommon.Log.setIdent(name)
        self.appName = name
        return

    def doLocalConfig(self, filename):
        """Runs local configuration.  Do NOT call this from a local conf file
        or else it will complain bitterly that you are stupid!"""
        Config.localConfDepth = Config.localConfDepth + 1
        if Config.localConfDepth > 1:
            raise RuntimeError('User Error: Do NOT call doLocalConfig ' + 'within a local conf file (FOOL!!!)!')
        localPath = os.environ['TWCROOT']
        localPath = localPath + '/local_conf/'
        script = localPath + filename
        if os.path.exists(script):
            execfile(script)
        Config.localConfDepth = Config.localConfDepth - 1
        return

