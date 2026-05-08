# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/clclient/clc_cmd.pyc
# RelativePath: clientlogic/clinterface/clclient/clc_cmd.pyc
# Source Generated with Decompyle++
# File: clc_cmd.pyc (Python 3.6)

from cl_protocol import C2L_FUNC, S2L_FUNC, S2L_RESPOND, C2GS_QUIT, S2L_CALL, S2L_RESP, F2L_CALL, F2L_RESP
from cl_object.logging import FightserverLog
from cl_net import FSFightFunction, FSDuonetCmd
from cl_duonet import Receive
from cllib.lib_net import GetCPacketData, SetPacketDataForUnpack, UnpackInt
from cl_only import PythonError
from cl_protocol import C2GS_WAR_NPCUI
import cl_net
from . import clc_rpc
from . import clc_lplayer
COPYMAN_IGNORE_CMD = (C2GS_WAR_NPCUI,)

def SetLogicFunction():
    global LogicFunction
    LogicFunction = {
        F2L_RESP: clc_rpc.OnFsRespond,
        F2L_CALL: clc_rpc.OnFsCallFunc,
        S2L_RESP: clc_rpc.OnRpcRespond,
        S2L_CALL: clc_rpc.OnRpcCallFunc,
        S2L_RESPOND: clc_rpc.OnRespond,
        S2L_FUNC: clc_rpc.OnCallFunction,
        C2L_FUNC: clc_rpc.OnClientCall }


def SetFightFunction():
    global FightFunction
    FightFunction = {
        C2GS_QUIT: clc_lplayer.C2GSQuit,
        C2L_FUNC: clc_rpc.OnClientCall }

if 'g_OtherCommand' not in globals():
    g_OtherCommand = { }

def SetOtherCommandFunction(dData):
    g_OtherCommand.update(dData)


def OnLogicCommand(iCmd):
    if iCmd in LogicFunction:
        func = LogicFunction[iCmd]
        func()
        return None
    if iCmd in g_OtherCommand:
        func = g_OtherCommand[iCmd]
        func(iCmd)


def OnPlayerCommand(who, iCmd):
    if iCmd in FSDuonetCmd:
        Receive(iCmd, 'C2FS', who.m_HeroObj)
    elif iCmd in FSFightFunction:
        FSFightFunction[iCmd](who.m_HeroObj.m_Game, who.m_HeroObj)
    elif iCmd in FightFunction:
        func = FightFunction[iCmd]
        func(who)


def OnPlayerTakeOverCommand(who, iCmd):
    if iCmd in FightFunction:
        func = FightFunction[iCmd]
        func(who)
        return None
    FightserverLog.Debug('%s %s ignorecmd %s' % (who.m_GameID, who.m_ID, iCmd))


def OnPlayerStopCommand(who, iCmd):
    if iCmd in FightFunction:
        func = FightFunction[iCmd]
        func(who)
        return None
    cl_net.OnStopFightCommand(who, iCmd)


def OnCopyPlayerCommand(who, iCmd):
    OnPlayerCommand(who, iCmd)
    oCopyHero = who.GetCopyHero()
    if not oCopyHero or not (oCopyHero.m_Game):
        return None
    sData = GetCPacketData()
    if sData:
        
        try:
            SetPacketDataForUnpack(sData)
            iCmd = UnpackInt(1)
            if iCmd not in COPYMAN_IGNORE_CMD:
                cl_net.OnProcessFightCommand(oCopyHero.m_Game, oCopyHero, iCmd)
        except:
            PythonError()


