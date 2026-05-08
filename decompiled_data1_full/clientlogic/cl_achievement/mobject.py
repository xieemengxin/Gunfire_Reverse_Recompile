# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobject.pyc
# RelativePath: clientlogic/cl_achievement/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_only import PythonError, SendAlert
from cl_object.lifecycle import CLifeCycle
import cl_msgcenter
import cl_msgcenter.eventcbobj
import cl_notify
from . import NewAchieveStat
from cl_object.logging import AchievementLog

class CAchieveStat(object):
    m_SID = 0
    m_Name = '第一滴血'
    m_TargetValue = 0
    m_Action = (None, None)
    m_CBFuncAction = { }
    
    def __init__(self, oContainer, iCurValue):
        self.m_Container = oContainer
        self.m_Owner = oContainer.m_Owner
        self.m_Game = oContainer.m_Game
        self.m_Key = 'Achieve%d-%d' % (self.m_Owner, self.m_SID)
        self.m_CurValue = iCurValue
        self.m_EventCB = cl_msgcenter.eventcbobj.CEventCB(self.m_CBFuncAction, self.m_Key)
        self.m_LifeCycle = CLifeCycle()
        self.m_LifeCycle.Init(self, self.m_Action[0], self.m_Action[1])

    
    def Release(self):
        self.m_LifeCycle.Disable(self.GetOwner())
        self.m_LifeCycle.Release()
        self.m_Container = None
        self.m_Game = None

    
    def Enable(self):
        self.m_LifeCycle.Enable(self.GetOwner())

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def Key(self):
        return self.m_Key

    
    def AttrCache(self):
        dData = {
            'AID': self.m_Owner,
            'AchieveStatSID': self.m_SID }
        return dData



class CAchievementStatMgr(object):
    
    def __init__(self, oGame, iOwner, iPlayerID):
        self.m_Game = oGame
        self.m_Owner = iOwner
        self.m_PlayerID = iPlayerID
        self.m_Stats = { }
        self.m_InitStatValue = { }
        self.AddAttention()

    
    def Release(self):
        self.DoneAttention()
        for iSID in list(self.m_Stats.keys()):
            if iSID not in self.m_Stats:
                continue
            oStat = self.m_Stats[iSID]
            oStat.Release()
        
        self.m_Stats = { }
        self.m_Game = None

    
    def AddAttention(self):
        oHero = self.m_Game.GetObject(self.m_Owner)
        if oHero:
            cl_msgcenter.AddAttentionFunc(oHero, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, InitPlayer, 'InitAchievement')

    
    def DoneAttention(self):
        oHero = self.m_Game.GetObject(self.m_Owner)
        if oHero:
            cl_msgcenter.DoneAttention(oHero, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, 'InitAchievement')

    
    def InitAchievement(self):
        for iSID, iCurValue in list(self.m_InitStatValue.items()):
            if iSID not in self.m_Stats:
                oStat = NewAchieveStat(iSID, self, iCurValue)
                if not oStat:
                    SendAlert('err', f'''成就 {iSID} 配置不存在''')
                    self.m_InitStatValue.pop(iSID)
                    continue
                self.m_Stats[iSID] = oStat
        
        for oStat in self.m_Stats.values():
            oStat.Enable()
        

    
    def Save(self):
        if self.m_Game.m_WarMgr.CheckInitSingleGame():
            return { }
        dStatValue = self.PreCollectProgress()
        dData = {
            'ISV': dStatValue }
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_InitStatValue = dData.get('ISV', { })

    
    def LoadStats(self, dStats):
        self.m_InitStatValue.update(dStats)

    
    def AddStat(self, iSID, iAdd):
        if iSID not in self.m_Stats:
            return None
        oStat = self.m_Stats[iSID]
        oStat.m_CurValue += iAdd
        AchievementLog.Debug('%d %d addstat %d %d' % (self.m_Game.m_ID, self.m_PlayerID, iSID, iAdd))
        if oStat.m_CurValue >= oStat.m_TargetValue:
            self.DoneAchievement(iSID)

    
    def DoneAchievement(self, iSID):
        oStat = self.m_Stats.pop(iSID)
        oStat.Release()
        iInitValue = self.m_InitStatValue.pop(iSID)
        iCurValue = oStat.m_CurValue
        dAchievement = {
            iSID: iCurValue - iInitValue }
        self.m_Game.m_WarMgr.HandleAchievementReport(self.m_PlayerID, dAchievement)
        oHero = self.m_Game.GetObject(self.m_Owner)
        oHero.DelSavedData('achieve%d' % iSID)
        cl_notify.InternalTips(oHero, '成就%d-%s达成' % (iSID, oStat.m_Name))

    
    def LevelReport(self):
        dChanged = { }
        for iSID, oStat in self.m_Stats.items():
            iInitValue = self.m_InitStatValue[iSID]
            iCurValue = oStat.m_CurValue
            if iCurValue > iInitValue:
                dChanged[iSID] = iCurValue - iInitValue
                self.m_InitStatValue[iSID] = iCurValue
        
        return dChanged

    
    def PreCollectProgress(self):
        dProgress = dict(self.m_InitStatValue)
        for iSID, oStat in self.m_Stats.items():
            iInitValue = dProgress[iSID]
            iCurValue = oStat.m_CurValue
            if iCurValue > iInitValue:
                dProgress[iSID] = iCurValue
        
        return dProgress



def InitPlayer(oListener, _oWarMgr, _dInfo):
    oListener.m_Achievement.InitAchievement()

