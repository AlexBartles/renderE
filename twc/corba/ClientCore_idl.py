# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: ClientCore_idl.py
# Compiled at: 2007-01-12 11:19:12
import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA
_omnipy.checkVersion(0, 5, __file__)
__name__ = 'twc.corba.ClientCore'
_0_ClientCore = omniORB.openModule('twc.corba.ClientCore', '/n/azmo/ud2/jmjones/svn/se/personality/domestic/release/v1.11p1/upgrade/work/domestic_upgrade/work/autobuild/twc_istar-2.6_p1/pkg/work/istar/src/pythonlib/twc/corba/../../../lib/twc_client/ClientCoreBase.idl')
_0_ClientCore__POA = omniORB.openModule('twc.corba.ClientCore__POA', '/n/azmo/ud2/jmjones/svn/se/personality/domestic/release/v1.11p1/upgrade/work/domestic_upgrade/work/autobuild/twc_istar-2.6_p1/pkg/work/istar/src/pythonlib/twc/corba/../../../lib/twc_client/ClientCoreBase.idl')

class StringList:
    _NP_RepositoryId = 'IDL:ClientCore/StringList:1.0'

    def __init__(self):
        raise RuntimeError('Cannot construct objects of this type.')
        return


_0_ClientCore.StringList = StringList
_0_ClientCore._d_StringList = (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string, 0), 0)
_0_ClientCore._ad_StringList = (omniORB.tcInternal.tv_alias, StringList._NP_RepositoryId, 'StringList', (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string, 0), 0))
_0_ClientCore._tc_StringList = omniORB.tcInternal.createTypeCode(_0_ClientCore._ad_StringList)
omniORB.registerType(StringList._NP_RepositoryId, _0_ClientCore._ad_StringList, _0_ClientCore._tc_StringList)
del StringList
__name__ = 'twc.corba.twc.corba.ClientCore_idl'
__name__ = 'twc.corba.ClientCore'
_0_ClientCore = omniORB.openModule('twc.corba.ClientCore', '/n/azmo/ud2/jmjones/svn/se/personality/domestic/release/v1.11p1/upgrade/work/domestic_upgrade/work/autobuild/twc_istar-2.6_p1/pkg/work/istar/src/pythonlib/twc/corba/../../../lib/twc_client/DataStoreSession.idl')
_0_ClientCore__POA = omniORB.openModule('twc.corba.ClientCore__POA', '/n/azmo/ud2/jmjones/svn/se/personality/domestic/release/v1.11p1/upgrade/work/domestic_upgrade/work/autobuild/twc_istar-2.6_p1/pkg/work/istar/src/pythonlib/twc/corba/../../../lib/twc_client/DataStoreSession.idl')
_0_ClientCore._d_DataStoreSession = (omniORB.tcInternal.tv_objref, 'IDL:ClientCore/DataStoreSession:1.0', 'DataStoreSession')
_0_ClientCore.DataStoreSession = omniORB.newEmptyClass()

