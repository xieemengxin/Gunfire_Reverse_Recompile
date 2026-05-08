# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/gamespace.pyc
# RelativePath: clientlogic/cl_betree/gamespace.pyc
# Source Generated with Decompyle++
# File: gamespace.pyc (Python 3.6)

from cl_only import ChooseKey
from cl_object.logging import BehaviorLog, ErrLog
import cl_world
import cl_behavior
import cl_betree.fsm
import time

def NewGameSpace(oGame):
    return CGameSpace(oGame)


class CGameSpace(cl_behavior.GetGameSpaceClass()):
    m_HeartBeatInterval = 15
    m_MaxContextNum = 15
    m_UpdateInterval = m_HeartBeatInterval // m_MaxContextNum
    
    def __init__(self, oGame):
        super(CGameSpace, self).__init__()
        self.m_Game = oGame
        iTimerID = oGame.NewNPCID()
        self.m_CallTime = cl_world.CObject(oGame, iTimerID)
        oGame.CreateObject(iTimerID, self.m_CallTime)
        self.m_CurContext = 0
        self.m_Open = 0
        for _ in range(self.m_MaxContextNum):
            oContext = self.NewContext()
            self.m_Context[oContext.m_ContextID] = oContext
        
        self.m_TempKey = '%s-%s' % (oGame.m_ID, iTimerID)
        BehaviorLog.Info('init %s' % self.m_TempKey)

    
    def Clear(self):
        BehaviorLog.Info('clear %s' % self.m_TempKey)
        super(CGameSpace, self).Clear()
        self.m_Game = None
        self.m_CallTime.RemoveFromList()
        self.m_CallTime = None

    
    def Call_Out(self, func, delay, sFlag):
        self.m_CallTime.Call_Out(func, delay, sFlag)

    
    def Remove_Call_Out(self, sFlag):
        self.m_CallTime.Remove_Call_Out(sFlag)

    
    def ChooseContext(self):
        iMinAgentCnt = 255
        dSame = { }
        for iContext, oContext in self.m_Context.items():
            iAgent = len(oContext.m_Agents)
            if iAgent > iMinAgentCnt:
                continue
            if iAgent < iMinAgentCnt:
                iMinAgentCnt = iAgent
                dSame = { }
            dSame[iContext] = 1
        
        iMinContext = ChooseKey(self.m_Game, dSame)
        if not iMinContext:
            ErrLog.Raise('%s gamespace full' % self.m_Game.m_ID)
        return iMinContext

    
    def BetreeHeartBeat(self, iFrame):
        if not self.m_Open:
            return None
        if not self.m_Game:
            BehaviorLog.Alert('nogame %s' % self.m_TempKey)
            self.m_Open = 0
            return None
        self.SetFrameSinceStartup(iFrame)
        if not iFrame % self.m_UpdateInterval:
            iNextContext = self.m_CurContext % self.m_MaxContextNum + 1
            self.m_CurContext = iNextContext
            oContext = self.m_Context[iNextContext]
            if not oContext.m_Agents:
                return None
            oContext.ExecAgents(self)

    
    def OnEvent(self, oAgent, iMsg, dParams):
        self.SetFrameSinceStartup(self.m_Game.GetFrameNum())
        super(CGameSpace, self).OnEvent(oAgent, iMsg, dParams)

    
    def GetFrameSinceStartup(self):
        return self.m_Game.GetFrameNum()

    
    def AddAgentToNextContext(self, oAgent):
        iNextContext = (self.m_CurContext + 1) % self.m_MaxContextNum + 1
        oContext = self.GetContext(oAgent.m_ContextID)
        oContext.RemoveAgent(oAgent)
        oNextContext = self.GetContext(iNextContext)
        oNextContext.AddAgent(oAgent)

    
    def CallDelayUpdate(self, oAgent, iFrame):
        iNextContext = (self.m_CurContext + iFrame - 1) % self.m_MaxContextNum + 1
        if iNextContext == oAgent.m_ContextID:
            return None
        oContext = self.GetContext(oAgent.m_ContextID)
        oContext.RemoveAgent(oAgent)
        oNextContext = self.m_Context[iNextContext]
        oNextContext.AddAgent(oAgent)

    
    def CreateFsmTask(self, sRelativePath):
        return cl_betree.fsm.CreateFsmTask(sRelativePath)

    
    def CreateFsm(self, sRelativePath):
        return cl_betree.fsm.CFsm(sRelativePath)

    
    def ReleaseDebug(self):
        if self.m_Debug:
            self.m_Debug.Release()
            self.m_Debug = None


