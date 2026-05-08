# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_newunlockprogress/mobject.pyc
# RelativePath: clientlogic/cl_newunlockprogress/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from . import GetWarUnlockProgressCls
from cl_object.logging import WarunlockprogressLog
import cl_notify
import cl_msgcenter
import cl_msgcenter.eventcbobj
import cl_object.lifecycle

class CUnlockProgress(object):
    m_SID = 0
    m_TargetValue = 0
    m_RewardType = 0
    m_Action = (None, None)
    m_CBFuncAction = { }
    
    def __init__(self, oContainer, iCurValue):
        self.m_Owner = oContainer.m_Owner
        self.m_Game = oContainer.m_Game
        self.m_Key = 'UnlockProgress%d-%d' % (self.m_Owner, self.m_SID)
        self.m_CurValue = iCurValue
        self.m_EventCB = cl_msgcenter.eventcbobj.CEventCB(self.m_CBFuncAction, self.m_Key)
        self.m_LifeCycle = cl_object.lifecycle.CLifeCycle()
        self.m_LifeCycle.Init(self, self.m_Action[0], self.m_Action[1])

    
    def Release(self):
        self.m_LifeCycle.Disable(self.GetOwner())
        self.m_LifeCycle.Release()
        self.m_Game = None

    
    def Enable(self):
        self.m_LifeCycle.Enable(self.GetOwner())

    
    def Disable(self):
        self.m_LifeCycle.Disable(self.GetOwner())

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def Key(self):
        return self.m_Key

    
    def AttrCache(self):
        dData = {
            'AID': self.m_Owner,
            'UnlockProgressSID': self.m_SID }
        return dData



class CUnlockProgressMgr(object):
    
    def __init__(self, oGame, iOwner, iPlayerID):
        self.m_Game = oGame
        self.m_Owner = iOwner
        self.m_PlayerID = iPlayerID
        self.m_Progress = { }
        self.m_Done = { }
        self.m_InitProgressValue = { }
        self.AddAttention()

    
    def AddAttention(self):
        oHero = self.m_Game.GetObject(self.m_Owner)
        if oHero:
            cl_msgcenter.AddAttentionFunc(oHero, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, InitPlayer, 'InitUnlockProgress')

    
    def DoneAttention(self):
        oHero = self.m_Game.GetObject(self.m_Owner)
        if oHero:
            cl_msgcenter.DoneAttention(oHero, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, 'InitUnlockProgress')

    
    def Release(self):
        self.DoneAttention()
        for oProgress in self.m_Progress.values():
            oProgress.Release()
        
        self.m_Progress = { }
        self.m_Game = None

    
    def Save(self):
        if self.m_Game.m_WarMgr.CheckInitSingleGame():
            return { }
        dInitProgressValue = self.PreCollectProgress()
        dData = {
            'IPV': dInitProgressValue }
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_InitProgressValue = dData.get('IPV', { })

    
    def InitUnlockProgresss(self):
        for iSID, iCurValue in list(self.m_InitProgressValue.items()):
            if iSID not in self.m_Progress:
                clsProgress = GetWarUnlockProgressCls(iSID)
                if not clsProgress:
                    WarunlockprogressLog.Alert('%d %d warunlockprogress%d fail' % (self.m_Game.m_ID, self.m_PlayerID, iSID))
                    self.m_InitProgressValue.pop(iSID)
                    continue
                self.m_Progress[iSID] = clsProgress(self, iCurValue)
        
        for oProgress in self.m_Progress.values():
            oProgress.Enable()
        

    
    def LoadProgress(self, dProgress):
        self.m_InitProgressValue.update(dProgress)

    
    def UpdateProgress(self, iSID, iAdd):
        if iSID not in self.m_Progress or iSID in self.m_Done:
            return None
        oProgress = self.m_Progress[iSID]
        iNew = oProgress.m_CurValue + iAdd
        oProgress.m_CurValue = iNew
        if oProgress.m_CurValue >= oProgress.m_TargetValue:
            self.DoneUnlockProgress(iSID)

    
    def DoneUnlockProgress(self, iSID):
        oProgress = self.m_Progress.pop(iSID)
        self.m_Done[iSID] = oProgress.m_TargetValue
        oProgress.Release()
        oHero = self.m_Game.GetObject(self.m_Owner)
        oHero.DelSavedData('unlockprogress%d' % iSID)
        cl_notify.InternalTips(oHero, '新解锁项%d达成' % iSID)

    
    def LevelReport(self):
        dChanged = { }
        for iSID, oProgress in self.m_Progress.items():
            iInitValue = self.m_InitProgressValue[iSID]
            iCurValue = oProgress.m_CurValue
            if iCurValue > iInitValue:
                dChanged[iSID] = iCurValue - iInitValue
                self.m_InitProgressValue[iSID] = iCurValue
        
        for iSID, iValue in self.m_Done.items():
            iInitValue = self.m_InitProgressValue[iSID]
            if iValue > iInitValue:
                dChanged[iSID] = iValue - iInitValue
                self.m_InitProgressValue[iSID] = iValue
        
        return dChanged

    
    def PreCollectProgress(self):
        dProgress = dict(self.m_InitProgressValue)
        for iSID, oProgress in self.m_Progress.items():
            iInitValue = dProgress[iSID]
            iCurValue = oProgress.m_CurValue
            if iCurValue > iInitValue:
                dProgress[iSID] = iCurValue
        
        for iSID, iValue in self.m_Done.items():
            iInitValue = dProgress[iSID]
            if iValue > iInitValue:
                dProgress[iSID] = iValue
        
        return dProgress

    
    def GetWarUnlockProgress(self):
        return list(self.m_Done)



def InitPlayer(oListener, _oWarMgr, _dInfo):
    oListener.m_NewUnlockProgressMgr.InitUnlockProgresss()

