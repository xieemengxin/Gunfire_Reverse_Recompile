# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_condition/con_aiperform.pyc
# RelativePath: clientlogic/cl_condition/con_aiperform.pyc
# Source Generated with Decompyle++
# File: con_aiperform.pyc (Python 3.6)

from cl_only import CELL_SPACESIZE, CELL_REC, PY_FLAG_DEAD, PY_FLAG_DIED
from cl_commondefines import WARRIOR_HERO, WARRIOR_MONSTER, ATT_SHAPE_SPHERE
from cl_pxlayer import PXMASK_MONSTER, PXMASK_PLAYER, PXMASK_LIVEOBJ, PXMASK_SIGHTBLK, PXMASK_MOVEBLK, PXMASK_SKILLBLK
import cl_math
import cl_gamedebug as debug

def GetSummonCnt(oOwner, dInfo, iSummonSID):
    iNowCnt = 0
    for iSummonID in oOwner.m_SummonDict:
        oSummon = oOwner.m_Game.GetObject(iSummonID, PY_FLAG_DEAD)
        if not oSummon:
            continue
        if iSummonSID and oSummon.m_SID != iSummonSID:
            continue
        iNowCnt += 1
    
    return iNowCnt


def GetMonsterSummonCnt(oOwner, dInfo, iSummonSID):
    iNowCnt = 0
    for iSummonID in oOwner.m_MonsterSummon:
        oSummon = oOwner.m_Game.GetObject(iSummonID, PY_FLAG_DEAD)
        if not oSummon:
            continue
        if iSummonSID and oSummon.m_SID != iSummonSID:
            continue
        iNowCnt += 1
    
    return iNowCnt


def GetSceneAliveMonsterCnt(oOwner, dInfo, iMonsterSID):
    oGame = oOwner.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
    if not oScene:
        return 0
    iNowCnt = 0
    for mid in oScene.GetObjectsByType('Monster'):
        oMonster = oGame.GetObject(mid, PY_FLAG_DEAD)
        if not oMonster:
            continue
        if not iMonsterSID == 0:
            if oMonster.m_SID == iMonsterSID:
                iNowCnt += 1
                continue
    
    return iNowCnt


def GetGroupAliveMonsterCnt(oOwner, dInfo, iMonsterDataSID):
    oGame = oOwner.m_Game
    iGroup = oOwner.m_Agent.GetConfig('GroupID', -1)
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLine = oLevelCtrl.GetLineNode(oOwner.m_LineIdx)
    if not oLine:
        return 0
    lstAlive = oLine.m_MonsterCtrl.GetGroupAliveMonster(iGroup)
    iNowCnt = 0
    for iMonsterID in lstAlive:
        oMonster = oGame.GetObject(iMonsterID)
        if iMonsterDataSID and oMonster.m_DataSID != iMonsterDataSID:
            continue
        iNowCnt += 1
    
    return iNowCnt


def GetObstacleCnt(oOwner, dInfo, iObstacleSID):
    oGame = oOwner.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
    if not oScene:
        return None
    lstObstacle = oScene.GetObjectsByType('Obstacle')
    iCnt = 0
    for iObstacle in lstObstacle:
        oObstacle = oGame.GetObject(iObstacle, PY_FLAG_DEAD)
        if not oObstacle:
            continue
        if iObstacleSID and oObstacle.m_SID != iObstacleSID:
            continue
        iCnt += 1
    
    return iCnt


def GetWinkDis(oOwner, dInfo):
    oTarget = oOwner.m_Agent.GetLockEnemy()
    if not oTarget:
        return 0
    iScene = oOwner.m_Scene
    vOwner = oOwner.GetPos()
    vTarget = oTarget.GetPos()
    vEnd = oOwner.m_Game.Scene_NavMeshRayCast(iScene, vOwner, vTarget)
    return cl_math.CalDistance3D(vOwner, vEnd)


def GetWinkDisSubTargetDis(oOwner, dInfo):
    oTarget = oOwner.m_Agent.GetLockEnemy()
    if not oTarget:
        return 100
    iScene = oOwner.m_Scene
    vOwner = oOwner.GetPos()
    vTarget = oTarget.GetPos()
    vEnd = oOwner.m_Game.Scene_NavMeshRayCast(iScene, vOwner, vTarget)
    return cl_math.CalDistance3D(vEnd, vTarget)


