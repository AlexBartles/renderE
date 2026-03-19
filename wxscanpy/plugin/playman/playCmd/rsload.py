# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: rsload.py
# Compiled at: 2007-05-14 11:20:55
import os, os.path, time, string, twccommon, twccommon.Log, twccommon.PluginManager, twc.dsmarshal as dsm, wxscan
from wxscan import dataUtil
import twc.MiscCorbaInterface
import rendereglobals as rg
from twc import psp

def init(config):
    global _config
    global _params
    global _pm
    _config = twccommon.Data()
    _config.__dict__.update(config.__dict__)
    _pm = twccommon.PluginManager.PluginManager(_config.packagePluginRoot)
    _config.root = '%s/local' % (_config.productRoot,)
    _config.shareDir = ['%s/pm/incl' % (_config.productRoot,)]
    _config.preRoll = dataUtil.secondsToFrames(4)
    _params = twccommon.Data()
    _params.root = _config.root
    _params.shareDir = _config.shareDir
    _params.tempDir = '%s/local' % (_config.tempDir,)
    return


def load(pDir, pName):
    _load(pDir, pName)
    return


def lock():
    params = twccommon.Data()
    params.imageFile = '/media/backgrounds/wxscan_upgrade_bg'
    _load('/usr/twc/wxscan/products/misc', 'SplashScreen', params)
    return


def _load(pDir, pName, params=twccommon.Data()):
    try:
        fname = pDir + '/' + pName + '.rs'
        f = open(fname)
        page = f.read()
        f.close()
        dname = os.path.dirname(fname)
        includePathList = []
        includePathList.append(dname)
        includePathList.append(dname + '/incl')
        includePathList += _params.shareDir
        psp.setIncludePath(includePathList)
        ns = {}
        ns['params'] = params
        page = psp.evalRenderScript(page, ns)
        fname = _params.tempDir + '/' + pName + '.rsc'
        f = open(fname, 'w')
        f.write(page)
        f.close()
        #twc.MiscCorbaInterface.runRenderScript(fname)
        rg.runrsfunction(fname)
    except Exception as e:
        twccommon.Log.logCurrentException()

    return
