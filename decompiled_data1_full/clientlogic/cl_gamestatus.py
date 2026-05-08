# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_gamestatus.pyc
# RelativePath: clientlogic/cl_gamestatus.pyc
# Source Generated with Decompyle++
# File: cl_gamestatus.pyc (Python 3.6)

from cllib.lib_only import DoCommand, GetCommandMode, GetCommandKey
from cli_player import GetPlayer
import C_frgame
import cl_snetwar
STAT_GAME_INIT = 1
STAT_GAME_STEPING = 2
STAT_GAME_STOPED = 3
STAT_GAME_RELEASED = 4

class CGameStatus(object):
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_Status = STAT_GAME_INIT
        self.m_AfterStartHook = { }

    
    def Release(self):
        self.m_Status = STAT_GAME_RELEASED
        self.m_AfterStartHook.clear()
        self.m_Game = None

    
    def IsSteping(self):
        return self.m_Status == STAT_GAME_STEPING

    
    def IsStoped(self):
        return self.m_Status == STAT_GAME_STOPED

    
    def StartStep(self):
        if self.m_Status not in (STAT_GAME_INIT, STAT_GAME_STOPED):
            return None
        C_frgame.AddCtrlGame(self.m_Game.m_ID)
        if self.m_Status == STAT_GAME_STOPED:
            self.StartCommand()
        self.m_Status = STAT_GAME_STEPING
        self.m_Game.ProcessCacheCommand()
        self.NotifyStatus()
        for after in self.m_AfterStartHook.values():
            after()
        

    
    def SetAfterStartHook(self, sKey, fAfterFunc = None):
        if not fAfterFunc:
            if sKey not in self.m_AfterStartHook:
                return None
            self.m_AfterStartHook.pop(sKey)
        else:
            self.m_AfterStartHook[sKey] = fAfterFunc

    
    def StopStep(self, fAfterFunc = None):
        if self.m_Status != STAT_GAME_STEPING:
            return None
        C_frgame.PopCtrlGame(self.m_Game.m_ID)
        self.m_Status = STAT_GAME_STOPED
        self.NotifyStatus()
        if fAfterFunc:
            fAfterFunc()
        self.StopCommand()

    
    def NotifyStatus(self, pid = 0):
        iStat = int(self.m_Status != STAT_GAME_STEPING)
        iFrame = self.m_Game.GetFrameNum()
        if pid:
            dPlayer = {
                pid: 1 }
        else:
            allList = self.m_Game.m_WarMgr.GetRoomPlayer()
            dPlayer = dict.fromkeys(allList, 1)
        cl_snetwar.GS2CWarStatus(self.m_Game, iStat, iFrame, dPlayer)

    
    def OnReady(self, pid):
        self.NotifyStatus(pid)

    
    def StartCommand(self):
        lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer()
        sKey = GetCommandKey()
        for pid in lstPlayer:
            who = GetPlayer(pid)
            if not who:
                continue
            cFun = who.GetCurPlayerCommand()
            if cFun:
                DoCommand(pid, sKey, {
                    'function': cFun })
        

    
    def StopCommand(self):
        lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer()
        sKey = GetCommandKey()
        cFun = GetCommandMode().OnPlayerStopCommand
        for pid in lstPlayer:
            DoCommand(pid, sKey, {
                'function': cFun })
        


