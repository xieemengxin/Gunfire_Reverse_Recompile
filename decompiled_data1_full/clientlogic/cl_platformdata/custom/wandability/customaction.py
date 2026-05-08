# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/wandability/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/wandability/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_commondefines import DAM_TYPE_TRUE
from cl_only import SendAlert, ShufferList, Time2Frame
from cl_item.defines import EQUIP_SNIPER, EQUIP_TYPE_FUNDAMENTALWEAPON
import cl_formula
import cl_action
import cl_condition

def CustomAction51271(oWarrior, oEventCB, dInfo):
    if 'CycleNum' not in dInfo or 'StateList' not in dInfo or 'ContinueTime' not in dInfo or 'MaxStateCount' not in dInfo:
        SendAlert('err', '%s 参数异常 %s' % (oEventCB.m_Key, dInfo))
        return None
    iCycleNum = dInfo['CycleNum']
    iCycleNum = cl_formula.GetResultByData(oWarrior, iCycleNum, oEventCB.GetCBEventInfo(), oEventCB.GetCBMsgInfo())
    lstState = dInfo['StateList']
    if iCycleNum > dInfo['ThresholdNum']:
        iCycleNum = dInfo['ThresholdNum']
    lstChooseState = []
    dStateInfo = oWarrior.QuerySavedData('51271RewardState', { })
    for iStateSID in lstState:
        oState = oWarrior.m_State.GetItemBySID(iStateSID)
        if not oState:
            iStateCount = 0
        else:
            iStateCount = oState.GetCount()
        if iStateCount >= dInfo['MaxStateCount']:
            continue
        dStateInfo[iStateSID] = iStateCount
        lstChooseState.append(iStateSID)
    
    iContinueTime = dInfo['ContinueTime']
    for _ in range(iCycleNum):
        if lstChooseState:
            iStateSID = ShufferList(oWarrior.m_Game, lstChooseState, 1)[0]
            dStateInfo[iStateSID] += 1
            if dStateInfo[iStateSID] >= dInfo['MaxStateCount']:
                lstChooseState.remove(iStateSID)
            else:
                iStateSID = ShufferList(oWarrior.m_Game, lstState, 1)[0]
        None.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), iStateSID, iContinueTime, { }, 1)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), iStateSID, 1, iContinueTime)
    
    oWarrior.SetSavedData('51271RewardState', dStateInfo)


def CustomAction51271_Recory(oWarrior, oEventCB, dInfo):
    if 'ContinueTime' not in dInfo:
        SendAlert('err', '%s 参数异常 %s' % (oEventCB.m_Key, dInfo))
        return None
    dStateInfo = oWarrior.QuerySavedData('51271RewardState', { })
    if not dStateInfo:
        return None
    for iStateSID, iCount in dStateInfo.items():
        if iStateSID and iCount:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), iStateSID, dInfo['ContinueTime'], { }, 1)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), iStateSID, iCount, dInfo['ContinueTime'])
    

