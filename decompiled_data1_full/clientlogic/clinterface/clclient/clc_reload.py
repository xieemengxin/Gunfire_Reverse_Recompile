# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/clclient/clc_reload.pyc
# RelativePath: clientlogic/clinterface/clclient/clc_reload.pyc
# Source Generated with Decompyle++
# File: clc_reload.pyc (Python 3.6)

from imp import reload
import enum
import importlib
import weakref
import types
import sys
import L_reload
import collections
func_attrs = [
    '__code__',
    '__defaults__',
    '__doc__',
    '__globals__',
    '__dict__',
    '__annotations__']

def refresh_object(new_obj, extra_args):
    if isinstance(new_obj, (list, tuple, set)):
        new_list = list(new_obj)
        for i, obj in enumerate(new_list[:]):
            args = extra_args.create_args()
            new_list[i] = refresh_object(obj, args)
        
        for i, obj in enumerate(new_obj):
            if new_list[i] is not obj and type(new_obj) is list:
                return new_list
            return type(new_obj)(new_list)
        else:
            return new_obj
    if isinstance(new_obj, dict):
        for k, v in list(new_obj.items()):
            new_k = refresh_object(k, extra_args)
            args = extra_args.create_args(name = k, dict = new_obj)
            new_v = refresh_object(v, args)
            if k is new_k:
                if new_obj[k] is new_v:
                    continue
                new_obj[k] = new_v
                continue
            del new_obj[k]
            new_obj[new_k] = new_v
        
        return new_obj
    if isinstance(new_obj, collections.Hashable) and new_obj in extra_args.cls_new2old:
        cls = extra_args.cls_new2old[new_obj]
        extra_args.set_parent_attr(cls)
        return cls
    cls = extra_args.cls_new2old.get(new_obj.__class__)
    if cls is not None:
        new_obj.__class__ = cls
    return new_obj


def inplace_container(old, new, extra_args):
    if type(old) is not type(new):
        raise TypeError('Two object types must be same exactly')
    if isinstance(old, list):
        new = refresh_object(new, extra_args)
        if old is new:
            return None
        old.clear()
        old.extend(new)
        return None
    if isinstance(old, (dict, set)):
        new = refresh_object(new, extra_args)
        if old is new:
            return None
        old.clear()
        old.update(new)
        return None
    raise TypeError('Type should be one of (list, dict, set), but got %s' % type(old))


def is_inplace_updatable(old, new):
    if type(old) is not type(new):
        return False
    return isinstance(old, (list, dict, set))


def update_function(old, new, extra_args):
    if old.__closure__ != new.__closure__:
        if isinstance(new.__closure__, tuple):
            new_closure = []
            cls_new2old = extra_args.cls_new2old
            for cell in new.__closure__:
                if cell.cell_contents in cls_new2old:
                    L_reload.SetCellContent(cell, cls_new2old[cell.cell_contents])
                new_closure.append(cell)
            
            L_reload.SetFuncClosure(old, tuple(new_closure))
        else:
            L_reload.SetFuncClosure(old, new.__closure__)
    for name in func_attrs:
        
        try:
            setattr(old, name, getattr(new, name))
        except (AttributeError, TypeError):
            continue

    
    extra_args.set_parent_attr(old)


def update_method(old, new, extra_args):
    args = extra_args.create_args()
    update_function(old.__func__, new.__func__, args)


def update_class(old, new, extra_args):
    if old in extra_args.cls_update_record:
        extra_args.set_parent_attr(old)
        return None
    extra_args.record_class_update(old, new)
    if extra_args.purge_members:
        removes = set(old.__dict__.keys()).difference(new.__dict__.keys())
        for key in removes:
            
            try:
                delattr(old, key)
            except AttributeError:
                continue

        
    for key, new_obj in list(new.__dict__.items()):
        
        try:
            old_obj = old.__dict__[key]
        except (AttributeError, KeyError):
            try:
                new_obj = refresh_object(new_obj, extra_args)
                setattr(old, key, new_obj)
            except (AttributeError, TypeError):
                pass
            continue

        if old_obj == new_obj:
            continue
        args = extra_args.create_args(name = key, obj = old)
        if update_generic(old_obj, new_obj, args):
            continue
        if type(old_obj) in extra_args.cls_update_record:
            continue
        
        try:
            new_obj = refresh_object(new_obj, extra_args)
            setattr(old, key, new_obj)
        except (AttributeError, TypeError):
            continue

    
    extra_args.set_parent_attr(old)


def update_property(old, new, extra_args):
    args = extra_args.create_args()
    update_generic(old.fdel, new.fdel, args)
    update_generic(old.fget, new.fget, args)
    update_generic(old.fset, new.fset, args)


