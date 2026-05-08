# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/buildaction.pyc
# RelativePath: clientlogic/cl_wardata/buildaction.pyc
# Source Generated with Decompyle++
# File: buildaction.pyc (Python 3.6)

from cl_only import Time2Frame, Functor, ChooseKey, SendAlert
from cl_commondefines import WARRIOR_TRAP_NORMAL, WARRIOR_OBSTACLE_STATICTRAN, WARRIOR_OBSTACLE_SLIDEDOOR, TRANSFER_DIRTO_HIDE, WARRIOR_OBSTACLE_TRANGATE, MG_SOURCE_SMASHOBSTACLE, SIDE_TYPE_HERO, WARRIOR_SUMMON_STELE, STATE_TIME_LIMIT, STATE_TIME_FOREVER, PARAM_LEVEL_MEDIUM_HIGH, MONSTERAI_TYPE_DEFAULT, MONSTERAI_TYPE_HATESEARCH, SIDE_TYPE_MONSTER, STATE_SPIDER_GUARANTEEDDIE
from cl_math import RotateByEuler
from cl_resmgr.aitempparam import GetAIConfParam
import math
import cl_reward
import cl_notify
import cl_snetwar
import cl_msgcenter
import cl_formula
import cl_state
import cl_object.reason

def SmashObstacleRewardItemList(oBuild, who, dMiniGame, iDelay, iLimitHeroSide = 1):
    if not who:
        return None
    if iLimitHeroSide and who.m_Side != SIDE_TYPE_HERO:
        return None
    iHero = who.m_ID
    sKey = 'BuildeReward'
    dExtInfo = {
        'CalOffset': 0,
        'CheckGoldenCup': 1 }
    dReward = { }
    for iMiniGame, dInfo in dMiniGame.items():
        dReward[iMiniGame] = (dInfo['Prop'], dInfo['Times'])
    
    if not iDelay:
        cl_reward.RewardItemByMiniGame(oBuild, iHero, dReward, sKey, MG_SOURCE_SMASHOBSTACLE, dExtInfo)
    else:
        oBuild.Call_Out(Functor(cl_reward.RewardItemByMiniGame, oBuild, iHero, dReward, sKey, MG_SOURCE_SMASHOBSTACLE, dExtInfo), Time2Frame(iDelay), sKey)


def SmashObstacleCreateTransfer(oBuild, who, iNpcSID, iLimitHeroSide = 1):
    if not who:
        return None
    if iLimitHeroSide and who.m_Side != SIDE_TYPE_HERO:
        return None
    oGame = oBuild.m_Game
    iScene = oBuild.m_Scene
    tAngle = oBuild.m_ModelData.m_ModelAngle
    tIntAngle = (int(tAngle[0]), int(tAngle[1]), int(tAngle[2]))
    dNpcInfo = {
        'SID': iNpcSID,
        'Pos': oBuild.GetPos(),
        'Facing': RotateByEuler((0, 0, 1), tIntAngle),
        'TransferDir': TRANSFER_DIRTO_HIDE,
        'HideLevel': oBuild.Query('HideLevel') }
    oNpc = oGame.m_ResMgr.CreateNpc(iScene, iNpcSID, dNpcInfo, oBuild.m_LineIdx)
    cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), 2210, {
        '$$name': who.m_OwnerName })
    cl_snetwar.GS2CTriggerBehavior(oGame, oNpc.m_ID, 65, oGame.GetRealPlayers())
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_FINDHIDELEVEL, who, {
        'iNpc': oNpc.m_ID })


def SmashObstacleCreateSummon(oBuild, who, iSummonSID, iShape, tShapeInfo, iLiveTime, iPerfom, iLimitHeroSide = 1):
    if not who:
        return None
    if iLimitHeroSide and who.m_Side != SIDE_TYPE_HERO:
        return None
    oGame = oBuild.m_Game
    iScene = oBuild.m_Scene
    dSummonInfo = {
        'Origin': oBuild.GetPos(),
        'Angle': oBuild.GetEuler(),
        'Shape': iShape,
        'Scale': (1, 1, 1),
        'Center': (0, 0, 0),
        'Size': tShapeInfo,
        'Owner': oBuild.m_ID }
    iLiveFrame = Time2Frame(iLiveTime)
    oSummon = oGame.m_ResMgr.CreateSummon(iScene, iSummonSID, dSummonInfo, oBuild.m_LineIdx)
    oSummon.SetLifeFrame(iLiveFrame)
    oSummon.TriggerSummon({
        'Perform': iPerfom })