def GetFallBackPos(oOwner, dInfo, fMinDis, fMaxDis, iMinAngle, iMaxAngle):
    oAgent = oOwner.m_Agent
    oGame = oAgent.m_Game
    oTarget = oAgent.GetLockEnemy()
    if not oTarget:
        return False
    oOwner = oAgent.m_OwnerObj
    vOwner = oOwner.GetPos()
    (ox, _, oz) = vOwner
    (tx, ty, tz) = oTarget.GetPos()
    iScene = oOwner.m_Scene
    iMinDis = int(fMinDis * CELL_SPACESIZE)
    iMaxDis = int(fMaxDis * CELL_SPACESIZE)
    iDis = oGame.Random(iMaxDis - iMinDis) + iMinDis
    fDis = iDis * CELL_REC
    for _ in range(3):
        iAngle = oGame.Random(iMaxAngle - iMinAngle) + iMinAngle
        if oGame.Random(2):
            iAngle = -iAngle
        (rx, rz) = cl_math.Vec2DestPosDir((ox, oz), (tx - ox, tz - oz), fDis, iAngle)
        vEnd = oGame.Scene_NavMeshRayCast(iScene, vOwner, (rx, ty, rz))
        if not cl_math.CheckDistance(vEnd, vOwner, fMinDis):
            oAgent.SetData('vEnd', vEnd)
            return True
    
    return False


def GetPerformRecord(oOwner, dInfo, dPerform):
    oAgent = oOwner.m_Agent
    dRecord = oAgent.GetData('PFRecord')
    if not dRecord:
        return 0
    iTotal = 0
    for iPerform in dPerform:
        iTimes = dRecord[iPerform] if iPerform in dRecord else 0
        iTotal += iTimes
    
    return iTotal


def AICheckHasState(oOwner, dInfo, iStateSID):
    if oOwner.m_State.GetItemBySID(iStateSID):
        return 1
    return 0


def AIGetRangeWarriorNum(oOwner, dInfo, iRange, iFightType, iIsExcSelf, iIsBlkStatic):
    if iFightType & WARRIOR_HERO:
        iPxMask = PXMASK_PLAYER
    elif iFightType & WARRIOR_MONSTER:
        iPxMask = PXMASK_MONSTER
    else:
        iPxMask = PXMASK_LIVEOBJ
    dMask = {
        'Mask': iPxMask }
    if not iIsBlkStatic:
        dMask['BlockMask'] = 0
    oGame = oOwner.m_Game
    lstArgs = [
        cl_math.Vec3Add(oOwner.GetPos(), (0, 0.08, 0)),
        iRange]
    lstVLST = cl_math.GetAttackTargetList(oGame, oOwner.m_Scene, ATT_SHAPE_SPHERE, lstArgs, dMask)
    iCount = 0
    for iTarget in lstVLST:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if (not oTarget or iFightType & oTarget.m_FightType != iFightType or iIsExcSelf) and oTarget is oOwner:
            continue
        iCount += 1
    
    return iCount


def JudgeAIFightLogicType(oOwner, dInfo, iType):
    if oOwner.m_Agent and oOwner.m_Agent.GetData('FightLogic', -1) == iType:
        return 1
    return 0


def JudgeEnemyInSight(oOwner, fOwnerHeightRatio, fTargetHeightRatio):
    oAgent = oOwner.m_Agent
    if not oAgent:
        return False
    oEnemy = oAgent.GetLockEnemy()
    if not oEnemy:
        return False
    vOwner = oOwner.GetPos()
    vTarget = oEnemy.GetPos()
    if cl_math.IsPlaneEqual(vOwner, vTarget):
        return True
    (x, z) = cl_math.Vec2DisplaceDir((vOwner[0], vOwner[2]), (vTarget[0] - vOwner[0], vTarget[2] - vOwner[2]), 0.5)
    vOwner = (x, vOwner[1] + oOwner.m_ModelHeight * fOwnerHeightRatio, z)
    vTarget = (vTarget[0], vTarget[1] + oEnemy.m_ModelHeight * fTargetHeightRatio, vTarget[2])
    oGame = oAgent.m_Game
    if oGame.m_WarMgr.Query('DebugRay'):
        debug.ClearDebugLine(oOwner.m_Game, debug.LINE_TILE)
        ox = float(vOwner[0])
        oy = float(vOwner[1])
        oz = float(vOwner[2])
        tx = float(vTarget[0])
        ty = float(vTarget[1])
        tz = float(vTarget[2])
        debug.DebugLine(oOwner.m_Game, ox, oy, oz, tx, ty, tz, 65280, debug.LINE_TILE)
    bSight = not oGame.Scene_RaycastAnyHit(oOwner.m_Scene, vOwner, vTarget, PXMASK_SIGHTBLK)
    return bSight


