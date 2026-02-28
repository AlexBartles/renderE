# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: MiscCorbaInterfaceImpl.py
# Compiled at: 2007-01-12 11:17:30
import twccommon
import twccommon.corba, twccommon.corba.CosEventComm__POA, twc.corba.ClientCore
CHANNEL_IOR = 'corbaname::localhost:4000#%s'

class InterfaceImpl:

    def __init__(self):
        self._consumer = None
        self._renderd = None
        self._vspoold = None
        return

    def signalEvent(self, chanName, eventType, eventValue):
        if self._consumer == None:
            channel = twccommon.corba.getOrb().string_to_object(CHANNEL_IOR % (chanName,))
            admin = channel.for_suppliers()
            self._consumer = admin.obtain_push_consumer()
        try:
            event = twc.corba.ClientCore.Event(eventType, eventValue)
            any = CORBA.Any(CORBA.TypeCode(twc.corba.ClientCore.Event), event)
            self._consumer.push(any)
        except:
            self._consumer = None
            raise

        return

    def runRenderScript(self, rsName, host, port, nsName):
        if self._renderd == None:
            self._renderd = twccommon.corba.getOrb().string_to_object('corbaname::%s:%d#%s' % (host, port, nsName))
        try:
            self._renderd.execPresentationScript(rsName)
        except:
            self._renderd = None
            raise

        return

    def queueMovie(self, moviefile, host, port, nsName):
        if self._vspoold == None:
            self._vspoold = twccommon.corba.getOrb().string_to_object('corbaname::%s:%d#%s' % (host, port, nsName))
        try:
            self._vspoold.addFile(moviefile + '.mpg')
        except:
            self._vspoold = None
            raise

        return

    def setMovieLooping(self, val, host, port, nsName):
        if self._vspoold == None:
            self._vspoold = twccommon.corba.getOrb().string_to_object('corbaname::%s:%d#%s' % (host, port, nsName))
        try:
            self._vspoold.setLooping(val)
        except:
            self._vspoold = None
            raise

        return

    def flushMovies(self, host, port, nsName):
        if self._vspoold == None:
            self._vspoold = twccommon.corba.getOrb().string_to_object('corbaname::%s:%d#%s' % (host, port, nsName))
        try:
            self._vspoold.flush()
        except:
            self._vspoold = None
            raise

        return


