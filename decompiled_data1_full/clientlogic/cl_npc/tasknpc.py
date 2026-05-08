# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/tasknpc.pyc
# RelativePath: clientlogic/cl_npc/tasknpc.pyc
# Source Generated with Decompyle++
# File: tasknpc.pyc (Python 3.6)

from cl_commondefines import NPC_CB_VALUE, TASK_STATUS_RUNNING, INTERACT_TYPE_FORBID, TASK_CREATETASKLIST, TASK_CHOOSETASK, NPC_CB_REFRESH, TASK_CHOOSE_STATUS_LOCK, TASK_CHOOSE_STATUS_CHOSEN, TASK_CHOOSE_STATUS_NORMAL, TASK_CHOOSE_STATUS_UNRECEIVED
from cl_object.logging import WarnpcLog
from cl_npc.tasknpcaction import GetTaskOptionAction, GetTaskSelectedAction
from cl_npc.tasknpccondition import GetTaskOptionCondition
from cl_only import SendAlert
import cl_msgcenter
import cl_platformdata
from . import mobject
from . import net
NPC_BASE_INTERACT_NUM = 1

class CTaskNPC(mobject.CNPC):
    
    def __init__(self, *args):
        super().__init__(*args)
        self.m_TaskData = { }
        oTaskElement = self.m_Game.m_WarMgr.GetComponent('TaskElement')
        self.m_RemainInteractNum = { }
        self.m_TaskExtraSubTask = { }
        self.m_ChooseRecord = { }
        self.m_ForbidExtraInteract = []
        self.m_MaxRunningTask = oTaskElement.m_MaxRunningTask if oTaskElement else 0
        self.m_ExcludeTask = { }

    
    def Interact(self, oHero, iType = 0):
        if not self.ValidInteract(oHero):
            return None
        iHero = oHero.m_ID
        if iHero not in self.m_TaskData and self.m_ActionFunc:
            self.m_RemainInteractNum[iHero] = NPC_BASE_INTERACT_NUM
            self.m_ActionFunc(self, oHero)
            if iHero in self.m_TaskData:
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TASK, oHero, {
                    'NpcID': self.m_ID,
                    'TaskInfo': self.m_TaskData[iHero] }, iSub = TASK_CREATETASKLIST)
                self.TaskSelectedAction(oHero)
        self.RefreshUI(oHero)

    
    def BuildExcludeTask(self, iHero):
        if iHero not in self.m_TaskData:
            return None
        dExclude = self.m_ExcludeTask.setdefault(iHero, { })
        for iTaskSID in self.m_TaskData[iHero].values():
            clsTask = cl_platformdata.GetTaskClass(iTaskSID)
            if clsTask and clsTask.m_NpcExcludeTask:
                dExclude[iTaskSID] = 1
                dExclude.update(clsTask.m_NpcExcludeTask)
        

    
    def GetNpcExcludeTask(self, iHero):
        if iHero in self.m_ExcludeTask:
            return list(self.m_ExcludeTask[iHero])
        return []

    
    def SetTaskInfo(self, iHero, dTaskInfo):
        if iHero in self.m_TaskData:
            return None
        oHero = self.m_Game.GetObject(iHero)
        WarnpcLog.Debug('%d %d taskinfo %s' % (self.m_Game.m_ID, oHero.m_PlayerID, dTaskInfo))
        self.m_TaskData[iHero] = dTaskInfo
        self.BuildExcludeTask(iHero)

    
    def TaskSelectedAction(self, oHero):
        dSelectedAction = GetTaskSelectedAction()
        iHero = oHero.m_ID
        dTaskInfo = self.m_TaskData[iHero]
        for iTaskSID in dTaskInfo.values():
            if iTaskSID not in dSelectedAction:
                continue
            funcOption = dSelectedAction[iTaskSID]['Func']
            funcOption(oHero, self, iTaskSID, dSelectedAction[iTaskSID]['Args'])
        

    
    def RefreshUI(self, oHero):
        iHero = oHero.m_ID
        if iHero not in self.m_TaskData:
            return None
        dTaskInfo = self.m_TaskData[iHero]
        lstTaskInfo = []
        dTaskChooseStatus = self.GetTaskChooseStatus(oHero, dTaskInfo)
        dTaskExtraSubTaskInfo = self.m_TaskExtraSubTask.setdefault(iHero, { })
        for iIndex, iTaskSID in dTaskInfo.items():
            if iTaskSID in dTaskExtraSubTaskInfo:
                iExtraSubTask = dTaskExtraSubTaskInfo[iTaskSID]
            else:
                iExtraSubTask = 0
            iChooseStatus = dTaskChooseStatus[iIndex]
            lstTaskInfo.append((iIndex, iTaskSID, iChooseStatus, iExtraSubTask))
        
        iCanRefreshTimes = oHero.QuerySavedData('save.TaskRefreshTimes', 0)
        net.GS2CNpcTask(oHero, self.m_ID, lstTaskInfo, iCanRefreshTimes)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, self.HeroChooseTaskBefore, self)
        if iCanRefreshTimes:
            net.SetNpcUICallBackFunction(oHero, NPC_CB_REFRESH, self.HeroRefreshTaskInfo, self)

    
    def GetTaskChooseStatus(self, oHero, dTaskInfo):
        iHero = oHero.m_ID
        dCondition = GetTaskOptionCondition()
        iForBidLastChoose = 0
        dLimitChooseInfo = self.GetArgValue('LimitTaskInfo', { })
        if iHero in dLimitChooseInfo and 'ChooseNum' in dLimitChooseInfo[iHero]:
            iForBidLastChoose = 1
        dChooseRecord = self.m_ChooseRecord[iHero] if iHero in self.m_ChooseRecord else { }
        dTaskChooseStatus = { }
        for iIndex, iTaskSID in dTaskInfo.items():
            iChooseStatus = TASK_CHOOSE_STATUS_NORMAL
            if iTaskSID in dChooseRecord:
                iChooseStatus = TASK_CHOOSE_STATUS_CHOSEN
            elif iIndex == len(dTaskInfo) - 1 and iForBidLastChoose:
                iChooseStatus = TASK_CHOOSE_STATUS_LOCK
            elif iTaskSID in dCondition:
                func = dCondition[iTaskSID]['Func']
                iEnable = func(oHero, iTaskSID, dCondition[iTaskSID]['Args'])
                if not iEnable:
                    iChooseStatus = TASK_CHOOSE_STATUS_UNRECEIVED
            dTaskChooseStatus[iIndex] = iChooseStatus
        
        return dTaskChooseStatus

    
    def HeroRefreshTaskInfo(self, oHero):
        iCanRefreshTimes = oHero.QuerySavedData('save.TaskRefreshTimes', 0)
        if iCanRefreshTimes <= 0:
            self.RefreshUI(oHero)
            WarnpcLog.Alert('%d %d no refreshtimes' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        iCanRefreshTimes -= 1
        iHero = oHero.m_ID
        oHero.SetSavedData('save.TaskRefreshTimes', iCanRefreshTimes)
        self.m_ChooseRecord.pop(iHero, None)
        self.m_TaskExtraSubTask.pop(iHero, None)
        self.Set('DebugMulChoose', 1)
        self.m_TaskData.pop(iHero, { })
        self.m_ActionFunc(self, oHero)
        if iHero in self.m_TaskData:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TASK, oHero, {
                'NpcID': self.m_ID,
                'TaskInfo': self.m_TaskData[iHero],
                'RefreshTask': 1 }, iSub = TASK_CREATETASKLIST)
            self.TaskSelectedAction(oHero)
        self.RefreshUI(oHero)

    
    def HeroChooseTaskBefore(self, oHero, iChoose):
        iHero = oHero.m_ID
        if iHero not in self.m_TaskData:
            WarnpcLog.Alert('%d %d taskdata %s empty' % (self.m_Game.m_ID, oHero.m_PlayerID, self.m_TaskData))
            return None
        dTask = self.m_TaskData[iHero]
        if iChoose not in dTask:
            WarnpcLog.Alert('%d %d %s answer%d err' % (self.m_Game.m_ID, oHero.m_PlayerID, dTask, iChoose))
            return None
        if self.m_MaxRunningTask and len(oHero.m_TaskCon.GetTasksByStatus(TASK_STATUS_RUNNING)) >= self.m_MaxRunningTask:
            WarnpcLog.Alert('%d %d task too more' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        iTaskSID = dTask[iChoose]
        dOptionAction = GetTaskOptionAction()
        if iTaskSID not in dOptionAction:
            self.HeroChooseTask(oHero, iTaskSID)
        else:
            funcOption = dOptionAction[iTaskSID]['Func']
            funcOption(oHero, self, iTaskSID, dOptionAction[iTaskSID]['Args'])

    
    def HeroChooseTask(self, oHero, iTaskSID):
        iHero = oHero.m_ID
        bForbidInteract = True
        iRemainInteractNum = self.m_RemainInteractNum[iHero]
        iSavedInteractNum = oHero.QuerySavedData('save.ExtraReceiveTaskNum', 0)
        if iRemainInteractNum > 0:
            iRemainInteractNum -= 1
            self.m_RemainInteractNum[iHero] = iRemainInteractNum
        elif iSavedInteractNum > 0:
            iSavedInteractNum -= 1
            oHero.SetSavedData('save.ExtraReceiveTaskNum', iSavedInteractNum)
        else:
            oHero.DelSavedData('save.ExtraReceiveTaskNum')
            self.SetPlayerInteractType(INTERACT_TYPE_FORBID, [
                oHero.m_PlayerID])
            SendAlert('err', '%s interactnum exception %s %s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, iTaskSID))
            return None
        if iRemainInteractNum > 0 or iSavedInteractNum > 0:
            bForbidInteract = False
        if iHero in self.m_ChooseRecord:
            self.m_ChooseRecord[iHero][iTaskSID] = 1
        else:
            self.m_ChooseRecord[iHero] = {
                iTaskSID: 1 }
        if bForbidInteract or iHero in self.m_ForbidExtraInteract:
            self.SetPlayerInteractType(INTERACT_TYPE_FORBID, [
                oHero.m_PlayerID])
        else:
            self.RefreshUI(oHero)
        dTaskExtraSubTaskInfo = self.m_TaskExtraSubTask.setdefault(iHero, { })
        dTaskInitData = { }
        if iTaskSID in dTaskExtraSubTaskInfo:
            dTaskInitData['SubTaskSID'] = dTaskExtraSubTaskInfo[iTaskSID]
        oTask = oHero.m_TaskCon.AddTask(iTaskSID, 'tasknpc', dInitData = dTaskInitData)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TASK, oHero, {
            'NpcID': self.m_ID,
            'TaskID': oTask.m_ID,
            'TaskSID': iTaskSID }, iSub = TASK_CHOOSETASK)
        return oTask

    
    def ForbidExtraInteract(self, oHero):
        iHero = oHero.m_ID
        if iHero not in self.m_ForbidExtraInteract:
            self.m_ForbidExtraInteract.append(iHero)