class DataStoreSession:
    _NP_RepositoryId = _0_ClientCore._d_DataStoreSession[1]

    def __init__(self):
        raise RuntimeError('Cannot construct objects of this type.')
        return

    _nil = CORBA.Object._nil
    _0_ClientCore.DataStoreSession.TransactionSizeExceeded = omniORB.newEmptyClass()

    class TransactionSizeExceeded(CORBA.UserException):
        _NP_RepositoryId = 'IDL:ClientCore/DataStoreSession/TransactionSizeExceeded:1.0'

    _d_TransactionSizeExceeded = (omniORB.tcInternal.tv_except, TransactionSizeExceeded, TransactionSizeExceeded._NP_RepositoryId, 'TransactionSizeExceeded')
    _tc_TransactionSizeExceeded = omniORB.tcInternal.createTypeCode(_d_TransactionSizeExceeded)
    omniORB.registerType(TransactionSizeExceeded._NP_RepositoryId, _d_TransactionSizeExceeded, _tc_TransactionSizeExceeded)
    _0_ClientCore.DataStoreSession.Entry = omniORB.newEmptyClass()

    class Entry:
        _NP_RepositoryId = 'IDL:ClientCore/DataStoreSession/Entry:1.0'

        def __init__(self, key, data, expir):
            self.key = key
            self.data = data
            self.expir = expir
            return

    _d_Entry = _0_ClientCore.DataStoreSession._d_Entry = (omniORB.tcInternal.tv_struct, Entry, Entry._NP_RepositoryId, 'Entry', 'key', (omniORB.tcInternal.tv_string, 0), 'data', (omniORB.tcInternal.tv_string, 0), 'expir', omniORB.tcInternal.tv_long)
    _tc_Entry = omniORB.tcInternal.createTypeCode(_d_Entry)
    omniORB.registerType(Entry._NP_RepositoryId, _d_Entry, _tc_Entry)

    class EntryList:
        _NP_RepositoryId = 'IDL:ClientCore/DataStoreSession/EntryList:1.0'

        def __init__(self):
            raise RuntimeError('Cannot construct objects of this type.')
            return

    _d_EntryList = (omniORB.tcInternal.tv_sequence, _d_Entry, 0)
    _ad_EntryList = (omniORB.tcInternal.tv_alias, EntryList._NP_RepositoryId, 'EntryList', (omniORB.tcInternal.tv_sequence, _d_Entry, 0))
    _tc_EntryList = omniORB.tcInternal.createTypeCode(_ad_EntryList)
    omniORB.registerType(EntryList._NP_RepositoryId, _ad_EntryList, _tc_EntryList)
    _0_ClientCore.DataStoreSession.Value = omniORB.newEmptyClass()

    class Value:
        _NP_RepositoryId = 'IDL:ClientCore/DataStoreSession/Value:1.0'

        def __init__(self, valid, data):
            self.valid = valid
            self.data = data
            return

    _d_Value = _0_ClientCore.DataStoreSession._d_Value = (omniORB.tcInternal.tv_struct, Value, Value._NP_RepositoryId, 'Value', 'valid', omniORB.tcInternal.tv_boolean, 'data', (omniORB.tcInternal.tv_string, 0))
    _tc_Value = omniORB.tcInternal.createTypeCode(_d_Value)
    omniORB.registerType(Value._NP_RepositoryId, _d_Value, _tc_Value)

    class ValueList:
        _NP_RepositoryId = 'IDL:ClientCore/DataStoreSession/ValueList:1.0'

        def __init__(self):
            raise RuntimeError('Cannot construct objects of this type.')
            return

    _d_ValueList = (omniORB.tcInternal.tv_sequence, _d_Value, 0)
    _ad_ValueList = (omniORB.tcInternal.tv_alias, ValueList._NP_RepositoryId, 'ValueList', (omniORB.tcInternal.tv_sequence, _d_Value, 0))
    _tc_ValueList = omniORB.tcInternal.createTypeCode(_ad_ValueList)
    omniORB.registerType(ValueList._NP_RepositoryId, _ad_ValueList, _tc_ValueList)


_0_ClientCore.DataStoreSession = DataStoreSession
_0_ClientCore._tc_DataStoreSession = omniORB.tcInternal.createTypeCode(_0_ClientCore._d_DataStoreSession)
omniORB.registerType(DataStoreSession._NP_RepositoryId, _0_ClientCore._d_DataStoreSession, _0_ClientCore._tc_DataStoreSession)
DataStoreSession._d_get = ((_0_ClientCore._d_StringList,), (_0_ClientCore.DataStoreSession._d_ValueList,), None)
DataStoreSession._d_set = ((_0_ClientCore.DataStoreSession._d_EntryList,), (), {(_0_ClientCore.DataStoreSession.TransactionSizeExceeded._NP_RepositoryId): (_0_ClientCore.DataStoreSession._d_TransactionSizeExceeded)})
DataStoreSession._d_remove = ((_0_ClientCore._d_StringList,), (), {(_0_ClientCore.DataStoreSession.TransactionSizeExceeded._NP_RepositoryId): (_0_ClientCore.DataStoreSession._d_TransactionSizeExceeded)})
DataStoreSession._d_commit = ((), (), None)
DataStoreSession._d_abort = ((), (), None)

