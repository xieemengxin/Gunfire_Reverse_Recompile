# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/cl_interface.pyc
# RelativePath: clientlogic/clinterface/cl_interface.pyc
# Source Generated with Decompyle++
# File: cl_interface.pyc (Python 3.6)

from cl_only import PLATFORM_ANDROID
from cl_framegame import GetGame, GetAllGame
from cl_object.logging import FightserverLog
from cl_commondefines import GetWarNo, PLAYMODE_MOBILE_DEMO, DEFAULT_HERO
import cl_framegame
import cli_player

def SetResourcePath(sPath):
    import cllib.lib_load
    import cl_wardata.levelconf.load
    cllib.lib_load.SetResourcePath(sPath)
    cl_wardata.levelconf.load.Init()


def SetResourcePathTest(sPath):
    import cllib.lib_load
    import cl_wardata.levelconf.load
    cllib.lib_load.SetResourcePathTest(sPath)
    cl_wardata.levelconf.load.Init()


def CreateLogicGame(iGameID, iRandSeed, dData):
    dWarInfo = dData['WarInfo']
    dPlayerInfo = dData['PlayerInfo']
    oGame = cl_framegame.CreateGame(iGameID, iRandSeed)
    oGame.InitWarInfo(dWarInfo, dPlayerInfo)
    sStartType = dData['StartType'] if 'StartType' in dData else 'Unknown'
    FightserverLog.Info('%d create %d %s-%s %s %s %s ' % (iGameID, dWarInfo['WarNo'], dWarInfo['Round'], dWarInfo['Cycle'], list(dPlayerInfo), GetGameCnt(), sStartType))
    return oGame


def ReleaseLogicGame(iGameID, sReason):
    FightserverLog.Info('%d release %s' % (iGameID, sReason))
    cl_framegame.ReleaseGame(iGameID)


def GetGameCnt():
    return len(cl_framegame.g_GameList)


def GetGameInfo():
    lstGameInfo = [
        0,
        0,
        0,
        0]
    for oGame in cl_framegame.g_GameList.values():
        if not oGame.m_WarMgr:
            continue
        lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
        iCnt = len(lstPlayer)
        if iCnt < 1 or iCnt > 4:
            if iCnt == 0:
                lstGameInfo[0] += 1
                continue
        lstGameInfo[iCnt - 1] += 1
    
    return lstGameInfo


def ReleaseAllGame():
    import C_logic
    import cllib.lib_flag as lib_flag
    dAllGame = cl_framegame.GetAllGame()
    for iGameID, oGame in dAllGame.items():
        if oGame.m_WarMgr:
            lstPlayer = oGame.m_WarMgr.GetAllPlayer()
            FightserverLog.Debug('releasebeforegame %s %s' % (iGameID, lstPlayer))
            for pid in lstPlayer:
                C_logic.DeleteLObject(pid)
            
        ReleaseLogicGame(iGameID, 'ReleaseAllGame')
    


def R_LogicGameStart(resfunc, iMaster, dMaster, iGameID, iRandSeed, dData):
    import clclient.clc_lplayer
    oGame = CreateLogicGame(iGameID, iRandSeed, dData)
    clclient.clc_lplayer.CreateLogicPlayer(iMaster, dMaster, oGame)


def R_KickPlayer(resfunc, pid):
    obj = cli_player.GetPlayer(pid)
    if not obj:
        return None
    oGame = GetGame(obj.m_GameID)
    if not oGame:
        obj.KickOut(obj.m_GameID, 1, 1)
        return None
    oGame.m_WarMgr.OnSystemKickOut(pid)


def R_SyncGameGSCash(resfunc, pid, iCash, iCurChangeNo):
    resfunc(0)
    oPlayer = cli_player.GetPlayer(pid)
    if not oPlayer:
        return None
    oGame = cl_framegame.GetGame(oPlayer.m_GameID)
    if not oGame:
        return None
    oHero = oGame.m_WarMgr.GetHeroByPlayer(pid)
    if not oHero:
        return None
    oHero.SetGSCash(iCash, iCurChangeNo)


def R_NeedKeepInRoom(resfunc, pid, iGameID):
    oGame = GetGame(iGameID)
    if not oGame or not (oGame.m_WarMgr) or not oGame.m_WarMgr.IsInRoom(pid):
        resfunc(0)
        return None
    resfunc(1)


def UpdateLogicScript(sCodeList):
    import clclient.clc_version
    clclient.clc_version.UpdateLogicScript(sCodeList)


def UpdateLogicEncryptScript(sCodeList):
    import clclient.clc_version
    clclient.clc_version.UpdateLogicEncryptScript(sCodeList)


def UpdateLogicScriptByteCode(sCode):
    import clclient.clc_version
    clclient.clc_version.UpdateLogicScriptByteCode(sCode)


def AcceptExtendData(sPath, sCode, iFinish):
    import clclient.clc_pyextend
    clclient.clc_pyextend.AcceptExtendData(sPath, sCode, iFinish)


