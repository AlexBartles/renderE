# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: renderTools.py
# Compiled at: 2007-04-27 10:00:47
from twc.embedded.renderd.renderUtil import rgbaConvert
from twc.embedded.renderd.RenderScript import Box
from twc.embedded.renderd.RenderScript import CompositeRenderable
from twc.embedded.renderd.RenderScript import EffectSequencer
from twc.embedded.renderd.RenderScript import Polygon
from twc.embedded.renderd.RenderScript import Fader
from twc.embedded.renderd.RenderScript import Slider
from twc.embedded.renderd.RenderScript import NullEffect
from twc.embedded.renderd.RenderScript import SetVisibility
from twc.embedded.renderd.RenderScript import SetPosition
from twc.embedded.renderd.RenderScript import Text
from twc.embedded.renderd.RenderScript import TTFont
from twc.embedded.renderd.RenderScript import TTOutlineFont
from functools import reduce

def sequenceOnPage(page, grSet, delayList, repeat=0):
    pageCount = len(grSet)
    count = 0
    delay = 1
    if len(grSet) == 1:
        for gr in grSet[0]:
            page.addItem(gr)

        return
    totFrames = reduce((lambda a, b: a + b), delayList)
    for grList in grSet:
        for gr in grList:
            es = EffectSequencer(gr, repeat=repeat)
            if count == 0:
                es.addEffect(SetVisibility(None, 1), delayList[count] - 5)
                es.addEffect(Fader(None, 1, 0, 5), 5)
                es.addEffect(SetVisibility(None, 0), 1)
                es.addEffect(Fader(None, 0, 1, 1), 1)
                es.addEffect(NullEffect(None), totFrames - (delayList[count] + 2))
            elif count == pageCount - 1:
                es.addEffect(SetVisibility(None, 0), delay)
                es.addEffect(Fader(None, 1, 0, 1), 1)
                es.addEffect(SetVisibility(None, 1), 1)
                es.addEffect(Fader(None, 0, 1, 5), 5)
                es.addEffect(NullEffect(None), totFrames - (delay + 7))
            else:
                es.addEffect(SetVisibility(None, 0), delay)
                es.addEffect(Fader(None, 1, 0, 1), 1)
                es.addEffect(SetVisibility(None, 1), 1)
                es.addEffect(Fader(None, 0, 1, 5), 5)
                es.addEffect(NullEffect(None), delayList[count] - 12)
                es.addEffect(Fader(None, 1, 0, 5), 5)
                es.addEffect(SetVisibility(None, 0), 1)
                es.addEffect(Fader(None, 0, 1, 1), 1)
                es.addEffect(NullEffect(None), totFrames - (delayList[count] + delay + 2))
            page.addItem(gr)
            page.addItem(es)

        delay = delayList[count] + delay
        count = count + 1

    return


def dataNotAvailable(page, xPos=None, yPos=None, text='Data Not Available'):
    (r, g, b, a) = rgbaConvert(235, 235, 235, 255)
    font = TTFont('/rsrc/fonts/Frutiger_Bold_Cond', 34)
    gr = Text(font, text)
    gr.setColor(r, g, b, a)
    if xPos is None:
        xPos = (720 - gr.size()[0]) / 2
    if yPos is None:
        yPos = (480 - gr.size()[1]) / 2
    gr.setPosition(xPos, yPos)
    page.addItem(gr)
    return gr
    return