class _objref_DataStoreSession(CORBA.Object):
    _NP_RepositoryId = DataStoreSession._NP_RepositoryId

    def __del__(self):
        if _omnipy is not None:
            _omnipy.releaseObjref(self)
        return

    def get(self, *args):
        return _omnipy.invoke(self, 'get', _0_ClientCore.DataStoreSession._d_get, args)
        return

    def set(self, *args):
        return _omnipy.invoke(self, 'set', _0_ClientCore.DataStoreSession._d_set, args)
        return

    def remove(self, *args):
        return _omnipy.invoke(self, 'remove', _0_ClientCore.DataStoreSession._d_remove, args)
        return

    def commit(self, *args):
        return _omnipy.invoke(self, 'commit', _0_ClientCore.DataStoreSession._d_commit, args)
        return

    def abort(self, *args):
        return _omnipy.invoke(self, 'abort', _0_ClientCore.DataStoreSession._d_abort, args)
        return

    __methods__ = [7, 8, 9, 10, 11] + CORBA.Object.__methods__


omniORB.registerObjref(DataStoreSession._NP_RepositoryId, _objref_DataStoreSession)
_0_ClientCore._objref_DataStoreSession = _objref_DataStoreSession
del DataStoreSession
del _objref_DataStoreSession
__name__ = 'twc.corba.ClientCore__POA'

class DataStoreSession(PortableServer.Servant):
    _NP_RepositoryId = _0_ClientCore.DataStoreSession._NP_RepositoryId

    def __del__(self):
        if _omnipy is not None:
            _omnipy.releaseObjref(self)
        return

    _omni_op_d = {'get': (_0_ClientCore.DataStoreSession._d_get), 'set': (_0_ClientCore.DataStoreSession._d_set), 'remove': (_0_ClientCore.DataStoreSession._d_remove), 'commit': (_0_ClientCore.DataStoreSession._d_commit), 'abort': (_0_ClientCore.DataStoreSession._d_abort)}


DataStoreSession._omni_skeleton = DataStoreSession
_0_ClientCore__POA.DataStoreSession = DataStoreSession
del DataStoreSession
__name__ = 'twc.corba.ClientCore'
__name__ = 'twc.corba.twc.corba.ClientCore_idl'
__name__ = 'twc.corba.ClientCore'
_0_ClientCore = omniORB.openModule('twc.corba.ClientCore', '/n/azmo/ud2/jmjones/svn/se/personality/domestic/release/v1.11p1/upgrade/work/domestic_upgrade/work/autobuild/twc_istar-2.6_p1/pkg/work/istar/src/pythonlib/twc/corba/../../../lib/twc_client/DataStore.idl')
_0_ClientCore__POA = omniORB.openModule('twc.corba.ClientCore__POA', '/n/azmo/ud2/jmjones/svn/se/personality/domestic/release/v1.11p1/upgrade/work/domestic_upgrade/work/autobuild/twc_istar-2.6_p1/pkg/work/istar/src/pythonlib/twc/corba/../../../lib/twc_client/DataStore.idl')
_0_ClientCore._d_DataStore = (omniORB.tcInternal.tv_objref, 'IDL:ClientCore/DataStore:1.0', 'DataStore')
_0_ClientCore.DataStore = omniORB.newEmptyClass()

class DataStore:
    _NP_RepositoryId = _0_ClientCore._d_DataStore[1]

    def __init__(self):
        raise RuntimeError('Cannot construct objects of this type.')
        return

    _nil = CORBA.Object._nil


_0_ClientCore.DataStore = DataStore
_0_ClientCore._tc_DataStore = omniORB.tcInternal.createTypeCode(_0_ClientCore._d_DataStore)
omniORB.registerType(DataStore._NP_RepositoryId, _0_ClientCore._d_DataStore, _0_ClientCore._tc_DataStore)
DataStore._d_checkDataFile = ((), (), None)
DataStore._d_startSession = ((), (_0_ClientCore._d_DataStoreSession,), None)
DataStore._d_endSession = ((_0_ClientCore._d_DataStoreSession,), (), None)

