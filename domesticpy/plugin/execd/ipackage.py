# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: ipackage.py
# Compiled at: 2007-01-12 11:33:37
import os, twc.dsmarshal, twccommon.Log
dsm = twc.dsmarshal

def init(config):
    global _config
    _config = config
    return


def uninit():
    return


def install(pkgPath, instPath):
    if not os.path.exists(pkgPath):
        twccommon.Log.error('cannot extract pkg; %s does not exist' % pkgPath)
        return
    baseName = os.path.basename(pkgPath)
    (pkg, ext) = os.path.splitext(baseName)
    ext = ext[1:]
    fullPath = '%s/%s' % (instPath, pkg)
    if ext == 'ipkg':
        cmd = 'nice -20 tar -xf %s -C %s' % (pkgPath, fullPath)
    elif ext == 'ipkz':
        cmd = 'nice -20 tar -zxf %s -C %s' % (pkgPath, fullPath)
    else:
        twccommon.Log.error('cannot extract pkg; invalid extention: %s' % ext)
        return
    twccommon.Log.info('extracting %s to %s' % (pkgPath, fullPath))
    if os.path.exists(fullPath):
        twccommon.Log.warning('cannot extract pkg; %s already exists' % fullPath)
    else:
        os.makedirs(fullPath)
    os.system(cmd)
    _execInstallScript(fullPath)
    return


def uninstall(pkg, path):
    instPath = '%s/%s' % (path, pkg)
    if os.path.exists(instPath):
        _execUninstallScript(instPath)
        os.system('rm -rf %s' % instPath)
    return

def execfile(filename, globa, loca):
    with open(filename, "r", encoding="windows-1252") as f:
        exec(compile(f.read(), filename, 'exec'), globa, loca)

def _execScript(fname, instPath):
    ns = {'dsm': dsm, 'PKG_ROOT': instPath}
    execfile(fname, ns, ns)
    return


def _execInstallScript(instPath):
    fname = '%s/.meta/install.py' % instPath
    if os.path.exists(fname):
        twccommon.Log.info('excuting pkg install script: %s' % fname)
        _execScript(fname, instPath)
    return


def _execUninstallScript(instPath):
    fname = '%s/.meta/uninstall.py' % instPath
    if os.path.exists(fname):
        twccommon.Log.info('excuting pkg uninstall script: %s' % fname)
        _execScript(fname, instPath)
    return