def CreateMobileDemoGame(iPlayer, *args):
    import cllib.lib_flag
    import rpc
    import C_logic
    FightserverLog.Info('%s mbdemo' % iPlayer)
    if not (cllib.lib_flag.g_IsMobileRun) or not (cllib.lib_flag.g_IsLogicLayer):
        FightserverLog.Error('%s mbdemo wrong ele' % iPlayer)
        return None
    iPlatform = C_logic.GetPlatform()
    if iPlatform != PLATFORM_ANDROID and not (cllib.lib_flag.g_IsInternalRun):
        FightserverLog.Error('%s mbdemo not android %s' % (iPlayer, iPlatform))
    rpc.g_Logic2Logic.SetLinkID(iPlayer)
    TestCreateGame(iPlayer, GetWarNo(PLAYMODE_MOBILE_DEMO))


def MobileDemoOperation(*args):
    FightserverLog.Info('mbdemo oper')
    dGame = GetAllGame()
    for iGame, oGame in dGame.items():
        if oGame.m_WarMgr.m_PlayMode == PLAYMODE_MOBILE_DEMO:
            oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
            oLevelNode = oLevelCtrl.m_CurNode
            lstHero = oGame.m_WarMgr.GetRoomHero()
            oNewbie = oGame.m_WarMgr.GetComponent('NewbieElement')
        lstPerform = oNewbie.m_PerformData if oNewbie else []
        FightserverLog.Info('mbdemo pass %s %s' % (iGame, lstPerform))
        oLevelCtrl.m_DemoFirstLevel = 0
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            for iPerform in lstPerform:
                oHero.m_Perform.RemovePerform(oHero, iPerform)
            
            oHero.DebugHPModifyCureFull()
        
        oLevelNode.PassLevel(lstHero, { })
    


def TestCreateGame(iPlayer, iWarNo, iHero = DEFAULT_HERO):
    import C_logic
    import random
    import cllib.lib_flag
    import clclient.clc_lplayer as lplayer
    import clclient.clc_cmd
    if not cllib.lib_flag.g_IsInternalRun:
        pass
    if not (cllib.lib_flag.g_IsAuthorityRun) and iWarNo != GetWarNo(PLAYMODE_MOBILE_DEMO):
        return None
    dWarInfo = {
        'MemberType': 1,
        'Round': 1,
        'Cycle': 0,
        'WarNo': iWarNo,
        'NewLevel': 0,
        'ReportID': (0, 0) }
    dPlayerInfo = {
        iPlayer: {
            'Side': 1,
            'LGS': 0,
            'Grade': 1,
            'Exp': 0,
            'Name': 'test%s' % iPlayer,
            'CurHero': iHero,
            'HeroData': { },
            'HeroGrade': 1,
            'Weapon': {
                'Unlock': () },
            'Relic': {
                'Unlock': () },
            'Talent': { },
            'Cash': 0,
            'FightIndex': 0,
            'CashChangeNo': 0,
            'UnlockProgress': { },
            'Sublimation': {
                6507: 1 },
            'MaxRoundInfo': (3, 7, 3) } }
    dData = {
        'WarInfo': dWarInfo,
        'PlayerInfo': dPlayerInfo }
    oGame = CreateLogicGame(0, random.randint(0, 268435455), dData)
    lplayer.CreateLogicPlayer(iPlayer, { }, oGame)


def TestGotoLevel(iPlayer, iLevel, sLine = ''):
    import cl_gamegm
    oPlayer = cli_player.GetPlayer(iPlayer)
    oGame = cl_framegame.GetGame(oPlayer.m_GameID)
    oHero = oGame.m_WarMgr.GetHeroByPlayer(iPlayer)
    cl_gamegm.judgegotolevel(oHero, iLevel)


def C_DebugGMCall(iPlayer, code):
    import cl_gamegm
    oPlayer = cli_player.GetPlayer(iPlayer)
    cl_gamegm.R_LogicCmdNew(None, oPlayer.m_ID, code)


def C_SetAuthorityRun():
    import C_logic
    import sys
    import re
    import cllib.lib_flag
    if cllib.lib_flag.g_IsStandalone:
        C_logic.SetLogicFeature(3, 1)
        print('opendebugprintbuffull')
    if not (cllib.lib_flag.g_IsMobile) or cllib.lib_flag.g_IsInternalRun:
        return None
    cllib.lib_flag.g_IsAuthorityRun = 1
    for path in sys.path:
        if 'data2' in path:
            sCond = '(\\S+mobilegame)\\/(data2.fls)'
            m = re.search(sCond, path)
            if m:
                sGmPath = '%s/gamegm.fls' % m.group(1)
                if sGmPath not in sys.path:
                    sys.path.append(sGmPath)
            break
    
    print('setpath', sys.path)


def C_SetFrameWaitTime(iWaitTime):
    import C_logic
    import cllib.lib_flag
    if not cllib.lib_flag.g_IsAuthorityRun:
        return None
    C_logic.SetFrameWaitTime(iWaitTime)
    print('set frame wait: %s' % (iWaitTime,))


def C_SetShenHe(iShenHe):
    import cllib.lib_flag
    import cl_dlcdata
    if iShenHe == cllib.lib_flag.g_IsMobileShenHeRun or not (cllib.lib_flag.g_IsMobile):
        return None
    cllib.lib_flag.g_IsMobileShenHeRun = iShenHe
    cl_dlcdata.InitDlcData()
    print('set shenhe: %s' % iShenHe)

