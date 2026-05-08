# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_action/ac_task.pyc
# RelativePath: clientlogic/cl_action/ac_task.pyc
# Source Generated with Decompyle++
# File: ac_task.pyc (Python 3.6)

from cl_commondefines import STATE_TIME_LIMIT, STATE_TIME_FOREVER, DISABLE_TYPE_STATE, TASK_STATUS_FAIL, TASK_STATUS_SUCCESS, TASK_STATUS_CLEARNING
from cl_only import Time2Frame, ShufferList, SendAlert
from cl_cscommondef import EQUIP_TYPE_MAINWEAPON
import cl_formula
import cl_object.reason
import cl_state
import cl_item.defines as itemdef
import cl_msgcenter
import cl_platformdata
import cl_minigame

def PauseTaskStatCal(oTarget, oLifeCycle, sReason):
    oTask = oLifeCycle.GetObject()
    if oTask:
        oTask.Pause(sReason)


def ResumeTaskStatCal(oTarget, oLifeCycle, sReason):
    oTask = oLifeCycle.GetObject()
    if oTask:
        oTask.Resume(sReason)


def TaskAddPerform(oTarget, oLifeCycle, iPerform):
    oTask = oLifeCycle.GetObject()
    if oTask:
        oTask.AddPerform(iPerform)


def TaskAddState(oTarget, oLifeCycle, iState, iTime, dArgs, iCloseRemove):
    dData = {
        'LifeCycle': oLifeCycle }
    dRet = cl_formula.CalArgsFormula(oTarget, dArgs, dData)
    oTask = oLifeCycle.GetObject()
    if not oTask:
        return None
    oReason = cl_object.reason.CStrReason(oLifeCycle.Key())
    dArgs = {
        'AID': oTarget.m_ID,
        'RS': oReason,
        'TaskID': oTask.m_ID,
        'TaskQuality': oTask.m_Quality,
        'arg': dRet }
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = cl_formula.GetResultByData(oTarget, iTime, dData)
    else:
        iTimeType = STATE_TIME_FOREVER
    oState = cl_state.AddState(oTarget, iState, iTimeType, Time2Frame(iTime), dArgs)
    if not oState:
        return None
    oState.Enable(oTarget)
    if iCloseRemove:
        oLifeCycle.AddDisableType(DISABLE_TYPE_STATE, {
            oTarget.m_ID: oState.m_ID })


def TaskTransDisableInscription(oTarget, oLifeCycle, iNum = 1):
    oTask = oLifeCycle.GetObject()
    if not oTask:
        return None
    oWeapon = oTarget.m_WieldCon.GetCurWeapon(itemdef.MAIN_HOLD)
    if not oWeapon or oWeapon.m_Type == itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON:
        lstWeapon = oTarget.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
        if not lstWeapon:
            return None
        oWeapon = lstWeapon[0]
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if not oInscriptionCom:
        return None
    sKey = 'DisableInscription-%s-%s' % (oTask.m_ID, oWeapon.m_ID)
    dInscription = oTask.GetSaveData(sKey, { })
    if not dInscription:
        dInscription = oInscriptionCom.RandomTempDisableInscription(sKey, iNum)
    oInscriptionCom.TransDisableInscirption(sKey, dInscription)


def TaskDisablePunishPassive(oTarget, oLifeCycle):
    oTask = oLifeCycle.GetObject()
    oTask.RemovePunish()


def TaskSetSaveInfo(oTarget, oLifeCycle, sKey, iValue):
    oTask = oLifeCycle.GetObject()
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    oTask.SetSaveData(sKey, iValue, iCover = 1)


def TaskAddSaveInfo(oTarget, oLifeCycle, sKey, iValue):
    oTask = oLifeCycle.GetObject()
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    oTask.AddSaveData(sKey, iValue)


def TaskGetSaveInfo(oTarget, oLifeCycle, sKey):
    oTask = oLifeCycle.GetObject()
    return oTask.GetSaveData(sKey)


def TaskDelInfo(oTarget, oLifeCycle, sKey):
    oTask = oLifeCycle.GetObject()
    return oTask.DelData(sKey)