def GetRound(oOwner):
    return oOwner.m_Game.m_WarMgr.m_Round


def GetGamePlayerCnt(oOwner):
    return oOwner.m_Game.m_WarMgr.GetAllPlayerCnt()


def JudgeEnemyAccessible(oOwner):
    oAgent = oOwner.m_Agent
    if not oAgent:
        return False
    oEnemy = oAgent.GetLockEnemy()
    if not oEnemy:
        return False
    vEnemy = oEnemy.GetPos()
    fModelRadius = oEnemy.m_ModelRadius
    oGame = oOwner.m_Game
    lstVictim = oGame.Scene_SweepMultiple(oEnemy.m_Scene, vEnemy, fModelRadius, (0, -1, 0), 0.1, PXMASK_MOVEBLK, {
        'BlockMask': PXMASK_MOVEBLK })
    if not lstVictim:
        return False
    vOwner = oOwner.GetPos()
    return oGame.Scene_IsDestPosAccessible(oOwner.m_Scene, vOwner, vEnemy)


def AIGetCustomData(oOwner, iPerform, sKey):
    oPerform = oOwner.GetPerform(iPerform)
    if not oPerform:
        return 0
    return oPerform.GetArgValue(sKey)


def CheckTargetHasFlag(oOwner, sFlag):
    oAgent = oOwner.m_Agent
    if not oAgent:
        return False
    oEnemy = oAgent.GetLockEnemy()
    if not oEnemy:
        return False
    if oEnemy.Query('ForceNoDest'):
        return True
    return False


def CheckTopObstacleDis(oOwner, fDis):
    vPos = oOwner.GetCenter()
    vEnd = (vPos[0], vPos[1] + fDis, vPos[2])
    bSight = not oOwner.m_Game.Scene_RaycastAnyHit(oOwner.m_Scene, vPos, vEnd, PXMASK_SKILLBLK)
    return bSight


def AICheckSelfStateCount(oOwner, iStateSID, iCount):
    oState = oOwner.m_State.GetItemBySID(iStateSID)
    if not oState:
        return 0
    if oState.GetCount() < iCount:
        return 0
    return 1


def CheckMonsterHinderNum(oOwner, iSceneNum, iSelfNum):
    oGame = oOwner.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
    if not oScene:
        return 0
    dMonsterHinder = oScene.m_SceneData.Query('MonsterHinder', { })
    iSceneTotal = len(dMonsterHinder)
    if iSceneTotal >= iSceneNum:
        return 0
    iOwner = oOwner.m_ID
    iHinderNum = 0
    for iCreator in dMonsterHinder.values():
        if iCreator == iOwner:
            iHinderNum += 1
    
    if iHinderNum >= iSelfNum:
        return 0
    return 1


def AIConGetCustomData(oOwner, sKey):
    return oOwner.Query(sKey, 0)


def GetNoDieNum(oOwner):
    oGame = oOwner.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
    if not oScene:
        return 0
    iCnt = 0
    for iHero in oScene.GetHeros():
        oHero = oGame.GetObject(iHero, PY_FLAG_DIED)
        if not oHero:
            continue
        iCnt += 1
    
    return iCnt


def GetTargetTypeOjCnt(oOwner, sType, iTargetObjSID):
    oGame = oOwner.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
    if not oScene:
        return 0
    lstObstacle = oScene.GetObjectsByType(sType)
    iCnt = 0
    for iObj in lstObstacle:
        oObj = oGame.GetObject(iObj, PY_FLAG_DEAD)
        if not oObj:
            continue
        if iTargetObjSID and oObj.m_SID != iTargetObjSID:
            continue
        iCnt += 1
    
    return iCnt

