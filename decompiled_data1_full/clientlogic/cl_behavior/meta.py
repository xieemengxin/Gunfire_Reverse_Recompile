# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/meta.pyc
# RelativePath: clientlogic/cl_behavior/meta.pyc
# Source Generated with Decompyle++
# File: meta.pyc (Python 3.6)

from __future__ import absolute_import
import importlib
from . import tools

def ParseMethod(dProperties, sValue, default):
    if sValue not in dProperties:
        return default
    if dProperties[sValue] is None:
        return default
    (func, tArgs) = dProperties[sValue]
    return tools.g_Tools.Functor(func, *tArgs)


def ParseProperty(dProperties, sValue, default):
    if sValue not in dProperties:
        return default
    return dProperties[sValue]


def TransMethod(oMethod):
    return ('', ())


def TransMethod2(oMethod):
    return ('', ())


def TransMethod3(oMethod1, sFlag, oMethod2):
    return ('', ())

