# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_task.pyc
# RelativePath: clientlogic/cl_minigame/mg_task.pyc
# Source Generated with Decompyle++
# File: mg_task.pyc (Python 3.6)

from cl_only import DeepCopy, ChooseKey
from cl_commondefines import MG_TASK, TASK_TYPE_HIDE
from cl_object.logging import TaskLog
import cl_platformdata
from .mobject import CRewardChooseGame, CBaseGameData

class CChooseTaskGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_TASK
    m_ChooseNum = 3
    m_ChooseWeight = { }
    m_QualityWeight = { }
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseNum = cls.m_ChooseNum
        oMiniGame.m_ChooseWeight = DeepCopy(cls.m_ChooseWeight)
        oMiniGame.m_QualityWeight = DeepCopy(cls.m_QualityWeight)
        oMiniGame.m_RewardReason = 'ChooseTaskGame'

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CChooseTaskGame

    GetGameClass = classmethod(GetGameClass)


class CChooseTaskGame(CRewardChooseGame):
    m_ChooseNum = 3
    m_QualityWeight = { }
    
    def GetRewardInfo(self):
        oGame = self.m_Game
        oHero = oGame.GetObject(self.m_Player)
        if not oHero:
            return { }
        dReward = { }
        lstQuality = []
        lstExclude = []
        iChooseNum = self.m_ChooseNum
        iExecChooseBeforeCond = 1
        if 'LimitTaskInfo' in self.m_Data:
            dLimitTaskInfo = self.m_Data['LimitTaskInfo']
            if self.m_Player in dLimitTaskInfo:
                dLimitHero = dLimitTaskInfo[self.m_Player]
                lstQuality = dLimitHero['Quality'] if 'Quality' in dLimitHero else []
                iChooseNum = dLimitHero['ChooseNum'] if 'ChooseNum' in dLimitHero else self.m_ChooseNum
                lstExclude = dLimitHero['ExcludeTasks'] if 'ExcludeTasks' in dLimitHero else []
                iExecChooseBeforeCond = dLimitHero['ExecChooseBeforeCond'] if 'ExecChooseBeforeCond' in dLimitHero else 1
        dChooseWeight = oHero.m_TaskCon.BuildChooseTask(self.m_ChooseWeight, iExecChooseBeforeCond)
        lstAllTask = cl_platformdata.GetAllTask()
        dQualityWeight = self.m_QualityWeight
        oTaskNpc = self.m_Game.GetObject(self.m_Owner)
        lstNpcExcludeTask = oTaskNpc.GetNpcExcludeTask(self.m_Player) if oTaskNpc else []
        if dQualityWeight:
            dTempChooseWeight = { }
            for iSID in dChooseWeight:
                if iSID in lstExclude:
                    continue
                if iSID in lstNpcExcludeTask:
                    continue
                dTempChooseWeight[iSID] = dChooseWeight[iSID]
            
            dChooseWeight = dTempChooseWeight
            if lstQuality:
                dTempQualityWeight = { }
                for iQuality in dQualityWeight:
                    if iQuality in lstQuality:
                        dTempQualityWeight[iQuality] = dQualityWeight[iQuality]
                
                dQualityWeight = dTempQualityWeight
            dQualityNum = { }
            if oHero.QuerySavedData('IsChooseMyth'):
                dQualityWeight.pop(TASK_TYPE_HIDE, { })
            for _ in range(iChooseNum):
                iQuality = ChooseKey(oGame, dQualityWeight)
                if iQuality == TASK_TYPE_HIDE:
                    oHero.SetSavedData('IsChooseMyth', 1)
                    dQualityWeight.pop(TASK_TYPE_HIDE, { })
                if iQuality in dQualityNum:
                    dQualityNum[iQuality] += 1
                    continue
                dQualityNum[iQuality] = 1
            
            iIndex = 0
            for iQuality, iNum in dQualityNum.items():
                dChooseTask = { dChooseWeight[k]: k for k in lstAllTask[iQuality] if k in dChooseWeight }
                for _ in range(iNum):
                    iTaskSID = ChooseKey(oGame, dChooseTask)
                    clsTask = cl_platformdata.GetTaskClass(iTaskSID)
                    if not clsTask:
                        TaskLog.Alert('%d %d taskmg%d choose%s task%s err' % (oGame.m_ID, oHero.m_PlayerID, self.m_SID, dChooseTask, iTaskSID))
                        break
                    dReward[iIndex] = iTaskSID
                    iIndex += 1
                    dChooseTask.pop(iTaskSID)
                    for iExcludeTask in clsTask.m_NpcExcludeTask:
                        dChooseTask.pop(iExcludeTask, 0)
                        dChooseWeight.pop(iExcludeTask, 0)
                    
                
            
        elif lstQuality or lstExclude:
            dLimitChooseWeight = { }
            lstTask = []
            for iQuality in lstQuality:
                if iQuality in lstAllTask:
                    lstTask.extend(lstAllTask[iQuality])
            
            for iTaskSID in dChooseWeight:
                if iTaskSID in lstExclude:
                    continue
                if iTaskSID not in lstTask:
                    continue
                if iTaskSID in lstNpcExcludeTask:
                    continue
                dLimitChooseWeight[iTaskSID] = dChooseWeight[iTaskSID]
            
            dChooseWeight = dLimitChooseWeight
        for iIndex in range(iChooseNum):
            iTaskSID = ChooseKey(oGame, dChooseWeight)
            clsTask = cl_platformdata.GetTaskClass(iTaskSID)
            if not clsTask:
                TaskLog.Alert('%d %d taskmg%d choose%s task%s err' % (oGame.m_ID, oHero.m_PlayerID, self.m_SID, dChooseWeight, iTaskSID))
                break
            dReward[iIndex] = iTaskSID
            dChooseWeight.pop(iTaskSID)
            for iExcludeTask in clsTask.m_NpcExcludeTask:
                dChooseWeight.pop(iExcludeTask, 0)
            
        
        return dReward

    
    def SendChoose(self):
        iHero = self.m_Player
        dReward = self.Query('Reward')
        oTaskNpc = self.m_Game.GetObject(self.m_Owner)
        self.Set('Reward', { })
        self.End()
        if not oTaskNpc:
            return None
        oTaskNpc.SetTaskInfo(iHero, dReward)


