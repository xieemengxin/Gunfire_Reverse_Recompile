# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_gamekeep.pyc
# RelativePath: clientlogic/cl_gamekeep.pyc
# Source Generated with Decompyle++
# File: cl_gamekeep.pyc (Python 3.6)

from cl_only import Functor, Time2Frame
from cli_player import GetPlayer
from cl_object.logging import OtherLog, FightserverLog
import time
import cl_snetwar
import cllib.lib_server as lib_server
import cllib.lib_flag as lib_flag

class CGameWarKeep(object):
    m_CheckWarKeepTime = 200
    m_PauseDelayTime = 600
    if lib_flag.g_IsMobile:
        m_ReleaseDelayTime = 30000
    else:
        m_ReleaseDelayTime = 60000
    if lib_flag.g_IsStandalone:
        m_KickDelayTime = 3600000
    else:
        m_KickDelayTime = 6000
    m_DeadReleaseDelayTime = 12000
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_WarKeepInfo = { }
        self.m_PauseStat = 0
        self.m_SupportPause = 0
        self.m_ReleaseReason = ''

    
    def Release(self):
        self.m_WarKeepInfo.clear()
        self.m_Game.m_Timer.Logic_Remove_Call_Out('CheckWarKeep')
        self.m_Game.m_Timer.Logic_Remove_Call_Out('CommonGamePause')
        self.m_Game = None

    
    def InitKeep(self):
        self.m_SupportPause = self.IsSupportPause()
        self.m_WarKeepInfo = { }
        self.m_Game.m_Timer.Logic_Call_Out(self.CheckWarKeep, self.m_CheckWarKeepTime, 'CheckWarKeep')
        if lib_flag.g_IsStandaloneClient and self.m_Game.m_WarMgr.IsSingleGame(bExcludeAIMember = True):
            self.m_PauseDelayTime = 3600000

    
    def CheckWarKeep(self):
        self.m_Game.m_Timer.Logic_Call_Out(self.CheckWarKeep, self.m_CheckWarKeepTime, 'CheckWarKeep')
        iNowTime = int(time.time() * 100)
        pauseList = []
        kickList = []
        for pid, iTime in self.m_WarKeepInfo.items():
            iDeltaTime = iNowTime - iTime
            if iDeltaTime > self.m_KickDelayTime:
                kickList.append(pid)
                continue
            if iDeltaTime > self.m_PauseDelayTime:
                pauseList.append(pid)
        
        if self.m_SupportPause:
            for pid in pauseList:
                self.PauseCtrl(pid, 1, 0, sReason = 'checkwarkeep')
            
        for pid in kickList:
            who = GetPlayer(pid)
            if who:
                who.KickOut(self.m_Game.m_ID, 0, 0)
            if pid in self.m_WarKeepInfo:
                self.m_WarKeepInfo.pop(pid)
        

    
    def WarKeepHeartBeat(self, oHero):
        iNowTime = int(time.time() * 100)
        self.m_WarKeepInfo[oHero.m_PlayerID] = iNowTime

    
    def IsSupportPause(self):
        if self.m_Game.m_WarMgr.IsSingleGame(bExcludeAIMember = True):
            return True
        return False

    
    def IsPaused(self):
        return self.m_PauseStat

    
    def CallOutCommonGamePause(self, iPauseTime, iDelayTime):
        oGame = self.m_Game
        oGame.m_Timer.Remove_Call_Out('CommonPause')
        if iDelayTime <= 0:
            self.CommonGamePause(iPauseTime)
        else:
            oGame.m_Timer.Call_Out(Functor(self.CommonGamePause, iPauseTime), Time2Frame(iDelayTime), 'CommonPause')

    
    def CommonGamePause(self, iPauseTime):
        oGame = self.m_Game
        oGame.m_Timer.Logic_Call_Out(Functor(self.MultiSyncEndPauseCB), iPauseTime, 'CommonGamePause')
        oGame.m_Status.StopStep(Functor(self.MultiSyncPauseStat, 1))

    
    def MultiSyncEndPauseCB(self):
        oGameStat = self.m_Game.m_Status
        oGameStat.StartStep()
        self.MultiSyncPauseStat(0)

    
    def MultiSyncPauseStat(self, iPause):
        self.m_PauseStat = iPause
        for pid in self.m_Game.m_WarMgr.GetRoomPlayer():
            self.SyncPauseStatus(pid)
        

    
    def PauseCtrl(self, pid, iPause, iSync = 1, sReason = ''):
        if not self.m_SupportPause:
            return False
        if not self.m_Game.m_WarMgr.IsInRoom(pid):
            return False
        oGameStat = self.m_Game.m_Status
        if iPause:
            if self.m_PauseStat or not oGameStat.IsSteping():
                if iSync:
                    self.SyncPauseStatus(pid)
                return False
            OtherLog.Debug('%s %s stopstep %s %s' % (self.m_Game.m_ID, pid, self.m_Game.GetFrameNum(), sReason))
            oGameStat.StopStep(Functor(self.AfterPauseCtrl, pid, iPause))
        elif not (self.m_PauseStat) or not oGameStat.IsStoped():
            if iSync:
                self.SyncPauseStatus(pid)
            return False
        OtherLog.Debug('%s %s startstep %s %s' % (self.m_Game.m_ID, pid, self.m_Game.GetFrameNum(), sReason))
        oGameStat.StartStep()
        self.AfterPauseCtrl(pid, iPause)
        return True

    
    def AfterPauseCtrl(self, pid, iPause):
        self.m_PauseStat = iPause
        self.SyncPauseStatus(pid)

    
    def SyncPauseStatus(self, pid):
        OtherLog.Debug('%s %s pausestatus %s %s %s' % (self.m_Game.m_ID, pid, self.m_Game.GetFrameNum(), self.m_PauseStat, self.m_Game.m_Status.m_Status))
        cl_snetwar.GS2CCWarPauseStat(self.m_Game, pid, self.m_PauseStat)

    
    def OnLogin(self, pid):
        self.m_Game.m_Timer.Logic_Remove_Call_Out('GameOverTime')
        self.m_WarKeepInfo[pid] = int(time.time() * 100)

    
    def OnReady(self, pid):
        if self.m_SupportPause:
            self.SyncPauseStatus(pid)

    
    def OnQuit(self, pid):
        if pid in self.m_WarKeepInfo:
            self.m_WarKeepInfo.pop(pid)
        if self.m_Game.m_WarMgr.GetRoomPlayer():
            if not self.m_Game.m_LinkMgr.GetLink():
                self.m_Game.m_Timer.Logic_Call_Out(self.GameEnd, self.m_ReleaseDelayTime, 'GameOverTime')
            return None
        sReason = self.m_ReleaseReason if self.m_ReleaseReason else 'AllQuit'
        if self.m_Game.m_WarMgr.IsDelayRemove():
            self.m_Game.m_Timer.Logic_Call_Out(Functor(lib_server.CtrlWarRelease, self.m_Game.m_ID, sReason), self.m_ReleaseDelayTime, 'DelayRelease')
            return None
        lib_server.CtrlWarRelease(self.m_Game.m_ID, sReason)

    
    def OnDisconnect(self, pid):
        if pid in self.m_WarKeepInfo and not (lib_flag.g_IsStandaloneClient):
            self.m_WarKeepInfo.pop(pid)
        iGameEndDelay = 0
        lstOnline = self.m_Game.m_LinkMgr.GetLink()
        if lstOnline:
            for iPlayer in lstOnline:
                oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(iPlayer)
                if oHero and not oHero.IsRealDied():
                    break
            else:
                iGameEndDelay = self.m_DeadReleaseDelayTime
        else:
            iGameEndDelay = self.m_ReleaseDelayTime
        FightserverLog.Debug('%s delaygameendcheck %s' % (self.m_Game.m_ID, iGameEndDelay))
        if iGameEndDelay:
            self.m_Game.m_Timer.Logic_Call_Out(self.GameEnd, iGameEndDelay, 'GameOverTime')

    
    def GameEnd(self):
        self.m_ReleaseReason = 'AllDisconnect'
        oGame = self.m_Game
        oGame.m_WarMgr.OnSystemKickOutAll()

    
    def ChangeKickDelayTime(self, iDelay):
        self.m_KickDelayTime = iDelay



def C2GSStartWarPause(oGame, oHero):
    OtherLog.Debug('%s %s startpause %s' % (oGame.m_ID, oHero.m_PlayerID, oHero.m_Game.GetFrameNum()))
    oGame.m_WarKeep.PauseCtrl(oHero.m_PlayerID, 1, sReason = 'startwarpause')


def C2GSEndWarPause(oGame, oHero):
    OtherLog.Debug('%s %s endwarpause %s' % (oGame.m_ID, oHero.m_PlayerID, oHero.m_Game.GetFrameNum()))
    oGame.m_WarKeep.WarKeepHeartBeat(oHero)
    oGame.m_WarKeep.PauseCtrl(oHero.m_PlayerID, 0, sReason = 'endwarpause')

