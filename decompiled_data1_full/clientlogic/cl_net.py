# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_net.pyc
# RelativePath: clientlogic/cl_net.pyc
# Source Generated with Decompyle++
# File: cl_net.pyc (Python 3.6)

from cl_protocol import C2GS_WAR_NOTIFY, C2GS_WAR_MOVE, C2GS_GAME_DEBUG, C2GS_TEXT, C2GS_SKILL_TRIGGER, C2GS_MAP_SCENE, C2GS_SKILL_START, C2GS_WAR_PING, C2GS_BULLETCHANGE_RULE, C2GS_WAR_MOVEBACK, C2GS_WAR, C2GS_WAR_ITEM, C2GS_WAR_NPCUI, C2GS_WAR_RELIC, C2GS_LEAVEGAME, C2GS_WAR_ENDPAUSE, C2GS_WAR_STARTPAUSE, C2GS_SKILL_TRIBULLET, C2GS_SKILL_DELEGATE, C2GS_SKILL_THROUGHINFO, C2GS_WAR_NEW_PING, C2GS_WAR_MINIGAME, C2GS_WAR_PET, C2GS_WAR_TALENT, C2GS_WAR_WAND, C2GS_WAR_DICE, C2GS_WAR_SEASONPLAY, C2GS_SPLIT_PROTO
from cllib.lib_net import GetCPacketData
from cl_framegame import GetGame
from cl_duonet import GetProcessedProtoSet, Receive
import cl_only

def Init():
    SetFightFunction()


def SetFightFunction():
    global FSFightFunction, FSDuonetCmd, StopDuonetCmd, CacheDuonetCmd
    import cl_perform.net
    import cl_link
    import cl_gamekeep
    import cl_gamedebug
    FSFightFunction = {
        C2GS_SPLIT_PROTO: cl_gamedebug.C2GSSplitPackage,
        C2GS_TEXT: cl_gamedebug.C2GSTextOP,
        C2GS_LEAVEGAME: cl_link.C2GSLeaveGame,
        C2GS_WAR_ENDPAUSE: cl_gamekeep.C2GSEndWarPause,
        C2GS_WAR_STARTPAUSE: cl_gamekeep.C2GSStartWarPause,
        C2GS_SKILL_TRIBULLET: cl_perform.net.C2GSSkillTriggerBulletChange,
        C2GS_SKILL_THROUGHINFO: cl_perform.net.C2GSSkillThroughInfo,
        C2GS_SKILL_DELEGATE: cl_perform.net.C2GSSkillDelegate,
        C2GS_SKILL_TRIGGER: cl_perform.net.C2GSSkillTrigger,
        C2GS_SKILL_START: cl_perform.net.C2GSSkillStart }
    FSDuonetCmd = GetProcessedProtoSet('C2FS')
    StopDuonetCmd = {
        C2GS_WAR_SEASONPLAY: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
        C2GS_WAR_DICE: (1, 2, 3, 4, 5, 6, 7, 9, 10),
        C2GS_WAR_WAND: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        C2GS_WAR_PET: (1, 2, 3, 4, 5, 6, 7, 8),
        C2GS_WAR_NOTIFY: (2,),
        C2GS_WAR_MINIGAME: (1,),
        C2GS_WAR_MOVE: (3,),
        C2GS_GAME_DEBUG: (2, 3),
        C2GS_BULLETCHANGE_RULE: (),
        C2GS_WAR_MOVEBACK: (),
        C2GS_WAR: (12, 14, 28, 32, 33, 37, 38, 39, 1, 41, 42, 40, 43, 46, 47, 96, 97, 99, 100, 101, 102),
        C2GS_WAR_NPCUI: (),
        C2GS_WAR_ITEM: (1, 3),
        C2GS_WAR_RELIC: (1, 2, 3, 4),
        C2GS_WAR_TALENT: (1,) }
    CacheDuonetCmd = {
        C2GS_WAR_MOVE: {
            1: 1,
            2: 1 },
        C2GS_WAR: {
            4: 1 } }

SetFightFunction()

def OnProcessFightCommand(oGame, oHero, iCmd):
    if iCmd in FSDuonetCmd:
        Receive(iCmd, 'C2FS', oHero)
    elif iCmd in FSFightFunction:
        func = FSFightFunction[iCmd]
        func(oGame, oHero)


def IsStopDuonetCmd(iCmd):
    if iCmd not in StopDuonetCmd:
        return False
    if not StopDuonetCmd[iCmd]:
        return True
    sData = GetCPacketData()
    if len(sData) <= 1:
        return False
    if int(sData[1]) not in StopDuonetCmd[iCmd]:
        return False
    return True


def IsCacheDuonetCmd(iCmd):
    if iCmd not in CacheDuonetCmd:
        return False
    if not CacheDuonetCmd[iCmd]:
        return True
    sData = GetCPacketData()
    if len(sData) <= 1:
        return False
    if int(sData[1]) in CacheDuonetCmd[iCmd]:
        return True
    return False


def OnStopFightCommand(who, iCmd):
    oGame = GetGame(who.m_GameID)
    if not oGame:
        return None
    oHero = oGame.m_WarMgr.GetHeroByPlayer(who.m_ID)
    if not oHero:
        return None
    if iCmd == C2GS_WAR_NEW_PING or iCmd == C2GS_WAR_PING:
        oGame.m_WarKeep.WarKeepHeartBeat(oHero)
    elif iCmd == C2GS_WAR_ENDPAUSE:
        OnProcessFightCommand(oGame, oHero, iCmd)
    elif iCmd == C2GS_LEAVEGAME:
        OnProcessFightCommand(oGame, oHero, iCmd)
    elif iCmd == C2GS_MAP_SCENE:
        OnProcessFightCommand(oGame, oHero, iCmd)
    elif iCmd == C2GS_TEXT:
        OnProcessFightCommand(oGame, oHero, iCmd)
    elif iCmd in (C2GS_SKILL_START, C2GS_SKILL_TRIGGER, C2GS_SKILL_DELEGATE, C2GS_SKILL_THROUGHINFO, C2GS_SKILL_TRIBULLET):
        oGame.PushCommandCache(oHero)
    elif IsStopDuonetCmd(iCmd):
        Receive(iCmd, 'C2FS', oHero)
    elif IsCacheDuonetCmd(iCmd):
        oGame.PushCommandCache(oHero)
    else:
        return None

