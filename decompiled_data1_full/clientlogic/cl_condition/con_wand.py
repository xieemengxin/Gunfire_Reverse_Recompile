# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_condition/con_wand.pyc
# RelativePath: clientlogic/cl_condition/con_wand.pyc
# Source Generated with Decompyle++
# File: con_wand.pyc (Python 3.6)


def WandCompGetArgValue(oOwner, oLifeCycle, sArg):
    oWandComp = oLifeCycle.GetObject()
    return oWandComp.GetArgValue(sArg, 0)


def WandCompGetKeepValue(oOwner, oLifeCycle, sKey):
    oWandComp = oLifeCycle.GetObject()
    return oWandComp.GetKeepValue(sKey, 0)

