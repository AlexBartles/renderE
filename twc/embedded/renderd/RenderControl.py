# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: RenderControl.py
# Compiled at: 2007-01-12 11:17:28
from . import _renderd
from .RenderScript import *
import rendereglobals as rg

def actuallyRunAQueuedCommand(cmd):
    if isinstance(cmd, SetLayerCmd):
        i = -1
        for i, layer in enumerate(rg.layers):
            if layer[0] == cmd.name:
                break
        if i > -1:
            rg.layers[i][1] = cmd[cmd.layer]
    elif isinstance(cmd, CreateNamedLayerCmd):
        rg.layers.append([
            cmd.name,
            None,
            cmd.time,
            cmd.frameOffset,
            cmd.depth,
            cmd.repeat,
            0,
            0,
            720,
            480,
            1,
            1,
            0,
            0,
            False
        ])
    elif isinstance(cmd, SetNamedLayerViewPortCmd):
        i = -1
        for i, layer in enumerate(rg.layers):
            if layer[0] == cmd.name:
                break
        if i > -1:
            rg.layers[i][6] = cmd.x
            rg.layers[i][7] = cmd.y
            rg.layers[i][8] = cmd.w
            rg.layers[i][9] = cmd.h
            rg.layers[i][10] = cmd.sx
            rg.layers[i][11] = cmd.sy
            rg.layers[i][12] = cmd.tx
            rg.layers[i][13] = cmd.ty
    elif isinstance(cmd, DestroyNamedLayerCmd):
        i = -1
        for i, layer in enumerate(rg.layers):
            if layer[0] == cmd.name:
                break
        if i > -1:
            del rg.layers[i]
    elif isinstance(cmd, ActivateLayerCmd):
        i = -1
        for i, layer in enumerate(rg.layers):
            if layer[0] == cmd.name:
                break
        if i > -1:
            rg.layers[i][14] = True
    elif isinstance(cmd, DeactivateLayerCmd):
        i = -1
        for i, layer in enumerate(rg.layers):
            if layer[0] == cmd.name:
                break
        if i > -1:
            rg.layers[i][14] = False

def queueCommand(cmd, time=0, frameOffset=0, estimatedCmd=0):
    rg.queuedcommands.append([cmd, time, frameOffset, estimatedCmd])


def createNamedLayer(name, depth, repeat=0, autoDestroy=1, time=0, frameOffset=0):
    cmd = CreateNamedLayerCmd(name, depth, repeat, autoDestroy)
    return queueCommand(cmd, time, frameOffset)
    return


def destroyNamedLayer(name, time=0, frameOffset=0):
    cmd = DestroyNamedLayerCmd(name)
    return queueCommand(cmd, time, frameOffset)
    return


def modifyNamedLayer(name, newName, depth, repeat, autoDestroy, time=0, frameOffset=0):
    cmd = ModifyNamedLayerCmd(name, newName, depth, repeat, autoDestroy)
    return queueCommand(cmd, time, frameOffset)
    return


def setLayer(name, layer, time=0, frameOffset=0):
    cmd = SetLayerCmd(name, layer)
    return queueCommand(cmd, time, frameOffset)
    return


def appendLayer(name, layer, time=0, frameOffset=0):
    cmd = AppendLayerCmd(name, layer)
    return queueCommand(cmd, time, frameOffset)
    return


def replaceLayer(name, layer, time=0, frameOffset=0):
    cmd = ReplaceLayerCmd(name, layer)
    return queueCommand(cmd, time, frameOffset)
    return


def removeLayer(name, time=0, frameOffset=0):
    cmd = RemoveLayerCmd(name)
    return queueCommand(cmd, time, frameOffset)
    return


def activateLayer(name, time=0, frameOffset=0):
    cmd = ActivateLayerCmd(name)
    return queueCommand(cmd, time, frameOffset)
    return


def deactivateLayer(name, time=0, frameOffset=0):
    cmd = DeactivateLayerCmd(name)
    return queueCommand(cmd, time, frameOffset)
    return


def loadPresentation(fileName, time=0, frameOffset=0):
    cmd = LoadPresentationCmd(fileName)
    return queueCommand(cmd, time, frameOffset)
    return


def selectInputSource(avPort, time=0, frameOffset=0):
    cmd = SelectInputSourceCmd(avPort)
    return queueCommand(cmd, time, frameOffset, 1)
    return


def activateGpiPin(pin, time=0, frameOffset=0):
    cmd = ActivateGpiPinCmd(pin)
    return queueCommand(cmd, time, frameOffset)
    return


def deactivateGpiPin(pin, time=0, frameOffset=0):
    cmd = DeactivateGpiPinCmd(pin)
    return queueCommand(cmd, time, frameOffset)
    return


