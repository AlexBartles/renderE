# if you want renderE's config, that's in rendereglobals.py
# this is just some stupid file for loading configs
# i never want to cross paths with this little rascal again
import twc

def getValues():
    return _values


def set(valName, val):
    _setValue(valName, val)

_values = twc.Data()

def _setValue(valName, val):
    _values.__dict__[valName] = val

