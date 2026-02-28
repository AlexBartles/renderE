# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: PluginManager.py
# Compiled at: 2006-04-03 09:02:55
"""
Provides a plugin facility.  Plugins are simply modules that can loaded
dynamically at run time.  Since Python is an interpreted scripting language
dynamic code loading is easy.  However, this module provides an interface
to do request loading (and reloading if file is replaced).  It also provides
an interface to request a module from a string name, an interface to 
query whether or not a named plugin has been loaded, and an interface for
querying the list of loaded plugins.
"""
import os.path, sys, twccommon
import importlib.util, importlib.machinery

def apply(func, args, kwargs=None):
    return func(*args) if kwargs is None else func(*args, **kwargs)

class PluginManager:

    def __init__(self, pluginRoot, nameSpace='plugins'):
        self._root = pluginRoot
        self._nameSpace = nameSpace
        self._plugins = {}
        return

    def _getPluginFileAttribs(self, pluginName):
        fdesc = None
        ftime = 0
        fl = [('py', 'r', 'source'), ('pyc', 'rb', 'compiled')]
        for fattr in fl:
            (ext, mode, type) = fattr
            fname = '%s/%s.%s' % (self._root, ".".join(pluginName.split(".")[:-1]), ext)
            if not os.path.exists(fname):
                continue
            ft = os.path.getmtime(fname)
            if ft > ftime:
                ftime = ft
                fdesc = (fname, ftime, fattr)

        if fdesc == None:
            raise ImportError('cannot find plugin %s/%s' % (self._root, pluginName))
        return fdesc
        return

    def _loadPlugin(self, pluginName, fname, ftime, fattr, initFnArgs):
        (ext, mode, _type) = fattr
        plugin = twccommon.Data(mtime=ftime)
        qualifiedName = '%s_%s' % (self._nameSpace, ".".join(pluginName.split(".")[:-1]))

        if ext == 'py':
            loader = importlib.machinery.SourceFileLoader(qualifiedName, fname)
        else:
            loader = importlib.machinery.SourcelessFileLoader(qualifiedName, fname)

        spec = importlib.util.spec_from_loader(qualifiedName, loader)
        module = importlib.util.module_from_spec(spec)
        # execute and register
        loader.exec_module(module)
        module.__file__ = fname
        plugin.mod = module
        fn = getattr(plugin.mod, FN_INIT, None)
        if fn is not None:
            apply(fn, initFnArgs)
        self._plugins[pluginName] = plugin
        return

    def _needsLoading(self, pluginName, ftime):
        load = 0
        try:
            plugin = self._plugins[pluginName]
            if ftime > plugin.mtime:
                load = 1
        except KeyError:
            load = 1

        return load
        return

    def needsLoading(self, pluginName):
        """Determine if the plugin file needs to be loaded (or reloaded).

        Parameters:
        - pluginName: The name of the plugin of interest.

        Return: 
            Returns true if either the plugin has not been loaded or
            if the plugin file has been replaced since it was last 
            loaded.
        """
        (fname, ftime, fattr) = self._getPluginFileAttribs(pluginName)
        return self._needsLoading(pluginName, ftime)
        return

    def isPluginLoaded(self, pluginName):
        """Indicates whether the specified plugin has been loaded.

        Parameters:
        - pluginName: The name of the plugin of interest.

        Return: 
        Returns true if the plugin has already been loaded.
        """
        return (pluginName in self._plugins)
        return

    def getPluginModule(self, pluginName):
        """Gets a module object for the specified plugin.
        No attempt is made to load (or reload) the module.

        It is an error to call this func. for a plugin that 
        has not been previously loaded.  The isPluginLoaded()
        function can be used as a test.

        Parameters:
        - pluginName: The name of the plugin of interest.

        Return: 
        Returns a ref. to the module corresponding to the plugin name.
        """
        return self._plugins[pluginName].mod
        return

    def loadPlugin(self, pluginName, initFnArgs=()):
        """Load (or reload) the specified plugin.
        
        If the plugin module has not been loaded before, then it will 
        be imported.  Otherwise it will be reloaded.  No test is performed
        to determine if the plugin file has been updated.  See 
        retrievePlugin().

        If the module has defined a function named 'init', it will be
        exectued and initFnArgs specifies the parametes for the call.

        If the plugin cannot be loaded, then a corresponding exception 
        will be raised: IOError, ImportError, etc.

        Parameters:
        - pluginName: The name of the plugin of interest.
        - initFnArgs: Parameters passed when the plugin modules init fn
        is invoked.  Must be a tuple with an arity matching
        the number of params.  Defaults to no params (an empty tuple).

        Return: 
        Returns a ref. to the module corresponding to the plugin name.
        """
        (fname, ftime, fattrs) = self._getPluginFile(pluginName)
        self._loadPlugin(pluginName, fname, ftime, fattrs, initFnArgs)
        return self._plugins[pluginName].mod
        return

    def retrievePlugin(self, pluginName, initFnArgs=()):
        """Get a module object for the specified plugin.
        If the plugin module has not been loaded before, then it will 
        be imported.  If the plugin file is newer than the last time
        it was loaded, then it will be reloaded.

        If the module has defined a function named 'init', it will be
        exectued and initFnArgs specifies the parametes for the call.

        If the plugin cannot be loaded, then a corresponding exception 
        will be raised: IOError, ImportError, etc.

        Parameters:
        - pluginName: The name of the plugin of interest.
        - initFnArgs: Parameters passed when the plugin modules init fn
        is invoked.  Must be a tuple with an arity matching
        the number of params.  Defaults to no params (an empty tuple).

        Return: 
        Returns a ref. to the module corresponding to the plugin name.
        """
        (fname, ftime, fattrs) = self._getPluginFileAttribs(pluginName)
        load = self._needsLoading(pluginName, ftime)
        if load:
            self._loadPlugin(pluginName, fname, ftime, fattrs, initFnArgs)
        return self._plugins[pluginName].mod
        return

    def getPlugins(self):
        """Return a list of loaded plugins.

        Return: 
        Returns a list of references to the modules corresponding to all of
        the loaded plugins.
        """
        list = []
        for p in self._plugins.values():
            list.append(p.mod)

        return list
        return


FN_INIT = 'init'
