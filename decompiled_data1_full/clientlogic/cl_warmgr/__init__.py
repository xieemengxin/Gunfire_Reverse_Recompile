# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/__init__.pyc
# RelativePath: clientlogic/cl_warmgr/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

import importlib
from . import mobject
from cl_only import PythonError

def LoadWarMgr(oGame, iWarNo):
    mod = importlib.import_module('cl_wardata.wm%4d' % iWarNo)
    iID = oGame.NewNPCID()
    obj = mod.CWarManager(oGame, iID)
    oGame.CreateObject(iID, obj)
    return obj

