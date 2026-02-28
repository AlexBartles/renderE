# Source Generated with Decompyle++
# File: __init__.pyc (Python 2.2)

'''Bootstrap for embedded python functionality.

This provides the base stuff that the embedded Python implementation
relies on.
'''
import code
import importlib.util
import marshal
import os
import string
import sys
import twccommon.IOCatcher as twccommon
import twccommon.Log as twccommon
import traceback
import zlib
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import twc
import twccommon
import rendereglobals as rg
_confclass = None

def runpyc(fname):
    '''Execute a precompiled python script in its own namespace.  The name
    space will disappear after execution, so in theory any vars created
    will die rather than live in __main__ (by default).
    '''
    mylocals = { }
    haderror = 0
    
    try:
        f = open(fname, 'r')
        magic = f.read(4)
        if magic != importlib.util.MAGIC_NUMBER:
            raise TypeError('not a pyc file')
        
        magic = f.read(4)
        codeobj = marshal.load(f)
        eval(codeobj, mylocals, mylocals)
    except:
        traceback.print_exc()
        haderror = 1

    mylocals.clear()
    if haderror == 1:
        raise RuntimeError('Encountered exception during embedded script')
    
def execfile(filename, globa, loca):
    with open(filename, "rb") as f:
        exec(compile(f.read(), filename, 'exec'), globa, loca)

def runpy(fname):
    '''Runs a python script in its own namespace.  The namespace will 
    go away after execution, so in theory any vars created will die after
    the script is finished rather than live in __main__ (by default).
    '''
    mylocals = {}
    haderror = 0
    
    try:
        execfile(fname, mylocals, mylocals)
    except:
        traceback.print_exc()
        haderror = 1

    mylocals.clear()
    if haderror == 1:
        raise RuntimeError('Encountered exception during embedded script')
    


def setconfclass(cls):
    global _confclass
    _confclass = cls


def runconfpy(fname):
    '''Runs a python script in its own namespace similar to runpy() func.
    The difference is that it calls _finalize() on the specified config 
    class instance.  This is done in order to provide a mechanism for 
    multiple instances of a config class to override values with the last
    one taking precednece (local configuration).
    
    During execution, the script is expected to specify
    a class instance by calling setconfclass().  This is done in 
    Configuration.Config.__init__().  So deriving from this class will
    automatically handle this requirement.
    '''
    global _confclass
    mylocals = {"twc": twc, "twccommon": twccommon}
    execfile(fname, mylocals, mylocals)
    if _confclass != None:
        _confclass._finalize()
    #i'll tell you, this whole thing was shoehorned in here
    if "config" in mylocals:
        if hasattr(mylocals["config"]._values, "appName"):
            rg.configs[mylocals["config"]._values.appName] = mylocals["config"]._values
    
    _confclass = None
    mylocals.clear()


def crc32(fname):
    '''Calculate the crc32 of a file in the same manner as the STAR XL client.
       Should also be compatible with GNU cksum'''
    return 0

def unsetenv(varName):
    '''Remove an environment variable from the environment'''
    del os.environ[varName]


def tzmktime(time, tz = 'UTC0'):
    '''Like time.mktime but lets you specify the timezone.
       Use the same timezone strings that you would when using C 
       date library functions and the TZ environ. variable.
    '''
    return _twc.tzmktime(time, tz)


class ObjectWrapper:
    '''Abstract base class of all classes that have an embedded partener.

    The inherited destructor frees the embedded mapping between its
    PyObject and the C++ object.  Constructors for any class derived
    from this should call a corresponding creation intrinsic that adds
    a new mapping.
    '''
    
    def __init__(self):
        raise RuntimeError('Instantiated abstract class: ' + self.__name__)

    
    def __del__(self):
        pass