def SmashObstacleCreateMonster(oBuild, oAttack, iMonster, dNumWeight, fRadius, iReward, iDelay):
    
    def CreateMonster():
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        iAddGrade = 0
        for tPos in lstPos:
            dAI = {
                'AIParamLv': PARAM_LEVEL_MEDIUM_HIGH,
                'AIMethod': MONSTERAI_TYPE_DEFAULT }
            dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH)
            dAI.update(dHateSearchAI)
            oMonster = oGame.m_ResMgr.CreateMonster(iScene, iMonster, tPos, tFace, SIDE_TYPE_MONSTER, iAddGrade, dAI, tLine, dExtInfo)
            if not oMonster:
                continue
            dArgs = {
                'AID': oBuild.m_ID,
                'RS': cl_object.reason.CStrReason('ObstacleAddState:%d_%d' % (oBuild.m_SID, oBuild.m_ID)) }
            oState = cl_state.AddState(oMonster, STATE_SPIDER_GUARANTEEDDIE, STATE_TIME_FOREVER, 0, dArgs)
            if oState:
                oState.Enable(oMonster)
            if not iReward:
                oMonster.m_Reward = { }
        

    oGame = oBuild.m_Game
    iScene = oBuild.m_Scene
    if not iScene:
        return None
    tFace = oBuild.GetFacing()
    tLine = oBuild.m_LineIdx
    fModelRadius = oBuild.m_ModelRadius
    iMonsterNum = ChooseKey(oGame, dNumWeight)
    vCenterPos = oBuild.GetPos()
    iTriTimes = 10
    lstPos = []
    for _ in range(iMonsterNum):
        for _ in range(iTriTimes):
            tPos = oGame.Scene_RandomPointSectorInMesh(iScene, vCenterPos, (1, 0, 0), fModelRadius, fRadius, 1, 180)
            if tPos:
                vCenterPos = tPos
                lstPos.append(tPos)
                break
        
    
    if not lstPos:
        return None
    iBuildID = oBuild.m_ID
    dExtInfo = {
        'OwnerObstacle': iBuildID,
        'SmashObstacleSummon': 1 }
    dMsgInfo = {
        'MonsterNum': len(lstPos),
        'OwnerObstacle': iBuildID,
        'ObstacleSID': oBuild.m_SID,
        'MonsterSID': iMonster,
        'LineIdx': tLine }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_SMASHOBSTACLE_CREATEMONSTER, oGame.m_WarMgr, dMsgInfo)
    iFrame = Time2Frame(iDelay)
    if iFrame > 0:
        sKey = 'SmashObstacleCreateMonster-%s' % oBuild.m_ID
        oGame.m_WarMgr.Call_Out(CreateMonster, iFrame, sKey)
    else:
        CreateMonster()


def SmashObstacleTriggerGroup(oBuild, who, dWeight):
    oGame = oBuild.m_Game
    iGroup = ChooseKey(oGame, dWeight)
    if iGroup == -1:
        return None
    if iGroup not in oBuild.m_SmashReserveGroup:
        iWarMgrSID = oGame.GetWarMgr().m_SID
        SendAlert('err', '战场%s 建筑%s 击碎行为备用组 %s 未配置 %s' % (iWarMgrSID, oBuild.m_SID, iGroup, dWeight))
        return None
    func = oBuild.m_SmashReserveGroup[iGroup]
    func(oBuild, who)