class _objref_DataStore(CORBA.Object):
    _NP_RepositoryId = DataStore._NP_RepositoryId

    def __del__(self):
        if _omnipy is not None:
            _omnipy.releaseObjref(self)
        return

    def checkDataFile(self, *args):
        return _omnipy.invoke(self, 'checkDataFile', _0_ClientCore.DataStore._d_checkDataFile, args)
        return

    def startSession(self, *args):
        return _omnipy.invoke(self, 'startSession', _0_ClientCore.DataStore._d_startSession, args)
        return

    def endSession(self, *args):
        return _omnipy.invoke(self, 'endSession', _0_ClientCore.DataStore._d_endSession, args)
        return

    __methods__ = ['checkDataFile', 'startSession', 'endSession'] + CORBA.Object.__methods__


omniORB.registerObjref(DataStore._NP_RepositoryId, _objref_DataStore)
_0_ClientCore._objref_DataStore = _objref_DataStore
del DataStore
del _objref_DataStore
__name__ = 'twc.corba.ClientCore__POA'

class DataStore(PortableServer.Servant):
    _NP_RepositoryId = _0_ClientCore.DataStore._NP_RepositoryId

    def __del__(self):
        if _omnipy is not None:
            _omnipy.releaseObjref(self)
        return

    _omni_op_d = {'checkDataFile': (_0_ClientCore.DataStore._d_checkDataFile), 'startSession': (_0_ClientCore.DataStore._d_startSession), 'endSession': (_0_ClientCore.DataStore._d_endSession)}


DataStore._omni_skeleton = DataStore
_0_ClientCore__POA.DataStore = DataStore
del DataStore
__name__ = 'twc.corba.ClientCore'
__name__ = 'twc.corba.twc.corba.ClientCore_idl'
__name__ = 'twc.corba.ClientCore'
_0_ClientCore = omniORB.openModule('twc.corba.ClientCore', '/n/azmo/ud2/jmjones/svn/se/personality/domestic/release/v1.11p1/upgrade/work/domestic_upgrade/work/autobuild/twc_istar-2.6_p1/pkg/work/istar/src/pythonlib/twc/corba/../../../lib/twc_client/Renderd.idl')
_0_ClientCore__POA = omniORB.openModule('twc.corba.ClientCore__POA', '/n/azmo/ud2/jmjones/svn/se/personality/domestic/release/v1.11p1/upgrade/work/domestic_upgrade/work/autobuild/twc_istar-2.6_p1/pkg/work/istar/src/pythonlib/twc/corba/../../../lib/twc_client/Renderd.idl')
_0_ClientCore._d_Renderd = (omniORB.tcInternal.tv_objref, 'IDL:ClientCore/Renderd:1.0', 'Renderd')
_0_ClientCore.Renderd = omniORB.newEmptyClass()

class Renderd:
    _NP_RepositoryId = _0_ClientCore._d_Renderd[1]

    def __init__(self):
        raise RuntimeError('Cannot construct objects of this type.')
        return

    _nil = CORBA.Object._nil


_0_ClientCore.Renderd = Renderd
_0_ClientCore._tc_Renderd = omniORB.tcInternal.createTypeCode(_0_ClientCore._d_Renderd)
omniORB.registerType(Renderd._NP_RepositoryId, _0_ClientCore._d_Renderd, _0_ClientCore._tc_Renderd)
Renderd._d_activateLayer = (((omniORB.tcInternal.tv_string, 0),), (), None)
Renderd._d_deactivateLayer = (((omniORB.tcInternal.tv_string, 0),), (), None)
Renderd._d_removeLayer = (((omniORB.tcInternal.tv_string, 0),), (), None)
Renderd._d_execPresentationScript = (((omniORB.tcInternal.tv_string, 0),), (), None)
Renderd._d_execPythonCommand = (((omniORB.tcInternal.tv_string, 0),), (), None)

class _objref_Renderd(CORBA.Object):
    _NP_RepositoryId = Renderd._NP_RepositoryId

    def __del__(self):
        if _omnipy is not None:
            _omnipy.releaseObjref(self)
        return

    def activateLayer(self, *args):
        return _omnipy.invoke(self, 'activateLayer', _0_ClientCore.Renderd._d_activateLayer, args)
        return

    def deactivateLayer(self, *args):
        return _omnipy.invoke(self, 'deactivateLayer', _0_ClientCore.Renderd._d_deactivateLayer, args)
        return

    def removeLayer(self, *args):
        return _omnipy.invoke(self, 'removeLayer', _0_ClientCore.Renderd._d_removeLayer, args)
        return

    def execPresentationScript(self, *args):
        return _omnipy.invoke(self, 'execPresentationScript', _0_ClientCore.Renderd._d_execPresentationScript, args)
        return

    def execPythonCommand(self, *args):
        return _omnipy.invoke(self, 'execPythonCommand', _0_ClientCore.Renderd._d_execPythonCommand, args)
        return

    __methods__ = [7, 8, 9, 10, 11] + CORBA.Object.__methods__


