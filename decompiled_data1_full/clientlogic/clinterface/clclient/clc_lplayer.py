# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/clclient/clc_lplayer.pyc
# RelativePath: clientlogic/clinterface/clclient/clc_lplayer.pyc
# Source Generated with Decompyle++
# File: clc_lplayer.pyc (Python 3.6)

from cl_duonet.netfunc import UnpackInt
from cl_object.logging import FightserverLog
from cl_only import PythonError
from . import clc_cmd
import C_logic
import cl_interface
import cl_only
import cllib.lib_flag
import cl_framegame

class CLogicPlayer(object):
    
    def __init__(self, pid, dInfo):
        self.m_ID = pid
        self.m_PlayerID = pid
        self.m_GameID = 0
        self.m_WarMaster = 0
        self.m_PacketSender = None
        self.InitConcrete(pid)
        self.m_Game = None
        self.m_HeroObj = None
        self.m_HeroCopyObj = None
        self.m_CurPlayerCommand = None

    
    def InitConcrete(self, pid):
        if cllib.lib_flag.g_IsTradition:
            import clclient.clc_packetsender
            self.m_PacketSender = clclient.clc_packetsender.CPacketSender(pid)

    
    def Remove(self):
        self.m_Game = None
        self.m_HeroObj = None
        self.m_HeroCopyObj = None
        self.m_CurPlayerCommand = None
        C_logic.DeleteLObject(self.m_ID)

    
    def BindHero(self, oHero):
        self.m_Game = oHero.m_Game
        self.m_HeroObj = oHero
        self.SetPlayerCommand(bEnable = True)

    
    def UnbindHero(self):
        self.m_Game = None
        self.m_HeroObj = None
        self.SetPlayerCommand(False)

    
    def BindCopyHero(self, oHero):
        self.m_HeroCopyObj = oHero
        self.SetPlayerCopyCommand(bEnable = True)

    
    def UnbindCopyHero(self):
        self.m_HeroCopyObj = None
        self.SetPlayerCopyCommand(bEnable = False)

    
    def GetCopyHero(self):
        return self.m_HeroCopyObj

    
    def Call_Out(self, func, delaytime, flag):
        C_logic.TimerCall(self.m_ID, func, delaytime, flag)

    
    def Remove_Call_Out(self, flag):
        C_logic.RemoveTimerCall(self.m_ID, flag)

    
    def Find_Call_Out(self, flag):
        C_logic.FindTimerCall(self.m_ID, flag)

    
    def Disconnected(self):
        FightserverLog.Info('%s disconnected %s' % (self.m_GameID, self.m_PlayerID))
        oGame = cl_interface.GetGame(self.m_GameID)
        if oGame:
            oGame.m_LinkMgr.Disconnected(self.m_PlayerID)

    
    def OnLogin(self, iReEnter = 0):
        FightserverLog.Info('%s onlogin %s' % (self.m_GameID, self.m_PlayerID))
        oGame = cl_interface.GetGame(self.m_GameID)
        if oGame:
            if self.m_PacketSender:
                self.m_PacketSender.Init('war-%s' % str(oGame.m_WarMgr.m_ReportID))
            oGame.m_LinkMgr.OnLogin(self.m_PlayerID, iReEnter)
        if cllib.lib_flag.g_IsStandaloneClient and oGame and iReEnter and not (self.m_WarMaster):
            oGame.m_WarMgr.ReSendCacheReport(self.m_PlayerID)

    
    def OnQuit(self):
        FightserverLog.Info('%s onquit %s' % (self.m_GameID, self.m_PlayerID))
        oGame = cl_interface.GetGame(self.m_GameID)
        if oGame:
            oGame.m_LinkMgr.OnQuit(self.m_PlayerID)

    
    def KickOut(self, iGameID, iLeaveGame, iNowDisconnect):
        if not cllib.lib_flag.g_IsStandaloneClient and self.m_WarMaster:
            FightserverLog.Info('%s kickout %s' % (self.m_GameID, self.m_PlayerID))
            oGame = cl_interface.GetGame(iGameID)
            if oGame:
                oGame.m_WarMgr.OnSystemKickOut(self.m_PlayerID)
                self.Call_Out(self.LoginOff, 1, 'kickloginoff')

    
    def LoginOff(self):
        FightserverLog.Info('%s loginoff %s' % (self.m_GameID, self.m_PlayerID))
        
        try:
            if not (self.m_WarMaster) and cllib.lib_flag.g_IsStandaloneClient:
                oGame = cl_interface.GetGame(self.m_GameID)
                if oGame:
                    oGame.m_WarMgr.OnSystemKickOut(self.m_PlayerID)
        except:
            PythonError()

        C_logic.DeleteLObject(self.m_ID)
        self.OnQuit()
        self.m_GameID = 0

    
    def SetPlayerCommand(self, bEnable):
        FightserverLog.Info('%s setcommand %s' % (self.m_PlayerID, bEnable))
        if bEnable:
            self.EnablePlayerCommand(clc_cmd.OnPlayerCommand)
        else:
            C_logic.DoCommand(self.m_ID, 'set_command', {
                'function': clc_cmd.OnPlayerTakeOverCommand })

    
    def SetPlayerCopyCommand(self, bEnable):
        FightserverLog.Info('%s setcopycommand %s' % (self.m_ID, bEnable))
        if bEnable:
            self.EnablePlayerCommand(clc_cmd.OnCopyPlayerCommand)
        elif not bEnable and self.m_HeroObj:
            self.EnablePlayerCommand(clc_cmd.OnPlayerCommand)

    
    def EnablePlayerCommand(self, cFunc):
        C_logic.DoCommand(self.m_ID, 'set_command', {
            'function': cFunc })
        self.m_CurPlayerCommand = cFunc

    
    def GetCurPlayerCommand(self):
        return self.m_CurPlayerCommand