def InitBuildSetGateEffectParam(oBuild, iCloseBehavior, iOpenBehavior, iCloseShowTime, iHideBehavior, iHideShowTime, iBornEffect):
    if oBuild.m_FightType not in (WARRIOR_OBSTACLE_TRANGATE, WARRIOR_OBSTACLE_STATICTRAN, WARRIOR_OBSTACLE_SLIDEDOOR):
        return None
    oBuild.m_CloseBehavior = iCloseBehavior
    oBuild.m_OpenBehavior = iOpenBehavior
    oBuild.m_HeroHideBehavior = iHideBehavior
    oBuild.m_HeroBornBehavior = iBornEffect
    oBuild.m_DelayShowCloseTime = iCloseShowTime
    oBuild.m_DelayTransferTime = iHideShowTime


def InitTrapEffectParam(oBuild, iBeginBehavior, iOverBehavior):
    if not oBuild.m_FightType == WARRIOR_TRAP_NORMAL:
        return None
    oBuild.m_BeginBehavior = iBeginBehavior
    oBuild.m_OverBehavior = iOverBehavior


def InitSummonStelaParam(oBuild, iActivatedRadius, iHPDecreaseRadius, iSpawnMonsterRadius, iMaxMonsterCount, iSuperProbability, dMonsterAf, iSpawnMonsterEffect, iForceRefreshTime, iAllDeadRefreshTime, iSupplementHP):
    if not oBuild.m_FightType == WARRIOR_SUMMON_STELE:
        return None
    oBuild.m_ActivatedRadius = iActivatedRadius
    oBuild.m_HPDecreaseRadius = iHPDecreaseRadius
    oBuild.m_SpawnMonsterRadius = iSpawnMonsterRadius
    oBuild.m_MaxMonsterCount = math.ceil(cl_formula.GetResultByData(oBuild, iMaxMonsterCount, { }) / 100)
    oBuild.m_SuperProbability = iSuperProbability
    oBuild.m_MonsterAfDict = dMonsterAf
    oBuild.m_SpawnMonsterEffect = iSpawnMonsterEffect
    oBuild.m_ForceRefreshFrame = Time2Frame(iForceRefreshTime)
    oBuild.m_AllDeadRefreshFrame = Time2Frame(iAllDeadRefreshTime)
    oBuild.m_SupplementHP = cl_formula.GetResultByData(oBuild, iSupplementHP, { })


def BuildTriggerClientBehavior(oNpc, oHero, iBehavior, iSendToAll):
    oGame = oNpc.m_Game
    if iSendToAll:
        lstPlayer = oGame.GetRealPlayers()
    else:
        lstPlayer = [
            oHero.m_PlayerID]
    cl_snetwar.GS2CTriggerBehavior(oGame, oNpc.m_ID, iBehavior, lstPlayer)


def BuildAddState(oBuild, iState, iTime):
    dArgs = {
        'AID': oBuild.m_ID,
        'RS': cl_object.reason.CStrReason('BuildAddState:%d_%d' % (oBuild.m_SID, oBuild.m_ID)) }
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = cl_formula.GetResultByData(oBuild, iTime, { })
    else:
        iTimeType = STATE_TIME_FOREVER
    oState = cl_state.AddState(oBuild, iState, iTimeType, Time2Frame(iTime), dArgs)
    if not oState:
        return None
    oState.Enable(oBuild)


def InitThunderTrapCenterPos(oBuild):
    oLevelCtrl = oBuild.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    (iLevel, iRoomPos, _) = oBuild.m_LineIdx
    oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
    oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
    lstCernterPos = []
    for oLine in oLevelNode.m_RoomList[iRoomPos]:
        lstLineCernterPos = oLevelConfData.GetLineConfig(iLevel, oLine.m_Name, 'thundercenterpos')
        if not lstLineCernterPos:
            continue
        lstCernterPos.extend(lstLineCernterPos)
    
    oBuild.Set('ThunderCernterPos', lstCernterPos)


def SetThunderTrapOrSwitchEffectParam(oBuild, iEnableBehavior, iCastingBehavior, iChargeBehavior):
    oBuild.m_EnableBehavior = iEnableBehavior
    oBuild.m_CastingBehavior = iCastingBehavior
    oBuild.m_ChargeBehavior = iChargeBehavior