omniORB.registerObjref(Renderd._NP_RepositoryId, _objref_Renderd)
_0_ClientCore._objref_Renderd = _objref_Renderd
del Renderd
del _objref_Renderd
__name__ = 'twc.corba.ClientCore__POA'

class Renderd(PortableServer.Servant):
    _NP_RepositoryId = _0_ClientCore.Renderd._NP_RepositoryId

    def __del__(self):
        if _omnipy is not None:
            _omnipy.releaseObjref(self)
        return

    _omni_op_d = {'activateLayer': (_0_ClientCore.Renderd._d_activateLayer), 'deactivateLayer': (_0_ClientCore.Renderd._d_deactivateLayer), 'removeLayer': (_0_ClientCore.Renderd._d_removeLayer), 'execPresentationScript': (_0_ClientCore.Renderd._d_execPresentationScript), 'execPythonCommand': (_0_ClientCore.Renderd._d_execPythonCommand)}


Renderd._omni_skeleton = Renderd
_0_ClientCore__POA.Renderd = Renderd
del Renderd
__name__ = 'twc.corba.ClientCore'
__name__ = 'twc.corba.twc.corba.ClientCore_idl'
__name__ = 'twc.corba.ClientCore'
_0_ClientCore = omniORB.openModule('twc.corba.ClientCore', '/n/azmo/ud2/jmjones/svn/se/personality/domestic/release/v1.11p1/upgrade/work/domestic_upgrade/work/autobuild/twc_istar-2.6_p1/pkg/work/istar/src/pythonlib/twc/corba/../../../lib/twc_client/Event.idl')
_0_ClientCore__POA = omniORB.openModule('twc.corba.ClientCore__POA', '/n/azmo/ud2/jmjones/svn/se/personality/domestic/release/v1.11p1/upgrade/work/domestic_upgrade/work/autobuild/twc_istar-2.6_p1/pkg/work/istar/src/pythonlib/twc/corba/../../../lib/twc_client/Event.idl')
_0_ClientCore.Event = omniORB.newEmptyClass()

class Event:
    _NP_RepositoryId = 'IDL:ClientCore/Event:1.0'

    def __init__(self, type, value):
        self.type = type
        self.value = value
        return


_0_ClientCore.Event = Event
_0_ClientCore._d_Event = (omniORB.tcInternal.tv_struct, Event, Event._NP_RepositoryId, 'Event', 'type', (omniORB.tcInternal.tv_string, 0), 'value', (omniORB.tcInternal.tv_string, 0))
_0_ClientCore._tc_Event = omniORB.tcInternal.createTypeCode(_0_ClientCore._d_Event)
omniORB.registerType(Event._NP_RepositoryId, _0_ClientCore._d_Event, _0_ClientCore._tc_Event)
del Event
__name__ = 'twc.corba.twc.corba.ClientCore_idl'
__name__ = 'twc.corba.ClientCore'
_0_ClientCore = omniORB.openModule('twc.corba.ClientCore', '/n/azmo/ud2/jmjones/svn/se/personality/domestic/release/v1.11p1/upgrade/work/domestic_upgrade/work/autobuild/twc_istar-2.6_p1/pkg/work/istar/src/pythonlib/twc/corba/../../../lib/twc_client/GpiInterface.idl')
_0_ClientCore__POA = omniORB.openModule('twc.corba.ClientCore__POA', '/n/azmo/ud2/jmjones/svn/se/personality/domestic/release/v1.11p1/upgrade/work/domestic_upgrade/work/autobuild/twc_istar-2.6_p1/pkg/work/istar/src/pythonlib/twc/corba/../../../lib/twc_client/GpiInterface.idl')
_0_ClientCore._d_GpiInterface = (omniORB.tcInternal.tv_objref, 'IDL:ClientCore/GpiInterface:1.0', 'GpiInterface')
_0_ClientCore.GpiInterface = omniORB.newEmptyClass()