def TaskChooseFailTaskReStart(oTarget, oLifeCycle, iNum, lstExcludeTask):
    oTask = oLifeCycle.GetObject()
    iFailTaskID = oTask.GetSaveData('RestartFailTask', 0)
    if iFailTaskID:
        return None
    dFailTask = { }
    iMaxQuality = 0
    lstFailTask = oTarget.m_TaskCon.GetTaskByHasPunish(iHasPunish = 1, iStatus = TASK_STATUS_FAIL)
    if len(lstFailTask) < 1:
        SendAlert('err', '%s 抽取失败任务异常 %s %s' % (oTarget.m_Game.m_ID, oTarget.m_PlayerID, oLifeCycle.Key()))
        return None
    lstFailTask = ShufferList(oTarget.m_Game, lstFailTask, iNum)
    lstFailTaskID = []
    for oFailTask in lstFailTask:
        iQuality = oFailTask.m_Quality
        iTaskSID = oFailTask.m_SID
        lstFailTaskID.append(oFailTask.m_ID)
        oFailTask.OnlyChangeStatus(TASK_STATUS_CLEARNING)
        if iTaskSID in lstExcludeTask:
            continue
        if iQuality > iMaxQuality:
            iMaxQuality = iQuality
        if iQuality not in dFailTask:
            dFailTask[iQuality] = [
                oFailTask]
            continue
        dFailTask[iQuality].append(oFailTask)
    
    oTask.SetSaveData('ClearPunishTask', lstFailTaskID)
    if not dFailTask:
        SendAlert('err', '%s 未抽取到失败任务 %s %s' % (oTarget.m_Game.m_ID, oTarget.m_PlayerID, oLifeCycle.Key()))
        return None
    lstTask = dFailTask[iMaxQuality]
    oFailTask = lstTask[oTarget.m_Game.Random(len(lstTask))]
    oTask.SetSaveData('RestartFailTask', oFailTask.m_ID)
    oTask.BuildSubTask(oFailTask.m_SID)


def TaskClearUpFailTaskPunish(oTarget, oLifeCycle, iClearAll = 0):
    oTask = oLifeCycle.GetObject()
    if iClearAll:
        lstClearPunishTaskID = [ oTask.m_ID for oTask in oTarget.m_TaskCon.GetTaskByHasPunish(iHasPunish = 1, iStatus = TASK_STATUS_FAIL) ]
    else:
        lstClearPunishTaskID = oTask.GetSaveData('ClearPunishTask', [])
    for iFailTaskID in lstClearPunishTaskID:
        oFailTask = oTarget.m_TaskCon.GetTaskByID(iFailTaskID)
        oFailTask.RemovePunish()
        if oFailTask.m_ClearAction:
            cls = cl_platformdata.GetTaskClass(oFailTask.m_SID)
            oTaskLifeCycle = oFailTask.m_LifeCycle
            cls.m_ClearAction(oTarget, oTaskLifeCycle)
        oFailTask.OnlyChangeStatus(TASK_STATUS_SUCCESS)
    


def TaskRecorvyInscriptionAndGrade(oTarget, oLifeCycle, iGrade):
    if iGrade < 0:
        SendAlert('err', '%s 任务恢复等级未配置' % oLifeCycle.Key())
        return None
    oTask = oLifeCycle.GetObject()
    lstWeapon = oTarget.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
    sKey = 'DisableInscription-%s-' % oTask.m_ID
    for oWeapon in lstWeapon:
        sTempKey = sKey + '%s' % oWeapon.m_ID
        dInscription = oTask.GetSaveData(sTempKey, { })
        if dInscription:
            iBaseGrade = oWeapon.m_BaseGrade
            oWeapon.SetBaseGrade(iBaseGrade + iGrade)
            oInscriptionCom = oWeapon.GetComponent('Inscription')
            for iSID, _ in dInscription.items():
                oInscriptionCom.OnRemoveDisableInscription(iSID)
            
    


def TaskBuildPreChooseSubTask(oTarget, oLifeCycle):
    oTask = oLifeCycle.GetObject()
    if oTask.m_SubTask:
        return None
    if 'SubTaskSID' in oTask.m_InitData:
        iSubTask = oTask.m_InitData['SubTaskSID']
        oTask.BuildSubTask(iSubTask)
    else:
        SendAlert('err', '%s 未获取到子任务 %s %s %s ' % (oTarget.m_Game.m_ID, oTarget.m_PlayerID, oLifeCycle.Key(), oTask.m_SID))


def TaskRecoverFailTaskStatus(oTarget, oLifeCycle):
    oTask = oLifeCycle.GetObject()
    lstClearPunishTaskID = oTask.GetSaveData('ClearPunishTask', [])
    for iFailTaskID in lstClearPunishTaskID:
        oFailTask = oTarget.m_TaskCon.GetTaskByID(iFailTaskID)
        oFailTask.OnlyChangeStatus(TASK_STATUS_FAIL)
    

