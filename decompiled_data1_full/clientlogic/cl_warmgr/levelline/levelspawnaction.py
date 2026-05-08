# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelline/levelspawnaction.pyc
# RelativePath: clientlogic/cl_warmgr/levelline/levelspawnaction.pyc
# Source Generated with Decompyle++
# File: levelspawnaction.pyc (Python 3.6)

from cl_only import ChooseKey, Time2Frame, Functor
from cl_commondefines import PLAYMODE_ROGUELIKE, LEVEL_SPAWN_TRIGGERNPC, LEVEL_SPAWN_BOSSNEWBIE, LEVEL_SPAWN_MONSTERALLDIE, LEVEL_SPAWN_GIVEHEROPASSIVE, LEVEL_SPAWN_REMOVEBUILD, DAM_USE_HP, DAM_TYPE_SCENE, KILLHISTORY_COMPATIBY, LEVEL_TYPE_BOSS, LEVEL_TYPE_HALL, LEVEL_TYPE_FIGHT, LEVEL_SPAWN_CALCNEWVERLAYER, DIE_PRIORITY_KILL
import cl_notify
import cl_msgcenter
import cl_snetwar
import cl_formula
import cl_reward
import cl_object.reason
import cllib.lib_flag

def SpawnPassLevelNotify(oLevelNode):
    if oLevelNode.m_LevelType != LEVEL_TYPE_FIGHT:
        return None
    oGame = oLevelNode.m_Game
    cl_notify.SendCommonNotify(oGame, oGame.m_WarMgr.GetLivePlayer(), 2008, { })


def SpawnTriggerRoomGoalMusic(oLevelNode, oScene):
    if oLevelNode.m_LevelType in (LEVEL_TYPE_HALL, LEVEL_TYPE_BOSS):
        return None
    iMusicBeh = 31
    oGame = oLevelNode.m_Game
    lstPlayer = oScene.GetPlayers()
    for pid in lstPlayer:
        iHero = oGame.m_WarMgr.GetHeroIDByPlayerID(pid)
        cl_snetwar.GS2CTriggerBehavior(oGame, iHero, iMusicBeh, [
            pid])
    


def SpawnBossNewBieBehavior(oLevelNode, tParam):
    if not oLevelNode:
        return None
    if oLevelNode.m_Game.m_WarMgr.m_PlayMode != PLAYMODE_ROGUELIKE:
        return None
    (iBehavior, lstMonster, iCnt) = tParam
    oGame = oLevelNode.m_Game
    lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
    for pid in lstPlayer:
        oHero = oGame.m_WarMgr.GetHeroByPlayer(pid)
        if not oHero:
            continue
        iHero = oHero.m_ID
        dMonster = oHero.Query('Monster')
        if 'KillBoss' not in dMonster:
            continue
        iKill = 0
        for iMonsterSID in lstMonster:
            iKill += dMonster['KillBoss'].get(iMonsterSID, 0)
        
        iKill += dMonster['KillBoss'].get(KILLHISTORY_COMPATIBY, 0)
        if iKill + 1 == iCnt:
            cl_snetwar.GS2CTriggerBehavior(oGame, iHero, iBehavior, [
                oHero.m_PlayerID])
    


def CheckSpawn(oLevelNode, dAction):
    oCtrlMgr = oLevelNode.m_CtrlMgr
    dWarData = oCtrlMgr.m_LevelCtrlConf
    lstUnSpawnRule = []
    if oLevelNode.m_LevelType == LEVEL_TYPE_BOSS:
        dBossInfo = dWarData[oCtrlMgr.m_LayerNum]['BossInfo']
        lstUnSpawnRule = dBossInfo['UnSpawnRuleInfo'][oLevelNode.m_Level] if oLevelNode.m_Level in dBossInfo['UnSpawnRuleInfo'] else []
    elif oLevelNode.m_LevelType == LEVEL_TYPE_FIGHT:
        dlevelInfo = dWarData[oCtrlMgr.m_LayerNum]['CtrlInfo'][oCtrlMgr.m_LevelNum]['NormalFilter']
        if oLevelNode.m_Level in dlevelInfo and 'UnSpawnRuleInfo' in dlevelInfo[oLevelNode.m_Level]:
            lstUnSpawnRule = dlevelInfo[oLevelNode.m_Level]['UnSpawnRuleInfo']
    for dUnSpawnRule in lstUnSpawnRule:
        if (dAction['func'] in (LEVEL_SPAWN_BOSSNEWBIE, LEVEL_SPAWN_GIVEHEROPASSIVE) or dUnSpawnRule['func'] == dAction['func']) and dUnSpawnRule['param'][0] == dAction['param'][0] and dUnSpawnRule['type'] == dAction['type']:
            return 0
        if dUnSpawnRule['func'] == dAction['func'] and dUnSpawnRule['type'] == dAction['type']:
            return 0
    
    return 1