class GpiInterface:
    _NP_RepositoryId = _0_ClientCore._d_GpiInterface[1]

    def __init__(self):
        raise RuntimeError('Cannot construct objects of this type.')
        return

    _nil = CORBA.Object._nil
    _0_ClientCore.GpiInterface.InvalidPin = omniORB.newEmptyClass()

    class InvalidPin(CORBA.UserException):
        _NP_RepositoryId = 'IDL:ClientCore/GpiInterface/InvalidPin:1.0'

        def __init__(self, pin, numPins):
            CORBA.UserException.__init__(self, pin, numPins)
            self.pin = pin
            self.numPins = numPins
            return

    _d_InvalidPin = (omniORB.tcInternal.tv_except, InvalidPin, InvalidPin._NP_RepositoryId, 'InvalidPin', 'pin', omniORB.tcInternal.tv_ushort, 'numPins', omniORB.tcInternal.tv_ushort)
    _tc_InvalidPin = omniORB.tcInternal.createTypeCode(_d_InvalidPin)
    omniORB.registerType(InvalidPin._NP_RepositoryId, _d_InvalidPin, _tc_InvalidPin)


_0_ClientCore.GpiInterface = GpiInterface
_0_ClientCore._tc_GpiInterface = omniORB.tcInternal.createTypeCode(_0_ClientCore._d_GpiInterface)
omniORB.registerType(GpiInterface._NP_RepositoryId, _0_ClientCore._d_GpiInterface, _0_ClientCore._tc_GpiInterface)
GpiInterface._d_numPins = ((), (omniORB.tcInternal.tv_ushort,), None)
GpiInterface._d_activate = ((omniORB.tcInternal.tv_ushort,), (), {(_0_ClientCore.GpiInterface.InvalidPin._NP_RepositoryId): (_0_ClientCore.GpiInterface._d_InvalidPin)})
GpiInterface._d_deactivate = ((omniORB.tcInternal.tv_ushort,), (), {(_0_ClientCore.GpiInterface.InvalidPin._NP_RepositoryId): (_0_ClientCore.GpiInterface._d_InvalidPin)})
GpiInterface._d_isActive = ((omniORB.tcInternal.tv_ushort,), (omniORB.tcInternal.tv_boolean,), {(_0_ClientCore.GpiInterface.InvalidPin._NP_RepositoryId): (_0_ClientCore.GpiInterface._d_InvalidPin)})

class _objref_GpiInterface(CORBA.Object):
    _NP_RepositoryId = GpiInterface._NP_RepositoryId

    def __del__(self):
        if _omnipy is not None:
            _omnipy.releaseObjref(self)
        return

    def numPins(self, *args):
        return _omnipy.invoke(self, 'numPins', _0_ClientCore.GpiInterface._d_numPins, args)
        return

    def activate(self, *args):
        return _omnipy.invoke(self, 'activate', _0_ClientCore.GpiInterface._d_activate, args)
        return

    def deactivate(self, *args):
        return _omnipy.invoke(self, 'deactivate', _0_ClientCore.GpiInterface._d_deactivate, args)
        return

    def isActive(self, *args):
        return _omnipy.invoke(self, 'isActive', _0_ClientCore.GpiInterface._d_isActive, args)
        return

    __methods__ = ['numPins', 'activate', 'deactivate', 'isActive'] + CORBA.Object.__methods__


omniORB.registerObjref(GpiInterface._NP_RepositoryId, _objref_GpiInterface)
_0_ClientCore._objref_GpiInterface = _objref_GpiInterface
del GpiInterface
del _objref_GpiInterface
__name__ = 'twc.corba.ClientCore__POA'

class GpiInterface(PortableServer.Servant):
    _NP_RepositoryId = _0_ClientCore.GpiInterface._NP_RepositoryId

    def __del__(self):
        if _omnipy is not None:
            _omnipy.releaseObjref(self)
        return

    _omni_op_d = {'numPins': (_0_ClientCore.GpiInterface._d_numPins), 'activate': (_0_ClientCore.GpiInterface._d_activate), 'deactivate': (_0_ClientCore.GpiInterface._d_deactivate), 'isActive': (_0_ClientCore.GpiInterface._d_isActive)}


