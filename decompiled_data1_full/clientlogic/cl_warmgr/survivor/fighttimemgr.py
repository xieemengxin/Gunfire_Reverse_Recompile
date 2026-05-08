# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/survivor/fighttimemgr.pyc
# RelativePath: clientlogic/cl_warmgr/survivor/fighttimemgr.pyc
# Source Generated with Decompyle++
# File: fighttimemgr.pyc (Python 3.6)

import cl_msgcenter
import cl_snetwar
from cl_object.logging import SurvivorLog
FIGHTTIME_DEFAULT = -1
FIGHTTIME_STOP = 0
FIGHTTIME_START = 1

class CFightTimeMgr(object):
    
    def __init__(self, oSurvivorElement):
        self.m_CallFlag = 'FightTime'
        self.m_Survivor = oSurvivorElement
        self.m_Game = oSurvivorElement.m_Game
        self.m_Status = FIGHTTIME_DEFAULT
        self.m_InitFrame = 0
        self.m_StartFrame = 0
        self.m_PauseFrame = 0
        self.m_PauseStartFrame = -1
        self.m_PauseReason = []

    
    def Init(self):
        self.m_Game.AddGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOk, self.m_CallFlag)

    
    def Release(self):
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_CallFlag)
        self.m_Survivor = None
        self.m_Game = None

    
    def Save(self):
        dData = { }
        dData['Frame'] = self.GetPlayFrame()
        dData['PauseReason'] = self.m_PauseReason
        dData['Statu'] = self.m_Status
        return dData

    
    def Load(self, dData):
        self.m_InitFrame = dData['Frame']
        self.m_PauseReason = dData['PauseReason']
        self.m_Status = dData['Statu']
        if self.m_Status == FIGHTTIME_STOP:
            self.m_PauseStartFrame = self.m_Game.GetFrameNum()

    
    def GetPlayFrame(self):
        if self.m_Status == FIGHTTIME_DEFAULT:
            return self.m_InitFrame
        iCurFrame = self.m_Game.GetFrameNum()
        iFrame = iCurFrame - self.m_StartFrame
        iFrame -= self.m_PauseFrame
        if self.m_Status == FIGHTTIME_STOP and self.m_PauseStartFrame != -1:
            iFrame -= iCurFrame - self.m_PauseStartFrame
        return self.m_InitFrame + iFrame

    
    def NotifyPlayFrame(self, lstPlayer = None):
        if lstPlayer is None:
            lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer()
        iFrame = self.GetPlayFrame()
        for pid in lstPlayer:
            cl_snetwar.GS2CPlayTime(self.m_Game, pid, iFrame, self.m_Status)
        

    
    def OnPlayerMapLoadOk(self, oWarMgr, oTarget, dInfo):
        if self.m_Status == FIGHTTIME_DEFAULT:
            return None
        self.NotifyPlayFrame([
            oTarget.m_PlayerID])

    
    def StartSummary(self):
        self.m_StartFrame = self.m_Game.GetFrameNum()
        self.m_PauseFrame = 0
        self.m_PauseStartFrame = -1
        self.m_Status = FIGHTTIME_START
        self.m_PauseReason = []
        self.NotifyPlayFrame()

    
    def PauseCounting(self, sReason):
        if sReason not in self.m_PauseReason:
            self.m_PauseReason.append(sReason)
        SurvivorLog.Debug('game:%d pausecounting:%s %s' % (self.m_Game.m_ID, self.m_PauseReason, self.m_Status))
        if self.m_Status == FIGHTTIME_STOP:
            return None
        self.m_Status = FIGHTTIME_STOP
        self.m_PauseStartFrame = self.m_Game.GetFrameNum()
        self.NotifyPlayFrame()

    
    def ResumeCounting(self, sReason):
        if sReason in self.m_PauseReason:
            self.m_PauseReason.remove(sReason)
        SurvivorLog.Debug('game:%d resumecounting:%s %s' % (self.m_Game.m_ID, self.m_PauseReason, self.m_Status))
        if self.m_PauseReason:
            return None
        if self.m_Status == FIGHTTIME_START:
            return None
        self.m_Status = FIGHTTIME_START
        if self.m_PauseStartFrame != -1:
            self.m_PauseFrame += self.m_Game.GetFrameNum() - self.m_PauseStartFrame
            self.m_PauseStartFrame = -1
        self.NotifyPlayFrame()

    
    def ResetStartFightTime(self, iStartFrame, iStatus):
        self.m_Status = iStatus
        self.m_StartFrame = iStartFrame
        self.m_PauseFrame = 0



def NewFightTimeManager(oSurvivorElement):
    oFightTimeMgr = CFightTimeMgr(oSurvivorElement)
    oFightTimeMgr.Init()
    return oFightTimeMgr

