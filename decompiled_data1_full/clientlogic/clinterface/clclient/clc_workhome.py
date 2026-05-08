# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/clclient/clc_workhome.pyc
# RelativePath: clientlogic/clinterface/clclient/clc_workhome.pyc
# Source Generated with Decompyle++
# File: clc_workhome.pyc (Python 3.6)

import os
import sys
import imp
import importlib.abc

class CModuleLoader(importlib.abc.SourceLoader):
    
    def __init__(self, basepath):
        self._basepath = basepath

    
    def module_repr(self, module):
        return '<urlmodule %r from %r>' % (module.__name__, module.__file__)

    
    def load_module(self, fullname):
        code = self.get_code(fullname)
        mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        mod.__file__ = self.get_filename(fullname)
        mod.__loader__ = self
        mod.__package__ = fullname.rpartition('.')[0]
        exec(code, mod.__dict__)
        return mod

    
    def get_code(self, fullname):
        src = self.get_source(fullname)
        return compile(src, self.get_filename(fullname), 'exec')

    
    def get_data(self, path):
        pass

    
    def get_filename(self, fullname):
        return self._basepath + '/' + '/'.join(fullname.split('.')) + '.py'

    
    def get_source(self, fullname):
        filename = self.get_filename(fullname)
        u = open(filename, mode = 'r', encoding = 'utf-8')
        source = u.read()
        print('temploader:', filename)
        return source

    
    def is_package(self, fullname):
        return False



class CPackageLoader(CModuleLoader):
    
    def load_module(self, fullname):
        mod = super().load_module(fullname)
        mod.__path__ = [
            self._basepath]
        mod.__package__ = fullname

    
    def get_filename(self, fullname):
        return self._basepath + '/' + '/'.join(fullname.split('.')) + '/__init__.py'

    
    def is_package(self, fullname):
        return True



class CMetaFinder(importlib.abc.MetaPathFinder):
    
    def __init__(self, path):
        self._path = path
        self._moduleLoader = CModuleLoader(self._path)
        self._packageLoader = CPackageLoader(self._path)

    
    def find_module(self, fullname, path = None):
        pathName = '%s/%s' % (self._path, '/'.join(fullname.split('.')))
        if os.path.exists(pathName + '.py'):
            return self._moduleLoader
        if os.path.exists(pathName + '/__init__.py'):
            return self._packageLoader


if 'g_IsWork' not in globals():
    g_IsWork = False
if g_IsWork:
    sys.meta_path.pop(0)
    g_IsWork = False
for path in sys.path:
    if 'templogic' in path:
        sys.meta_path.insert(0, CMetaFinder(path))
        g_CanWork = True
        break


def Work():
    if not g_IsWork:
        return None
    
    try:
        import tempinit
        print('workhome: tempinit succ')
    except:
        print('workhome: tempinit fail')