GpiInterface._omni_skeleton = GpiInterface
_0_ClientCore__POA.GpiInterface = GpiInterface
del GpiInterface
__name__ = 'twc.corba.ClientCore'
__name__ = 'twc.corba.twc.corba.ClientCore_idl'
__name__ = 'twc.corba.ClientCore'
_0_ClientCore = omniORB.openModule('twc.corba.ClientCore', '/n/azmo/ud2/jmjones/svn/se/personality/domestic/release/v1.11p1/upgrade/work/domestic_upgrade/work/autobuild/twc_istar-2.6_p1/pkg/work/istar/src/pythonlib/twc/corba/../../../lib/twc_client/Vspoold.idl')
_0_ClientCore__POA = omniORB.openModule('twc.corba.ClientCore__POA', '/n/azmo/ud2/jmjones/svn/se/personality/domestic/release/v1.11p1/upgrade/work/domestic_upgrade/work/autobuild/twc_istar-2.6_p1/pkg/work/istar/src/pythonlib/twc/corba/../../../lib/twc_client/Vspoold.idl')
_0_ClientCore._d_Vspoold = (omniORB.tcInternal.tv_objref, 'IDL:ClientCore/Vspoold:1.0', 'Vspoold')
_0_ClientCore.Vspoold = omniORB.newEmptyClass()

class Vspoold:
    _NP_RepositoryId = _0_ClientCore._d_Vspoold[1]

    def __init__(self):
        raise RuntimeError('Cannot construct objects of this type.')
        return

    _nil = CORBA.Object._nil


_0_ClientCore.Vspoold = Vspoold
_0_ClientCore._tc_Vspoold = omniORB.tcInternal.createTypeCode(_0_ClientCore._d_Vspoold)
omniORB.registerType(Vspoold._NP_RepositoryId, _0_ClientCore._d_Vspoold, _0_ClientCore._tc_Vspoold)
Vspoold._d_addFile = (((omniORB.tcInternal.tv_string, 0),), (), None)
Vspoold._d_setLooping = ((omniORB.tcInternal.tv_long,), (), None)
Vspoold._d_flush = ((), (), None)

class _objref_Vspoold(CORBA.Object):
    _NP_RepositoryId = Vspoold._NP_RepositoryId

    def __del__(self):
        if _omnipy is not None:
            _omnipy.releaseObjref(self)
        return

    def addFile(self, *args):
        return _omnipy.invoke(self, 'addFile', _0_ClientCore.Vspoold._d_addFile, args)
        return

    def setLooping(self, *args):
        return _omnipy.invoke(self, 'setLooping', _0_ClientCore.Vspoold._d_setLooping, args)
        return

    def flush(self, *args):
        return _omnipy.invoke(self, 'flush', _0_ClientCore.Vspoold._d_flush, args)
        return

    __methods__ = ['addFile', 'setLooping', 'flush'] + CORBA.Object.__methods__


omniORB.registerObjref(Vspoold._NP_RepositoryId, _objref_Vspoold)
_0_ClientCore._objref_Vspoold = _objref_Vspoold
del Vspoold
del _objref_Vspoold
__name__ = 'twc.corba.ClientCore__POA'

class Vspoold(PortableServer.Servant):
    _NP_RepositoryId = _0_ClientCore.Vspoold._NP_RepositoryId

    def __del__(self):
        if _omnipy is not None:
            _omnipy.releaseObjref(self)
        return

    _omni_op_d = {'addFile': (_0_ClientCore.Vspoold._d_addFile), 'setLooping': (_0_ClientCore.Vspoold._d_setLooping), 'flush': (_0_ClientCore.Vspoold._d_flush)}


Vspoold._omni_skeleton = Vspoold
_0_ClientCore__POA.Vspoold = Vspoold
del Vspoold
__name__ = 'twc.corba.ClientCore'
__name__ = 'twc.corba.twc.corba.ClientCore_idl'
_exported_modules = ('twc.corba.ClientCore',)
return