def SpawnTriggerBehavior(oLevelNode, tParam):
    if not oLevelNode:
        return None
    (iBehavior, iReSend) = tParam
    oGame = oLevelNode.m_Game
    lstHero = oGame.m_WarMgr.GetRoomHero()
    for iHero in lstHero:
        oHero = oGame.GetObject(iHero)
        cl_snetwar.GS2CTriggerBehavior(oGame, iHero, iBehavior, [
            oHero.m_PlayerID])
    
    oLevelCtrl = oLevelNode.m_CtrlMgr
    if not oLevelCtrl:
        return None
    oGame.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, 'LevelSpawnClientBehavior')
    if iReSend:
        oGame.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, Functor(ReEnterClientBehavior, iBehavior), 'LevelSpawnClientBehavior')


def ReEnterClientBehavior(iBehavior, oWarMgr, oWarrior, dInfo):
    iPlayer = oWarrior.m_PlayerID
    cl_snetwar.GS2CTriggerBehavior(oWarMgr.m_Game, oWarrior.m_ID, iBehavior, [
        iPlayer])


def SpawnTriggerNpc(oLevelNode, tParam):
    pass


def SpawnRemoveBuild(oLevelNode, tParam):
    (_, iDelay) = tParam
    if iDelay:
        func = Functor(DelaySpawnRemoveBuild, oLevelNode, tParam)
        oLevelNode.m_CtrlMgr.Call_Out(func, Time2Frame(iDelay), 'RemoveBuild')
    else:
        DelaySpawnRemoveBuild(oLevelNode, tParam)


def DelaySpawnRemoveBuild(oLevelNode, tParam):
    (lstPrefab, _) = tParam
    oGame = oLevelNode.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oLevelNode.m_Scene)
    if not oScene:
        return None
    lstBuild = oScene.GetObjectsByTypes([
        'Build',
        'Obstacle',
        'Trap',
        'GateControl'])
    for bid in lstBuild:
        oBuild = oGame.GetObject(bid)
        if not oBuild:
            continue
        if oBuild.m_Prefab in lstPrefab:
            oBuild.DirectRemove('LevelSpawnRemove')
    


def SpawnSceneMonsterAllDie(oLevelNode, tParam):
    oGame = oLevelNode.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oLevelNode.m_Scene)
    oReason = cl_object.reason.CStrReason('LevelSpawnAction', None, {
        'DamType': DAM_TYPE_SCENE | DAM_USE_HP })
    for tRoomList in oLevelNode.m_RoomList:
        for oLineNode in tRoomList:
            oLineNode.m_MonsterCtrl.ClearPendSpawnMonster()
        
    
    for mid in oScene.GetObjectsByType('Monster'):
        oMonster = oGame.GetObject(mid)
        if not oMonster:
            continue
        oMonster.Set('RelifeInfo', { })
        oMonster.SetDiePriority(DIE_PRIORITY_KILL, 'LevelSpawnAction')
        oMonster.HPDirectModify('HP', 0, -(oMonster.m_HP), oReason)
    


def SpawnGiveHeroPassive(oLevelNode, tParam):
    (iPerform, iRemove) = tParam
    oGame = oLevelNode.m_Game
    lstLiveHero = oGame.m_WarMgr.GetLiveHero()
    for iHero in lstLiveHero:
        oHero = oGame.GetObject(iHero)
        if not oHero:
            continue
        if iRemove:
            oHero.m_Perform.RemovePerform(oHero, iPerform)
            continue
        oHero.AddPerform(iPerform, 1)
    


def SpawnCalcIsNewVerLayer(oLevelNode, tParam):
    if cllib.lib_flag.g_IsMobile:
        return None
    oGame = oLevelNode.m_Game
    oWarMgr = oGame.m_WarMgr
    (lstBoss, iCnt, iFinalRatio, iDecRatio) = tParam
    if oWarMgr.IsEndless():
        iRatio = iFinalRatio
    else:
        lstHero = oWarMgr.GetRoomHero(iCalAI = 0)
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iRatio = 0
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            dMonster = oHero.Query('Monster', { })
            if 'KillBoss' not in dMonster:
                continue
            iKill = 0
            for iMonsterSID in lstBoss:
                iKill += dMonster['KillBoss'].get(iMonsterSID, 0)
            
            if iKill < iCnt:
                continue
            dPassNum = oHero.Query('NewVerLayer', { })
            iPassNum = dPassNum[oLevelCtrl.m_LayerNum] if oLevelCtrl.m_LayerNum in dPassNum else 0
            iHeroRatio = max(iFinalRatio, 100 - iPassNum * iDecRatio)
            iRatio = max(iRatio, iHeroRatio)
        
    if oGame.Random(100) < iRatio:
        oWarMgr.SetNewVerLayer(iIsNew = 1)
    else:
        oWarMgr.SetNewVerLayer(iIsNew = 0)

g_SpawnFunc = {
    LEVEL_SPAWN_CALCNEWVERLAYER: SpawnCalcIsNewVerLayer,
    LEVEL_SPAWN_BOSSNEWBIE: SpawnBossNewBieBehavior,
    LEVEL_SPAWN_GIVEHEROPASSIVE: SpawnGiveHeroPassive,
    LEVEL_SPAWN_MONSTERALLDIE: SpawnSceneMonsterAllDie,
    LEVEL_SPAWN_REMOVEBUILD: SpawnRemoveBuild,
    LEVEL_SPAWN_TRIGGERNPC: SpawnTriggerNpc }

def GetSpawnFunc(idx):
    if idx in g_SpawnFunc:
        return g_SpawnFunc[idx]

