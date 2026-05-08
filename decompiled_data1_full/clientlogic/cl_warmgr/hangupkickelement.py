# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/hangupkickelement.pyc
# RelativePath: clientlogic/cl_warmgr/hangupkickelement.pyc
# Source Generated with Decompyle++
# File: hangupkickelement.pyc (Python 3.6)

from cl_commondefines import GAMETYPE_JUMP, SETTLE_HANGUP
from cl_only import Functor, Time2Frame
from cl_warmgr.mobject import CBaseElement
from cl_object.logging import WarobjLog
import cl_msgcenter
import cl_notify
import cl_math

class CHangUpKickElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CHangUpKickElement, self).__init__(oGame, nid, oData)
        self.m_CallFlag = 'HangUpKickElement'
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_KickFrame = Time2Frame(self.m_Data.m_Config.get('TOTALTIME', 90000))
        self.m_CheckFrame = Time2Frame(self.m_Data.m_Config.get('CHECKTIME', 2000))
        self.m_HeroPos = { }
        self.m_StopFrame = { }
        self.m_Death = { }
        self.m_Level = { }

    
    def Init(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnRemovePlayer, 'OnRemovePlayer' + self.m_CallFlag, -1, 0, 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.AddPlayer, 'AddPlayer' + self.m_CallFlag, -1, 0, 0)

    
    def AddPlayer(self, oWarMgr, dInfo):
        iHero = dInfo['Hero']
        oHero = self.m_Game.GetObject(iHero)
        self.m_HeroPos[iHero] = oHero.GetPos()
        self.m_StopFrame[iHero] = 0
        self.AddAttention(iHero)
        oHero.Call_Out(Functor(self.AddStopFrame, oHero), self.m_CheckFrame, 'AddStopFrame' + self.m_CallFlag)

    
    def AddStopFrame(self, oHero):
        iValid = self.CheckValidLevel(oHero)
        if (not iValid or oHero.m_ID in self.m_Death) and self.m_Death[oHero.m_ID]:
            oHero.Remove_Call_Out('AddStopFrame' + self.m_CallFlag)
            oHero.Call_Out(Functor(self.AddStopFrame, oHero), self.m_CheckFrame, 'AddStopFrame' + self.m_CallFlag)
            return None
        iHero = oHero.m_ID
        vNow = oHero.GetPos()
        if cl_math.CalDistance(vNow, self.m_HeroPos[iHero]) < 1:
            self.m_StopFrame[iHero] += self.m_CheckFrame
        else:
            self.m_HeroPos[iHero] = oHero.GetPos()
            self.m_StopFrame[iHero] = 0
        if self.m_StopFrame[iHero] >= self.m_KickFrame:
            WarobjLog.Info('HangUpKick %d:%s' % (oHero.m_PlayerID, oHero.m_OwnerName))
            self.HangUpKick(oHero)
        else:
            oHero.Remove_Call_Out('AddStopFrame' + self.m_CallFlag)
            oHero.Call_Out(Functor(self.AddStopFrame, oHero), self.m_CheckFrame, 'AddStopFrame' + self.m_CallFlag)

    
    def AddAttention(self, iHero):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ENTERSCENE, self.EnterScene, 'EnterScene' + self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DIEDIST, self.RealDied, 'RealDied' + self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_RELIFE, self.Relife, 'Relife' + self.m_CallFlag)

    
    def DoneAttention(self, lstHero):
        oWarMgr = self.m_WarMgr
        for iHero in lstHero:
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ENTERSCENE, 'EnterScene' + self.m_CallFlag)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DIEDIST, 'RealDied' + self.m_CallFlag)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_RELIFE, 'Relife' + self.m_CallFlag)
        

    
    def HangUpKick(self, oHero):
        pid = oHero.m_PlayerID
        oWarMgr = self.m_WarMgr
        oWarMgr.HandlePlayerLevelReport(pid, SETTLE_HANGUP)
        oWarMgr.HandlePlayerSettle(pid, SETTLE_HANGUP)
        oWarMgr.RemovePlayer(pid, 1)
        cl_notify.SendCommonNotify(self.m_Game, self.m_Game.GetRealPlayers(), 7257, {
            '$$playername': oHero.m_OwnerName })
        oWarMgr.CheckWarEnd()

    
    def EnterScene(self, oWarMgr, oHero, dInfo):
        self.m_HeroPos[oHero.m_ID] = oHero.GetPos()

    
    def RealDied(self, oWarMgr, oHero, dInfo):
        self.m_Death[oHero.m_ID] = 1

    
    def Relife(self, oWarMgr, oHero, dInfo):
        self.m_Death[oHero.m_ID] = 0

    
    def Release(self):
        oWarMgr = self.m_WarMgr
        lstHero = oWarMgr.GetRoomHero()
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, 'OnRemovePlayer' + self.m_CallFlag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, 'AddPlayer' + self.m_CallFlag)
        self.DoneAttention(lstHero)
        self.m_WarMgr = None
        self.m_HeroPos = { }
        self.m_StopFrame = { }
        self.m_Death = { }
        self.m_Level = { }
        super(CHangUpKickElement, self).Release()

    
    def OnRemovePlayer(self, oWarMgr, dInfo):
        iHero = dInfo['Hero']
        oHero = self.m_Game.GetObject(iHero)
        oHero.Remove_Call_Out('AddStopFrame' + self.m_CallFlag)
        self.m_HeroPos.pop(iHero, 0)
        self.m_StopFrame.pop(iHero, 0)
        self.m_Death.pop(iHero, 0)
        self.DoneAttention([
            iHero])

    
    def CheckValidLevel(self, oHero):
        oGame = self.m_Game
        iFrame = oGame.GetFrameNum()
        if iFrame not in self.m_Level:
            dLevel = { }
            oWarMgr = self.m_WarMgr
            lstHero = oWarMgr.GetRoomHero()
            for iHero in lstHero:
                oHeroTemp = oGame.GetObject(iHero)
                oScene = oGame.m_SceneMgr.GetScene(oHeroTemp.m_Scene)
                if oScene:
                    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
                    oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
                    if oLevelNode and oLevelNode.m_GameType == GAMETYPE_JUMP:
                        dLevel[iHero] = 1
            
            self.m_Level = { }
            self.m_Level[iFrame] = dLevel
        dLevelInfo = self.m_Level[iFrame]
        if dLevelInfo and oHero.m_ID not in dLevelInfo:
            return 0
        return 1



def GetComponentClass(oMgrManager):
    return CHangUpKickElement

