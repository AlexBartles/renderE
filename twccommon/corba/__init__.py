# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: __init__.py
# Compiled at: 2006-04-03 09:02:54
"""Grouping of all the corba interfaces.
"""
import CosNaming

def getNamePath(str):
    return map((lambda e: CosNaming.NameComponent(e, '')), str.split('.'))
    return


def setOrb(orb):
    global _orb
    _orb = orb
    return


def getOrb():
    return _orb
    return


_orb = None