def update_enum(old, new, extra_args):
    changed_values = []
    all_values = set()
    if extra_args.purge_members:
        old._member_map_.clear()
        old._value2member_map_.clear()
    old._member_map_.update(new._member_map_)
    for name, value in list(old._member_map_.items()):
        new_value = refresh_object(value, extra_args)
        if new_value is not value:
            changed_values.append((value, new_value))
            old._member_map_[name] = new_value
        
        try:
            all_values.add(new_value)
        except TypeError:
            continue

    
    old._value2member_map_.update(new._value2member_map_)
    value2member = old._value2member_map_.copy()
    for old_value, new_value in changed_values:
        if old_value not in value2member:
            continue
        name = value2member[old_value]
        del value2member[old_value]
        value2member[new_value] = name
    
    if len(all_values) > 0:
        for value in list(value2member.keys()):
            if value in all_values:
                continue
            del value2member[value]
        
    old._value2member_map_.clear()
    old._value2member_map_.update(value2member)
    if extra_args.purge_members:
        old._member_names_.clear()
        old._member_names_.extend(new._member_names_)
    else:
        names = set(new._member_names_)
        names.symmetric_difference_update(old._member_names_)
        old._member_names_.extend(names)


def isinstance2(a, b, typ):
    if isinstance(a, typ):
        pass
    return isinstance(b, typ)

UPDATE_RULES = [
    ((lambda a, b: isinstance2(a, b, enum.EnumMeta)), update_enum),
    ((lambda a, b: isinstance2(a, b, type)), update_class),
    ((lambda a, b: isinstance2(a, b, types.FunctionType)), update_function),
    ((lambda a, b: isinstance2(a, b, property)), update_property),
    ((lambda a, b: isinstance2(a, b, types.MemberDescriptorType)), (lambda a, b, extra: L_reload.ResetDescriptor(a, b))),
    ((lambda a, b: isinstance2(a, b, types.GetSetDescriptorType)), (lambda a, b, extra: L_reload.ResetDescriptor(a, b))),
    ((lambda a, b: isinstance2(a, b, types.MethodType)), update_method),
    ((lambda a, b: isinstance2(a, b, staticmethod)), update_method),
    ((lambda a, b: isinstance2(a, b, classmethod)), update_method),
    (is_inplace_updatable, inplace_container)]

def update_generic(a, b, extra_args):
    for type_check, update in UPDATE_RULES:
        if type_check(a, b):
            update(a, b, extra_args)
            return True
    
    return False


class StrongRef(object):
    
    def __init__(self, obj):
        self.obj = obj

    
    def __call__(self):
        return self.obj



class ExtraArgs(object):
    
    def __init__(self, root = None):
        self._root = root

    
    def init_root(self, purge_members):
        self._root = None
        self._cls_update_record = { }
        self._cls_new2old = { }
        self._purge_members = purge_members

    
    def clear(self):
        self.cls_update_record.clear()
        self.cls_new2old.clear()

    
    def is_root(self):
        return self._root is None

    
    def root(self):
        if self.is_root():
            return self
        return self._root

    root = property(root)
    
    def cls_update_record(self):
        if self.is_root():
            return self._cls_update_record
        return self._root._cls_update_record

    cls_update_record = property(cls_update_record)
    
    def cls_new2old(self):
        if self.is_root():
            return self._cls_new2old
        return self._root._cls_new2old

    cls_new2old = property(cls_new2old)
    
    def purge_members(self):
        if self.is_root():
            return self._purge_members
        return self._root._purge_members

    purge_members = property(purge_members)
    
    def create_args(self, **kwargs):
        args = ExtraArgs(self.root)
        args.extra = kwargs
        return args

    
    def record_class_update(self, old, new):
        self.cls_update_record[old] = new
        self.cls_new2old[new] = old

    
    def set_parent_attr(self, val):
        parent_info = self.extra
        if not parent_info:
            return None
        if 'obj' in parent_info:
            setattr(parent_info['obj'], parent_info['name'], val)
        else:
            parent_info['dict'][parent_info['name']] = val



def refresh_global_collection(module_dict, extra_args):
    for name, new_obj in list(module_dict.items()):
        args = extra_args.create_args(name = name, dict = module_dict)
        obj = refresh_object(new_obj, args)
        if obj is new_obj:
            continue
        module_dict[name] = obj
    


def module_rollback(module, old_dict):
    module.__dict__.clear()
    module.__dict__.update(old_dict)


