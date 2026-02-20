# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
# Embedded file name: mediapack.py
# Compiled at: 2007-01-12 11:33:37
import os, errno, tempfile, twc.dsmarshal, twccommon.Log
dsm = twc.dsmarshal

def init(config):
    global _config
    _config = config
    return


def uninit():
    return


def install(pack, replace):
    packName = os.path.basename(pack)
    if not os.path.exists(pack):
        twccommon.Log.error('Media pack %s does not exist' % pack)
        return
    workdir = _mkdtemp('mpack')
    if _extract(pack, workdir, _META_FILE):
        prefix = ''
    elif _extract(pack, workdir, './' + _META_FILE):
        prefix = './'
    else:
        twccommon.Log.warning('Extract of metadata for media pack %s failed' % pack)
        _remove_dir(workdir)
        return
    metadata = {}
    execfile('%s/%s' % (workdir, _META_FILE), metadata)
    try:
        packName = metadata['name']
        subdir = metadata['subdir']
        version_file = metadata['version_file']
    except KeyError as e:
        twccommon.Log.error('Missing required metadata %s for pack %s' % (e.__str__(), pack))
        _remove_dir(workdir)
        return

    if len(subdir) == 0:
        twccommon.Log.error('Empty media subdir for pack %s' % packName)
        _remove_dir(workdir)
        return
    if len(version_file) == 0:
        twccommon.Log.error('Empty media version file for pack %s' % packName)
        _remove_dir(workdir)
        return
    if replace:
        _makedirs('/media/tmp')
        _remove_dir('/media/tmp/%s' % subdir)
        destdir = '/media/tmp'
    else:
        destdir = '/media'
    if not _extract(pack, destdir, '%s%s %s%s' % (prefix, subdir, prefix, version_file)):
        twccommon.Log.warning('Extract of media pack %s failed' % packName)
        _remove_dir(workdir)
        _remove(pack)
        return
    if replace:
        _makedirs('/media/%s' % os.path.dirname(subdir))
        _rename_dir('/media/%s' % subdir, '/media/%s.old' % subdir)
        status = os.system('mv /media/tmp/%s /media/%s' % (subdir, subdir))
        if not os.WIFEXITED(status) or os.WEXITSTATUS(status) != 0:
            twccommon.Log.warning('Unable to install media pack %s' % packName)
            _rename_dir('/media/%s.old' % subdir, '/media/%s' % subdir)
            _remove_dir(workdir)
            _remove(pack)
            return
        _remove_dir('/media/%s.old' % subdir)
        os.system('mv /media/tmp/%s /media' % version_file)
    if _extract(pack, workdir, prefix + _INSTALL_SCRIPT):
        twccommon.Log.info('Executing post install script for media pack %s' % packName)
        os.system('%s/%s' % (workdir, _INSTALL_SCRIPT))
    _remove_dir(workdir)
    _remove(pack)
    if replace:
        twccommon.Log.info('Installed media pack %s' % packName)
    else:
        twccommon.Log.info('Merged media pack %s' % packName)
    return


_META_FILE = '+META'
_INSTALL_SCRIPT = '+POST-INSTALL'

def _makedirs(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    return


def _mkdtemp(suffix):
    while 1:
        workdir = tempfile.mktemp(suffix)
        try:
            os.makedirs(workdir)
            return workdir
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    return


def _remove(file):
    try:
        os.remove(file)
    except:
        pass

    return


def _extract(pack, workdir, files):
    tarCmd = 'nice -20 tar xzf %s -C %s %s' % (pack, workdir, files)
    status = os.system(tarCmd)
    if not os.WIFEXITED(status) or os.WEXITSTATUS(status) != 0:
        return 0
    else:
        return 1
    return


def _remove_dir(dir):
    os.system('rm -rf %s' % dir)
    return


def _rename_dir(oldname, newname):
    _remove_dir(newname)
    if os.path.exists(oldname):
        os.system('mv %s %s' % (oldname, newname))
    return
