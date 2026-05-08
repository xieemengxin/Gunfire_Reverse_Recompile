# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_condition/con_task.pyc
# RelativePath: clientlogic/cl_condition/con_task.pyc
# Source Generated with Decompyle++
# File: con_task.pyc (Python 3.6)


def TaskCheckTaskStatus(oTarget, oLifeCycle, iStatus):
    oTask = oLifeCycle.GetObject()
    if not oTask:
        return 0
    if oTask.m_Status != iStatus:
        return 0
    return 1


def TaskCheckSelfSubTask(oTarget, oLifeCycle):
    oTask = oLifeCycle.GetObject()
    if oTask.m_ParentTaskID:
        return 1
    return 0


def TaskCheckOwnerTaskNum(oTarget, iHasPunish, iStatus, dSpecialPunish):
    lstTask = oTarget.m_TaskCon.GetTaskByHasPunish(iHasPunish = iHasPunish, iStatus = iStatus)
    iNum = 0
    for oTask in lstTask:
        if iHasPunish and oTask.m_SID in dSpecialPunish:
            oState = oTarget.m_State.GetItemBySID(dSpecialPunish[oTask.m_SID])
            if oState and oState.GetCount() == 0:
                continue
            continue
        iNum += 1
    
    return iNum


def TaskCheckTaskNPCRefreshNum(oTarget):
    oTaskElement = oTarget.m_Game.m_WarMgr.GetComponent('TaskElement')
    if oTaskElement:
        return oTaskElement.m_TaskNum
    return 0


def TaskGetTaskStatValue(oTarget, oLifeCycle, iStatIdx):
    oTask = oLifeCycle.GetObject()
    if oTask:
        return oTask.GetTaskStatValue(iStatIdx)
    return 0


def TaskGetOwnerSavedData(oTarget, sKey):
    return oTarget.QuerySavedData('save.' + sKey)

