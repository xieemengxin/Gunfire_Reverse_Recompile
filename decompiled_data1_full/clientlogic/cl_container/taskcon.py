# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/taskcon.pyc
# RelativePath: clientlogic/cl_container/taskcon.pyc
# Source Generated with Decompyle++
# File: taskcon.pyc (Python 3.6)

from cl_only import WeakProxy, DeepCopy
from cl_object.logging import TaskLog
from cl_commondefines import BAG_TYPE_TASK, LEVEL_TYPE_FIGHT, TASK_STATUS_RUNNING
from cl_commondecorator import CheckFaultTolerance
import cl_task
import cl_snetwar
import cl_msgcenter
import cl_platformdata

class CTaskContainer(object):
    m_BagType = BAG_TYPE_TASK
    
    def __init__(self, oWarrior):
        self.m_Owner = oWarrior.m_ID
        self.m_PlayerID = oWarrior.m_PlayerID
        self.m_Game = oWarrior.m_Game
        self.m_Task = { }
        self.m_PauseReason = { }
        self.m_PauseSelfReason = { }
        self.m_OnlyPunishInFightLevelTask = { }
        self.m_ExcludeTask = { }
        self.m_SubTasks = { }
        self.AddAttention()

    
    def Release(self):
        if not self.m_Game:
            return None
        self.DoneAttention()
        for oTask in self.m_Task.values():
            oTask.Release()
        
        self.m_Task = { }
        self.m_Game = None

    
    def Save(self):
        dData = { }
        lstTaskSaveInfo = []
        for oTask in self.m_Task.values():
            lstTaskSaveInfo.append(oTask.Save())
        
        dData['SaveInfo'] = DeepCopy(lstTaskSaveInfo)
        return dData

    
    def Load(self, dData):
        if not dData or 'SaveInfo' not in dData:
            return None
        for dTaskData in dData['SaveInfo']:
            iTaskSID = dTaskData['SID']
            self.AddTask(iTaskSID, 'load', dTaskData, iNotify = 0)
        
        self.Refresh()

    
    def AddAttention(self):
        oOwner = self.GetOwner()
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_DIEDIST, self.OnOwnerDie, 'TaskOwnerDie', iOnce = 0)
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_RELIFE, self.OnOwnerRelife, 'TaskOwnerRelife', iOnce = 0)
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnOwnerEnterScene, 'TaskOwnerEnterScene', iOnce = 0)

    
    def DoneAttention(self):
        oOwner = self.GetOwner()
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_DIEDIST, 'TaskOwnerDie')
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_RELIFE, 'TaskOwnerRelife')
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_ENTERSCENE, 'TaskOwnerEnterScene')

    
    def OnOwnerDie(self, oOwner, dMsgInfo):
        self.PauseSelf('Die')

    
    def OnOwnerRelife(self, oOwner, dMsgInfo):
        self.ResumeSelf('Die')

    
    def OnOwnerEnterScene(self, oOwner, dMsgInfo):
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        if not oScene:
            return None
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.GetLevelType(oScene.m_Level) == LEVEL_TYPE_FIGHT:
            self.Resume('LeaveFightLevel')
            if not self.m_PauseReason:
                for iTaskID in self.m_OnlyPunishInFightLevelTask:
                    oTask = self.m_Task[iTaskID]
                    oTask.EnablePunish()
                
            else:
                self.Pause('LeaveFightLevel')
                for iTaskID in self.m_OnlyPunishInFightLevelTask:
                    oTask = self.m_Task[iTaskID]
                    oTask.DisablePunish()
                

    
    def Pause(self, sReason):
        if sReason in self.m_PauseReason:
            return None
        TaskLog.Debug('%d %d pause %s %s' % (self.m_Game.m_ID, self.m_PlayerID, sReason, list(self.m_PauseReason)))
        if not self.m_PauseReason:
            for oTask in self.GetTasksByStatus(TASK_STATUS_RUNNING):
                oTask.Disable(iPause = 1)
            
        self.m_PauseReason[sReason] = 1

    
    def Resume(self, sReason):
        if sReason not in self.m_PauseReason:
            return None
        TaskLog.Debug('%d %d resume %s %s' % (self.m_Game.m_ID, self.m_PlayerID, sReason, list(self.m_PauseReason)))
        self.m_PauseReason.pop(sReason)
        if not self.m_PauseReason:
            for oTask in self.GetTasksByStatus(TASK_STATUS_RUNNING):
                oTask.Enable()
            

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def Refresh(self):
        lstTask = list(self.m_Task.values())
        lstStatusInfo = []
        lstStatInfo = []
        for oTask in lstTask:
            lstStatusInfo.append(oTask.BuildStatusInfo())
            if not oTask.IsEnd():
                lstStatInfo.append(oTask.BuildAllStatInfo())
        
        self.GS2CTaskStatus(lstStatusInfo)
        self.GS2CTaskStat(lstStatInfo)

    
    def OnTaskChangeStatus(self, iTaskID, iParentTaskID = 0):
        if iTaskID not in self.m_Task and not iParentTaskID:
            return None
        if not iParentTaskID:
            oTask = self.m_Task[iTaskID]
            if oTask.m_OnlyPunishInFightLevel and oTask.IsEnd():
                self.m_OnlyPunishInFightLevelTask.pop(iTaskID, 0)
            else:
                oParentTask = self.GetTaskByID(iParentTaskID)
                oTask = oParentTask.m_SubTask
        None.GS2CTaskStatus([
            oTask.BuildStatusInfo()])

    
    def OnTaskChangeStat(self, iTaskID, iStatIndex, iValue):
        self.GS2CTaskStat([
            (iTaskID, ((iStatIndex, iValue),))])

    
    def GS2CTaskStatus(self, lstStatusInfo):
        if not lstStatusInfo:
            return None
        cl_snetwar.GS2CTaskStatus(self.m_PlayerID, lstStatusInfo)

    
    def GS2CTaskStat(self, lstStatInfo):
        if not lstStatInfo:
            return None
        cl_snetwar.GS2CTaskStat(self.m_PlayerID, lstStatInfo)

    
    def AddTask(self, iTaskSID, sReason, dData = None, iNotify = 1, dInitData = None):
        if dInitData is None:
            dInitData = { }
        iID = dData['ID'] if dData and 'ID' in dData else self.m_Game.NewNoSceneObjID()
        oTask = cl_task.NewTask(iTaskSID, iID, self.m_Game, self.m_Owner)
        if not oTask:
            TaskLog.Alert('%d %d add %d err %s' % (self.m_Game.m_ID, self.m_PlayerID, iTaskSID, sReason))
            return None
        oTask.m_InitData = dInitData
        TaskLog.Info('%d %d add %d-%d %s' % (self.m_Game.m_ID, self.m_PlayerID, iID, iTaskSID, sReason))
        oTask.m_Container = WeakProxy(self)
        self.m_Task[oTask.m_ID] = oTask
        oTask.Load(dData)
        if not self.m_PauseReason:
            oTask.Enable()
        if oTask.m_ExcludeTask:
            self.m_ExcludeTask.update(oTask.m_ExcludeTask)
        if oTask.m_OnlyPunishInFightLevel and not oTask.IsEnd():
            self.m_OnlyPunishInFightLevelTask[oTask.m_ID] = 1
        if iNotify:
            self.GS2CTaskStatus([
                oTask.BuildStatusInfo()])
            self.GS2CTaskStat([
                oTask.BuildAllStatInfo()])
        return oTask

    
    def RemoveTask(self, iTaskID, sReason):
        if iTaskID not in self.m_Task:
            return None
        oTask = self.m_Task[iTaskID]
        TaskLog.Info('%d %d remove %d-%d %s' % (self.m_Game.m_ID, self.m_PlayerID, iTaskID, oTask.m_SID, sReason))
        if oTask.m_OnlyPunishInFightLevel:
            self.m_OnlyPunishInFightLevelTask.pop(iTaskID, 0)
        oTask.Release()
        self.m_Task.pop(iTaskID)

    
    def GetTasksByStatus(self, iStatus):
        lstTask = []
        for oTask in self.m_Task.values():
            if oTask.m_Status == iStatus:
                lstTask.append(oTask)
        
        return lstTask

    
    def GetTaskByHasPunish(self, iHasPunish, iStatus = 0):
        lstTask = []
        for oTask in self.m_Task.values():
            if not oTask.m_HasPunish == iHasPunish or not iStatus:
                if oTask.m_Status == iStatus:
                    lstTask.append(oTask)
                    continue
        
        return lstTask

    
    def GetTaskByID(self, iTaskID):
        if iTaskID not in self.m_Task:
            return None
        return self.m_Task[iTaskID]

    
    def GetAllTaskStatus(self):
        dTaskStatus = { }
        for oTask in self.m_Task.values():
            dTaskStatus[oTask.m_SID] = oTask.m_Status
        
        return dTaskStatus

    
    def GetRunningTaskCntBySID(self, tSID):
        return len([ oTask for oTask in self.GetTasksByStatus(TASK_STATUS_RUNNING) if oTask.m_SID in tSID ])

    
    def BuildChooseTask(self, dChooseWeight, iExecChooseBeforeCond = 1):
        dCanChooseTask = { }
        dTaskBeforeChooseCond = cl_platformdata.GetTaskBeforeChooseCond()
        oTaskElement = self.m_Game.m_WarMgr.GetComponent('TaskElement')
        dTeamExcludeTask = oTaskElement.GetTeamExcludeTask() if oTaskElement else { }
        oOwner = self.m_Game.GetObject(self.m_Owner)
        for iSID in dChooseWeight:
            if iSID in self.m_ExcludeTask:
                continue
            if iSID in dTeamExcludeTask:
                continue
            if iExecChooseBeforeCond and iSID in dTaskBeforeChooseCond:
                clsTask = cl_platformdata.GetTaskClass(iSID)
                if not clsTask:
                    continue
                if not clsTask.m_BeforeChooseCond(oOwner):
                    continue
                continue
            dCanChooseTask[iSID] = dChooseWeight[iSID]
        
        return dCanChooseTask

    
    def AllTaskDisable(self):
        for oTask in self.m_Task.values():
            oTask.AllDisable()
        

    
    def AllTaskPerformDisable(self):
        for oTask in self.m_Task.values():
            oTask.AllPerformDisable()
        

    
    def AllTaskPerformEnable(self):
        for oTask in self.m_Task.values():
            oTask.AllPerformEnable()
        

    
    def PauseSelf(self, sReason):
        self.Pause(sReason)
        if not self.m_PauseSelfReason:
            self.AllTaskPerformDisable()
        self.m_PauseSelfReason[sReason] = 1

    PauseSelf = CheckFaultTolerance(PauseSelf)
    
    def ResumeSelf(self, sReason):
        self.Resume(sReason)
        if sReason not in self.m_PauseSelfReason:
            return None
        self.m_PauseSelfReason.pop(sReason)
        if not self.m_PauseSelfReason:
            self.AllTaskPerformEnable()
            self.OnOwnerEnterScene(self.GetOwner(), { })

    
    def EnableTaskPerform(self, dTask):
        for oTask in self.m_Task.values():
            if oTask.m_SID not in dTask:
                continue
            for iPerform in dTask[oTask.m_SID]:
                oTask.EnablePerform(iPerform)
            
        

    
    def AddSubTask(self, iTaskID, iSubTaskID, sReason):
        if iTaskID not in self.m_Task:
            TaskLog.Debug('%d %d addsubtask err %s' % (self.m_Game.m_ID, self.m_PlayerID, sReason))
            return None
        if iSubTaskID in self.m_SubTasks:
            return None
        self.m_SubTasks[iSubTaskID] = iTaskID

    
    def GetParentIDBySubTaskID(self, iSubTaskID):
        if iSubTaskID not in self.m_SubTasks:
            return 0
        return self.m_SubTasks[iSubTaskID]

    
    def CheckSubTaskRunning(self, iSubTaskID):
        if iSubTaskID in self.m_SubTasks:
            return 1
        return 0

    
    def RemoveSubTask(self, iSubTaskID):
        if iSubTaskID in self.m_SubTasks:
            self.m_SubTasks.pop(iSubTaskID, 0)


