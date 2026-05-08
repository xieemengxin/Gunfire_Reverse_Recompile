# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_task/mobject.pyc
# RelativePath: clientlogic/cl_task/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_object.logging import TaskLog
from cl_commondefines import TASK_STATUS_RUNNING, TASK_STATUS_SUCCESS, TASK_STATUS_FAIL, TASK_TYPE_NORMAL, TASK_CHANGESTATUS
from cl_only import WeakProxy
import cl_msgcenter
import cl_object.lifecycle
import cl_msgcenter.eventcbobj
import cl_task
import cl_platformdata

class CBaseTask(object):
    m_SID = 0
    m_TargetSID = 0
    m_Name = ''
    m_Description = ''
    m_Quality = TASK_TYPE_NORMAL
    m_TargetStats = { }
    m_LimitTarget = { }
    m_RecordStats = { }
    m_Action = (None, None)
    m_ClearAction = None
    m_CBFuncAction = { }
    m_RewardPerformSID = 0
    m_PunishPerformSID = 0
    m_OnlyPunishInFightLevel = 0
    m_ExcludeTask = { }
    m_HasPunish = 0
    m_StatsLimit = { }
    m_NpcExcludeTask = { }
    
    def __init__(self, iID, oGame, iOwner):
        self.m_ID = iID
        self.m_TargetSID = self.m_SID
        self.m_Game = oGame
        self.m_Owner = iOwner
        self.m_Container = None
        self.m_Key = 'Task%d-%d' % (self.m_SID, self.m_ID)
        self.m_CurStats = { }
        self.m_LimitStats = { }
        self.m_CurRecordStats = { }
        self.m_Enable = 0
        self.m_Status = TASK_STATUS_RUNNING
        self.m_Data = { }
        self.m_SaveData = { }
        self.m_Perform = { }
        self.m_SubTask = None
        self.m_ParentTaskID = 0
        self.OnInit()
        self.m_InitData = { }

    
    def OnInit(self):
        self.m_LifeCycle = cl_object.lifecycle.CLifeCycle()
        self.m_EventCB = cl_msgcenter.eventcbobj.CEventCB(self.m_CBFuncAction, self.m_Key)
        self.m_LifeCycle.Init(self, self.m_Action[0], self.m_Action[1])

    
    def Release(self):
        oOwner = self.GetOwner()
        for oPerform in self.m_Perform.values():
            oPerform.Disable(oOwner, iReleaseFlag = 1)
            oPerform.Release()
        
        self.m_Perform = { }
        self.Disable()
        if self.m_LifeCycle:
            self.m_LifeCycle.Release()
            self.m_LifeCycle = None
        self.m_EventCB = None
        self.m_Game = None
        self.m_Container = None
        self.m_Data = { }

    
    def Save(self):
        dData = {
            'ID': self.m_ID,
            'SID': self.m_SID,
            'CS': self.m_CurStats,
            'LS': self.m_LimitStats,
            'RS': self.m_CurRecordStats,
            'Status': self.m_Status,
            'SD': self.m_SaveData,
            'PF': list(self.m_Perform),
            'ST': self.m_SubTask.Save() if self.m_SubTask is not None else { } }
        return dData

    
    def Load(self, dData):
        if not dData:
            self.InitStats()
            self.InitPerform()
            return None
        self.m_CurStats = dData['CS']
        self.m_LimitStats = dData['LS']
        self.m_CurRecordStats = dData.get('RS', { })
        self.m_SaveData = dData.get('SD', { })
        self.m_Status = dData['Status']
        for iPerformSID in dData.get('PF', []):
            self.AddPerform(iPerformSID)
        
        if 'ST' in dData and dData['ST']:
            self.LoadSubTask(dData['ST'])

    
    def LoadSubTask(self, dData):
        oSubTask = None
        if dData:
            oSubTask = CTargetSubTask(dData['ID'], dData['SID'], self.m_Game, self.m_Owner, self.m_ID, self.m_SID)
            oSubTask.m_CurStats = dData['CS']
            oSubTask.m_LimitStats = dData['LS']
            oSubTask.m_CurRecordStats = dData.get('RS', { })
            oSubTask.m_SaveData = dData.get('SD', { })
            oSubTask.m_Status = dData['Status']
            oSubTask.m_Container = WeakProxy(self.m_Container)
            for iPerformSID in dData.get('PF', []):
                oSubTask.AddPerform(iPerformSID)
            
        self.m_SubTask = oSubTask
        self.m_Container.AddSubTask(self.m_ID, oSubTask.m_ID, '%s-%s' % (self.m_SID, oSubTask.m_SID))

    
    def SetSaveData(self, sKey, iAdd, iCover = 0):
        if sKey in self.m_SaveData and not iCover:
            return None
        self.m_SaveData[sKey] = iAdd

    
    def AddSaveData(self, sKey, iAdd):
        if sKey not in self.m_SaveData:
            return None
        self.m_SaveData[sKey] += iAdd

    
    def GetSaveData(self, sKey, default = 0):
        if sKey not in self.m_SaveData:
            return default
        return self.m_SaveData[sKey]

    
    def DelSaveData(self, sKey):
        if sKey in self.m_SaveData:
            self.m_SaveData.pop(sKey)

    
    def SetData(self, sKey, iValue):
        self.m_Data[sKey] = iValue

    
    def GetData(self, sKey, default = 0):
        if sKey not in self.m_Data:
            return default
        return self.m_Data[sKey]

    
    def DelData(self, sKey):
        if sKey in self.m_Data:
            self.m_Data.pop(sKey)

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def Key(self):
        return self.m_Key

    
    def AttrCache(self):
        return {
            'TaskID': self.m_ID,
            'TaskSID': self.m_SID,
            'AID': self.m_Owner }

    
    def Enable(self):
        if self.m_Enable or self.IsEnd():
            return None
        self.m_Enable = 1
        if self.m_SubTask:
            self.m_SubTask.Enable()
        self.m_LifeCycle.Enable(self.GetOwner())

    
    def Disable(self, iPause = 0):
        if not self.m_Enable:
            return None
        self.m_Enable = 0
        if self.m_SubTask and iPause:
            self.m_SubTask.Disable()
        self.m_LifeCycle.Disable(self.GetOwner())

    
    def InitPerform(self):
        if self.m_RewardPerformSID:
            self.AddPerform(self.m_RewardPerformSID)
        if self.m_PunishPerformSID:
            self.AddPerform(self.m_PunishPerformSID)

    
    def AddPerform(self, iPerformSID):
        oOwner = self.GetOwner()
        oPerform = oOwner.m_Game.m_ResMgr.NewPerform(iPerformSID, oOwner, 1)
        if not oPerform:
            return None
        oPerform.m_OwnerTask = self.m_ID
        self.m_Perform[iPerformSID] = oPerform
        oPerform.Enable(oOwner)
        return oPerform

    
    def RemovePerform(self, iPerformSID):
        if iPerformSID not in self.m_Perform:
            return None
        oPerform = self.m_Perform[iPerformSID]
        oPerform.Disable(self.GetOwner(), iNotify = 0)
        oPerform.Release()
        self.m_Perform.pop(iPerformSID)

    
    def EnablePerform(self, iPerformSID):
        if iPerformSID not in self.m_Perform:
            return None
        oPerform = self.m_Perform[iPerformSID]
        oPerform.Enable(self.GetOwner())

    
    def DisablePerform(self, iPerformSID):
        if iPerformSID not in self.m_Perform:
            return None
        oPerform = self.m_Perform[iPerformSID]
        oPerform.Disable(self.GetOwner(), iNotify = 0)

    
    def EnablePunish(self):
        if self.m_PunishPerformSID:
            self.EnablePerform(self.m_PunishPerformSID)

    
    def DisablePunish(self):
        if self.m_PunishPerformSID:
            self.DisablePerform(self.m_PunishPerformSID)

    
    def RemovePunish(self):
        if self.m_PunishPerformSID:
            self.RemovePerform(self.m_PunishPerformSID)

    
    def InitStats(self):
        for iStatIdx in self.m_TargetStats:
            self.m_CurStats[iStatIdx] = 0
        
        for iLimitIdx in self.m_LimitTarget:
            self.m_LimitStats[iLimitIdx] = 0
        
        for iRecordIdx in self.m_RecordStats:
            self.m_CurRecordStats[iRecordIdx] = 0
        

    
    def AddStat(self, iStatIdx, iAdd):
        if self.m_Status != TASK_STATUS_RUNNING:
            return None
        if iStatIdx in self.m_TargetStats:
            self.AddTargetStat(iStatIdx, iAdd)
        elif iStatIdx in self.m_LimitStats:
            self.AddLimitStat(iStatIdx, iAdd)
        else:
            self.AddRecordStat(iStatIdx, iAdd)

    
    def GetRecordStat(self, iStatIdx):
        if iStatIdx in self.m_RecordStats:
            return self.m_CurRecordStats[iStatIdx]
        return 0

    
    def GetTaskStatValue(self, iStatIdx):
        if iStatIdx in self.m_CurStats:
            return self.m_CurStats[iStatIdx]
        if iStatIdx in self.m_LimitStats:
            return self.m_LimitStats[iStatIdx]
        if iStatIdx in self.m_CurRecordStats:
            return self.m_CurRecordStats[iStatIdx]
        return 0

    
    def AddTargetStat(self, iStatIdx, iAdd):
        if iStatIdx not in self.m_CurStats:
            return None
        iOldStat = self.m_CurStats[iStatIdx]
        iCurStat = iOldStat + iAdd
        if iCurStat < 0:
            iCurStat = 0
        self.m_CurStats[iStatIdx] = iCurStat
        iTargetStat = self.GetTargetStat(iStatIdx)
        if self.m_CurStats[iStatIdx] >= iTargetStat:
            self.m_Container.OnTaskChangeStat(self.m_ID, iStatIdx, self.m_CurStats[iStatIdx])
            self.m_CurStats.pop(iStatIdx)
            if not self.m_CurStats:
                self.ChangeStatus(TASK_STATUS_SUCCESS)
            else:
                self.m_Container.OnTaskChangeStat(self.m_ID, iStatIdx, self.m_CurStats[iStatIdx])

    
    def GetTargetStat(self, iStatIdx):
        if self.m_StatsLimit[iStatIdx]:
            return self.m_TargetStats[iStatIdx] + 1
        return self.m_TargetStats[iStatIdx]

    
    def AddLimitStat(self, iLimitIdx, iAdd):
        iLimitTarget = self.GetLimitTarget(iLimitIdx)
        if self.m_LimitStats[iLimitIdx] >= iLimitTarget:
            return None
        self.m_LimitStats[iLimitIdx] += iAdd
        if self.m_LimitStats[iLimitIdx] < 0:
            self.m_LimitStats[iLimitIdx] = 0
        if self.m_LimitStats[iLimitIdx] >= iLimitTarget:
            self.m_LimitStats[iLimitIdx] = iLimitTarget
            self.m_Container.OnTaskChangeStat(self.m_ID, iLimitIdx, self.m_LimitStats[iLimitIdx])
            self.ChangeStatus(TASK_STATUS_FAIL)
        else:
            self.m_Container.OnTaskChangeStat(self.m_ID, iLimitIdx, self.m_LimitStats[iLimitIdx])

    
    def GetLimitTarget(self, iLimitIdx):
        if self.m_StatsLimit[iLimitIdx]:
            return self.m_LimitTarget[iLimitIdx] + 1
        return self.m_LimitTarget[iLimitIdx]

    
    def AddRecordStat(self, iRecordIdx, iAdd):
        self.m_CurRecordStats[iRecordIdx] += iAdd
        self.m_Container.OnTaskChangeStat(self.m_ID, iRecordIdx, self.m_CurRecordStats[iRecordIdx])

    
    def ChangeStatus(self, iStatus, iCheckEnd = 1, iNotify = 1):
        if (iStatus == self.m_Status or iCheckEnd) and self.IsEnd():
            return None
        oHero = self.GetOwner()
        TaskLog.Info('%d %d %d-%d changestatus %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, self.m_ID, self.m_SID, self.m_Status, iStatus))
        self.m_Status = iStatus
        dMsgInfo = {
            'TaskID': self.m_ID,
            'TaskSID': self.m_SID,
            'Status': self.m_Status }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TASK, oHero, dMsgInfo, iSub = TASK_CHANGESTATUS)
        if iNotify:
            self.m_Container.OnTaskChangeStatus(self.m_ID, self.m_ParentTaskID)
        if iStatus in (TASK_STATUS_SUCCESS, TASK_STATUS_FAIL):
            self.End()

    
    def OnlyChangeStatus(self, iStatus):
        oHero = self.GetOwner()
        TaskLog.Info('%d %d %d-%d changestatus %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, self.m_ID, self.m_SID, self.m_Status, iStatus))
        self.m_Status = iStatus
        self.m_Container.OnTaskChangeStatus(self.m_ID, self.m_ParentTaskID)

    
    def BuildStatusInfo(self):
        oTask = self
        if self.m_SubTask:
            oTask = self.m_SubTask
        return (oTask.m_ID, oTask.m_SID, oTask.m_TargetSID, oTask.m_Status)

    
    def BuildAllStatInfo(self):
        lstSubStatInfo = []
        oTask = self
        if self.m_SubTask:
            oTask = self.m_SubTask
        for iStatIdx in oTask.m_TargetStats:
            if iStatIdx in oTask.m_CurStats:
                iCurValue = oTask.m_CurStats[iStatIdx]
            else:
                iCurValue = oTask.m_TargetStats[iStatIdx]
            lstSubStatInfo.append((iStatIdx, iCurValue))
        
        for iLimitIdx, iCurValue in oTask.m_LimitStats.items():
            lstSubStatInfo.append((iLimitIdx, iCurValue))
        
        for iRecordIdx, iCurValue in oTask.m_CurRecordStats.items():
            lstSubStatInfo.append((iRecordIdx, iCurValue))
        
        lstStatInfo = (oTask.m_ID, tuple(lstSubStatInfo))
        return lstStatInfo

    
    def AllDisable(self):
        self.Disable()
        for oPerform in self.m_Perform.values():
            oPerform.Disable(self.GetOwner(), iNotify = 0)
        

    
    def AllPerformDisable(self):
        for oPerform in self.m_Perform.values():
            oPerform.Disable(self.GetOwner(), iNotify = 0)
        

    
    def AllPerformEnable(self):
        for oPerform in self.m_Perform.values():
            oPerform.Enable(self.GetOwner())
        

    
    def End(self):
        self.Disable()
        if self.m_Status == TASK_STATUS_SUCCESS:
            self.RemovePerform(self.m_PunishPerformSID)

    
    def IsEnd(self):
        return self.m_Status in (TASK_STATUS_SUCCESS, TASK_STATUS_FAIL)

    
    def BuildSubTask(self, iSubTaskSID):
        oHero = self.GetOwner()
        TaskLog.Info('%d %d %d-%d buildsubtask %d' % (self.m_Game.m_ID, oHero.m_PlayerID, self.m_ID, self.m_SID, iSubTaskSID))
        iID = self.m_Game.NewNoSceneObjID()
        oSubTask = CTargetSubTask(iID, iSubTaskSID, self.m_Game, self.m_Owner, self.m_ID, self.m_SID)
        oSubTask.m_Container = WeakProxy(self.m_Container)
        oSubTask.InitStats()
        self.m_SubTask = oSubTask
        self.m_Container.AddSubTask(self.m_ID, oSubTask.m_ID, '%s-%s' % (self.m_SID, oSubTask.m_SID))
        oSubTask.Enable()



class CTargetSubTask(CBaseTask):
    
    def __init__(self, iID, iSID, oGame, iOwner, iParentTaskID, iParentSID):
        super(CTargetSubTask, self).__init__(iID, oGame, iOwner)
        self.UpdateTaskInfo(iSID)
        self.m_TargetSID = iParentSID
        self.m_Key = 'Task%d-%d' % (self.m_SID, self.m_ID)
        self.m_ParentTaskID = iParentTaskID
        self.OnInit()

    
    def OnInit(self):
        self.m_LifeCycle = cl_object.lifecycle.CLifeCycle()
        self.m_EventCB = cl_msgcenter.eventcbobj.CEventCB(self.m_CBFuncAction, self.m_Key)
        self.m_LifeCycle.Init(self, self.m_Action[0], None)

    
    def UpdateTaskInfo(self, iTaskSID):
        clsTask = cl_platformdata.GetTaskClass(iTaskSID)
        self.m_SID = clsTask.m_SID
        self.m_Name = clsTask.m_Name
        self.m_Description = clsTask.m_Description
        self.m_Quality = clsTask.m_Quality
        self.m_RewardPerformSID = clsTask.m_RewardPerformSID
        self.m_PunishPerformSID = clsTask.m_PunishPerformSID
        self.m_TargetStats = clsTask.m_TargetStats
        self.m_LimitTarget = clsTask.m_LimitTarget
        self.m_RecordStats = clsTask.m_RecordStats
        self.m_Action = clsTask.m_Action
        self.m_ClearAction = clsTask.m_ClearAction
        self.m_CBFuncAction = clsTask.m_CBFuncAction
        self.m_OnlyPunishInFightLevel = clsTask.m_OnlyPunishInFightLevel
        self.m_ExcludeTask = clsTask.m_ExcludeTask
        self.m_HasPunish = clsTask.m_HasPunish
        self.m_BeforeChooseCond = clsTask.m_BeforeChooseCond
        self.m_StatsLimit = clsTask.m_StatsLimit

    
    def Save(self):
        dData = {
            'ID': self.m_ID,
            'SID': self.m_SID,
            'TargetSID': self.m_TargetSID,
            'CS': self.m_CurStats,
            'LS': self.m_LimitStats,
            'RS': self.m_CurRecordStats,
            'Status': self.m_Status,
            'SD': self.m_SaveData,
            'PF': list(self.m_Perform),
            'ST': { },
            'PT': self.m_ParentTaskID }
        return dData

    
    def Disable(self):
        if not self.m_Enable:
            return None
        self.m_Enable = 0
        self.m_LifeCycle.Disable(self.GetOwner())

    
    def Enable(self):
        if self.m_Enable or self.IsEnd():
            return None
        self.m_Enable = 1
        self.m_LifeCycle.Enable(self.GetOwner())

    
    def End(self):
        self.Disable()
        self.m_Container.RemoveSubTask(self.m_ID)
        oParentTask = self.m_Container.GetTaskByID(self.m_ParentTaskID)
        oParentTask.m_SubTask = None