def CreateLogicPlayer(pid, dInfo, oGame):
    obj = CLogicPlayer(pid, dInfo)
    
    try:
        C_logic.CreateLPlayer(pid, {
            'object': obj })
    except:
        C_logic.PythonError()
        C_logic.DeleteLObject(pid)
        return None

    C_logic.DoCommand(obj.m_ID, 'net_linkentity', {
        'entity_id': pid })
    obj.m_GameID = oGame.m_ID
    iReEnter = dInfo.get('ReEnter', 0)
    obj.OnLogin(iReEnter)
    return obj


def ReEnterGame(pid):
    lstGameID = cl_framegame.GetAllGameID()
    if not lstGameID:
        FightserverLog.Alert('%s nogame' % pid)
        return None
    iGameID = lstGameID[0]
    oGame = cl_framegame.GetGame(iGameID)
    if not oGame:
        FightserverLog.Alert('%s nogame %s' % (iGameID, pid))
        return None
    oWarMgr = oGame.m_WarMgr
    lstAllPlayer = oWarMgr.GetAllPlayer()
    if pid not in lstAllPlayer:
        FightserverLog.Alert('%s invalid %s %s' % (iGameID, pid, lstAllPlayer))
        return None
    if oWarMgr.IsInRoom(pid):
        FightserverLog.Alert('%s repeat %s' % (iGameID, pid))
        return None
    if oWarMgr.HasSettled(pid):
        FightserverLog.Alert('%s settled %s' % (iGameID, pid))
        return None
    oWarMgr.ReAddPlayer(pid)
    CreateLogicPlayer(pid, {
        'ReEnter': 1 }, oGame)


def C2GSQuit(who):
    iSub = UnpackInt(1)
    FightserverLog.Info('%s c2gsquit %s' % (who.m_ID, iSub))
    if iSub == 1:
        who.LoginOff()
    elif iSub == 2:
        who.OnLogin(1)
    elif iSub == 3:
        cl_interface.ReleaseAllGame()


def C_ReConnect(pid, iType):
    FightserverLog.Info('tryreconnect %s %s' % (pid, iType))
    pid = int(pid)
    who = C_logic.GetLObject(pid)
    if who and not who.Find_Call_Out('tryreconnect'):
        who.Call_Out(cl_only.Functor(who.OnLogin, 1), 200, 'tryreconnect')
    if not who and iType in (3, 4):
        ReEnterGame(pid)


def C_Disconnect(pid):
    who = C_logic.GetLObject(int(pid))
    if who:
        who.Disconnected()

