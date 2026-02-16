# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: __init__.py
# Compiled at: 2006-04-03 09:02:55
import os.path
TRUE = 1
FALSE = 0

def _compare(a, b):
    return a == b
    return


class Data:
    """An empty data structure.  Useful for data structures with dynamic
    member fields, i.e. adding new member variables at run time.
    """

    def __init__(self, other=None, **kw):
        self.update(other, **kw)
        return

    def __repr__(self):
        c = self.__class__
        s = '%s.%s(' % (c.__module__, c.__name__)
        for (k, v) in self.__dict__.items():
            s += '%s=%s, ' % (k, repr(v))

        s += ')'
        return s
        return

    def update(self, other=None, **kw):
        if other != None:
            self.__dict__.update(other.__dict__)
        self.__dict__.update(kw)
        return

    def clone(self):
        other = Data()
        other.update(self)
        return other
        return


class DefaultedData(Data):
    """An empty data structure, like Data.  This one, however, returns a 
    specified default value for any undefined field.  This avoid having 
    to set up alot of exception handlers in order to test whether a given 
    field is present.  It also accepts a Data in its c'tor.  This is useful 
    for wrapping an existing Data when the 'defualted' behavior is desired.
    
    example:
        d = Data(x=1, y=2)
        dd = DefaultedData(data=d, a=100)
        dd.x  =>  1
        dd.y  =>  2
        dd.a  =>  100
        dd.b  =>  None        
    """

    def __init__(self, data=Data(), default=None, **kw):
        data.__dict__.update(kw)
        self.__dict__['__default'] = default
        self.__dict__['__data'] = data
        return

    def __getattr__(self, name):
        try:
            return self.__dict__['__data'].__dict__[name]
        except KeyError:
            if name[0:2] == '__' and name[-2:] == '__':
                raise AttributeError
            return self.__dict__['__default']

        return

    def __setattr__(self, name, val):
        self.__dict__['__data'].__dict__[name] = val
        return

    def __repr__(self):
        c = self.__class__
        sdata = repr(self.__dict__['__data'])
        s = '%s.%s(%s)' % (c.__module__, c.__name__, sdata)
        return s
        return

    def __str__(self):
        return str(self.__dict__['__data'])
        return


def mergeStructs(dataList, default=None):
    """Take a list of Data() structures and merge into 1 structure
    containing the union of all fields of all structures.  In the 
    case of matching field names, the last item in the list takes 
    precedence.
    """
    res = Data()
    if default != None:
        res.__dict__.update(default.__dict__)
    for data in dataList:
        res.__dict__.update(data.__dict__)

    return res
    return


def compare(l, r):
    """Compares 2 numbers in a way useful for the sort routine."""
    if l < r:
        return -1
    elif l > r:
        return 1
    else:
        return 0
    return


def findFirstFile(fname, dirList):
    """Find the 1st instance of the specified file name in the given directories.
    Search through the directories, in the list's order, for a file with the
    specified name.  The full path, including filename, of the first one found
    will be returned or None if one is not found.
    """
    for d in dirList:
        fullName = '%s/%s' % (d, fname)
        if os.path.exists(fullName):
            return fullName

    return None
    return


import urllib, xml.sax, os.path, string, time

class SAXHandler(xml.sax.ContentHandler):
    """Extend the start/end-Element methods of this class to use more tag-
    specific handlers provided in derived classes"""

    def startDocument(self):
        self.__tag = None
        return

    def startElement(self, tag, attrs):
        self.__tag = tag
        handler = getattr(self, 'start%s' % (tag,), None)
        if handler != None:
            handler(attrs)
        return

    def endElement(self, tag):
        handler = getattr(self, 'end%s' % (tag,), None)
        if handler != None:
            handler()
        self.__tag = None
        return

    def characters(self, content):
        handler = getattr(self, 'characters%s' % self.__tag, None)
        if handler != None:
            handler(content)
        return

    def ignoreableWhitespace(self, content):
        handler = getattr(self, 'ignoreableWhitespace%s' % (self.__tag,), None)
        if handler != None:
            handler(content)
        return

    def getCurrentTag(self):
        return self.__tag
        return


class SubHandler:
    """This class implements a framework that allows a container class to be
    extended at runtime with various specialized "plug-ins".
    Basically, what you do is subclass this thing with whatever specialized
    handling methods a particular xml doc type needs.
    On init, this class will extend its (passed-in) container class with a bunch
    of tag-handling plug-in methods whose names begin with 'start' and 'end'.
    When you call deatch(), it removes these doc-specific tag handlers.
    To avoid run-time name conflicts, make sure the container class does not
    already have methods that begin with 'start' or 'end' AND have the same 
    name as methods in your derived class!"""

    def __init__(self, container):
        """Look for subclassed methods that begin with 'start' or 'end'.
        Add them to the containter class"""
        self._container = container
        for key in dir(self):
            if key.find('start', 0, 5) >= 0 or key.find('end', 0, 3) >= 0 or key.find('characters', 0, 10) >= 0:
                if hasattr(container, key) != 0:
                    raise RuntimeError('Method Name Conflict: %s' % (key,))
                setattr(container, key, getattr(self, key))

        return

    def finished(self):
        return

    def detach(self):
        """Delete all the methods that were added to the container class"""
        for key in dir(self):
            if key.find('start', 0, 5) >= 0 or key.find('end', 0, 3) >= 0 or key.find('characters', 0, 10) >= 0:
                delattr(self._container, key)

        return


