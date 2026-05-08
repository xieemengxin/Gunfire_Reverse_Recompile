# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/daytrialpf/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/daytrialpf/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_commondefines import TYPE_RELIFE_PASSIVE, LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS
import cl_action

def CustonAction6723(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'LevelType' not in dMsgInfo:
        return None
    oLifeCycle = oEventCB.GetCBLifeCycle()
    sKey = oLifeCycle.GetStableKey()
    dRelifeIndo = oWarrior.Query('RelifeInfo', { })
    dType = dRelifeIndo.get(TYPE_RELIFE_PASSIVE, { })
    if sKey not in dType:
        return None
    iMaxTimes = dType[sKey][2]
    oWarrior.ModifyRelifeCnt(TYPE_RELIFE_PASSIVE, sKey, iMaxTimes)


def CustomAction6789(oWarrior, oEventCB, dInfo):
    oLifeCycle = oEventCB.GetCBLifeCycle()
    sKey = oLifeCycle.GetStableKey()
    iFlag = oWarrior.QuerySavedData(sKey, 0)
    if iFlag:
        return None
    oWarrior.SetSavedData(sKey, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0)

