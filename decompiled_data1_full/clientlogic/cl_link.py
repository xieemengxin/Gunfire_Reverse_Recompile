# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_link.pyc
# RelativePath: clientlogic/cl_link.pyc
# Source Generated with Decompyle++
# File: cl_link.pyc (Python 3.6)

from cl_cscommondef import LINK_ONLINE, LINK_QUIT, LINK_DISCONNECT
from cl_object.logging import SceneLog, FightserverLog
from cl_duonet.netfunc import UnpackInt
from cl_commondefines import LEAVE_TYPE_NORECORDE, LEAVE_TYPE_RECORDE
import weakref
import cl_msgcenter
import cl_scene
import cl_snetwar
import cllib.lib_flag as lib_flag
import cli_player

class CLinkManager(object):
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_OnlineLink = { }
        self.m_NewLoginPlayer = { }
        self.m_ReLoginPlayer = { }

    
    def OnLogin(self, pid, iReEnter):
        oGame = self.m_Game
        oHero = oGame.m_WarMgr.GetHeroByPlayer(pid)
        FightserverLog.Info('%s login %s %s %s' % (oGame.m_ID, pid, oHero.m_ID, iReEnter))
        who = cli_player.GetPlayer(pid, oGame.m_ID)
        if who:
            who.BindHero(weakref.proxy(oHero))
        else:
            FightserverLog.Alert('%s %s noplayer' % (oGame.m_ID, pid))
        self.m_NewLoginPlayer[pid] = 1
        dPlayerCtrl = { }
        if lib_flag.g_IsPCRunFight:
            lstPlayer = oGame.m_WarMgr.GetAllPlayer()
            dHero = oGame.m_WarMgr.GetAllPlayerHero()
            for iPlayer in lstPlayer:
                iAccount = oGame.m_WarMgr.GetPlayerAccount(iPlayer)
                dPlayerCtrl[iAccount] = dHero[iPlayer]
            
        else:
            dPlayerCtrl = oGame.m_WarMgr.GetAllPlayerHero()
        cl_snetwar.GS2CMainCtrl(oGame, oHero.m_ID, pid, dPlayerCtrl)
        if iReEnter:
            self.m_ReLoginPlayer[pid] = 1
            if oHero.m_Scene:
                cl_scene.GS2CMapSceneEnter(oHero, oHero.m_Scene, oHero.GetPos(), oHero.GetNetFacing())
                oScene = oGame.m_SceneMgr.GetScene(oHero.m_Scene)
                if oScene:
                    oScene.DelPlayer(pid, oHero.m_ID)
        cl_snetwar.GS2CPlayType(oGame, pid)
        self.AddOnlineLink(pid)
        oGame.m_WarKeep.OnLogin(pid)
        cl_snetwar.GS2CFightInfo(pid, oGame.m_WarMgr.m_WarMask)
        cl_snetwar.GS2CLastActionNum(pid, oHero.GetLastActionNum())
        SceneLog.Info('%s enterscene%d mode%d' % (pid, oHero.m_Scene, iReEnter))
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PLAYERLOGIN, oHero, {
            'pid': pid,
            'reenter': iReEnter })

    
    def OnReady(self, pid):
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        if not oHero:
            return None
        iNewLogin = self.m_NewLoginPlayer.pop(pid, 0)
        iReEnter = self.m_ReLoginPlayer.pop(pid, 0)
        oHero.OnPlayerReady(iNewLogin)
        self.m_Game.m_WarMgr.OnReady(pid)
        self.m_Game.m_Status.OnReady(pid)
        self.m_Game.m_WarKeep.OnReady(pid)
        cl_msgcenter.SendCoreMsg(cl_msgcenter.MSG_WAR_PLAYERONREADY, oHero, {
            'pid': pid,
            'reenter': iReEnter,
            'newlogin': iNewLogin })

    
    def OnQuit(self, pid):
        self.DelOnlineLink(pid)
        FightserverLog.Info('%s quit %s' % (self.m_Game.m_ID if self.m_Game else 0, pid))
        if self.m_Game:
            oGame = self.m_Game
            cl_snetwar.GS2CQuitGame(oGame, pid)
            oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
            if oHero:
                oHero.SetLinkStatus(LINK_QUIT)
            oGame.m_WarKeep.OnQuit(pid)

    
    def Disconnected(self, pid):
        self.DelOnlineLink(pid)
        FightserverLog.Info('%s linkdisconnect %s' % (self.m_Game.m_ID if self.m_Game else 0, pid))
        if self.m_Game:
            oGame = self.m_Game
            cl_snetwar.GS2CDisconnected(oGame, pid)
            oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
            if oHero:
                oHero.SetLinkStatus(LINK_DISCONNECT)
            oGame.m_WarKeep.OnDisconnect(pid)

    
    def AddOnlineLink(self, pid):
        self.m_OnlineLink[pid] = 1
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        if oHero:
            oHero.SetLinkStatus(LINK_ONLINE)

    
    def DelOnlineLink(self, pid):
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        if oHero:
            oScene = self.m_Game.m_SceneMgr.GetScene(oHero.m_Scene)
            if oScene:
                oScene.DelPlayer(pid, oHero.m_ID)
        if pid in self.m_OnlineLink:
            del self.m_OnlineLink[pid]

    
    def GetLink(self):
        return self.m_OnlineLink

    
    def Release(self):
        self.m_Game = None



def C2GSLeaveGame(oGame, oHero):
    iLeaveType = UnpackInt(1)
    FightserverLog.Info('%s leave %s %d' % (oGame.m_ID, oHero.m_PlayerID, iLeaveType))
    if not oGame.m_WarMgr.IsSingleGame() and iLeaveType == LEAVE_TYPE_RECORDE:
        iLeaveType = LEAVE_TYPE_NORECORDE
    oGame.m_WarMgr.OnDirectLeave(oHero.m_PlayerID, iLeaveType)