def _superreload(module, reload, old_objects, purge_members):
    module_ref = { }
    for name, obj in list(module.__dict__.items()):
        if isinstance(obj, types.ModuleType):
            module_ref[name] = weakref.ref(obj)
        if not hasattr(obj, '__module__') or obj.__module__ != module.__name__:
            continue
        key = (module.__name__, name)
        
        try:
            old_objects.setdefault(key, []).append(weakref.ref(obj))
        except TypeError:
            continue

    
    old_dict = module.__dict__.copy()
    if purge_members:
        module.__dict__.clear()
        for name in old_dict.keys():
            if not name.startswith('__') and name.endswith('__'):
                continue
            module.__dict__[name] = old_dict[name]
        
    
    try:
        module = reload(module)
    except:
        module_rollback(module, old_dict)
        raise

    for name, obj in list(module.__dict__.items()):
        if name not in old_dict:
            continue
        old_obj = old_dict[name]
        if not isinstance2(obj, old_obj, type):
            continue
        if not hasattr(obj, '__module__') or obj.__module__ != module.__name__:
            continue
        old_slots = getattr(old_obj, '__slots__', None)
        new_slots = getattr(obj, '__slots__', None)
        if old_slots != new_slots:
            module_rollback(module, old_dict)
            raise TypeError('__slots__ attribute of two types must be same')
    
    extra_args = ExtraArgs()
    extra_args.init_root(purge_members)
    
    try:
        for name, new_obj in list(module.__dict__.items()):
            key = (module.__name__, name)
            if key not in old_objects:
                continue
            new_refs = []
            args = extra_args.create_args(name = name, dict = module.__dict__)
            for old_ref in old_objects[key]:
                old_obj = old_ref()
                if old_obj is None:
                    continue
                new_refs.append(old_ref)
                update_generic(old_obj, new_obj, args)
            
            if new_refs:
                old_objects[key] = new_refs
                continue
            del old_objects[key]
        
        for name, old_obj in module_ref.items():
            if hasattr(module, name):
                continue
            obj = old_obj()
            if obj is None:
                continue
            setattr(module, name, obj)
        
        new2old = extra_args.cls_new2old
        for old, new in extra_args.cls_update_record.items():
            if old.__bases__ == new.__bases__:
                continue
            bases = []
            for base in new.__bases__:
                old_base = new2old.get(base)
                if old_base is None:
                    bases.append(base)
                else:
                    bases.append(old_base)
            
            old.__bases__ = tuple(bases)
        
        refresh_global_collection(module.__dict__, extra_args)
    except:
        module_rollback(module, old_dict)
        raise

    extra_args.clear()
    return module

_RELOADING = { }

def superreload(module, reload = importlib.reload, old_objects = { }, purge_members = False):
    if hasattr(module, '__originmodule__'):
        dummy_module = module
        module = module._GetOriginModule(1)
        sys.modules[module.__name__] = module
    else:
        dummy_module = None
    
    try:
        name = module.__spec__.name
    except AttributeError:
        name = module.__name__

    if name in _RELOADING:
        return _RELOADING[name]
    _RELOADING[name] = module
    
    try:
        return _superreload(module, reload, old_objects, purge_members)
    finally:
        
        try:
            del _RELOADING[name]
        except KeyError:
            pass




def MyImport(sMod):
    if sMod.endswith('.__init__'):
        sMod = sMod[:-9]
    __import__(sMod)
    return sys.modules[sMod]


def RealReload(sMod):
    mod = MyImport(sMod)
    lstKeep = { }
    for cls in dir(mod):
        obj = getattr(mod, cls)
        l = type(obj)
        if not l == type:
            if l == type:
                attrlist = { }
                for attr in dir(obj):
                    if attr[0] == '_' and attr[1] != '_' or type(getattr(obj, attr)) == list:
                        attrlist[attr] = []
                        tempList = getattr(obj, attr)
                        for item in tempList:
                            attrlist[attr].append(item)
                        
                    elif type(getattr(obj, attr)) == dict:
                        attrlist[attr] = { }
                        tempList = getattr(obj, attr)
                        for key, val in tempList.items():
                            attrlist[attr][key] = val
                        
                    else:
                        attrlist[attr] = getattr(obj, attr)
                    if attr in obj.__dict__:
                        fatherlist = obj.mro()
                        for father in fatherlist:
                            if father == obj:
                                continue
                            if attr in father.__dict__:
                                delattr(obj, attr)
                                break
                        
                
        if len(attrlist):
            lstKeep[cls] = attrlist
    
    bPurge = False
    superreload(mod, purge_members = bPurge)
    if not bPurge:
        for cls, attrlist in lstKeep.items():
            obj = getattr(mod, cls)
            for attr, val in attrlist.items():
                if not not hasattr(obj, attr):
                    if getattr(obj, attr) != val or type(getattr(obj, attr)) == list:
                        tempList = getattr(obj, attr)
                        for item in val:
                            tempList.append(item)
                        
                    elif type(getattr(obj, attr)) == dict:
                        tempDict = getattr(obj, attr)
                        for key, value in val.items():
                            tempDict[key] = value
                        
                    else:
                        setattr(obj, attr, val)
                not hasattr(obj, attr)('恢复类%s属性:%s' % (cls, attr))
            
        
    if hasattr(mod, 'Init') and mod.Init.__module__ == mod.__name__:
        mod.Init()
    return mod

