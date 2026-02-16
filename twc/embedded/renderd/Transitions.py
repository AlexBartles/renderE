# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: Transitions.py
# Compiled at: 2007-01-12 11:17:28
import traceback
from RenderScript import *

def add(transName, page):
    if transName == None:
        return
    try:
        fn = _fnMap[transName]
        for elem in page.elements():
            if isinstance(elem, GraphicRenderable) and elem.transitionable():
                es = EffectSequencer(elem)
                fn(page, es)
                page.addItem(es)

    except Exception:
        print('error adding transition:')
        traceback.print_exc()

    return


def _none(page, es):
    return


def _fadeIn(page, es):
    dur = _transDuration - 1
    es.addEffect(Fader(None, 1, 0, 1), 1)
    es.addEffect(Fader(None, 0, 1, dur), dur)
    return


def _fadeOut(page, es):
    es.addEffect(NullEffect(), page.duration() - _transDuration)
    es.addEffect(Fader(startAlpha=1, endAlpha=0, frames=_transDuration), _transDuration)
    return


_transDuration = 15
_fnMap = {'None': _none, 'FadeIn': _fadeIn, 'FadeOut': _fadeOut}