# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/monsteragent.pyc
# RelativePath: clientlogic/cl_betree/monsteragent.pyc
# Source Generated with Decompyle++
# File: monsteragent.pyc (Python 3.6)

from cl_only import GAME_FRAME_SECOND, ShufferList, PY_FLAG_DIED, PY_FLAG_DEAD, GAME_FRAME, Time2Frame, Functor, ChooseKey, CELL_REC, CELL_SPACESIZE, HALF_GAME_FRAME, OutputPos, PY_FLAG_MONSTERTARGET, PY_FLAG_DYING, PY_FLAG_EXCLUDEHATE, Frame2Time, ChooseRange
from cl_betree.mobject import CAgent as CBaseAgent
from cl_betree.mobject import EVENT_SCENE, EVENT_SELF
from cl_behavior.defines import status, BT_RUNNING, BT_FAILURE, BT_SUCCESS
from cl_pxlayer import PXMASK_SIGHTBLK, PXMASK_MONSTER, PXMASK_MOVEBLK, PXMASK_OBJECT, PXMASK_MOVEBLK, PXMASK_BLOCK, PXMASK_GROUNDBLK
from cl_commondefines import STATUS_PATROL, STATUS_SPRINT, STATUS_RUN, STATE_TIME_LIMIT, STATE_GUARD_ACT, SIDE_TYPE_VERTIGO, MONSTER_STATUS_ATTACK, PF_TYPE_MONSTERACT, PATHMODE_GHOST, CBEHAVIOR_MONSTER_TURNEND, CBEHAVIOR_MONSTER_TURNSTART, WARRIOR_MONSTER, FACE_STATUS_DIR, FACE_STATUS_CROSSPATH, FACE_STATUS_PATH, FACE_STATUS_TARGET, MONSTER_STATUS_DEFAULT, FORBID_MOVE, PF_TYPE_THROW, MOVE_TYPE_FLY, MOVE_TYPE_NORMAL, CBEHAVIOR_MONSTER_WARN, STATE_TIME_FOREVER, STATE_UNDER_ATTACK, PF_SUBMSG_CAREERPF, PF_SUBMSG_THROW, FIGHT_LOGIC_OVERALLAWAIT, FIGHT_LOGIC_OVERALLGUERRILLA, FIGHT_LOGIC_OVERALLCHARGE, FIGHT_LOGIC_CHARGE, FIGHT_LOGIC_DEFAULT, MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, WARRIOR_HERO, PF_TYPE_CAREERPF, ATT_SHAPE_SPHERE, WARRIOR_SERVANT, PF_SUBMSG_SERVANT, WARRIOR_DEVICE, WARRIOR_PET, PET_TYPE_SHIELD, SIDE_TYPE_HERO, MONSTERAI_TYPE_AREAMOVE, PF_TYPE_ATIVE, MONSTERAGENT_FLAG_NOCOMBAUSEPF, DEFEND_TREND_SHIELD, DEFEND_TREND_ARMOR, TOSHOWPOS_STATE, FLYINGKNIGHT_DROP_BOMB
from cl_object.logging import BehaviorLog
import enum
import cl_math
import cl_war
import cl_msgcenter
import cl_state
import cl_object.reason
import cl_snetwar
import cl_action
import cl_betree.pfai
import cl_betree.fuzzy
import cl_gamedebug as debug
import cl_movectrl.net as movenet
import cl_behavior
import cl_forbid
import cl_platformdata
import cllib.lib_flag as lib_flag
MONSTER_HATE_FIGHTTYPE = WARRIOR_SERVANT | WARRIOR_HERO | WARRIOR_PET

def ValidSceneAttention(oAgent, oTarget):
    if oAgent.m_OwnerObj.m_Side == oTarget.m_Side:
        return False
    if not oAgent.CheckInAttentionArea(oTarget):
        return False
    return True


def JumpCheckVal(oOwner, dMsgInfo):
    oAgent = oOwner.m_Agent
    iTarget = dMsgInfo['Target']
    oTarget = oOwner.m_Game.GetObject(iTarget, oAgent.m_CheckExcludeFlag)
    if not oTarget:
        return None
    if not ValidSceneAttention(oAgent, oTarget):
        return None
    oAgent.SetActCheckVal(iTarget, 500, 300, 0)


def ThrowCheckVal(oOwner, dMsgInfo):
    oSkill = dMsgInfo['Skill']
    if oSkill.m_Base['PFType'] != PF_TYPE_THROW:
        return None
    oAgent = oOwner.m_Agent
    iTarget = oSkill.m_Base['AID']
    oTarget = oOwner.m_Game.GetObject(iTarget, oAgent.m_CheckExcludeFlag)
    if not oTarget:
        return None
    if not ValidSceneAttention(oAgent, oTarget):
        return None
    oAgent.SetActCheckVal(iTarget, 600, 400, 0)


def CareerPerformCheckVal(oOwner, dMsgInfo):
    oSkill = dMsgInfo['Skill']
    if oSkill.m_Base['PFType'] != PF_TYPE_CAREERPF:
        return None
    oAgent = oOwner.m_Agent
    iTarget = oSkill.m_Base['AID']
    oTarget = oOwner.m_Game.GetObject(iTarget, oAgent.m_CheckExcludeFlag)
    if not oTarget:
        return None
    if not ValidSceneAttention(oAgent, oTarget):
        return None
    oAgent.SetActCheckVal(iTarget, 600, 400, 0)


def AttCheckVal(oOwner, dMsgInfo):
    oAgent = oOwner.m_Agent
    oSkill = dMsgInfo['Skill']
    iTarget = oSkill.m_Base['AID']
    lstPos = oSkill.m_Collect.get('CartoonPos', [])
    if not lstPos:
        return None
    oTarget = oOwner.m_Game.GetObject(iTarget, oAgent.m_CheckExcludeFlag)
    if not oTarget:
        return None
    for _vStart, vEnd in lstPos:
        if oAgent.InShootNear(iTarget, vEnd):
            oAgent.SetActCheckVal(iTarget, 800, 600, 400)
            break
        if ValidSceneAttention(oAgent, oTarget):
            oAgent.SetActCheckVal(iTarget, 600, 400, 0)
            break
    


def DamCheckVal(oOwner, dMsgInfo):
    iTarget = dMsgInfo['AID']
    oTarget = oOwner.m_Game.GetObject(iTarget, PY_FLAG_MONSTERTARGET)
    if not oTarget:
        return None
    oAgent = oOwner.m_Agent
    if oTarget.m_FightType & MONSTER_HATE_FIGHTTYPE:
        oAgent.SetActCheckVal(iTarget, 1000, 1000, 1000)
    elif oTarget.m_FightType & WARRIOR_DEVICE:
        oAgent.SetActCheckVal(oTarget.m_Owner, 1000, 1000, 1000)


def AttDodgeVal(oOwner, dMsgInfo):
    oAgent = oOwner.m_Agent
    oSkill = dMsgInfo['Skill']
    iTarget = oSkill.m_Base['AID']
    lstPos = oSkill.m_Collect.get('CartoonPos', [])
    if not lstPos:
        return None
    for _vStart, vEnd in lstPos:
        if oAgent.InShootNear(iTarget, vEnd):
            iCurFrame = oAgent.m_Game.GetFrameNum()
            oAgent.SetData('DodgeLastAtt', (iTarget, iCurFrame))
            break
    


def DamDodgeVal(oOwner, dMsgInfo):
    oTarget = oOwner.m_Game.GetObject(dMsgInfo['AID'], PY_FLAG_DEAD)
    if not oTarget or not (oTarget.m_FightType & MONSTER_HATE_FIGHTTYPE):
        return None
    oAgent = oOwner.m_Agent
    iCurFrame = oAgent.m_Game.GetFrameNum()
    oAgent.SetData('DodgeLastAtt', (oTarget.m_ID, iCurFrame))


def DamBlinkVal(oOwner, dMsgInfo):
    oTarget = oOwner.m_Game.GetObject(dMsgInfo['AID'])
    if not oTarget or not (oTarget.m_FightType & MONSTER_HATE_FIGHTTYPE):
        return None
    oAgent = oOwner.m_Agent
    iCurFrame = oAgent.m_Game.GetFrameNum()
    if not oAgent.GetData('BlinkAtt', 0):
        oAgent.SetData('BlinkAtt', iCurFrame)


def DamHateVal(oOwner, dMsgInfo):
    iTarget = dMsgInfo['AID']
    oTarget = oOwner.m_Game.GetObject(iTarget, PY_FLAG_MONSTERTARGET)
    if not oTarget or not (oTarget.m_FightType & MONSTER_HATE_FIGHTTYPE):
        return None
    iAllDam = sum(dMsgInfo['TotalDam'])
    iAllDam = iAllDam * oTarget.m_HateFactor
    oAgent = oOwner.m_Agent
    dHateData = oAgent.GetData('HateData', { })
    iCurFrame = oAgent.m_Game.GetFrameNum()
    if iTarget not in dHateData:
        dHateData[iTarget] = {
            'Dam': { },
            'Hate': [
                0,
                iCurFrame],
            'Immutable': 0 }
    if iCurFrame not in dHateData[iTarget]['Dam']:
        dHateData[iTarget]['Dam'][iCurFrame] = 0
    dHateData[iTarget]['Dam'][iCurFrame] += iAllDam
    oAgent.SetData('HateData', dHateData)


def GroupHateVal(oOwner, dMsgInfo):
    oAgent = oOwner.m_Agent
    iAIState = oAgent.GetData('AIState', 0)
    if iAIState not in (1, 2):
        return None
    iTargetGroup = dMsgInfo['Group']
    iGroup = oAgent.GetConfig('GroupID', -1)
    if iGroup == -1 or iTargetGroup != iGroup:
        return None
    iDelayTime = oAgent.GetConfig('GroupHateDelay', 0)
    lstTarget = dMsgInfo['Target']
    if iDelayTime:
        if oAgent.Find_Call_Out('GroupHateDelay'):
            return None
        oAgent.Call_Out(Functor(DelayGroupHate, oOwner, lstTarget), Time2Frame(iDelayTime), 'GroupHateDelay')
    else:
        DelayGroupHate(oOwner, lstTarget)


def DelayGroupHate(oOwner, lstTarget):
    if oOwner.IsDead():
        return None
    oAgent = oOwner.m_Agent
    iAIState = oAgent.GetData('AIState', 0)
    if iAIState not in (1, 2):
        return None
    oGame = oOwner.m_Game
    (iNearestTarget, fMinDis) = (0, 500)
    dDis = oAgent.GetSceneEnemyDis(iOnlyHero = 0)
    for iTarget, fDis in dDis.items():
        if iTarget not in lstTarget:
            continue
        if fDis >= fMinDis:
            continue
        oTarget = oGame.GetObject(iTarget, PY_FLAG_MONSTERTARGET)
        if not oTarget:
            continue
        iNearestTarget = iTarget
        fMinDis = fDis
    
    if iNearestTarget:
        oAgent.SetActCheckVal(iNearestTarget, 1000, 1000, 1000)


def ServantPerformCheckVal(oOwner, dMsgInfo):
    oSkill = dMsgInfo['Skill']
    oAttack = oSkill.GetAttack()
    if not oAttack or not (oAttack.m_FightType & WARRIOR_SERVANT):
        return None
    oGame = oOwner.m_Game
    oAgent = oOwner.m_Agent
    iTarget = oAttack.m_ID
    oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
    if not oScene or iTarget not in oScene.m_MonsterEnemy:
        return None
    oTarget = oGame.GetObject(iTarget, oAgent.m_CheckExcludeFlag)
    if not oTarget:
        return None
    if not ValidSceneAttention(oAgent, oTarget):
        return None
    oAgent.SetActCheckVal(iTarget, 600, 400, 0)


def KnockedBack(oOwner, iDelayFrame):
    oAgent = oOwner.m_Agent
    if not oAgent:
        return None
    sKey = 'Struck'
    oOwner.Set(sKey, (iDelayFrame + oOwner.m_Game.GetFrameNum(), oOwner.QueryAttr('StruckIgnoreFrame')))
    oAgent.PauseAgent(sKey)
    oAgent.StopMoving(oAgent)
    oAgent.HaltPerform(oAgent)
    oAgent.ResetSquat()
    oAgent.Remove_Call_Out(sKey)
    oAgent.Call_Out(Functor(StruckEnd, oAgent, sKey), iDelayFrame, sKey)


def Struck(oOwner, sKey, iDelayFrame):
    oAgent = oOwner.m_Agent
    if not oAgent:
        return None
    oAgent.PauseAgent(sKey)
    oAgent.StopMoving(oAgent)
    oAgent.HaltPerform(oAgent)
    oAgent.ResetSquat()
    oAgent.Remove_Call_Out(sKey)
    oAgent.Call_Out(Functor(StruckEnd, oAgent, sKey), iDelayFrame, sKey)


def StruckEnd(oAgent, sKey):
    oAgent.Remove_Call_Out(sKey)
    oOwner = oAgent.m_OwnerObj
    if not oOwner.IsDead():
        oAgent.ResumeAgent(sKey)
        oAgent.ResumeFaceStatus()
        oAgent.BTExec()


def StruckChangeSpeed(oOwner, sOldKey, dFrameShaft):
    if not oOwner.m_Agent:
        return None
    iCurFrame = oOwner.m_Game.GetFrameNum()
    sKey = 'Struck'
    (iCallFrame, iStruckIgnoreFrame) = oOwner.Query(sKey, (0, 0))
    iCallFrame -= iStruckIgnoreFrame
    if iCallFrame <= iCurFrame:
        return None
    iNewFrame = oOwner.GetDelayFrameOnChangeSpeed(iCallFrame, sOldKey, dFrameShaft)
    oOwner.Set(sKey, (iCurFrame + iNewFrame + iStruckIgnoreFrame, iStruckIgnoreFrame))
    oAgent = oOwner.m_Agent
    oAgent.Remove_Call_Out(sKey)
    oAgent.Call_Out(Functor(StruckEnd, oAgent, sKey), iNewFrame, sKey)


def Unbalance(oOwner):
    oAgent = oOwner.m_Agent
    if not oAgent:
        return None
    oAgent.StopMoving(oAgent)
    oAgent.HaltPerform(oAgent)


def ClearPlayerHate(oOwner, oTarget, dInfo):
    if not (oTarget.m_FightType & MONSTER_HATE_FIGHTTYPE) or oOwner.IsDead() or dInfo.get('NewScene', 0) == oOwner.m_Scene:
        return None
    oAgent = oOwner.m_Agent
    iTarget = oTarget.m_ID
    dHateData = oAgent.GetData('HateData', { })
    dAllCheckVal = oAgent.GetData('ActCheckVal', { })
    if iTarget in dHateData:
        dHateData.pop(iTarget)
    if iTarget in dAllCheckVal:
        dAllCheckVal.pop(iTarget)
    oAgent.GetLockEnemy()


def OnDieAtAgent(oOwner, dInfo):
    oGame = oOwner.m_Game
    oAgent = oOwner.m_Agent
    if not oAgent:
        return None
    oAgent.ReleaseChosenPos()
    oSurvivorElement = oGame.m_WarMgr.GetComponent('SurvivorElement')
    if not oSurvivorElement:
        return None
    (iTarget, iAttackCost) = oAgent.GetData('AttackCost', (0, 0))
    if not iTarget:
        return None
    oSurvivorElement.AddTokenCost(iTarget, -iAttackCost)


def AddPetActCheckVal(oOwner):
    oAgent = oOwner.m_Agent
    oGame = oAgent.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
    if not oScene:
        return None
    lstPet = oScene.GetObjectsByType('Pet')
    if not lstPet:
        return None
    dCheckVal = oAgent.SetDefaultData('ActCheckVal', { })
    dWeight = {
        300: 10,
        500: 10,
        800: 10,
        1000: 10,
        1500: 20 }
    for iPet in lstPet:
        oPet = oGame.GetObject(iPet, PY_FLAG_DEAD)
        if not oPet:
            continue
        if oPet.m_PetType != PET_TYPE_SHIELD:
            continue
        if iPet not in dCheckVal:
            iVal = ChooseKey(oGame, dWeight)
            dCheckVal[iPet] = [
                iVal,
                0]
    


def ConfigFuncGetLockTargetDis(oAgent):
    return CAgent.GetLockTargetDis(oAgent)


def ConfigFuncGetIntervalTime(oAgent):
    oOwner = oAgent.m_OwnerObj
    return oOwner.QueryAttr('IntervalTime')


def MoveToLockEnemyEnd(oAgent, iStatus):
    oAgent.SetData('LastFollowTar', 0)


def StopMoveToLockEnemyCBFunc(oOwner, vTar, iFail):
    if not iFail and not oOwner.IsDead():
        oAgent = oOwner.m_Agent
        oAgent.SetData('LastFollowTar', 0)
        oAgent.BTExec()


def MoveToFlyLockEnemyEnd(oAgent, iStatus):
    oAgent.SetData('LastFollowTar', 0)


def StopMoveToFlyLockEnemyCBFunc(oOwner, vTar, iFail):
    if not iFail and not oOwner.IsDead():
        oAgent = oOwner.m_Agent
        oAgent.SetData('LastFollowTar', 0)
        oAgent.BTExec()


def MoveToPosEnd(oAgent, iStatus):
    oAgent.SetData('LastArrIdx', 0)
    oAgent.ReleaseChosenPos()
    if iStatus == BT_SUCCESS:
        oAgent.m_GameSpace.CallDelayUpdate(oAgent, 1)


def MoveToPosEndCB(oOwner, _tPos, iFail):
    if not iFail:
        oOwner.m_Agent.BTExec()


def FlyToPosEnd(oAgent, iStatus):
    oAgent.SetData('LastArrIdx', 0)


def FlyToPosEndCB(oOwner, _tPos, iFail):
    if not iFail:
        oOwner.m_Agent.BTExec()


def KeepMovingEnd(oAgent, iStatus):
    oAgent.Stop()
    oAgent.SetData('StartingPoint', ())
    oAgent.Remove_Call_Out('KeepMoving')


def KeepMoving(oAgent, fRadius):
    oOwner = oAgent.m_OwnerObj
    vCurTarget = oAgent.GetData('ArrivePos')
    vCurOwner = oOwner.GetPos()
    if not vCurTarget or cl_math.CheckDistance(vCurOwner, vCurTarget, 0.5):
        vCenter = oAgent.GetData('StartingPoint')
        oGame = oAgent.m_Game
        fFarthestDis = 0
        vNewTarget = None
        for i in range(3):
            vDir = (1, 0, 0) if oGame.Random(2) else (-1, 0, 0)
            vPos = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vCenter, vDir, 1, fRadius, 1, 179)
            if not vPos:
                continue
            if vPos and not vCurTarget:
                vNewTarget = vPos
                break
            fDis = cl_math.CalDistance(vPos, vCurTarget)
            if fDis > 2.5:
                vNewTarget = vPos
                break
            if fDis > fFarthestDis:
                fFarthestDis = fDis
                vNewTarget = vPos
        
        if vNewTarget:
            oAgent.SetData('ArrivePos', vNewTarget)
            oAgent.SeekPath(oOwner, vNewTarget)
    if not oAgent.Find_Call_Out('KeepMoving'):
        oAgent.Call_Out(Functor(KeepMoving, oAgent, fRadius), 8, 'KeepMoving')


def ClearTurnToLockEnemyEndFrame(oAgent, iStatus):
    oAgent.SetData('FaceEnemyEnd', 0)


def KeepTurning(oAgent, iLimitAngle):
    oAgent.Remove_Call_Out('KeepTurning')
    oOwner = oAgent.m_OwnerObj
    oGame = oAgent.m_Game
    if not oAgent.IsActive():
        return BT_FAILURE
    vTarget = oAgent.GetData('ArrivePos')
    if not vTarget:
        return BT_FAILURE
    iStartFrame = oAgent.GetData('TurningStart', 0)
    iCurFrame = oAgent.m_Game.GetFrameNum()
    if iStartFrame or iStartFrame + GAME_FRAME * 5 < iCurFrame:
        return BT_SUCCESS
    oAgent.SetData('TurningStart', iCurFrame)
    vFacing = oOwner.GetFacing()
    vCur = oOwner.GetPos()
    vDir = cl_math.Vec3Minus(vTarget, vCur)
    iAngle = cl_math.CalAngle2D(vFacing, vDir) if vDir[0] or vDir[2] else 0
    if iAngle <= 30:
        oAgent.m_GameSpace.CallDelayUpdate(oAgent, 1)
        return BT_SUCCESS
    vPreDir = oOwner.GetFacing()
    vNewDir = vPreDir
    iAngle = cl_math.CalAngle3D(vPreDir, vDir)
    if iAngle:
        iAngle = min(iLimitAngle // GAME_FRAME, iAngle)
        tAxis = cl_math.Vec3Normalize(cl_math.VectorCross3D(vPreDir, vDir))
        vNewDir = cl_math.Vec3Normalize(cl_math.RotateAroundVector(vPreDir, tAxis, iAngle))
    fStepDis = oOwner.QueryAttr('MoveSpeed') * GAME_FRAME_SECOND
    vTar = cl_math.Vec3Mad(vCur, vNewDir, fStepDis)
    vTar = oAgent.m_Game.Scene_NavMeshRayCast(oOwner.m_Scene, vCur, vTar)
    if oAgent.m_Game.GetWarMgr().Query('DebugRay'):
        (ox, oy, oz) = vCur
        (tx, ty, tz) = vTar
        debug.DebugLine(oAgent.m_Game, ox, oy, oz, tx, ty, tz, 65280, debug.LINE_TILE)
    oOwner.m_FaceCtrl.OnNextPath(oOwner, vNewDir[0], vNewDir[2])
    oCtrl = oOwner.m_MoveCtrl
    oOwner.m_Game.Scene_Walk(oOwner.m_ID, vTar)
    vNow = oOwner.RefreshPos()
    oCtrl.m_MoveFrame += 1
    movenet.GS2CMapTrack(oOwner, [
        vCur,
        vNow])
    movenet.GS2CMapTickPos(oOwner, oCtrl.m_MoveFrame, vNow)
    oAgent.Call_Out(Functor(KeepTurning, oAgent, iLimitAngle), 1, 'KeepTurning')
    lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
    cl_snetwar.GS2CTriggerBehavior(oGame, oOwner.m_ID, CBEHAVIOR_MONSTER_TURNSTART, lstPlayer)
    return BT_RUNNING


def TurningEndFunc(oAgent, iStatus):
    oGame = oAgent.m_Game
    oOwner = oAgent.m_OwnerObj
    lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
    cl_snetwar.GS2CTriggerBehavior(oGame, oOwner.m_ID, CBEHAVIOR_MONSTER_TURNEND, lstPlayer)
    oAgent.Stop()
    oAgent.SetData('TurningStart', 0)
    oOwner.m_MoveCtrl.ClearPathMode('TurningMove')
    oAgent.Remove_Call_Out('KeepTurning')


def PathMoveEnd(oAgent, iStatus):
    oAgent.Stop()
    oAgent.SetData('LastArrIdx', 0)


def PathMoveEndCB(oOwner, _tPos, iFail):
    oAgent = oOwner.m_Agent
    oAgent.SetData('LastArrIdx', -1)
    oOwner.m_Agent.BTExec()


def AbsoluteArcMoveEnd(oAgent, iStatus):
    oAgent.Stop()
    oAgent.SetData('LastArrIdx', 0)
    oAgent.SetData('ArrivePath', None)
    oAgent.SetData('StopFrame', 0)
    if oAgent.m_Game.GetWarMgr().Query('DebugRay'):
        vOwner = oAgent.m_OwnerObj.GetPos()
        debug.ClearDebugLine(oAgent.m_Game, debug.LINE_NORMAL)
        debug.DebugCircle(oAgent.m_Game, vOwner, 10, debug.LINE_NORMAL)


def AbsoluteArcMoveEndCB(oOwner, _tPos, iFail):
    oAgent = oOwner.m_Agent
    oAgent.SetData('LastArrIdx', -1)
    oAgent.SetData('ArrivePath', None)
    oAgent.SetData('StopFrame', 0)
    oOwner.m_Agent.BTExec()


def ArcMoveEnd(oAgent, iStatus):
    oAgent.Stop()
    oAgent.SetData('LastArrIdx', 0)
    oAgent.SetData('ArrivePath', None)
    oAgent.SetData('StopFrame', 0)
    oAgent.SetData('ClockWise', 0)
    if oAgent.m_Game.GetWarMgr().Query('DebugRay'):
        vOwner = oAgent.m_OwnerObj.GetPos()
        debug.ClearDebugLine(oAgent.m_Game, debug.LINE_NORMAL)
        debug.DebugCircle(oAgent.m_Game, vOwner, 10, debug.LINE_NORMAL)


def ArcMoveEndCB(oOwner, _tPos, iFail):
    oAgent = oOwner.m_Agent
    oAgent.SetData('LastArrIdx', -1)
    oAgent.SetData('ArrivePath', None)
    oAgent.SetData('StopFrame', 0)
    oAgent.SetData('ClockWise', 0)
    oOwner.m_Agent.BTExec()


def UsePerformGroupEnd(oAgent, iStatus):
    oAgent.Remove_Call_Out('DelayUsePFGroup')
    oAgent.SetData('PFUsed', 0)
    oAgent.SetData('PFTotal', 0)
    oAgent.SetData('NextPFFrame', 0)
    oAgent.SetData('CurPFGroup', { })


def SkillCastingEndFunc(oOwner, iPerform, oSkill):
    iBackSwingFrame = oOwner.GetBackSwingRemainingFrame(iPerform)
    iDelayUpdateFrame = iBackSwingFrame + 1
    oAgent = oOwner.m_Agent
    oAgent.m_GameSpace.CallDelayUpdate(oAgent, iDelayUpdateFrame)


def ClearBornActionEndFrame(oAgent, iStatus):
    oAgent.m_OwnerObj.m_BornActionEndFrame = 0


def ClearOwnerMarkEndFunc(oAgent, iStatus):
    if iStatus == BT_FAILURE:
        oOwner = oAgent.m_OwnerObj
        iMonsterOwner = oOwner.m_Owner
        oMonsterOwner = oAgent.m_Game.GetObject(iMonsterOwner)
        if oMonsterOwner:
            dMarkTarget = oMonsterOwner.Query('MarkTarget', { })
            dMarkTarget[oOwner.m_ID] = 0
            oMonsterOwner.Set('MarkTarget', dMarkTarget)


def ChooseZigFlyNextPos(oAgent, vEnd, fIntervalDis, iShiftAngle, fMinHigh, fMaxHigh):
    oOwner = oAgent.m_OwnerObj
    oGame = oOwner.m_Game
    vStart = oOwner.GetPos()
    fDistance = cl_math.CalDistance3D(vStart, vEnd)
    iScene = oOwner.m_Scene
    if fDistance <= fIntervalDis:
        vNextPos = vEnd
    else:
        fHighDiff = max(20, fMaxHigh - fMinHigh)
        (_, fDownY, _) = oGame.Scene_FlyRayCast(iScene, vStart, cl_math.Vec3Add(vStart, [
            0,
            -fHighDiff,
            0]))
        (_, fUpY, _) = oGame.Scene_FlyRayCast(iScene, vStart, cl_math.Vec3Add(vStart, [
            0,
            fHighDiff,
            0]))
        fMinHigh = min(fDownY + fMinHigh, fUpY)
        fMaxHigh = min(fDownY + fMaxHigh, fUpY)
        vLastPos = oAgent.GetData('ArrivePos')
        if vLastPos:
            fMid = (fMinHigh + fMaxHigh) / 2
            if vLastPos[1] < fMid:
                fMinHigh = fMid
            else:
                fMaxHigh = fMid
        vDir = cl_math.Vec3Minus(vEnd, vStart)
        iShiftAngle = -iShiftAngle + oGame.Random(iShiftAngle * 2)
        (x, z) = cl_math.Vec2DestPosDir([
            vStart[0],
            vStart[2]], [
            vDir[0],
            vDir[2]], fIntervalDis, iShiftAngle)
        y = ChooseRange(oGame, int(fMinHigh * 100), int(fMaxHigh * 100)) / 100
        vNextPos = (x, y, z)
    (iRet, vNextPos) = oGame.Scene_FlyGetSpace(iScene, vNextPos)
    if not iRet:
        return None
    lstPath = oGame.Scene_FlyNavFindPath(iScene, vStart, vNextPos)
    if not lstPath:
        return None
    return vNextPos


def KeepZigFlying(oAgent, iTarget, fCatchDis, fIntervalDis, iShiftAngle, fMinHigh, fMaxHigh):
    
    def ZigFlyingCB(_oOwner, tPos, iFail):
        _oAgent = _oOwner.m_Agent
        KeepZigFlying(_oAgent, iTarget, fCatchDis, fIntervalDis, iShiftAngle, fMinHigh, fMaxHigh)

    oAgent.SetData('ZigFlyTarget', 0)
    oOwner = oAgent.m_OwnerObj
    oTarget = oOwner.m_Game.GetObject(iTarget)
    if not oTarget:
        return BT_FAILURE
    vTarget = oTarget.GetPos()
    fDistance = cl_math.CalDistance3D(oOwner.GetPos(), vTarget)
    if fDistance <= fCatchDis:
        return BT_SUCCESS
    vNextZigPos = None
    for _ in range(3):
        vNextZigPos = ChooseZigFlyNextPos(oAgent, oTarget.GetPos(), fIntervalDis, iShiftAngle, fMinHigh, fMaxHigh)
        if vNextZigPos:
            break
    
    if not vNextZigPos:
        if oAgent.FlyFollowMove(oOwner, iTarget, fCatchDis, fHeight = 0, func = ZigFlyingCB):
            return BT_RUNNING
        return BT_FAILURE
    if oAgent.SeekPath(oOwner, vNextZigPos, ZigFlyingCB):
        oAgent.SetData('ArrivePos', vNextZigPos)
        oAgent.SetData('ZigFlyTarget', iTarget)
        return BT_RUNNING
    return BT_FAILURE


def ZigFlyToLockTargetEnd(oAgent, iStatus):
    oAgent.SetData('ZigFlyTarget', 0)
    oAgent.SetData('ArrivePos', ())


class ChoosePFType(enum.Enum):
    tType1 = ('追击技能组', MONSTER_PFAI_CATCH)
    tType2 = ('躲避技能组', MONSTER_PFAI_DODGE)


class ActionSMArgType(enum.Enum):
    tType1 = ('Trigger', 1)
    tType2 = ('Bool', 2)
    tType3 = ('Float', 3)


class FightLogicType(enum.Enum):
    tType1 = ('默认', FIGHT_LOGIC_DEFAULT)
    tType2 = ('追击', FIGHT_LOGIC_CHARGE)
    tType3 = ('全局追击', FIGHT_LOGIC_OVERALLCHARGE)
    tType4 = ('全局游击', FIGHT_LOGIC_OVERALLGUERRILLA)
    tType5 = ('全局待机', FIGHT_LOGIC_OVERALLAWAIT)


class SpeedUpType(enum.Enum):
    tType1 = ('无', 0)
    tType2 = ('四方向', 1)
    tType3 = ('冲刺', 2)


class HPType(enum.Enum):
    tType1 = ('血量', 'HP')
    tType2 = ('护甲', 'Armor')
    tType3 = ('护盾', 'Shield')


class PosChooseType(enum.Enum):
    tType1 = ('随机', 0)
    tType2 = ('离仇恨目标最远的点', 1)
    tType3 = ('恢复技能区域点', 2)
    tType4 = ('强化技能区域点', 3)


class SkillShotType(enum.Enum):
    tType1 = ('无距离', 0)
    tType2 = ('近距离', 1)
    tType3 = ('中距离', 2)
    tType4 = ('远距离', 3)


class PyFlag(enum.Enum):
    tType1 = ('死亡', PY_FLAG_DIED)
    tType2 = ('濒死', PY_FLAG_DYING)
    tType3 = ('死亡与濒死', PY_FLAG_DEAD)
    tType4 = ('不纳入仇恨目标', PY_FLAG_EXCLUDEHATE)
    tType5 = ('不纳入怪物仇恨目标', PY_FLAG_MONSTERTARGET)


class CAgent(CBaseAgent):
    m_EventKey = { }
    m_ConfigKey = {
        '巡逻路径': 'PatrolPos',
        '巡逻面向': 'PatrolFace',
        '是否游击期间攻击': 'GuerrillaAttack',
        '游击间隔': 'GuerrillaInterval',
        '模糊攻击间隔': 'FuzzyInterval',
        '远程位置半径': 'RangedPosR',
        '远程位置最小距离': 'RangedPosMinDis',
        '远程位置最大距离': 'RangedPosMaxDis',
        '远程位置最小角度': 'RangedPosMinAngle',
        '远程位置最大角度': 'RangedPosMaxAngle',
        '掩护躲藏时间': 'CoverTime',
        '掩护攻击停顿时间': 'CoverAttackStandingTime',
        '掩体抽取半径': 'HideR',
        '掩体躲藏时间': 'HideTime',
        '掩体攻击停顿时间': 'HideAttackStandingTime',
        '是否播放追击动作': 'ShowCatchAni',
        '仇恨目标当前距离': 'LockTargetDis',
        '重算间隔': 'IntervalTime',
        '最远作战距离': 'FightMaxDis',
        '最近作战距离': 'FightMinDis',
        '待机巡逻移动半径': 'WaitPatrolRadius',
        '出场方式': 'ShowWay' }
    m_Time2FrameConfig = {
        'GuardTime': 1,
        'GuerrillaInterval': 1,
        'FuzzyInterval': 1,
        'CoverTime': 1,
        'CoverAttackStandingTime': 1,
        'HideTime': 1,
        'HideAttackStandingTime': 1 }
    m_DataKey = {
        '当前技能使用范围': 'CurPerformUseDis',
        '标记': 'Flag' }
    m_CacheKey = { }
    m_AgentEventKey = {
        '受伤侦察事件': (cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, EVENT_SELF, DamCheckVal, '伤害侦察'),
        '投掷技能侦察事件': (cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, EVENT_SCENE, ThrowCheckVal, '投掷技能侦察'),
        '职业技能侦察事件': (cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, EVENT_SCENE, CareerPerformCheckVal, '职业技能侦察'),
        '开枪侦察事件': (cl_msgcenter.MSG_WAR_ATTACK_END, -1, EVENT_SCENE, AttCheckVal, '开枪侦察'),
        '跳跃侦察事件': (cl_msgcenter.MSG_CMD_JUMP, -1, EVENT_SCENE, JumpCheckVal, '跳跃侦察'),
        '开枪闪避事件': (cl_msgcenter.MSG_WAR_ATTACK_END, -1, EVENT_SCENE, AttDodgeVal, '开枪闪避'),
        '受伤闪避事件': (cl_msgcenter.MSG_WAR_ATTACKED, -1, EVENT_SELF, DamDodgeVal, '受伤闪避'),
        '受伤瞬移事件': (cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, EVENT_SELF, DamBlinkVal, '受伤瞬移'),
        '受伤仇恨事件': (cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, EVENT_SELF, DamHateVal, '伤害仇恨'),
        '小队仇恨侦察事件': (cl_msgcenter.MSG_WAR_GROUPHATE, -1, EVENT_SCENE, GroupHateVal, '小队仇恨'),
        '仆从技能侦察事件': (cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_SERVANT, EVENT_SCENE, ServantPerformCheckVal, '仆从技能侦察') }
    m_IgnoreNotify = {
        'SceneAttentionArea': 1,
        'RangedAreaGroup': 1,
        'BroadcastCatch': 1,
        'DodgeMaxTimes': 1,
        'DodgeCD': 1,
        'MonsterNo': 1,
        'GroupID': 1,
        'UseGroupHate': 1,
        'ShowWarning': 1,
        'ChooseNewArea': 1,
        'GroupHateDelay': 1,
        'ShowCatchAni': 1,
        'BackToBornPos': 1,
        'ShowPosID': [
            1],
        'PatrolPos': 1,
        'PatrolFace': 1,
        'SummonAreaGroup': 1,
        'ShowPos': 1,
        'ShowWay': 1,
        'AIMethod': 1 }
    m_DefaultConfig = {
        'GuardTime': 120,
        'ViewR': 30,
        'ViewAngle': 75,
        'GuardDis': 30,
        'SearchDis': 30,
        'NearDis': 2,
        'BroadcastCatch': 0,
        'DodgeMaxTimes': 3,
        'DodgeCD': 300,
        'RangedPosR': 10,
        'GuerrillaInterval': 300,
        'GuerrillaAttack': 1,
        'GuerrillaProb': 100,
        'RangedPosMinDis': 3,
        'RangedPosMaxDis': 5,
        'RangedPosMinAngle': 75,
        'RangedPosMaxAngle': 90,
        'CoverDis': 10,
        'GuardianNo': 0,
        'CoverTime': 100,
        'CoverAttackStandingTime': 100,
        'HideR': 15,
        'HideTime': 100,
        'HideAttackStandingTime': 50,
        'ShowWay': 0 }
    m_GetWhileRunConfig = {
        'LockTargetDis': ConfigFuncGetLockTargetDis,
        'IntervalTime': ConfigFuncGetIntervalTime }
    m_CheckExcludeFlag = PY_FLAG_DEAD
    m_FollowMoveExcludeFlag = PY_FLAG_DEAD
    
    def __init__(self):
        super(CAgent, self).__init__()
        self.m_PFAI = None
        self.m_SentAlert = { }
        self.m_CurPerformUseHeight = 0
        self.m_CatchStartFrame = 0

    
    def Config(self, oOwner, dConfig):
        super(CAgent, self).Config(oOwner, dConfig)
        if 'PFAI' in dConfig:
            self.m_PFAI = cl_betree.pfai.NewPFAI(dConfig['PFAI'], oOwner)
        self.InitDodgeInfo()
        self.m_Game.AddGlobalAttention(self.m_OwnerObj.m_ID, cl_msgcenter.MSG_WAR_LEAVESCENE, ClearPlayerHate, 'ClearHate', iSub = SIDE_TYPE_HERO)
        self.m_Game.AddGlobalAttention(self.m_OwnerObj.m_ID, cl_msgcenter.MSG_WAR_DIEDIST, ClearPlayerHate, 'ClearHate')
        cl_msgcenter.AddFunction(self.m_OwnerObj, cl_msgcenter.MSG_WAR_DIE, OnDieAtAgent, 'AgentOnDie', iSub = -1, iOnce = 0)

    
    def Release(self):
        if self.m_PFAI:
            self.m_PFAI.Release()
        self.ReleaseChosenPos()
        self.m_Game.DoneGlobalAttention(self.m_OwnerObj.m_ID, cl_msgcenter.MSG_WAR_LEAVESCENE, 'ClearHate', iSub = SIDE_TYPE_HERO)
        self.m_Game.DoneGlobalAttention(self.m_OwnerObj.m_ID, cl_msgcenter.MSG_WAR_DIEDIST, 'ClearHate')
        super(CAgent, self).Release()

    
    def EnterScene(self, oScene):
        super(CAgent, self).EnterScene(oScene)
        self.SetData('BornPos', self.m_OwnerObj.GetPos())

    
    def GetConfig(self, sKey, default = None):
        if sKey in self.m_GetWhileRunConfig:
            pFunc = self.m_GetWhileRunConfig[sKey]
            return pFunc(self)
        if sKey not in self.m_Config or self.m_Config[sKey] == default:
            if sKey not in self.m_IgnoreNotify:
                self.SendUnConfiguredAlert(sKey)
            if default is None and sKey in self.m_DefaultConfig:
                return self.m_DefaultConfig[sKey]
            return default
        if sKey in self.m_Time2FrameConfig:
            return Time2Frame(self.m_Config[sKey])
        return self.m_Config[sKey]

    
    def SendUnConfiguredAlert(self, sKey):
        if sKey in self.m_SentAlert:
            return None
        self.m_SentAlert[sKey] = 1
        oOwner = self.m_OwnerObj
        if not oOwner or not (oOwner.m_FightType & WARRIOR_MONSTER):
            return None
        oGame = oOwner.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLine = oLevelCtrl.GetLineNode(oOwner.m_LineIdx)
        iLevelNode = oLine.m_LevelNode.m_Level if oLine else 0
        sLine = oLine.m_Name if oLine else 'None'
        sText = '请检查怪物%d配置%s 区域编号%d 场景%d 关卡%d 路线%s' % (oOwner.m_SID, sKey, oOwner.m_AreaIndex, oScene.SID(), iLevelNode, sLine)
        if sLine != 'None':
            BehaviorLog.Alert(sText)
        else:
            BehaviorLog.Debug(sText)

    
    def SetLockEnemy(self, iTarget):
        self.m_OwnerObj.SetLockEnemy(iTarget)

    
    def GetLockEnemy(self):
        iLockEnemy = self.m_OwnerObj.Query('LockEnemy', 0)
        if iLockEnemy:
            oEnemy = self.m_Game.GetObject(iLockEnemy, PY_FLAG_MONSTERTARGET)
            if oEnemy and oEnemy.m_Scene == self.m_OwnerObj.m_Scene:
                return oEnemy
            self.SetLockEnemy(0)

    
    def InitDodgeInfo(self):
        iMax = self.GetConfig('DodgeMaxTimes', 0)
        iCD = Time2Frame(self.GetConfig('DodgeCD', 0))
        dDodge = {
            'Times': iMax,
            'CD': iCD,
            'CDFrame': 0 }
        self.SetData('Dodge', dDodge)

    
    def ReleaseChosenPos(self):
        iArea = self.GetData('ChosenArea', -1)
        if iArea != -1:
            sKey = 'ChosenArea'
            iIndex = iArea
        else:
            iHidePos = self.GetData('ChosenHidePos', -1)
            if iHidePos != -1:
                sKey = 'ChosenHidePos'
                iIndex = iHidePos
            else:
                return None
        self.SetData(sKey, -1)
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_OwnerObj.m_Scene)
        if oScene:
            oSceneData = oScene.m_SceneData
            dChosen = oSceneData.Query(sKey, { })
            dChosen.pop(iIndex, 0)
            oSceneData.Set(sKey, dChosen)

    
    def UsePerformGroupEnd(self):
        UsePerformGroupEnd(self, iStatus = 0)

    
    def GetClassTypeName():
        return 'CMonsterAgent'

    GetClassTypeName = staticmethod(GetClassTypeName)
    
    def SetActCheckVal(self, iTarget, iSearchVal, iGuardVal, iFarValue):
        oTarget = self.m_Game.GetObject(iTarget, self.m_CheckExcludeFlag)
        if not oTarget:
            return None
        dCheckVal = self.GetData('ActCheckVal', { })
        if iTarget not in dCheckVal:
            dCheckVal[iTarget] = [
                0,
                0]
        iNowVal = 0
        dDis = self.GetSceneEnemyDis(iOnlyHero = 0)
        if not dDis:
            return None
        if iTarget not in dDis:
            return None
        iDis = dDis[iTarget]
        if iDis <= self.GetConfig('SearchDis', 0):
            iNowVal = iSearchVal
        elif iDis <= self.GetConfig('GuardDis', 0):
            iNowVal = iGuardVal
        else:
            iNowVal = iFarValue
        if iNowVal and iNowVal > dCheckVal[iTarget][0]:
            dCheckVal[iTarget][0] = iNowVal
            self.SetData('ActCheckVal', dCheckVal)

    
    def CalCheckVal(oAgent):
        iMaxActVal = oAgent.GetCache('MaxActVal', 0)
        if iMaxActVal:
            return iMaxActVal
        oAgent.CalMoveCheckVal()
        oAgent.CalHateCheckValue()
        dCheckVal = oAgent.GetData('ActCheckVal', { })
        if dCheckVal:
            for iTarget, lstVal in dCheckVal.items():
                iVal = lstVal[0] + lstVal[1]
                if iVal > iMaxActVal:
                    iMaxActVal = iVal
            
        dDis = oAgent.GetSceneEnemyDis(iOnlyHero = 0)
        fViewR = oAgent.GetConfig('ViewR', 0)
        iViewAngle = oAgent.GetConfig('ViewAngle', 0)
        iViewMaxVal = 1500
        if dDis:
            oOwner = oAgent.m_OwnerObj
            for iTarget, fDis in dDis.items():
                if fDis > fViewR:
                    continue
                oTarget = oAgent.m_Game.GetObject(iTarget, PY_FLAG_MONSTERTARGET)
                if not oTarget:
                    continue
                if oAgent.IsHeroInSight(oOwner, oTarget, iViewAngle) or iTarget not in dCheckVal:
                    dCheckVal[iTarget] = [
                        0,
                        0]
                iVal = iViewMaxVal * (fViewR - fDis) // fViewR
                dCheckVal[iTarget][1] = iVal
                iTotal = dCheckVal[iTarget][0] + dCheckVal[iTarget][1]
                if iTotal > iMaxActVal:
                    iMaxActVal = iTotal
            
        oAgent.SetData('ActCheckVal', dCheckVal)
        oAgent.SetCache('MaxActVal', iMaxActVal)
        return iMaxActVal

    CalCheckVal = staticmethod(CalCheckVal)
    
    def CalMoveCheckVal(self):
        if not self.GetData('MoveCheck', False):
            return None
        oGame = self.m_Game
        oOwner = self.m_OwnerObj
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        if not oScene:
            return None
        dCurPos = { }
        for iTarget in oScene.m_MonsterEnemy:
            oTarget = oGame.GetObject(iTarget, self.m_CheckExcludeFlag)
            if not oTarget:
                continue
            if ValidSceneAttention(self, oTarget):
                dCurPos[iTarget] = oTarget.GetPos()
        
        if not dCurPos:
            return None
        dLastPos = self.GetData('MCPos', { })
        if dLastPos:
            for iTarget, vPos in dCurPos.items():
                if iTarget not in dLastPos:
                    continue
                if not cl_math.CheckDistance(vPos, dLastPos[iTarget], 0.01):
                    self.SetActCheckVal(iTarget, 500, 300, 0)
            
        self.SetData('MCPos', dCurPos)

    
    def CalHateCheckValue(self):
        dHateData = self.GetData('HateData', { })
        if not dHateData:
            return None
        dCheck = self.GetData('ActCheckVal', { })
        for iTarget, dHate in dHateData.items():
            if not dHate['Immutable']:
                return None
            dCheck[iTarget] = [
                300,
                300]
        
        self.SetData('ActCheckVal', dCheck)

    
    def ClearCheckVal(oAgent):
        oAgent.SetData('ActCheckVal', { })
        return BT_SUCCESS

    ClearCheckVal = staticmethod(ClearCheckVal)
    
    def ClearHateVal(self):
        self.SetData('HateData', { })

    
    def SetCheckExcludeFlag(iFlag, oAgent):
        oAgent.m_CheckExcludeFlag = iFlag
        return BT_SUCCESS

    SetCheckExcludeFlag = staticmethod(SetCheckExcludeFlag)
    
    def SetFollowMoveExcludeFlag(iFlag, oAgent):
        oAgent.m_FollowMoveExcludeFlag = iFlag
        return BT_SUCCESS

    SetFollowMoveExcludeFlag = staticmethod(SetFollowMoveExcludeFlag)
    
    def GetHateListCnt(oAgent):
        dHate = oAgent.GetData('HateData', { })
        oGame = oAgent.m_Game
        lstRemove = []
        for iTarget in dHate:
            if not oGame.GetObject(iTarget, PY_FLAG_MONSTERTARGET):
                lstRemove.append(iTarget)
        
        if lstRemove:
            dAllCheckVal = oAgent.GetData('ActCheckVal', { })
            for iTarget in lstRemove:
                dHate.pop(iTarget)
                dAllCheckVal.pop(iTarget, 0)
            
        return len(dHate)

    GetHateListCnt = staticmethod(GetHateListCnt)
    
    def GetLiveHeroCnt(oAgent):
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        if not oScene:
            return 0
        iCnt = 0
        for iHero in oScene.m_Heros:
            if oGame.GetObject(iHero, PY_FLAG_DEAD):
                iCnt += 1
        
        return iCnt

    GetLiveHeroCnt = staticmethod(GetLiveHeroCnt)
    
    def HateAllPlayer(oAgent):
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        dTarget = { }
        lstHero = oGame.m_WarMgr.GetRoomHero()
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if oHero.m_Scene == oOwner.m_Scene:
                dTarget[iHero] = 1
        
        if not dTarget:
            return BT_FAILURE
        iCurFrame = oGame.GetFrameNum()
        dHateData = oAgent.GetData('HateData', { })
        for iTarget in dTarget:
            if iTarget not in dHateData:
                dHateData[iTarget] = {
                    'Dam': { },
                    'Hate': [
                        0,
                        iCurFrame],
                    'Immutable': 0 }
        
        oAgent.SetData('HateData', dHateData)
        return BT_SUCCESS

    HateAllPlayer = staticmethod(HateAllPlayer)
    
    def HateTargetByID(self, iTarget):
        dHateData = self.GetData('HateData', { })
        if iTarget in dHateData:
            return None
        oGame = self.m_Game
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            return None
        oOwner = self.m_OwnerObj
        if oTarget.m_Scene != oOwner.m_Scene:
            return None
        iCurFrame = oGame.GetFrameNum()
        dHateData[iTarget] = {
            'Dam': { },
            'Hate': [
                0,
                iCurFrame],
            'Immutable': 0 }
        self.SetData('HateData', dHateData)

    
    def TestUpdateAIRuningState(iState, oAgent):
        iOldState = oAgent.GetData('AIState', 0)
        oAgent.SetData('AIState', iState)
        if iState == 3 and iOldState != iState:
            oGame = oAgent.m_Game
            oAgent.m_CatchStartFrame = 0
            oOwner = oAgent.m_OwnerObj
            oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
            if oScene:
                iGroup = oAgent.GetConfig('GroupID', -1)
                if iGroup != -1:
                    lstTarget = oAgent.GetGroupHateTarget()
                    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GROUPHATE, oOwner, {
                        'Group': iGroup,
                        'Target': lstTarget })
                iStateSID = STATE_UNDER_ATTACK
                iTimeType = STATE_TIME_FOREVER
                for iHero in oScene.GetHeros():
                    oHero = oGame.GetObject(iHero, PY_FLAG_DEAD)
                    if oHero:
                        oState = cl_state.AddState(oHero, iStateSID, iTimeType, 0, {
                            'AID': oOwner.m_ID,
                            'RS': cl_object.reason.CStrReason('BehaviorTree') })
                        if oState:
                            oState.Enable(oHero)
                
                if oAgent.GetConfig('ShowWarning', 0):
                    cl_snetwar.GS2CTriggerBehavior(oGame, oOwner.m_ID, CBEHAVIOR_MONSTER_WARN, oScene.GetPlayers())
                else:
                    oAgent.SetLockEnemy(0)

    TestUpdateAIRuningState = staticmethod(TestUpdateAIRuningState)
    
    def GetGroupHateTarget(self):
        lstTarget = []
        dAllCheckVal = self.GetData('ActCheckVal', { })
        if dAllCheckVal:
            iMaxActVal = 0
            iMaxTarget = 0
            for iTarget, lstVal in dAllCheckVal.items():
                iVal = lstVal[0] + lstVal[1]
                if iVal > iMaxActVal:
                    iMaxActVal = iVal
                    iMaxTarget = iTarget
            
            if iMaxTarget:
                oGame = self.m_Game
                oMaxTarget = oGame.GetObject(iMaxTarget, PY_FLAG_DEAD)
                if oMaxTarget:
                    vCenter = oMaxTarget.GetPos()
                    oScene = oGame.m_SceneMgr.GetScene(self.m_OwnerObj.m_Scene)
                    for iTarget in oScene.m_MonsterEnemy:
                        if iTarget == iMaxTarget:
                            continue
                        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
                        if oTarget and cl_math.CheckDistance(oTarget.GetPos(), vCenter, 10):
                            lstTarget.append(iTarget)
                    
                    if not lstTarget:
                        lstTarget.append(iMaxTarget)
        return lstTarget

    
    def DealActCheckVal(self, iLimitAct, iLockMaxAct = 1):
        iCurFrame = self.m_Game.GetFrameNum()
        dAllCheckVal = self.GetData('ActCheckVal', { })
        if dAllCheckVal:
            iMaxActVal = 0
            iMaxTarget = 0
            dHate = { }
            for iTarget, lstVal in dAllCheckVal.items():
                iVal = lstVal[0] + lstVal[1]
                if iVal > iMaxActVal:
                    iMaxActVal = iVal
                    iMaxTarget = iTarget
                if iVal >= iLimitAct:
                    dHate[iTarget] = {
                        'Dam': { },
                        'Hate': [
                            0,
                            iCurFrame],
                        'Immutable': 0 }
            
            self.SetData('HateData', dHate)
            self.SetData('ActCheckVal', { })
            if iLockMaxAct and iMaxTarget:
                self.SetLockEnemy(iMaxTarget)
                self.SetData('LockEnemyFrame', iCurFrame)

    
    def ChooseHateTarget(iLimitAct, oAgent):
        if not oAgent.GetData('HateData', { }):
            dAllCheckVal = oAgent.GetData('ActCheckVal', { })
            if dAllCheckVal:
                oAgent.DealActCheckVal(iLimitAct)
                return BT_SUCCESS
        iCurFrame = oAgent.m_Game.GetFrameNum()
        iLockFrame = oAgent.GetData('LockEnemyFrame', 0)
        oNowTarget = oAgent.GetLockEnemy()
        if not oNowTarget or iCurFrame - iLockFrame >= 5 * GAME_FRAME:
            oAgent.UpdateHate()
            dHateData = oAgent.GetData('HateData', { })
            iMaxVal = -1
            iNowTarget = oNowTarget.m_ID if oNowTarget else 0
            iMaxTarget = iNowTarget
            for iTarget, dData in dHateData.items():
                if iMaxVal < dData['Hate'][0]:
                    iMaxVal = dData['Hate'][0]
                    iMaxTarget = iTarget
            
            if iMaxVal == 0 and dHateData:
                idx = oAgent.m_Game.Random(len(dHateData))
                iMaxTarget = list(dHateData)[idx]
            if iMaxTarget:
                if iMaxTarget != iNowTarget:
                    iNowVal = dHateData[iNowTarget]['Hate'][0] if iNowTarget in dHateData else -1
                    if iMaxVal > iNowVal * 1.1:
                        oAgent.SetLockEnemy(iMaxTarget)
                        oAgent.SetData('LockEnemyFrame', iCurFrame)
                        oAgent.SetData('LastEnemyHate', iMaxVal)
                return BT_SUCCESS
            oAgent.SetLockEnemy(0)
            oAgent.SetData('LockEnemyFrame', 0)
        if oAgent.m_OwnerObj.Query('LockEnemy', 0):
            return BT_SUCCESS
        return BT_FAILURE

    ChooseHateTarget = staticmethod(ChooseHateTarget)
    
    def ChooseNearestHateTarget(iLimitAct, oAgent):
        if not oAgent.GetData('HateData', { }):
            dAllCheckVal = oAgent.GetData('ActCheckVal', { })
            if dAllCheckVal:
                oAgent.DealActCheckVal(iLimitAct, iLockMaxAct = 0)
        oGame = oAgent.m_Game
        iCurFrame = oGame.GetFrameNum()
        iLockFrame = oAgent.GetData('LockEnemyFrame', 0)
        oNowTarget = oAgent.GetLockEnemy()
        if not oNowTarget or iCurFrame - iLockFrame >= 5 * GAME_FRAME:
            oAgent.UpdateHate()
            dHateData = oAgent.GetData('HateData', { })
            iNowTarget = oNowTarget.m_ID if oNowTarget else 0
            iNearest = iNowTarget
            fMinDis = 999
            oOwner = oAgent.m_OwnerObj
            dDis = oGame.Scene_GetTargetDisMap(oOwner.m_ID, list(dHateData), 1)
            for iTarget, fDis in dDis.items():
                if fDis < fMinDis:
                    fMinDis = fDis
                    iNearest = iTarget
            
            if iNearest:
                if iNearest != iNowTarget:
                    oAgent.SetLockEnemy(iNearest)
                    oAgent.SetData('LockEnemyFrame', iCurFrame)
                return BT_SUCCESS
            oAgent.SetLockEnemy(0)
            oAgent.SetData('LockEnemyFrame', 0)
        if oAgent.m_OwnerObj.Query('LockEnemy', 0):
            return BT_SUCCESS
        return BT_FAILURE

    ChooseNearestHateTarget = staticmethod(ChooseNearestHateTarget)
    
    def ChooseHateHero(iLimitAct, oAgent):
        if not oAgent.GetData('HateData', { }):
            dAllCheckVal = oAgent.GetData('ActCheckVal', { })
            if dAllCheckVal:
                oAgent.DealActCheckVal(iLimitAct, iLockMaxAct = 0)
        iCurFrame = oAgent.m_Game.GetFrameNum()
        iLockFrame = oAgent.GetData('LockEnemyFrame', 0)
        oNowTarget = oAgent.GetLockEnemy()
        if not oNowTarget or not (oNowTarget.m_FightType & WARRIOR_HERO) or iCurFrame - iLockFrame >= 5 * GAME_FRAME:
            oScene = oAgent.m_Game.m_SceneMgr.GetScene(oAgent.m_SceneData.m_Scene)
            if not oScene:
                return BT_FAILURE
            oAgent.UpdateHate()
            dHateData = oAgent.GetData('HateData', { })
            iMaxVal = -1
            iNowTarget = oNowTarget.m_ID if oNowTarget and oNowTarget.m_FightType & WARRIOR_HERO else 0
            iMaxTarget = iNowTarget
            for iTarget, dData in dHateData.items():
                if iTarget not in oScene.m_Heros:
                    continue
                if iMaxVal < dData['Hate'][0]:
                    iMaxVal = dData['Hate'][0]
                    iMaxTarget = iTarget
            
            if iMaxVal == 0 and dHateData:
                if iMaxTarget:
                    lstTarget = [ iTarget for iTarget in dHateData if iTarget in oScene.m_Heros ]
                else:
                    lstTarget = list(dHateData)
                idx = oAgent.m_Game.Random(len(lstTarget))
                iMaxTarget = lstTarget[idx]
            if iMaxTarget:
                if iMaxTarget != iNowTarget:
                    iNowVal = dHateData[iNowTarget]['Hate'][0] if iNowTarget in dHateData else -1
                    if iMaxVal > iNowVal * 1.1:
                        oAgent.SetLockEnemy(iMaxTarget)
                        oAgent.SetData('LockEnemyFrame', iCurFrame)
                        oAgent.SetData('LastEnemyHate', iMaxVal)
                return BT_SUCCESS
            oAgent.SetLockEnemy(0)
            oAgent.SetData('LockEnemyFrame', 0)
        if oAgent.m_OwnerObj.Query('LockEnemy', 0):
            return BT_SUCCESS
        return BT_FAILURE

    ChooseHateHero = staticmethod(ChooseHateHero)
    
    def UpdateHate(self):
        dHateData = self.GetData('HateData', { })
        iCurFrame = self.m_Game.GetFrameNum()
        iValidFrame = iCurFrame - 5 * GAME_FRAME
        lstPop = []
        for iTarget, dData in dHateData.items():
            oTarget = self.m_Game.GetObject(iTarget, PY_FLAG_MONSTERTARGET)
            if not oTarget:
                lstPop.append(iTarget)
                continue
            if dData['Immutable']:
                continue
            dNewDam = { }
            iAllDam = 0
            for iFrame in dData['Dam']:
                if iFrame < iValidFrame:
                    continue
                iAllDam += dData['Dam'][iFrame]
                dNewDam[iFrame] = dData['Dam'][iFrame]
            
            (iDam, iDamFrame) = dData['Hate']
            dData['Dam'] = dNewDam
            if iDam == 0 and iAllDam == 0 or iCurFrame - iDamFrame >= 999 * GAME_FRAME:
                lstPop.append(iTarget)
                continue
            dData['Hate'] = [
                iAllDam,
                iCurFrame]
        
        iNowTarget = self.m_OwnerObj.Query('LockEnemy', 0)
        for iPop in lstPop:
            if iNowTarget == iPop:
                self.SetLockEnemy(0)
            dHateData.pop(iPop)
        
        self.SetData('HateData', dHateData)

    
    def ChooseOwnerSameTarget(oAgent):
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        iMonsterOwner = oOwner.m_Owner
        oMonsterOwner = oGame.GetObject(iMonsterOwner, PY_FLAG_DEAD)
        if not oMonsterOwner:
            return BT_FAILURE
        iNowTarget = oOwner.Query('LockEnemy', 0)
        iHateTarget = oMonsterOwner.Query('LockEnemy', 0)
        if iNowTarget != iHateTarget:
            oAgent.SetLockEnemy(iHateTarget)
        if oOwner.Query('LockEnemy', 0):
            return BT_SUCCESS
        return BT_FAILURE

    ChooseOwnerSameTarget = staticmethod(ChooseOwnerSameTarget)
    
    def IsChooseNoMaxHateTarget(oAgent):
        lstIgnoreSkill = oAgent.GetData('IgnoreSkills', [])
        dCurPFGroup = oAgent.GetData('CurPFGroup')
        for _, tInfo in dCurPFGroup.items():
            if tInfo[0] in lstIgnoreSkill:
                return False
        
        iRatio = oAgent.GetData('NoMaxHateRatio', 0)
        if not iRatio:
            return False
        if iRatio == 100:
            return True
        iNoRatio = 100 - iRatio
        dRatio = {
            0: iNoRatio,
            1: iRatio }
        iRes = ChooseKey(oAgent.m_Game, dRatio)
        if not iRes:
            return False
        return True

    IsChooseNoMaxHateTarget = staticmethod(IsChooseNoMaxHateTarget)
    
    def ChooseNoMaxHateTarget(oAgent):
        oAgent.SetData('NoMaxHateRatio', 0)
        oAgent.UpdateHate()
        dHateData = oAgent.GetData('HateData', { })
        if not dHateData:
            return BT_FAILURE
        iMaxVal = -1
        iMaxTarget = 0
        for iTarget, dData in dHateData.items():
            if iMaxVal < dData['Hate'][0]:
                iMaxVal = dData['Hate'][0]
                iMaxTarget = iTarget
        
        dHateData.pop(iMaxTarget)
        if not dHateData:
            return BT_FAILURE
        lstHateData = list(dHateData.keys())
        iIndex = oAgent.m_Game.Random(len(lstHateData))
        iTarget = lstHateData[iIndex]
        oAgent.SetLockEnemy(iTarget)
        return BT_SUCCESS

    ChooseNoMaxHateTarget = staticmethod(ChooseNoMaxHateTarget)
    
    def ChooseOwnerOutSideMarkTarget(oAgent):
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        iMonsterOwner = oOwner.m_Owner
        oMonsterOwner = oGame.GetObject(iMonsterOwner, PY_FLAG_DEAD)
        oAgent.AddCurNodeEndFunc(ClearOwnerMarkEndFunc)
        if not oMonsterOwner:
            return BT_FAILURE
        dHateData = oMonsterOwner.m_Agent.GetData('HateData', { })
        if not dHateData:
            return BT_FAILURE
        iOwnerTarget = oMonsterOwner.Query('LockEnemy', 0)
        dMarkTarget = oMonsterOwner.Query('MarkTarget', { })
        lstMark = []
        for iMonster, iTarget in dMarkTarget.items():
            if not iTarget or oOwner.m_ID == iMonster:
                continue
            lstMark.append(iTarget)
        
        lstTarget = []
        lstLive = []
        for iTarget in dHateData:
            oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
            if not oTarget:
                continue
            lstLive.append(iTarget)
            if iOwnerTarget == iTarget or iTarget in lstMark:
                continue
            lstTarget.append(iTarget)
        
        if not lstTarget:
            if not lstLive:
                return BT_FAILURE
            iIndex = oGame.Random(len(lstLive))
            iMarkTarget = lstLive[iIndex]
        else:
            iIndex = oGame.Random(len(lstTarget))
            iMarkTarget = lstTarget[iIndex]
        oAgent.SetLockEnemy(iMarkTarget)
        if oOwner.Query('LockEnemy', 0):
            dMarkTarget[oOwner.m_ID] = iMarkTarget
            oMonsterOwner.Set('MarkTarget', dMarkTarget)
            return BT_SUCCESS
        return BT_FAILURE

    ChooseOwnerOutSideMarkTarget = staticmethod(ChooseOwnerOutSideMarkTarget)
    
    def GetLockTargetDis(oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return 0
        return cl_math.CalDistance(oAgent.m_OwnerObj.GetPos(), oTarget.GetPos())

    GetLockTargetDis = staticmethod(GetLockTargetDis)
    
    def GetCatchFrame(oAgent):
        return oAgent.m_Game.GetFrameNum() - oAgent.m_CatchStartFrame

    GetCatchFrame = staticmethod(GetCatchFrame)
    
    def ChooseGuardPos(oAgent):
        dAllCheckVal = oAgent.GetData('ActCheckVal', { })
        iMaxActVal = 0
        iMaxTarget = 0
        for iTarget, lstVal in dAllCheckVal.items():
            iVal = lstVal[0] + lstVal[1]
            if iVal > iMaxActVal:
                iMaxActVal = iVal
                iMaxTarget = iTarget
        
        if iMaxTarget:
            oTarget = oAgent.m_Game.GetObject(iMaxTarget, PY_FLAG_DEAD)
            if oTarget:
                (tx, ty, tz) = oTarget.GetPos()
                (ox, oy, oz) = oAgent.m_OwnerObj.GetPos()
                oAgent.SetData('ArrivePos', (tx, ty, tz))
                iTurnSpeed = 0
                oAgent.SetData('FaceDir', ((tx - ox, 0, tz - oz), iTurnSpeed))
                return BT_SUCCESS
        return BT_FAILURE

    ChooseGuardPos = staticmethod(ChooseGuardPos)
    
    def InShootNear(self, iAttack, vEnd):
        oGame = self.m_Game
        oEnemy = oGame.GetObject(iAttack, PY_FLAG_DEAD)
        if not oEnemy:
            return False
        vOwner = self.m_OwnerObj.GetPos()
        vStart = oEnemy.GetPos()
        fNearDis = self.GetConfig('NearDis')
        if fNearDis == 0:
            return False
        if cl_math.GetLinePointDis(vOwner[0], vOwner[2], vStart[0], vStart[2], vEnd[0], vEnd[2]) < fNearDis:
            v1 = cl_math.Vec3Minus(vEnd, vStart)
            v2 = cl_math.Vec3Minus(vOwner, vEnd)
            v3 = cl_math.Vec3Minus(vOwner, vStart)
            if not (cl_math.VectorDot2D(v1, v2) > 0 or cl_math.VectorDot2D(v1, v3) < 0) and cl_math.CheckDistance(vOwner, vEnd, fNearDis):
                return False
            return True
        return False

    
    def StopMoving(oAgent):
        iRet = oAgent.Stop()
        if iRet:
            oAgent.SetData('LastFollowTar', 0)
            oAgent.SetData('LastArrIdx', 0)
            return BT_SUCCESS
        return BT_FAILURE

    StopMoving = staticmethod(StopMoving)
    
    def ChooseEnemyAroundPos(fMinRadius, fMaxRadius, fLimitDis, oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return BT_FAILURE
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        vEnemy = oTarget.GetPos()
        if cl_math.CheckDistance(vEnemy, vOwner, fMaxRadius + fLimitDis):
            bCheckDis = True
            vDir = cl_math.Vec3Minus(vEnemy, vOwner)
            iMaxAngle = 120
        else:
            bCheckDis = False
            vDir = (1, 0, 0)
            iMaxAngle = 179
        for _ in range(5):
            vPos = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vEnemy, vDir, fMinRadius, fMaxRadius, 1, iMaxAngle)
            if (vPos or bCheckDis) and cl_math.CheckDistance(vPos, vOwner, fLimitDis) and iMaxAngle > 30:
                iMaxAngle -= 30
                continue
        else:
            return oAgent.ChooseEnemyPos(oAgent)
        oAgent.SetData('ArrivePos', vPos)
        oAgent.SetData('vEnd', vPos)
        if oGame.GetWarMgr().Query('DebugRay'):
            debug.ClearDebugLine(oAgent.m_Game, debug.LINE_TILE)
            (ox, oy, oz) = oOwner.GetPos()
            (tx, ty, tz) = vPos
            debug.DebugLine(oAgent.m_Game, ox, oy, oz, tx, ty, tz, 65535, debug.LINE_TILE)
        return BT_SUCCESS

    ChooseEnemyAroundPos = staticmethod(ChooseEnemyAroundPos)
    
    def ChooseFriendAroundPos(fMinRadius, fMaxRadius, oAgent):
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        if not oScene:
            return BT_FAILURE
        oTarget = None
        iCmpValue = 0
        for mid in oScene.GetObjectsByType('Monster'):
            if mid == oOwner.m_ID:
                continue
            oMonster = oGame.GetObject(mid)
            if not oMonster:
                continue
            iMonsterHP = oMonster.HP()
            if not not iCmpValue:
                if iMonsterHP < iCmpValue:
                    oTarget = oMonster
                    iCmpValue = iMonsterHP
                    continue
        
        if not oTarget:
            return BT_FAILURE
        vTarget = oTarget.GetPos()
        vPos = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vTarget, (1, 0, 0), fMinRadius, fMaxRadius, 1, 179)
        if not vPos:
            return BT_FAILURE
        oAgent.SetData('ArrivePos', vPos)
        if oGame.GetWarMgr().Query('DebugRay'):
            debug.ClearDebugLine(oAgent.m_Game, debug.LINE_TILE)
            (ox, oy, oz) = oOwner.GetPos()
            (tx, ty, tz) = vPos
            debug.DebugLine(oAgent.m_Game, ox, oy, oz, tx, ty, tz, 65535, debug.LINE_TILE)
        return BT_SUCCESS

    ChooseFriendAroundPos = staticmethod(ChooseFriendAroundPos)
    
    def ChooseDodgePos(fMinDis, fMaxDis, iMinAngle, iMaxAngle, oAgent):
        oGame = oAgent.m_Game
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        (ox, oy, oz) = vOwner
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
                oAgent.SetData('DodgeAngle', iAngle)
                oAgent.SetData('vEnd', vEnd)
                return BT_SUCCESS
        
        return BT_FAILURE

    ChooseDodgePos = staticmethod(ChooseDodgePos)
    
    def ChooseTargetAwayPos(fRange, fAngle, iRayNum, fCheckDistance, oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        vTarget = oTarget.GetPos()
        vEnd = oOwner.m_MoveCtrl.E_KeepAwayRayCastPos(vTarget, fRange, -fAngle, fAngle, iRayNum)
        if fCheckDistance >= 0.01:
            vOwner = oOwner.GetPos()
            if cl_math.CheckDistance3D(vOwner, vEnd, fCheckDistance):
                vEnd = oOwner.m_MoveCtrl.E_KeepAwayRayCastPos(vTarget, fRange, -178, 178, iRayNum)
        oAgent.SetData('ArrivePos', vEnd)
        return BT_SUCCESS

    ChooseTargetAwayPos = staticmethod(ChooseTargetAwayPos)
    
    def CalDodgeTimes(self):
        dDodge = self.GetData('Dodge')
        iCD = dDodge['CD']
        iTimes = dDodge['Times']
        iFrame = dDodge['CDFrame']
        iMax = self.GetConfig('DodgeMaxTimes', 0)
        if not iCD or not iMax:
            return 0
        if iTimes < iMax:
            iCur = self.m_Game.GetFrameNum()
            if iFrame:
                iAdd = (iCur - iFrame) // iCD
                iFrame = iFrame + iAdd * iCD
                dDodge['Times'] = min(iTimes + iAdd, iMax)
            else:
                iFrame = iCur
            dDodge['CDFrame'] = iFrame
        return iTimes

    
    def NeedToDodge(oAgent):
        oOwner = oAgent.m_OwnerObj
        oGame = oAgent.m_Game
        if not oOwner.m_MoveMode & MOVE_TYPE_NORMAL:
            return BT_FAILURE
        if oOwner.m_CastingSkill or oOwner.m_BackSwingSkill:
            return BT_FAILURE
        iCur = oGame.GetFrameNum()
        (iLastAID, iLastAttFrame) = oAgent.GetData('DodgeLastAtt', (0, 0))
        if iCur - iLastAttFrame > HALF_GAME_FRAME:
            return BT_FAILURE
        iDodgeLastFrame = oAgent.GetData('DodgeLastFrame', 0)
        iDodgeCDFrame = oOwner.m_DodgeCDFrame
        if iDodgeCDFrame and iDodgeLastFrame and iCur < iDodgeLastFrame + iDodgeCDFrame:
            return BT_FAILURE
        dDodgedAttack = oAgent.m_SceneData.Query('DodgedAttack', { })
        iNextDodgeFrame = dDodgedAttack[iLastAID] if iLastAID in dDodgedAttack else 0
        if iNextDodgeFrame and iCur < iNextDodgeFrame:
            return BT_FAILURE
        iRandom = oGame.Random(100)
        iDodgeProb = oOwner.QueryAttr('DodgeProb')
        if iRandom >= iDodgeProb:
            return BT_FAILURE
        if oAgent.CalDodgeTimes() > 0:
            dDodgedAttack[iLastAID] = iLastAttFrame + HALF_GAME_FRAME
            oAgent.m_SceneData.Set('DodgedAttack', dDodgedAttack)
            dDodge = oAgent.GetData('Dodge')
            dDodge['Times'] -= 1
            oAgent.SetData('DodgeLastAtt', (0, 0))
            return BT_SUCCESS
        return BT_FAILURE

    NeedToDodge = staticmethod(NeedToDodge)
    
    def NeedToBlink(iTime, oAgent):
        oOwner = oAgent.m_OwnerObj
        oGame = oAgent.m_Game
        if oOwner.m_CastingSkill or oOwner.m_BackSwingSkill:
            return BT_FAILURE
        iCur = oGame.GetFrameNum()
        iLastAttFrame = oAgent.GetData('BlinkAtt', 0)
        if iLastAttFrame and iCur - iLastAttFrame >= Time2Frame(iTime):
            oAgent.SetData('BlinkAtt', 0)
            return BT_SUCCESS
        return BT_FAILURE

    NeedToBlink = staticmethod(NeedToBlink)
    
    def IsLockEnemyPosAccessible(oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return False
        vEnemy = oEnemy.GetPos()
        oGame = oAgent.m_Game
        fModelRadius = oEnemy.m_ModelRadius
        lstVictim = oGame.Scene_SweepMultiple(oEnemy.m_Scene, vEnemy, fModelRadius, (0, -1, 0), 0.1, PXMASK_MOVEBLK, {
            'BlockMask': PXMASK_MOVEBLK })
        if not lstVictim:
            return True
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        return oGame.Scene_IsDestPosAccessible(oOwner.m_Scene, vOwner, vEnemy)

    IsLockEnemyPosAccessible = staticmethod(IsLockEnemyPosAccessible)
    
    def IsLockEnemyPosRangeAccessible(fRange, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return False
        vEnemy = oEnemy.GetPos()
        oGame = oAgent.m_Game
        fModelRadius = oEnemy.m_ModelRadius
        lstVictim = oGame.Scene_SweepMultiple(oEnemy.m_Scene, vEnemy, fModelRadius, (0, -1, 0), 0.1, PXMASK_MOVEBLK, {
            'BlockMask': PXMASK_MOVEBLK })
        if not lstVictim:
            return True
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        (iRet, vDest) = oGame.Scene_GetAccessibleDestPos(oOwner.m_Scene, vOwner, vEnemy)
        if not iRet:
            return False
        fDis = cl_math.CalDistance3D(vEnemy, vDest)
        return fDis <= fRange

    IsLockEnemyPosRangeAccessible = staticmethod(IsLockEnemyPosRangeAccessible)
    
    def MoveToLockEnemy(fCatchDis, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        if fCatchDis <= 0:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        iLastID = oAgent.GetData('LastFollowTar', 0)
        if iLastID == oEnemy.m_ID and iLastID != oOwner.m_MoveCtrl.m_FollowTarget:
            return BT_FAILURE
        vOwner = oOwner.GetPos()
        vEnemy = oEnemy.GetPos()
        if cl_math.CheckDistance3D(vOwner, vEnemy, fCatchDis) and abs(vOwner[1] - vEnemy[1]) <= 1.5:
            if oAgent.Stop():
                return BT_SUCCESS
            if not oOwner.IsStop():
                return BT_RUNNING
            return BT_FAILURE
        oAgent.AddCurNodeEndFunc(MoveToLockEnemyEnd)
        if oAgent.FollowMove(oOwner, oEnemy.m_ID, fCatchDis, StopMoveToLockEnemyCBFunc, iPyFlag = oAgent.m_FollowMoveExcludeFlag):
            oAgent.SetData('LastFollowTar', oEnemy.m_ID)
            return BT_RUNNING
        return BT_FAILURE

    MoveToLockEnemy = staticmethod(MoveToLockEnemy)
    
    def MoveToFlyLockEnemy(fCatchDis, fMinHeight, fMaxHeight, oAgent):
        oOwner = oAgent.m_OwnerObj
        if not oOwner.m_UseFlyNav:
            return CAgent.MoveToLockEnemy(fCatchDis, oAgent)
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        if fCatchDis <= 0:
            return BT_FAILURE
        iLastID = oAgent.GetData('LastFollowTar', 0)
        if iLastID == oEnemy.m_ID and iLastID != oOwner.m_MoveCtrl.m_FollowTarget:
            return BT_FAILURE
        vOwner = oOwner.GetPos()
        vEnemy = oEnemy.GetPos()
        if cl_math.CheckDistance(vOwner, vEnemy, fCatchDis):
            if oAgent.Stop():
                return BT_SUCCESS
            if not oOwner.IsStop():
                return BT_RUNNING
            return BT_FAILURE
        oAgent.AddCurNodeEndFunc(MoveToFlyLockEnemyEnd)
        fHeight = oAgent.m_Game.Random(int(100 * (fMaxHeight - fMinHeight))) / 100 + fMinHeight
        if oAgent.FlyFollowMove(oOwner, oEnemy.m_ID, fCatchDis, fHeight, StopMoveToFlyLockEnemyCBFunc):
            oAgent.SetData('LastFollowTar', oEnemy.m_ID)
            return BT_RUNNING
        return BT_FAILURE

    MoveToFlyLockEnemy = staticmethod(MoveToFlyLockEnemy)
    
    def MoveToSlopeLockEnemy(fCatchDis, iRefreshTime, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        if not fCatchDis or fCatchDis <= 0:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        iLastID = oAgent.GetData('LastFollowTar', 0)
        if iLastID == oEnemy.m_ID and iLastID != oOwner.m_MoveCtrl.m_FollowTarget:
            return BT_FAILURE
        vOwner = oOwner.GetPos()
        vEnemy = oEnemy.GetPos()
        if cl_math.CheckDistance3D(vOwner, vEnemy, fCatchDis):
            if oAgent.Stop():
                return BT_SUCCESS
            if not oOwner.IsStop():
                return BT_RUNNING
            return BT_FAILURE
        oAgent.AddCurNodeEndFunc(MoveToLockEnemyEnd)
        iRefreshFrame = Time2Frame(iRefreshTime)
        if oAgent.FollowMove(oOwner, oEnemy.m_ID, fCatchDis, StopMoveToLockEnemyCBFunc, iAppointFrame = iRefreshFrame):
            oAgent.SetData('LastFollowTar', oEnemy.m_ID)
            return BT_RUNNING
        return BT_FAILURE

    MoveToSlopeLockEnemy = staticmethod(MoveToSlopeLockEnemy)
    
    def GetMonsterOwnerPos(oAgent):
        oOwner = oAgent.m_OwnerObj
        iMonsterOwner = oOwner.m_Owner
        oMonsterOwner = oAgent.m_Game.GetObject(iMonsterOwner)
        if not oMonsterOwner:
            return BT_FAILURE
        vMonsterOwner = oMonsterOwner.GetPos()
        oAgent.SetData('ArrivePos', vMonsterOwner)
        return BT_SUCCESS

    GetMonsterOwnerPos = staticmethod(GetMonsterOwnerPos)
    
    def MoveToPos(oAgent):
        vTarget = oAgent.GetData('ArrivePos')
        if not vTarget:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        oAgent.AddCurNodeEndFunc(MoveToPosEnd)
        iOldIdx = oAgent.GetData('LastArrIdx', 0)
        if iOldIdx and oOwner.m_MoveMode == MOVE_TYPE_NORMAL and cl_math.CheckDistance(vOwner, vTarget, 1):
            if oAgent.Stop():
                return BT_SUCCESS
            if not oOwner.IsStop():
                return BT_RUNNING
            return BT_FAILURE
        oMoveCtrl = oOwner.m_MoveCtrl
        if iOldIdx:
            if not (oMoveCtrl.m_ArriveInfo) or iOldIdx != oMoveCtrl.m_ArriveInfo[0]:
                return BT_FAILURE
        if oAgent.SeekPath(oOwner, vTarget, func = MoveToPosEndCB):
            oAgent.SetData('LastArrIdx', oMoveCtrl.m_ArriveInfo[0])
            return BT_RUNNING
        return BT_FAILURE

    MoveToPos = staticmethod(MoveToPos)
    
    def GetLastArrIdx(oAgent):
        return oAgent.GetData('LastArrIdx', 0)

    GetLastArrIdx = staticmethod(GetLastArrIdx)
    
    def FlyToPos(oAgent):
        oOwner = oAgent.m_OwnerObj
        vTarget = oAgent.GetData('ArrivePos')
        if not vTarget:
            return BT_FAILURE
        vOwnerPos = oOwner.GetPos()
        oAgent.AddCurNodeEndFunc(FlyToPosEnd)
        iOldIdx = oAgent.GetData('LastArrIdx', 0)
        if iOldIdx and oOwner.m_MoveMode == MOVE_TYPE_FLY and cl_math.CheckDistance(vOwnerPos, vTarget, 0.1) and oAgent.Stop():
            return BT_SUCCESS
        oMoveCtrl = oOwner.m_MoveCtrl
        if oAgent.AirMove(oOwner, vTarget, oOwner.MoveSpeed(), func = FlyToPosEndCB):
            oAgent.SetData('LastArrIdx', oMoveCtrl.m_ArriveInfo[0])
            return BT_RUNNING
        return BT_FAILURE

    FlyToPos = staticmethod(FlyToPos)
    
    def CurveFlyToPos(oAgent):
        oOwner = oAgent.m_OwnerObj
        oCurve = oOwner.m_CurveCompute
        if not oCurve:
            return BT_FAILURE
        vEnd = oCurve.m_End
        vOwnerPos = oOwner.GetPos()
        oAgent.AddCurNodeEndFunc(FlyToPosEnd)
        iOldIdx = oAgent.GetData('LastArrIdx', 0)
        if iOldIdx and oOwner.m_MoveMode == MOVE_TYPE_FLY and cl_math.CheckDistance(vOwnerPos, vEnd, 0.1) and oAgent.Stop():
            return BT_SUCCESS
        oMoveCtrl = oOwner.m_MoveCtrl
        if oAgent.AirCurveMove(oOwner, oOwner.MoveSpeed(), func = FlyToPosEndCB):
            oAgent.SetData('LastArrIdx', oMoveCtrl.m_ArriveInfo[0])
            return BT_RUNNING
        return BT_FAILURE

    CurveFlyToPos = staticmethod(CurveFlyToPos)
    
    def KeepMoving(fRadius, oAgent):
        oOwner = oAgent.m_OwnerObj
        vStart = oAgent.GetData('StartingPoint', ())
        if not vStart:
            vOwner = oOwner.GetPos()
            oAgent.SetData('ArrivePos', ())
            oAgent.SetData('StartingPoint', vOwner)
        oAgent.AddCurNodeEndFunc(KeepMovingEnd)
        KeepMoving(oAgent, fRadius)
        return BT_RUNNING

    KeepMoving = staticmethod(KeepMoving)
    
    def HasToStartGuerrilla(oAgent):
        iGuerrillaProb = oAgent.GetConfig('GuerrillaProb', -1)
        if iGuerrillaProb < 0 or iGuerrillaProb > 100:
            return False
        return oAgent.m_Game.Random(100) < iGuerrillaProb

    HasToStartGuerrilla = staticmethod(HasToStartGuerrilla)
    
    def HasToStartFuzzy(oAgent):
        iFuzzyProb = oAgent.GetConfig('FuzzyProb', -1)
        if iFuzzyProb < 0 or iFuzzyProb > 100:
            return False
        return oAgent.m_Game.Random(100) < iFuzzyProb

    HasToStartFuzzy = staticmethod(HasToStartFuzzy)
    
    def IsTooApproachedToTarget(fRadius, iHalfAngle, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return False
        oOwner = oAgent.m_OwnerObj
        (dx, dz) = oOwner.GetPathDir()
        if not dx and not dz:
            return False
        vOwner = oOwner.GetPos()
        vEnemy = oEnemy.GetPos()
        if not cl_math.CheckDistance3D(vOwner, vEnemy, fRadius):
            return False
        vMoveDir = (dx, 0, dz)
        vDir = cl_math.Vec3Minus(vEnemy, vOwner)
        if cl_math.CalAngle2D(vDir, vMoveDir) > iHalfAngle:
            return False
        return True

    IsTooApproachedToTarget = staticmethod(IsTooApproachedToTarget)
    
    def ChooseRangedPos(fRadius, fMinDis, fMaxDis, iMinAngle, iMaxAngle, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        oAgent.Remove_Call_Out('CleanMoveDir')
        oOwner = oAgent.m_OwnerObj
        oGame = oAgent.m_Game
        vOwner = oOwner.GetPos()
        vEnemy = oEnemy.GetPos()
        tMoveDir = oAgent.GetData('MoveDir', None)
        vEnd = None
        if tMoveDir and tMoveDir[0] and cl_math.CheckDistance(vOwner, vEnemy, 2 * fRadius):
            (vLastDir, fFirstDis) = tMoveDir
            iAngle = oGame.Random(46)
            iAngle = -iAngle if oGame.Random(2) else iAngle
            fDis = oGame.Random(int(100 * (fMaxDis - fMinDis))) / 100 + fMinDis
            vDir = cl_math.RotateAroundVector(vLastDir, (0, 1, 0), iAngle)
            vEnd = cl_math.Vec3DisplaceDir(vOwner, vDir, fDis)
            fGroundDis = oGame.Scene_GroundDistance(oOwner.m_Scene, vEnd, 2, PXMASK_MOVEBLK | PXMASK_OBJECT, oOwner.m_ID)
            vEnd = oGame.Scene_NavMeshRayCast(oOwner.m_Scene, vOwner, (vEnd[0], vEnd[1] - fGroundDis, vEnd[2]))
            if cl_math.CheckDistance(vEnd, vEnemy, 5):
                vEnd = None
            else:
                oAgent.SetData('MoveDir', (vDir, fFirstDis))
        if not vEnd or cl_math.CheckDistance(vEnd, vOwner, 0.01):
            vDir = cl_math.Vec3Minus(vEnemy, vOwner)
            if vEnemy == vOwner:
                vCenter = vEnemy
            else:
                vCenter = cl_math.Vec3DisplacePos(vEnemy, vOwner, fRadius)
                vCenter = oGame.Scene_NavMeshRayCast(oOwner.m_Scene, vEnemy, vCenter)
            vEnd = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vCenter, vDir, fMinDis, fMaxDis, iMinAngle, iMaxAngle)
            if not vEnd:
                (fMinDis, fMaxDis, iMinAngle, iMaxAngle) = (3, fMaxDis + 2, 60, 120)
                for i in range(3):
                    vEnd = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vOwner, vDir, fMinDis, fMaxDis, iMinAngle, iMaxAngle)
                    if vEnd:
                        break
                
                if not vEnd:
                    oAgent.SetData('MoveDir', None)
                    return BT_FAILURE
            vMoveDir = cl_math.Vec3Minus(vEnd, vOwner)
            oAgent.SetData('MoveDir', (vMoveDir, cl_math.CalDistance(vOwner, vEnd)))
        oAgent.SetData('ArrivePos', vEnd)
        return BT_SUCCESS

    ChooseRangedPos = staticmethod(ChooseRangedPos)
    
    def ChooseRangedFlyPos(fRadius, fMinDis, fMaxDis, iMinAngle, iMaxAngle, fMinHeight, fMaxHeight, oAgent):
        oOwner = oAgent.m_OwnerObj
        if not oOwner.m_UseFlyNav:
            return CAgent.ChooseRangedPos(fRadius, fMinDis, fMaxDis, iMinAngle, iMaxAngle, oAgent)
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        oAgent.Remove_Call_Out('CleanMoveDir')
        oGame = oAgent.m_Game
        vOwner = oOwner.GetPos()
        vEnemy = oEnemy.GetPos()
        tMoveDir = oAgent.GetData('MoveDir', None)
        vEnd = None
        if tMoveDir and tMoveDir[0] and cl_math.CheckDistance(vOwner, vEnemy, 2 * fRadius):
            (vLastDir, fFirstDis) = tMoveDir
            iAngle = oGame.Random(46)
            iAngle = -iAngle if oGame.Random(2) else iAngle
            fDis = oGame.Random(int(100 * (fMaxDis - fMinDis))) / 100 + fMinDis
            vDir = cl_math.RotateAroundVector(vLastDir, (0, 1, 0), iAngle)
            vEnd = cl_math.Vec3HorizonDisplaceDir(vOwner, vDir, fDis)
            fGroundDis = oGame.Scene_GroundDistance(oOwner.m_Scene, vEnd, 10, PXMASK_MOVEBLK | PXMASK_OBJECT, oOwner.m_ID)
            fHeight = oGame.Random(int(100 * (fMaxHeight - fMinHeight))) / 100 + fMinHeight
            vEnd = oAgent.m_Game.Scene_FlyRayCast(oOwner.m_Scene, vOwner, (vEnd[0], vEnd[1] + fHeight - fGroundDis, vEnd[2]))
            if cl_math.CheckDistance(vEnd, vEnemy, 5):
                vEnd = None
            else:
                oAgent.SetData('MoveDir', (vDir, fFirstDis))
        if not vEnd or cl_math.CheckDistance(vEnd, vOwner, 0.01):
            vDir = cl_math.Vec3Minus(vEnemy, vOwner)
            if vEnemy == vOwner:
                vCenter = vEnemy
            else:
                vCenter = cl_math.Vec3HorizonDisplacePos(vEnemy, vOwner, fRadius)
            vEnd = oGame.Scene_FlyRandomPointSector(oOwner.m_Scene, vCenter, vDir, fMinDis, fMaxDis, iMinAngle, iMaxAngle, fMinHeight, fMaxHeight)
            if vEnd:
                vMoveDir = cl_math.Vec3Minus(vEnd, vOwner)
                oAgent.SetData('MoveDir', (vMoveDir, cl_math.CalDistance(vOwner, vEnd)))
        oAgent.SetData('ArrivePos', vEnd)
        return BT_SUCCESS

    ChooseRangedFlyPos = staticmethod(ChooseRangedFlyPos)
    
    def ChooseHateFlankPos(fMinDis, fMaxDis, iMinAngle, iMaxAngle, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        oGame = oAgent.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        lstMonster = oScene.GetObjectsByType('Monster')
        vMonster = [
            0,
            0,
            0]
        iCnt = 0
        for iMonster in lstMonster:
            oMonster = oGame.GetObject(iMonster)
            if oMonster:
                vMonster = cl_math.Vec3Add(vMonster, oMonster.GetPos())
                iCnt += 1
        
        if iCnt:
            vStart = cl_math.Vec3MulF(vMonster, 1 / iCnt)
        else:
            vStart = oOwner.GetPos()
        vEnemy = oEnemy.GetPos()
        vDir = cl_math.Vec3Minus(vStart, vEnemy)
        vEnd = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vEnemy, vDir, fMinDis, fMaxDis, iMinAngle, iMaxAngle)
        if not vEnd:
            return BT_FAILURE
        oAgent.SetData('FlankEnemyPos', vEnemy)
        oAgent.SetData('ArrivePos', vEnd)
        return BT_SUCCESS

    ChooseHateFlankPos = staticmethod(ChooseHateFlankPos)
    
    def TryReChooseHateFlankPos(fMoveDis, fMinDis, fMaxDis, iMinAngle, iMaxAngle, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        vLastEnemy = oAgent.GetData('FlankEnemyPos', None)
        if oEnemy and vLastEnemy:
            vEnemy = oEnemy.GetPos()
            if not cl_math.CheckDistance3D(vLastEnemy, vEnemy, fMoveDis):
                iRet = oAgent.ChooseHateFlankPos(fMinDis, fMaxDis, iMinAngle, iMaxAngle, oAgent)
                if iRet == BT_SUCCESS:
                    oAgent.SetData('LastArrIdx', 0)
        return BT_SUCCESS

    TryReChooseHateFlankPos = staticmethod(TryReChooseHateFlankPos)
    
    def ChooseRangedAreaPos(fDis, fMaxDisToOwner, fHeightLimit, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelConfData = oLevelCtrl.m_LevelConfData
        dAllArea = { }
        if oOwner.m_LineIdx:
            oLine = oLevelCtrl.GetLineNode(oOwner.m_LineIdx)
            dAllArea = oLevelConfData.GetLineConfig(oLine.m_LevelNode.m_Level, oLine.m_Name, 'monsterarea')
        if not dAllArea:
            oAgent.SendUnConfiguredAlert('MonsterArea')
            return BT_FAILURE
        lstGroup = oAgent.GetConfig('RangedAreaGroup')
        bChooseNewArea = oAgent.GetConfig('ChooseNewArea', True)
        iLastArea = oAgent.GetData('ChosenArea', -1)
        oSceneData = oAgent.m_SceneData
        dChosen = oSceneData.Query('ChosenArea', { })
        lstAreaIdx = list(dAllArea)
        oSurvivorElement = oGame.m_WarMgr.GetComponent('SurvivorElement')
        sType = ''
        if oSurvivorElement:
            dRangedAreaWeight = oAgent.GetConfig('RangedAreaWeight')
            if not dRangedAreaWeight:
                return BT_FAILURE
            sType = ChooseKey(oAgent.m_Game, dRangedAreaWeight)
            if not sType:
                return BT_FAILURE
        if lstGroup and sType != 'far':
            for iIdx, dArea in dAllArea.items():
                if dArea['group'] not in lstGroup:
                    lstAreaIdx.remove(iIdx)
            
        if not bChooseNewArea or len(lstAreaIdx) <= 1:
            iLastArea = -1
        vOwner = oOwner.GetPos()
        vEnemy = oEnemy.GetPos()
        dAvailable = { }
        dFarEnoughToTarget = { }
        dCloseEnoughToOwner = { }
        fMinDis = 999
        iClosest = -1
        for iIdx in lstAreaIdx:
            if iIdx == iLastArea or iIdx in dChosen:
                continue
            dAvailable[iIdx] = 1
            tCenter = dAllArea[iIdx]['center']
            vCenter = (tCenter[0], 0, tCenter[2])
            fDistanceToTarger = cl_math.CalDistance(vCenter, vEnemy)
            if fDistanceToTarger >= fDis:
                dFarEnoughToTarget[iIdx] = 1
        
        if not dFarEnoughToTarget:
            dFarEnoughToTarget = dAvailable
        for iIdx in lstAreaIdx:
            if iIdx not in dFarEnoughToTarget:
                continue
            tCenter = dAllArea[iIdx]['center']
            if fHeightLimit and abs(vOwner[1] - tCenter[1]) > fHeightLimit:
                continue
            vCenter = (tCenter[0], 0, tCenter[2])
            fDistanceToOwner = cl_math.CalDistance(vCenter, vOwner)
            if fMinDis > fDistanceToOwner:
                fMinDis = fDistanceToOwner
                iClosest = iIdx
            if fDistanceToOwner <= fMaxDisToOwner:
                dCloseEnoughToOwner[iIdx] = 1
        
        if not dCloseEnoughToOwner:
            iArea = iClosest
        else:
            iArea = ChooseKey(oGame, dCloseEnoughToOwner)
        if iArea not in dAllArea:
            if not oOwner.Query('RangedAreaAlert'):
                oOwner.Set('RangedAreaAlert', 1)
                iMonsterNo = oAgent.GetConfig('MonsterNo', 0)
                BehaviorLog.Alert('关卡%d路线%s未配置足够的怪物远程作战区域, 触发怪物%d-%d-%s 坐标%s' % (oLine.m_LevelNode.m_Level, oLine.m_Name, iMonsterNo, oOwner.m_SID, oOwner.m_Name, OutputPos(vOwner)))
            return BT_FAILURE
        lstVertices = dAllArea[iArea]['vertices']
        if len(lstVertices) < 3:
            return BT_FAILURE
        vEnd = oGame.Scene_RandomPointPolyInMesh(oOwner.m_Scene, lstVertices)
        if not vEnd:
            return BT_FAILURE
        oAgent.SetData('ArrivePos', vEnd)
        dChosen[iArea] = 1
        oSceneData.Set('ChosenArea', dChosen)
        oAgent.SetData('ChosenArea', iArea)
        return BT_SUCCESS

    ChooseRangedAreaPos = staticmethod(ChooseRangedAreaPos)
    
    def ChooseShowPos(oAgent):
        oGame = oAgent.m_Game
        vShowPos = oAgent.GetConfig('ShowPos', None)
        oAgent.SetCheckExcludeFlag(PY_FLAG_MONSTERTARGET, oAgent)
        if vShowPos:
            oAgent.SetData('ArrivePos', vShowPos)
            return BT_SUCCESS
        oOwner = oAgent.m_OwnerObj
        dAllPos = { }
        lstPos = oAgent.GetConfig('ShowPosID', [])
        if isinstance(lstPos, int):
            lstPos = [
                lstPos]
        if 0 in lstPos:
            lstPos.remove(0)
        if not lstPos:
            return BT_FAILURE
        idx = oGame.Random(len(lstPos))
        iPos = lstPos[idx]
        if oOwner.m_LineIdx:
            oLevelCtrl = oOwner.m_Game.m_WarMgr.GetComponent('LevelCtrl')
            oLevelConfData = oLevelCtrl.m_LevelConfData
            oLine = oLevelCtrl.GetLineNode(oOwner.m_LineIdx)
            dAllPos = oLevelConfData.GetLineConfig(oLine.m_LevelNode.m_Level, oLine.m_Name, 'monstershowpos')
        if not dAllPos or iPos not in dAllPos:
            oAgent.SendUnConfiguredAlert('ShowPosID')
            return BT_FAILURE
        vPos = dAllPos[iPos]
        oAgent.SetData('ArrivePos', vPos)
        return BT_SUCCESS

    ChooseShowPos = staticmethod(ChooseShowPos)
    
    def ChooseHorizontalPos(fMinDis, fMaxDis, oAgent):
        oOwner = oAgent.m_OwnerObj
        oGame = oAgent.m_Game
        vOwner = oOwner.GetPos()
        (ox, oy, oz) = vOwner
        (dx, _, dz) = oOwner.GetFacing()
        iScene = oOwner.m_Scene
        iMinDis = int(fMinDis * CELL_SPACESIZE)
        iMaxDis = int(fMaxDis * CELL_SPACESIZE)
        iDis = oGame.Random(iMaxDis - iMinDis) + iMinDis
        fDis = iDis * CELL_REC
        iAngle = 90
        if oGame.Random(2):
            iAngle = -iAngle
        (rx, rz) = cl_math.Vec2DestPosDir((ox, oz), (dx, dz), fDis, iAngle)
        vEnd = oGame.Scene_NavMeshRayCast(iScene, vOwner, (rx, oy, rz))
        oAgent.SetData('ArrivePos', vEnd)
        return BT_SUCCESS

    ChooseHorizontalPos = staticmethod(ChooseHorizontalPos)
    
    def SetPatrolPos(oAgent):
        dPatrolPos = oAgent.GetData('PatrolPos', { })
        if dPatrolPos:
            lstPos = dPatrolPos['Pos']
            iIdx = (dPatrolPos['Idx'] + 1) % len(lstPos)
        else:
            oOwner = oAgent.m_OwnerObj
            (ox, oy, oz) = oOwner.GetPos()
            tPatrolPos = oAgent.GetConfig('PatrolPos')
            if not tPatrolPos:
                oAgent.SendUnConfiguredAlert('PatrolPos')
                return BT_FAILURE
            lstPos = [
                (ox, oy, oz)]
            lstPos.extend(list(tPatrolPos))
            iIdx = 1
            dPatrolPos['Pos'] = lstPos
        tCurPos = lstPos[iIdx]
        dPatrolPos['Idx'] = iIdx
        oAgent.SetData('ArrivePos', tCurPos)
        oAgent.SetData('PatrolPos', dPatrolPos)
        return BT_SUCCESS

    SetPatrolPos = staticmethod(SetPatrolPos)
    
    def SetFlyPatrolPos(fMinHeight, fMaxHeight, oAgent):
        oOwner = oAgent.m_OwnerObj
        if not oOwner.m_UseFlyNav:
            return CAgent.SetPatrolPos(oAgent)
        dPatrolPos = oAgent.GetData('PatrolPos', { })
        if dPatrolPos:
            lstPos = dPatrolPos['Pos']
            iIdx = (dPatrolPos['Idx'] + 1) % len(lstPos)
        else:
            (ox, oy, oz) = oOwner.GetPos()
            tPatrolPos = oAgent.GetConfig('PatrolPos')
            if not tPatrolPos:
                oAgent.SendUnConfiguredAlert('PatrolPos')
                return BT_FAILURE
            lstPos = [
                (ox, oy, oz)]
            lstPos.extend(list(tPatrolPos))
            iIdx = 1
            dPatrolPos['Pos'] = lstPos
        tCurPos = lstPos[iIdx]
        dPatrolPos['Idx'] = iIdx
        fHeight = oAgent.m_Game.Random(int(100 * (fMaxHeight - fMinHeight))) / 100 + fMinHeight
        tCurPos = (tCurPos[0], tCurPos[1] + fHeight, tCurPos[2])
        oAgent.SetData('ArrivePos', tCurPos)
        oAgent.SetData('PatrolPos', dPatrolPos)
        return BT_SUCCESS

    SetFlyPatrolPos = staticmethod(SetFlyPatrolPos)
    
    def NextPatrolPos(oAgent):
        dPatrolPos = oAgent.GetData('PatrolPos', { })
        if dPatrolPos:
            lstPos = dPatrolPos['Pos']
            iIdx = (dPatrolPos['Idx'] + 1) % len(lstPos)
            tCurPos = lstPos[iIdx]
        elif oAgent.GetConfig('BackToBornPos', 0):
            tCurPos = oAgent.GetData('BornPos')
        elif oAgent.GetConfig('AIMethod', 0) == MONSTERAI_TYPE_AREAMOVE:
            tCurPos = None
        else:
            oOwner = oAgent.m_OwnerObj
            tCurPos = oAgent.m_Game.Scene_RandomPointSectorInMesh(oOwner.m_Scene, oOwner.GetPos(), (1, 0, 0), 10, 15, 1, 179)
        oAgent.SetData('ArrivePos', tCurPos)
        return BT_SUCCESS

    NextPatrolPos = staticmethod(NextPatrolPos)
    
    def SetFacePatrolDir(oAgent):
        dPatrolFace = oAgent.GetData('PatrolFace', { })
        if dPatrolFace:
            lstDir = dPatrolFace['Dir']
            iIdx = (dPatrolFace['Idx'] + 1) % len(lstDir)
        else:
            tPatrolFace = oAgent.GetConfig('PatrolFace')
            if not tPatrolFace:
                oAgent.SendUnConfiguredAlert('PatrolFace')
                return BT_FAILURE
            (iAngle, iTime) = tPatrolFace
            if iAngle <= 0 or iTime <= 0:
                oAgent.SendUnConfiguredAlert('PatrolFace')
                return BT_FAILURE
            iTurnSpeed = int(iAngle // Time2Frame(iTime))
            dPatrolFace['TurnSpeed'] = iTurnSpeed
            oOwner = oAgent.m_OwnerObj
            (x, _, z) = oOwner.GetFacing()
            (tx, tz) = cl_math.Vec2DestPosDir((0, 0), (x, z), 1.28, iAngle)
            lstDir = [
                (x, 0, z),
                (tx, 0, tz)]
            iIdx = 1
            dPatrolFace['Dir'] = lstDir
        dPatrolFace['Idx'] = iIdx
        oAgent.SetData('FaceDir', (lstDir[iIdx], dPatrolFace['TurnSpeed']))
        oAgent.SetData('PatrolFace', dPatrolFace)
        return BT_SUCCESS

    SetFacePatrolDir = staticmethod(SetFacePatrolDir)
    
    def GetPatrol(oAgent):
        sRes = oAgent.GetData('PatrolWay', '')
        if sRes:
            return sRes
        tPatrolPos = oAgent.GetConfig('PatrolPos')
        tPatrolFace = oAgent.GetConfig('PatrolFace')
        if tPatrolPos and tPatrolFace:
            sRes = 'patrolpos'
        elif tPatrolPos:
            sRes = 'patrolpos'
        elif tPatrolFace:
            sRes = 'patrolface'
        else:
            oAgent.SendUnConfiguredAlert('PatrolWay')
        oAgent.SetData('PatrolWay', sRes)
        return sRes

    GetPatrol = staticmethod(GetPatrol)
    
    def SetMoveStatusRun(oAgent):
        return BT_FAILURE

    SetMoveStatusRun = staticmethod(SetMoveStatusRun)
    
    def SetMoveStatusWalk(oAgent):
        return BT_FAILURE

    SetMoveStatusWalk = staticmethod(SetMoveStatusWalk)
    
    def SeekPath(self, oOwner, tPos, func = None):
        iForbidMove = oOwner.IsForbid(FORBID_MOVE)
        bNormal = oOwner.m_MoveMode == MOVE_TYPE_NORMAL
        if iForbidMove and oOwner.HasRule(cl_forbid.NAVSEEK_RULE) and not oOwner.Query('SeekAlert'):
            oCurrent = oOwner.m_Agent.m_CurrentBT
            sName = oCurrent.GetName() if oCurrent else ''
            oOwner.Set('SeekAlert', 1)
            BehaviorLog.Error(f'''怪物{oOwner.m_SID}关闭导航期间禁止seekpath 请检查{sName}''')
        if iForbidMove and bNormal:
            return False
        oMoveCtrl = oOwner.m_MoveCtrl
        if oMoveCtrl.HasSameArriveInfo(tPos):
            return True
        if iForbidMove or not bNormal:
            return False
        if oMoveCtrl.SeekPath(oOwner, tPos, func):
            return True
        return False

    
    def FollowMove(self, oOwner, iTarget, fStopDis, func = None, iAppointFrame = 0, iPyFlag = PY_FLAG_DEAD):
        iForbidMove = oOwner.IsForbid(FORBID_MOVE)
        bNormal = oOwner.m_MoveMode == MOVE_TYPE_NORMAL
        if iForbidMove and oOwner.HasRule(cl_forbid.NAVSEEK_RULE) and not oOwner.Query('SeekAlert'):
            oCurrent = oOwner.m_Agent.m_CurrentBT
            sName = oCurrent.GetName() if oCurrent else ''
            oOwner.Set('SeekAlert', 1)
            BehaviorLog.Error(f'''怪物{oOwner.m_SID}关闭导航期间禁止followmove 请检查{sName}''')
        if iForbidMove and bNormal:
            return False
        oMoveCtrl = oOwner.m_MoveCtrl
        if oMoveCtrl.HasSameArriveTarget(iTarget):
            return True
        if iForbidMove or not bNormal:
            return False
        if oMoveCtrl.FollowMove(oOwner, iTarget, fStopDis, func, iAppointFrame = iAppointFrame, iPyFlag = iPyFlag):
            return True
        return False

    
    def FlyFollowMove(self, oOwner, iTarget, fStopDis, fHeight, func = None, iAppointFrame = 0):
        iForbidMove = oOwner.IsForbid(FORBID_MOVE)
        bNormal = oOwner.m_MoveMode == MOVE_TYPE_NORMAL
        if iForbidMove and oOwner.HasRule(cl_forbid.NAVSEEK_RULE) and not oOwner.Query('SeekAlert'):
            oCurrent = oOwner.m_Agent.m_CurrentBT
            sName = oCurrent.GetName() if oCurrent else ''
            oOwner.Set('SeekAlert', 1)
            BehaviorLog.Error(f'''怪物{oOwner.m_SID}关闭导航期间禁止followmove 请检查{sName}''')
        if iForbidMove and bNormal:
            return False
        oMoveCtrl = oOwner.m_MoveCtrl
        if oMoveCtrl.HasSameArriveTarget(iTarget):
            return True
        if iForbidMove or not bNormal:
            return False
        if oMoveCtrl.FollowMove(oOwner, iTarget, fStopDis, fHeight, func, iAppointFrame = iAppointFrame):
            return True
        return False

    
    def DirectMove(self, oOwner, lstPath, func = None, iGround = 1):
        if oOwner.IsForbid(FORBID_MOVE):
            return False
        if oOwner.m_MoveCtrl.DirectMove(oOwner, lstPath, 0, func, iGround):
            return True
        return False

    
    def AirMove(self, oOwner, vEnd, fSpeed, func = None):
        if oOwner.IsForbid(FORBID_MOVE):
            return False
        oMoveCtrl = oOwner.m_MoveCtrl
        if oMoveCtrl.HasSameArriveInfo(vEnd):
            return True
        if oOwner.m_MoveCtrl.AirMove(oOwner, vEnd, fSpeed, True, func):
            return True
        return False

    
    def AirCurveMove(self, oOwner, fSpeed, func):
        if oOwner.IsForbid(FORBID_MOVE):
            return False
        oMoveCtrl = oOwner.m_MoveCtrl
        vEnd = oOwner.m_CurveCompute.m_End
        if oMoveCtrl.HasSameArriveInfo(vEnd):
            return True
        if oOwner.m_MoveCtrl.AirCurveMove(oOwner, fSpeed, func):
            return True
        return False

    
    def CleanMoveDir(self):
        self.SetData('MoveDir', None)

    
    def Stop(self):
        oOwner = self.m_OwnerObj
        oMoveCtrl = oOwner.m_MoveCtrl
        if not oMoveCtrl:
            return 0
        if oOwner.m_MoveMode not in (MOVE_TYPE_NORMAL, MOVE_TYPE_FLY):
            return 0
        oMoveCtrl.OverArrive(oOwner, 0, iCallBack = 0)
        self.Remove_Call_Out('KeepMoving')
        if self.GetData('MoveDir', None):
            self.Call_Out(self.CleanMoveDir, HALF_GAME_FRAME, 'CleanMoveDir')
        if oOwner.m_MoveMode == MOVE_TYPE_FLY:
            return oMoveCtrl.AirStop(oOwner)
        return oMoveCtrl.Stop(oOwner)

    
    def ChooseRangeHidePosAndAttPos(fMinDis, fMaxDis, oAgent):
        oGame = oAgent.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oAgent.m_OwnerObj.m_Scene)
        if not oScene:
            return BT_FAILURE
        dChosen = oScene.m_SceneData.Query('ChosenHidePos', { })
        tHideInfo = oAgent.GetCache('HidePos', None)
        if not tHideInfo:
            lstFilterPosID = list(dChosen.keys())
            tHideInfo = oAgent.ChooseHidePosAndAttPos(oScene, fMaxDis, lstFilterPosID, fMinDis)
            if not tHideInfo:
                return BT_FAILURE
        oAgent.SetData('ArrivePos', tHideInfo[1])
        oAgent.SetData('AttPos', tHideInfo[2])
        dChosen[tHideInfo[0]] = 1
        oScene.m_SceneData.Set('ChosenHidePos', dChosen)
        oAgent.SetData('ChosenHidePos', tHideInfo[0])
        return BT_SUCCESS

    ChooseRangeHidePosAndAttPos = staticmethod(ChooseRangeHidePosAndAttPos)
    if lib_flag.g_IsMobileRun and lib_flag.g_IsLogicLayer:
        
        def ChooseHidePosAndAttPos(self, oScene, fRadius, lstFilterPosID, fMinDis = 0):
            oGame = self.m_Game
            lstCheckPos = []
            lstHero = oGame.m_WarMgr.GetLiveHero()
            for iHero in lstHero:
                oHero = oGame.GetObject(iHero, PY_FLAG_DEAD)
                if not oHero or oHero.m_Scene != self.m_OwnerObj.m_Scene:
                    continue
                lstCheckPos.append(oHero.GetPos())
            
            if fMinDis:
                tHideInfo = oGame.ChooseRangeHidePosAndAttPos(oScene.m_SID, fMinDis, fRadius, self.m_OwnerObj.GetPos(), lstCheckPos, lstFilterPosID)
            else:
                tHideInfo = oGame.ChooseHidePosAndAttPos(oScene.m_SID, fRadius, self.m_OwnerObj.GetPos(), lstCheckPos, lstFilterPosID)
            return tHideInfo

    else:
        
        def ChooseHidePosAndAttPos(self, oScene, fRadius, lstFilterPosID, fMinDis = 0):
            oGame = self.m_Game
            lstCheckPos = []
            lstHero = oGame.m_WarMgr.GetLiveHero()
            for iHero in lstHero:
                oHero = oGame.GetObject(iHero, PY_FLAG_DEAD)
                if not oHero or oHero.m_Scene != self.m_OwnerObj.m_Scene:
                    continue
                lstCheckPos.append(oHero.GetPos())
            
            if fMinDis:
                tHideInfo = oGame.ChooseRangeHidePosAndAttPos(oScene.m_ID, fMinDis, fRadius, self.m_OwnerObj.GetPos(), lstCheckPos, lstFilterPosID)
            else:
                tHideInfo = oGame.ChooseHidePosAndAttPos(oScene.m_ID, fRadius, self.m_OwnerObj.GetPos(), lstCheckPos, lstFilterPosID)
            return tHideInfo

    
    def ChooseAreaConfigPos(iRule, oAgent):
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelConfData = oLevelCtrl.m_LevelConfData
        if not oOwner.m_LineIdx:
            return BT_FAILURE
        oLine = oLevelCtrl.GetLineNode(oOwner.m_LineIdx)
        dAllArea = oLevelConfData.GetLineConfig(oLine.m_LevelNode.m_Level, oLine.m_Name, 'monsterarea')
        lstGroup = oAgent.GetConfig('RangedAreaGroup')
        iLastArea = oAgent.GetData('ChosenArea', -1)
        iArea = -1
        lstPos = []
        if lstGroup:
            iPos = 0
            for iIdx, dArea in dAllArea.items():
                if dArea['group'] in lstGroup:
                    lstPos.append((iPos, dArea['center']))
                    iPos += 1
            
        if not lstPos:
            return BT_FAILURE
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            iRule = 0
        vChoosePos = None
        vOwnerPos = oOwner.GetPos()
        fSame = 1
        if iRule == 0:
            lstPos = ShufferList(oGame, lstPos)
            for iIdx, vPos in lstPos:
                if iIdx == iLastArea:
                    continue
                if cl_math.CheckDistance(vOwnerPos, vPos, fSame):
                    continue
                vChoosePos = vPos
                iArea = iIdx
            
        elif iRule == 1:
            fMaxDis = 0
            vTarget = oTarget.GetPos()
            for iIdx, vPos in lstPos:
                if iIdx == iLastArea:
                    continue
                if cl_math.CheckDistance(vOwnerPos, vPos, fSame):
                    continue
                fDis = cl_math.CalDistance3D(vTarget, vPos)
                if fDis > fMaxDis:
                    fMaxDis = fDis
                    vChoosePos = vPos
                    iArea = iIdx
            
        elif iRule == 2:
            iRange = oOwner.Query('LifeRange', 10)
            dTypeWeight = oOwner.Query('TypeWeight', { })
            lstLifeWeight = oOwner.Query('LifeWeight', [])
            fMaxWeight = 0
            for _, vPos in lstPos:
                fWeight = 0
                fGroundDis = oGame.Scene_GroundDistance(oOwner.m_Scene, vPos, 10, PXMASK_BLOCK, oOwner.m_ID)
                vGroundPos = (vPos[0], vPos[1] - fGroundDis, vPos[2])
                lstArgs = [
                    vGroundPos,
                    iRange]
                dMask = {
                    'Mask': PXMASK_MONSTER }
                lstMonster = cl_math.GetAttackTargetList(oGame, oOwner.m_Scene, ATT_SHAPE_SPHERE, lstArgs, dMask)
                for iMonster in lstMonster:
                    oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
                    if not oMonster:
                        continue
                    if oMonster.m_SID not in dTypeWeight:
                        continue
                    fTypeWeight = dTypeWeight[oMonster.m_SID]
                    iLifeRatio = int(((oMonster.HP() + oMonster.Armor() + oMonster.Shield()) / (oMonster.QueryAttr('HPMax') + oMonster.QueryAttr('ArmorMax') + oMonster.QueryAttr('ShieldMax'))) * 100)
                    fLifeWeight = 0
                    for iLife, fWeightConfig in lstLifeWeight:
                        if iLifeRatio >= iLife:
                            fLifeWeight = fWeightConfig
                            break
                    
                    fWeight += fTypeWeight * fLifeWeight
                
                if fWeight > fMaxWeight:
                    fMaxWeight = fWeight
                    vChoosePos = vPos
            
        elif iRule == 3:
            iRange = oOwner.Query('SuperRange', 10)
            dSuperWeight = oOwner.Query('SuperWeight', { })
            fMaxWeight = 0
            for _, vPos in lstPos:
                fWeight = 0
                fGroundDis = oGame.Scene_GroundDistance(oOwner.m_Scene, vPos, 10, PXMASK_BLOCK, oOwner.m_ID)
                vGroundPos = (vPos[0], vPos[1] - fGroundDis, vPos[2])
                lstArgs = [
                    vGroundPos,
                    iRange]
                dMask = {
                    'Mask': PXMASK_MONSTER }
                lstMonster = cl_math.GetAttackTargetList(oGame, oOwner.m_Scene, ATT_SHAPE_SPHERE, lstArgs, dMask)
                for iMonster in lstMonster:
                    oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
                    if not oMonster:
                        continue
                    if oMonster.m_SID not in dSuperWeight:
                        continue
                    fSuperWeight = dSuperWeight[oMonster.m_SID]
                    if oMonster.SuperLevel() > 0:
                        continue
                    fWeight += fSuperWeight
                
                if fWeight >= fMaxWeight:
                    fMaxWeight = fWeight
                    vChoosePos = vPos
            
        if not vChoosePos:
            return BT_FAILURE
        oAgent.SetData('ArrivePos', vChoosePos)
        oAgent.SetData('ChosenArea', iArea)
        (tx, _, tz) = vChoosePos
        (ox, _, oz) = oOwner.GetPos()
        oAgent.SetData('FaceDir', ((tx - ox, 0, tz - oz), oOwner.QueryAttr('TurnSpeed')))
        return BT_SUCCESS

    ChooseAreaConfigPos = staticmethod(ChooseAreaConfigPos)
    
    def GetNearestHidePosDis(fRadius, oAgent):
        if not fRadius:
            fRadius = oAgent.GetConfig('HideR', 20)
        oGame = oAgent.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oAgent.m_OwnerObj.m_Scene)
        if oScene:
            dChosen = oScene.m_SceneData.Query('ChosenHidePos', { })
            tHideInfo = oAgent.ChooseHidePosAndAttPos(oScene, fRadius, list(dChosen.keys()))
            if tHideInfo:
                oAgent.SetCache('HidePos', tHideInfo)
                return cl_math.CalDistance3D(oAgent.m_OwnerObj.GetPos(), tHideInfo[1])
        return 999

    GetNearestHidePosDis = staticmethod(GetNearestHidePosDis)
    
    def SetAttackPos(oAgent):
        vAttPos = oAgent.GetData('AttPos', ())
        if not vAttPos:
            return BT_FAILURE
        oAgent.SetData('ArrivePos', vAttPos)
        return BT_SUCCESS

    SetAttackPos = staticmethod(SetAttackPos)
    
    def GetArrivePosDis(oAgent):
        vPos = oAgent.GetData('ArrivePos', None)
        if not vPos:
            return 0
        return cl_math.CalDistance(oAgent.m_OwnerObj.GetPos(), vPos)

    GetArrivePosDis = staticmethod(GetArrivePosDis)
    
    def GetLockEnemyDis(oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return 0
        return cl_math.CalDistance(oEnemy.GetPos(), oAgent.m_OwnerObj.GetPos())

    GetLockEnemyDis = staticmethod(GetLockEnemyDis)
    
    def GetFirstRangedArrivePosDis(oAgent):
        tMoveDir = oAgent.GetData('MoveDir', None)
        if tMoveDir:
            return tMoveDir[1]
        vPos = oAgent.GetData('ArrivePos', None)
        if not vPos:
            return 0
        return cl_math.CalDistance(oAgent.m_OwnerObj.GetPos(), vPos)

    GetFirstRangedArrivePosDis = staticmethod(GetFirstRangedArrivePosDis)
    
    def GetCoveredPos(oAgent):
        oGuardian = oAgent.GetGuardian()
        if not oGuardian:
            return BT_FAILURE
        vOwner = oAgent.m_OwnerObj.GetPos()
        vGuardian = oGuardian.GetPos()
        fCoverDis = oAgent.GetConfig('CoverDis')
        if not cl_math.CheckDistance3D(vOwner, vGuardian, fCoverDis):
            return BT_FAILURE
        iScene = oAgent.m_OwnerObj.m_Scene
        tFace = oGuardian.GetFacing()
        fDis = 2.5
        vPos = cl_math.Vec3DisplaceDir(vGuardian, tFace, -fDis)
        vEnd = oAgent.m_Game.Scene_NavMeshRayCast(iScene, vGuardian, vPos)
        if cl_math.CheckDistance(vEnd, vGuardian, fDis - 0.5):
            return BT_FAILURE
        oAgent.SetData('ArrivePos', vEnd)
        return BT_SUCCESS

    GetCoveredPos = staticmethod(GetCoveredPos)
    
    def GetGuardian(self):
        oGame = self.m_Game
        iGuardian = self.GetData('GuardianID', 0)
        if not iGuardian:
            iGuardianNo = self.GetConfig('GuardianNo')
            if not iGuardianNo:
                return None
            oOwner = self.m_OwnerObj
            oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
            oMonsterCtrl = oLevelCtrl.GetMonsterCtrl(oOwner.m_LineIdx)
            if not oMonsterCtrl:
                return None
            lstGuardian = oMonsterCtrl.GetMonsterByNo(iGuardianNo)
            iGuardian = lstGuardian[0] if lstGuardian else 0
            self.SetData('GuardianID', iGuardian)
        oGuardian = oGame.GetObject(iGuardian, PY_FLAG_DEAD)
        return oGuardian

    
    def SetFightStatusAttack(oAgent):
        oOwner = oAgent.m_OwnerObj
        oOwner.m_FightStatusMgr.ChangeStatus(oOwner, MONSTER_STATUS_ATTACK)
        return BT_SUCCESS

    SetFightStatusAttack = staticmethod(SetFightStatusAttack)
    
    def SetFightStatusDefault(oAgent):
        oOwner = oAgent.m_OwnerObj
        oOwner.m_FightStatusMgr.ChangeStatus(oOwner, MONSTER_STATUS_DEFAULT)
        return BT_SUCCESS

    SetFightStatusDefault = staticmethod(SetFightStatusDefault)
    
    def SetActionSMArgs(iType, sArgsName, sArgsValue, oAgent):
        if iType == 1:
            fArgsValue = 0
        elif iType == 2:
            if not sArgsValue:
                return BT_FAILURE
            if sArgsValue.lower() in ('true', '1'):
                fArgsValue = 1
            else:
                fArgsValue = 0
        elif iType == 3:
            if not sArgsValue:
                return BT_FAILURE
            fArgsValue = round(float(sArgsValue), 2)
        else:
            return BT_FAILURE
        cl_snetwar.GS2CMonsterActionSM(oAgent.m_OwnerObj, iType, sArgsName, fArgsValue)
        return BT_SUCCESS

    SetActionSMArgs = staticmethod(SetActionSMArgs)
    
    def SetFightLogicType(iType, oAgent):
        oAgent.m_SceneData.SetFightLogicType(oAgent, iType)
        oAgent.SetData('FightLogic', iType)
        return BT_SUCCESS

    SetFightLogicType = staticmethod(SetFightLogicType)
    
    def Squat(iProb, iTime, oAgent):
        oGame = oAgent.m_Game
        iCurFrame = oGame.GetFrameNum()
        iEndFrame = oAgent.GetData('SquatEndF', 0)
        if iEndFrame:
            if iCurFrame >= iEndFrame:
                oAgent.SetData('SquatEndF', 0)
                return BT_SUCCESS
            return BT_RUNNING
        dDis = oAgent.GetSceneEnemyDis(iOnlyHero = 1)
        for iTarget, fDis in dDis.items():
            if fDis < 5 and oGame.GetObject(iTarget, PY_FLAG_DEAD):
                return BT_SUCCESS
        
        if oGame.Random(100) < iProb:
            oAgent.SetData('Squat', 1)
            cl_snetwar.GS2CMonsterActionSM(oAgent.m_OwnerObj, 2, 'IsSquat', 1)
            iFrame = Time2Frame(iTime)
            oAgent.SetData('SquatEndF', iCurFrame + iFrame)
            oAgent.m_GameSpace.CallDelayUpdate(oAgent, iFrame)
            return BT_RUNNING
        return BT_SUCCESS

    Squat = staticmethod(Squat)
    
    def StandUp(iTime, oAgent):
        oGame = oAgent.m_Game
        iCurFrame = oGame.GetFrameNum()
        iEndFrame = oAgent.GetData('StandEndF', 0)
        if iEndFrame:
            if iCurFrame >= iEndFrame:
                oAgent.SetData('Squat', 0)
                oAgent.SetData('StandEndF', 0)
                return BT_SUCCESS
            return BT_RUNNING
        if oAgent.GetData('Squat', 0):
            cl_snetwar.GS2CMonsterActionSM(oAgent.m_OwnerObj, 2, 'IsSquat', 0)
            iFrame = Time2Frame(iTime)
            oAgent.SetData('StandEndF', iCurFrame + iFrame)
            oAgent.m_GameSpace.CallDelayUpdate(oAgent, iFrame)
            return BT_RUNNING
        return BT_SUCCESS

    StandUp = staticmethod(StandUp)
    
    def ResetSquat(self):
        self.SetData('Squat', 0)
        self.SetData('SquatEndF', 1)
        self.SetData('StandEndF', 1)
        cl_snetwar.GS2CMonsterActionSM(self.m_OwnerObj, 2, 'IsSquat', 0)

    
    def FaceLockEnemy(iKeep, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        lstArgs = [
            oEnemy.m_ID,
            'AI',
            0,
            iKeep]
        oOwner.m_FaceCtrl.FaceTarget(oOwner, *lstArgs)
        oAgent.SetData('LastFaceStatus', (FACE_STATUS_TARGET, lstArgs))
        return BT_SUCCESS

    FaceLockEnemy = staticmethod(FaceLockEnemy)
    
    def TurnToLockEnemy(iTurnTime, iKeep, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        iCurFrame = oAgent.m_Game.GetFrameNum()
        iEndFrame = oAgent.GetData('FaceEnemyEnd', 0)
        if iEndFrame:
            if iEndFrame <= iCurFrame:
                return BT_SUCCESS
            return BT_RUNNING
        oOwner = oAgent.m_OwnerObj
        lstArgs = [
            oEnemy.m_ID,
            'AI',
            iTurnTime,
            iKeep]
        oAgent.SetData('LastFaceStatus', (FACE_STATUS_TARGET, lstArgs))
        oOwner.m_FaceCtrl.FaceTarget(oOwner, *lstArgs)
        if iTurnTime:
            iTurnFrame = Time2Frame(iTurnTime)
            oAgent.SetData('FaceEnemyEnd', iCurFrame + iTurnFrame)
            oAgent.AddCurNodeEndFunc(ClearTurnToLockEnemyEndFrame)
            oAgent.m_GameSpace.CallDelayUpdate(oAgent, iTurnFrame)
            return BT_RUNNING
        return BT_SUCCESS

    TurnToLockEnemy = staticmethod(TurnToLockEnemy)
    
    def CheckLockFaceIsLockTarget(oAgent):
        oOwner = oAgent.m_OwnerObj
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return False
        return oOwner.m_FaceCtrl.m_FaceVictim == oEnemy.m_ID

    CheckLockFaceIsLockTarget = staticmethod(CheckLockFaceIsLockTarget)
    
    def FacePath(oAgent):
        oOwner = oAgent.m_OwnerObj
        if not oAgent.GetData('ForceFaceStatus'):
            oOwner.m_FaceCtrl.FacePath(oOwner, 'AI')
        oAgent.SetData('LastFaceStatus', (FACE_STATUS_PATH, ('AI',)))
        return BT_SUCCESS

    FacePath = staticmethod(FacePath)
    
    def FaceCrossPath(oAgent):
        oOwner = oAgent.m_OwnerObj
        if not oAgent.GetData('ForceFaceStatus'):
            oOwner.m_FaceCtrl.FaceCrossPath(oOwner, 'AI')
        oAgent.SetData('LastFaceStatus', (FACE_STATUS_CROSSPATH, ('AI',)))
        return BT_SUCCESS

    FaceCrossPath = staticmethod(FaceCrossPath)
    
    def FaceDir(bWaitRotate, oAgent):
        (tPos, iTurnSpeed) = oAgent.GetData('FaceDir')
        oOwner = oAgent.m_OwnerObj
        lstArgs = [
            tPos,
            'AI',
            iTurnSpeed]
        (iStatus, vLastDir) = oAgent.GetData('LastFaceStatus', (0, (0, 0, 0)))
        if iStatus == FACE_STATUS_DIR and lstArgs == vLastDir and bWaitRotate and oOwner.m_FaceCtrl.IsRotating():
            return BT_RUNNING
        if not oAgent.GetData('ForceFaceStatus'):
            oOwner.m_FaceCtrl.FaceDir(oOwner, *lstArgs)
        oAgent.SetData('LastFaceStatus', (FACE_STATUS_DIR, lstArgs))
        return BT_SUCCESS

    FaceDir = staticmethod(FaceDir)
    
    def SetFaceDir(x, z, oAgent):
        oAgent.SetData('FaceDir', ((x, 0, z), 0))
        return BT_SUCCESS

    SetFaceDir = staticmethod(SetFaceDir)
    
    def SetFaceMapCenterDir(x, z, oAgent):
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        vFaceDir = (x - vOwner[0], 0, z - vOwner[2])
        oAgent.SetData('FaceDir', (vFaceDir, 0))
        return BT_SUCCESS

    SetFaceMapCenterDir = staticmethod(SetFaceMapCenterDir)
    
    def SetDirToLockEnemy(oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        iTurnSpeed = 0
        tPatrolFace = oAgent.GetConfig('PatrolFace')
        if tPatrolFace:
            (iAngle, iTime) = tPatrolFace
            if iAngle > 0 and iTime > 0:
                iTurnSpeed = int(iAngle // Time2Frame(iTime))
        if not iTurnSpeed:
            iTurnSpeed = oOwner.QueryAttr('TurnSpeed')
        if not iTurnSpeed:
            oAgent.SendUnConfiguredAlert('TurnSpeed')
            return BT_FAILURE
        (tx, ty, tz) = oEnemy.GetPos()
        (ox, oy, oz) = oOwner.GetPos()
        oAgent.SetData('FaceDir', ((tx - ox, 0, tz - oz), iTurnSpeed))
        return BT_SUCCESS

    SetDirToLockEnemy = staticmethod(SetDirToLockEnemy)
    
    def ResumeFaceStatus(self):
        if not self.m_bActive:
            return None
        tPreFaceStatus = self.GetData('LastFaceStatus', ())
        if tPreFaceStatus:
            oOwner = self.m_OwnerObj
            (iStatus, lstArgs) = tPreFaceStatus
            oOwner.m_FaceCtrl.m_FaceVictim = 0
            if iStatus == FACE_STATUS_PATH:
                oOwner.m_FaceCtrl.FacePath(oOwner, *lstArgs)
            elif iStatus == FACE_STATUS_TARGET:
                oOwner.m_FaceCtrl.FaceTarget(oOwner, *lstArgs)

    
    def SeeEnemy(fArea, iAngle, oAgent):
        if oAgent.GetLockEnemy():
            return BT_SUCCESS
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        dDis = oAgent.GetSceneEnemyDis(iOnlyHero = 0)
        if not dDis:
            return BT_FAILURE
        for iTarget, fDis in dDis.items():
            if fDis > fArea:
                continue
            oTarget = oGame.GetObject(iTarget, PY_FLAG_MONSTERTARGET)
            if not oTarget:
                continue
            if oAgent.IsHeroInSight(oOwner, oTarget, iAngle):
                oAgent.SetLockEnemy(iTarget)
                return BT_SUCCESS
        
        return BT_FAILURE

    SeeEnemy = staticmethod(SeeEnemy)
    
    def RecvDamHateAtt(oAgent):
        iAttack = oAgent.GetTreeVar('Target', 0)
        oGame = oAgent.m_Game
        oEnemy = oGame.GetObject(iAttack, PY_FLAG_DEAD)
        if oEnemy:
            oAgent.SetLockEnemy(iAttack)
            return BT_SUCCESS
        return BT_FAILURE

    RecvDamHateAtt = staticmethod(RecvDamHateAtt)
    
    def CheckCanSeeLock(oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return False
        return oAgent.IsHeroInSight(oAgent.m_OwnerObj, oEnemy, 180, iUsePerform = 1)

    CheckCanSeeLock = staticmethod(CheckCanSeeLock)
    
    def CheckInSigntLock(iAngle, bBlock, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return False
        return oAgent.IsHeroInSight(oAgent.m_OwnerObj, oEnemy, iAngle, iUsePerform = 0, bBlock = bBlock)

    CheckInSigntLock = staticmethod(CheckInSigntLock)
    
    def CheckLockCoveredByMonster(oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return False
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        vTarget = oTarget.GetPos()
        vOwner = (vOwner[0], vOwner[1] + oOwner.m_ModelHeight * 0.85, vOwner[2])
        vTarget = (vTarget[0], vTarget[1] + oTarget.m_ModelHeight * 0.85, vTarget[2])
        tRetPos = oAgent.m_Game.Scene_RaycastSingle(oOwner.m_Scene, vOwner, vTarget, PXMASK_SIGHTBLK | PXMASK_MONSTER, {
            'PassID': oOwner.m_ID })
        iVictim = tRetPos[0]
        if iVictim != -1:
            oVictim = oAgent.m_Game.GetObject(iVictim, PY_FLAG_DEAD)
            if oVictim and oVictim.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
                return True
        return False

    CheckLockCoveredByMonster = staticmethod(CheckLockCoveredByMonster)
    
    def CheckInLockEnemySight(iAngle, fDis, bBlock, oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return False
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        vTarget = oTarget.GetPos()
        if not cl_math.CheckDistance3D(vTarget, vOwner, fDis):
            return False
        bSight = oAgent.IsHeroInSight(oOwner, oTarget, iAngle, iUsePerform = 1, bBlock = bBlock, bReverse = True)
        return bSight

    CheckInLockEnemySight = staticmethod(CheckInLockEnemySight)
    
    def CheckLockAlive(oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return False
        if oTarget.IsDead():
            return False
        return True

    CheckLockAlive = staticmethod(CheckLockAlive)
    
    def GetSceneEnemyDis(self, iOnlyHero = 0):
        dDis = self.GetCache('SceneDis', { })
        if dDis:
            return dDis
        oGame = self.m_Game
        oOwner = self.m_OwnerObj
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        if not oScene:
            return { }
        lstEnemy = list(oScene.m_Heros) if iOnlyHero else oScene.m_MonsterEnemy
        if not lstEnemy:
            return { }
        dDis = oGame.Scene_GetTargetDisMap(oOwner.m_ID, lstEnemy)
        self.SetCache('SceneDis', dDis)
        return dDis

    
    def IsHeroInSight(self, oOwner, oTarget, iAngle, iUsePerform = 0, bBlock = True, bReverse = False):
        dInSight = self.GetCache('InSight', { })
        if oTarget.m_ID in dInSight:
            (iCacheAngle, bRes, iCacheUse, bCacheBlock, bCacheReverse) = dInSight[oTarget.m_ID]
            if bReverse == bCacheReverse and bBlock == bCacheBlock and iUsePerform == iCacheUse:
                if bRes and iAngle >= iCacheAngle:
                    return bRes
                if not bRes and iAngle <= iCacheAngle:
                    return bRes
        vOwner = oOwner.GetPos()
        vTarget = oTarget.GetPos()
        if cl_math.IsPlaneEqual(vOwner, vTarget):
            return True
        if iUsePerform:
            fOwnerCheckHeight = self.m_CurPerformUseHeight if self.m_CurPerformUseHeight else oOwner.m_ModelHeight * 0.55
        else:
            fOwnerCheckHeight = oOwner.m_ModelHeight * 0.85
        vOwner = (vOwner[0], vOwner[1] + fOwnerCheckHeight, vOwner[2])
        vTarget = (vTarget[0], vTarget[1] + oTarget.m_ModelHeight * 0.93, vTarget[2])
        if iAngle < 180:
            if bReverse:
                vFace = oTarget.GetFacing()
                disp = cl_math.Vec3Minus(vOwner, vTarget)
            else:
                vFace = oOwner.GetFacing()
                disp = cl_math.Vec3Minus(vTarget, vOwner)
            if cl_math.CheckVector2Angle(disp, vFace, iAngle):
                return False
        oGame = self.m_Game
        if bBlock:
            bSight = not oGame.Scene_RaycastAnyHit(oOwner.m_Scene, vOwner, vTarget, PXMASK_SIGHTBLK)
        else:
            bSight = True
        dInSight[oTarget.m_ID] = (iAngle, bSight, iUsePerform, bBlock, bReverse)
        self.SetCache('InSight', dInSight)
        self.m_SceneData.SetSightData(oOwner.m_ID, oTarget.m_ID, bSight)
        if bSight:
            self.UpdateData('LastSee', {
                oTarget.m_ID: oGame.GetFrameNum() })
        return bSight

    
    def StartAttack(iMethod, iIntervalTime, oAgent):
        oGame = oAgent.m_Game
        iCurFrame = oGame.GetFrameNum()
        tLast = oAgent.GetData('StartAttackResult', None)
        if tLast:
            (iLastFrame, bLastResult) = tLast
            if iCurFrame < iLastFrame + Time2Frame(iIntervalTime):
                return bLastResult
        iTendency = 0
        iStartFrame = oAgent.m_CatchStartFrame
        if iMethod == 0:
            if iStartFrame:
                iCatchFrame = iCurFrame - iStartFrame
                iTendency = 10 * iCatchFrame // GAME_FRAME
            else:
                iTendency = 100
        elif iMethod == 1:
            oOwner = oAgent.m_OwnerObj
            iCatchFrame = iCurFrame - iStartFrame
            oSceneData = oAgent.m_SceneData
            iTotalPlayer = oSceneData.Query('TotalPlayer', 0)
            if not iTotalPlayer:
                iTotalPlayer = oAgent.m_Game.GetWarMgr().GetAllPlayerCnt()
                oSceneData.Set('TotalPlayer', iTotalPlayer)
            fOverAllChargeCF = oSceneData.GetCombatForceByFightLogic(FIGHT_LOGIC_OVERALLCHARGE)
            fOverAllGuerrillaCF = oSceneData.GetCombatForceByFightLogic(FIGHT_LOGIC_OVERALLGUERRILLA)
            fOverAllAwaitCF = oSceneData.GetCombatForceByFightLogic(FIGHT_LOGIC_OVERALLAWAIT)
            fCombatForceVar = fOverAllChargeCF * 3 + fOverAllGuerrillaCF * 2 + fOverAllAwaitCF
            oTarget = oAgent.GetLockEnemy()
            fDistToTarget = cl_math.CalDistance(oOwner.GetPos(), oTarget.GetPos()) if oTarget else 1000
            fDisVar = max(0, (fDistToTarget - 5) * 0.5)
            iTendency = (iCatchFrame // GAME_FRAME) * max(3, 20 * iTotalPlayer - fCombatForceVar - fDisVar)
        elif iMethod == 2:
            iIntervalFrame = Time2Frame(iIntervalTime)
            if not iIntervalFrame:
                sErrKey = 'IntervalTimeErr'
                if not oAgent.GetData(sErrKey, 0):
                    oAgent.SetData(sErrKey, 1)
                    oOwner = oAgent.m_OwnerObj
                    BehaviorLog.Alert('%s %s %s intervaltime %s err' % (oGame.m_ID, oGame.m_WarMgr.m_SID, oOwner.m_SID, iIntervalTime))
                iIntervalFrame = GAME_FRAME
            if iStartFrame:
                iPastFrame = iCurFrame - iStartFrame
                iTendency = (iPastFrame // iIntervalFrame) * 10
            else:
                oAgent.m_CatchStartFrame = iCurFrame
        bRet = oGame.Random(100) < iTendency
        oAgent.SetData('StartAttackResult', (iCurFrame, bRet))
        if not bRet and iMethod == 2:
            oAgent.m_GameSpace.CallDelayUpdate(oAgent, iIntervalFrame)
        return bRet

    StartAttack = staticmethod(StartAttack)
    
    def ChoosePosFarAwayFromEnemy(fDis, oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        vCenter = (132.4, 0, 133)
        fRadius = 34
        vTarget = oTarget.GetPos()
        vDir = cl_math.Vec3Minus(vCenter, vTarget)
        iAngle = 179
        oGame = oAgent.m_Game
        for _ in range(5):
            vPos = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vTarget, vDir, fDis, fRadius * 2, 1, iAngle)
            if not vPos or not cl_math.CheckDistance(vPos, vCenter, fRadius):
                iAngle -= 30
                continue
        else:
            vTarget = oGame.Scene_NavMeshRayCast(oOwner.m_Scene, vCenter, vTarget)
            vPos = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vTarget, vDir, fDis, fRadius * 2, 1, 179)
            if not vPos:
                return BT_FAILURE
        oAgent.SetData('ArrivePos', vPos)
        return BT_SUCCESS

    ChoosePosFarAwayFromEnemy = staticmethod(ChoosePosFarAwayFromEnemy)
    
    def FlashToPos(oAgent):
        vTarget = oAgent.GetData('ArrivePos')
        if not vTarget:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        oOwner.WalkTo(vTarget)
        return BT_SUCCESS

    FlashToPos = staticmethod(FlashToPos)
    
    def ChooseMapCenterPos(oAgent):
        vCenter = oAgent.GetData('MapCenter', None)
        if not vCenter:
            oOwner = oAgent.m_OwnerObj
            vCenter = (132.4, 3, 133)
            vCenter = oAgent.m_Game.Scene_NavMeshRayCast(oOwner.m_Scene, vCenter, (vCenter[0], 0, vCenter[2]))
            if not oOwner.m_LineIdx:
                oGame = oAgent.m_Game
                oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
                if oScene.m_SID != 1020201:
                    vCenter = oOwner.GetPos()
            oAgent.SetData('MapCenter', vCenter)
        oAgent.SetData('ArrivePos', vCenter)
        oAgent.SetData('vEnd', vCenter)
        return BT_SUCCESS

    ChooseMapCenterPos = staticmethod(ChooseMapCenterPos)
    
    def ChooseEnemyPos(oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return BT_FAILURE
        vTarget = oTarget.GetPos()
        oAgent.SetData('ArrivePos', vTarget)
        oAgent.SetData('vEnd', vTarget)
        return BT_SUCCESS

    ChooseEnemyPos = staticmethod(ChooseEnemyPos)
    
    def TurningMove(iLimitAngle, oAgent):
        oOwner = oAgent.m_OwnerObj
        oAgent.AddCurNodeEndFunc(TurningEndFunc)
        oOwner.m_FaceCtrl.FacePath(oOwner, 'KeepTurning')
        oOwner.m_MoveCtrl.SetPathMode('TurningMove', PATHMODE_GHOST)
        return KeepTurning(oAgent, iLimitAngle)

    TurningMove = staticmethod(TurningMove)
    
    def TurningMoveToLockTarget(iLimitAngle, oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return BT_FAILURE
        vTarget = oTarget.GetPos()
        oAgent.SetData('ArrivePos', vTarget)
        oOwner = oAgent.m_OwnerObj
        oAgent.AddCurNodeEndFunc(TurningEndFunc)
        oOwner.m_FaceCtrl.FacePath(oOwner, 'KeepTurning')
        oOwner.m_MoveCtrl.SetPathMode('TurningMove', PATHMODE_GHOST)
        return KeepTurning(oAgent, iLimitAngle)

    TurningMoveToLockTarget = staticmethod(TurningMoveToLockTarget)
    
    def PathMove(oAgent):
        lstPath = oAgent.GetData('ArrivePath')
        if not lstPath:
            return BT_FAILURE
        oAgent.AddCurNodeEndFunc(PathMoveEnd)
        iOldIdx = oAgent.GetData('LastArrIdx', 0)
        if iOldIdx == -1:
            return BT_SUCCESS
        if iOldIdx:
            return BT_RUNNING
        oOwner = oAgent.m_OwnerObj
        oMoveCtrl = oOwner.m_MoveCtrl
        if oAgent.DirectMove(oAgent.m_OwnerObj, lstPath, PathMoveEndCB) and oMoveCtrl.m_ArriveInfo:
            oAgent.SetData('LastArrIdx', oMoveCtrl.m_ArriveInfo[0])
            return BT_RUNNING
        return BT_FAILURE

    PathMove = staticmethod(PathMove)
    
    def ChooseCurvePathToArrivePos(iSection, fMinDis, fArg1, fArg2, oAgent):
        vPos = oAgent.GetData('ArrivePos')
        if not vPos:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        vStart = oOwner.GetPos()
        lstPath = oAgent.m_Game.Scene_CurvePathDataInMesh(oAgent.m_OwnerObj.m_Scene, vStart, vPos, iSection, fMinDis, fArg1, fArg2)
        oAgent.SetData('ArrivePath', lstPath)
        if oAgent.m_Game.GetWarMgr().Query('DebugRay'):
            debug.ClearDebugLine(oAgent.m_Game, debug.LINE_TILE)
            for i in range(len(lstPath) - 1):
                (ox, oy, oz) = lstPath[i]
                (tx, ty, tz) = lstPath[i + 1]
                debug.DebugLine(oAgent.m_Game, ox, oy, oz, tx, ty, tz, 65280, debug.LINE_TILE)
            
        return BT_SUCCESS

    ChooseCurvePathToArrivePos = staticmethod(ChooseCurvePathToArrivePos)
    
    def AbsoluteArcMove(fDis, iPosCnt, iHalfAngle, iStopTime, oAgent):
        oAgent.AddCurNodeEndFunc(AbsoluteArcMoveEnd)
        iOldIdx = oAgent.GetData('LastArrIdx', 0)
        if iOldIdx == -1:
            return BT_SUCCESS
        oGame = oAgent.m_Game
        iCurFrame = oGame.GetFrameNum()
        iStopFrame = oAgent.GetData('StopFrame', 0)
        if iStopFrame and iCurFrame >= iStopFrame:
            return BT_SUCCESS
        if iOldIdx:
            return BT_RUNNING
        oOwner = oAgent.m_OwnerObj
        vCenter = (32, 0, 4.7)
        vOwner = oOwner.GetPos()
        iClockWise = 1 if vOwner[0] > vCenter[0] else -1
        iDebug = oGame.GetWarMgr().Query('DebugRay')
        lstPath = oAgent.GetData('ArrivePath')
        if not lstPath:
            vStartDir = cl_math.Vec3Minus(vOwner, vCenter)
            vEndDir = (1, 0, 0)
            lstPath = []
            iTotalAngle = cl_math.CalAngle2D(vStartDir, vEndDir) + iHalfAngle
            iAngle = iTotalAngle // iPosCnt
            if not iAngle:
                return BT_SUCCESS
            if iDebug:
                debug.ClearDebugLine(oGame, debug.LINE_NORMAL)
            for i in range(1, iPosCnt):
                vPos = cl_math.Vec3DestPosDirPlane(vCenter, vStartDir, fDis, i * iAngle * iClockWise)
                iMoveAngle = cl_math.CalAngle3D((0, 0, 1), cl_math.Vec3Minus(vPos, vCenter))
                if iMoveAngle > iHalfAngle:
                    break
                lstPath.append(vPos)
                if iDebug:
                    debug.DebugCircle(oGame, vPos, 0.5, debug.LINE_NORMAL)
            
            if not lstPath:
                return BT_SUCCESS
            oAgent.SetData('ArrivePath', lstPath)
        oMoveCtrl = oOwner.m_MoveCtrl
        if oAgent.DirectMove(oOwner, lstPath, AbsoluteArcMoveEndCB, iGround = 0):
            iWaitFrame = Time2Frame(iStopTime)
            iStopFrame = iCurFrame + iWaitFrame
            oAgent.SetData('StopFrame', iStopFrame)
            if oMoveCtrl.m_ArriveInfo:
                oAgent.SetData('LastArrIdx', oMoveCtrl.m_ArriveInfo[0])
                oAgent.m_GameSpace.CallDelayUpdate(oAgent, iWaitFrame)
                return BT_RUNNING
        return BT_FAILURE

    AbsoluteArcMove = staticmethod(AbsoluteArcMove)
    
    def ArcMove(fDis, iPosCnt, iHalfAngle, iStopTime, oAgent):
        oAgent.AddCurNodeEndFunc(ArcMoveEnd)
        iOldIdx = oAgent.GetData('LastArrIdx', 0)
        if iOldIdx == -1:
            return BT_SUCCESS
        oGame = oAgent.m_Game
        iCurFrame = oGame.GetFrameNum()
        iStopFrame = oAgent.GetData('StopFrame', 0)
        if iStopFrame and iCurFrame >= iStopFrame:
            return BT_SUCCESS
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        vCenter = (32, 0, 4.7)
        vOwner = oOwner.GetPos()
        vEnemy = oEnemy.GetPos()
        vDir = cl_math.Vec3Minus(vCenter, vOwner)
        vCompareDir = cl_math.Vec3Minus(vEnemy, vOwner)
        iClockWise = 1 if cl_math.VectorCross2D(vDir, vCompareDir) < 0 else -1
        iLastClockWise = oAgent.GetData('ClockWise', 0)
        if iLastClockWise and iLastClockWise != iClockWise:
            return BT_SUCCESS
        if iOldIdx:
            return BT_RUNNING
        iDebug = oGame.GetWarMgr().Query('DebugRay')
        lstPath = oAgent.GetData('ArrivePath')
        if not lstPath:
            vStartDir = cl_math.Vec3Minus(vOwner, vCenter)
            vEndDir = cl_math.Vec3Minus((vEnemy[0], vOwner[1], vEnemy[2]), vCenter)
            lstPath = []
            iTotalAngle = cl_math.CalAngle2D(vStartDir, vEndDir)
            iAngle = iTotalAngle // iPosCnt
            if not iAngle:
                return BT_SUCCESS
            if iDebug:
                debug.ClearDebugLine(oGame, debug.LINE_NORMAL)
            for i in range(1, iPosCnt):
                vPos = cl_math.Vec3DestPosDirPlane(vCenter, vStartDir, fDis, i * iAngle * iClockWise)
                iMoveAngle = cl_math.CalAngle3D((0, 0, 1), cl_math.Vec3Minus(vPos, vCenter))
                if iMoveAngle > iHalfAngle:
                    break
                lstPath.append(vPos)
                if iDebug:
                    debug.DebugCircle(oGame, vPos, 0.5, debug.LINE_NORMAL)
            
            if not lstPath:
                return BT_SUCCESS
            oAgent.SetData('ArrivePath', lstPath)
            oAgent.SetData('ClockWise', iClockWise)
        oMoveCtrl = oOwner.m_MoveCtrl
        if oAgent.DirectMove(oOwner, lstPath, ArcMoveEndCB, iGround = 0):
            iWaitFrame = Time2Frame(iStopTime)
            iStopFrame = iCurFrame + iWaitFrame
            oAgent.SetData('StopFrame', iStopFrame)
            if oMoveCtrl.m_ArriveInfo:
                oAgent.SetData('LastArrIdx', oMoveCtrl.m_ArriveInfo[0])
                oAgent.m_GameSpace.CallDelayUpdate(oAgent, iWaitFrame)
                return BT_RUNNING
        return BT_FAILURE

    ArcMove = staticmethod(ArcMove)
    
    def CheckStateChange(sName, oAgent):
        sKey = 'StatePolicy%s' % sName
        dState = oAgent.GetData(sKey, { })
        if not dState:
            return BT_FAILURE
        dWeight = { }
        for iState, (iBase, iPerAdd, iTotalAdd) in dState.items():
            dWeight[iState] = max(iBase + iTotalAdd, 0)
        
        iNextState = ChooseKey(oAgent.m_Game, dWeight)
        for iState, (iBase, iPerAdd, iTotalAdd) in dState.items():
            if iState == iNextState:
                dState[iState] = (iBase, iPerAdd, iTotalAdd + iPerAdd)
                continue
            dState[iState] = (iBase, iPerAdd, 0)
        
        oAgent.SetCache(sKey, iNextState)
        return BT_SUCCESS

    CheckStateChange = staticmethod(CheckStateChange)
    
    def GetNextState(sName, oAgent):
        iNextState = oAgent.GetCache('StatePolicy%s' % sName, -1)
        return iNextState

    GetNextState = staticmethod(GetNextState)
    
    def IsGroupAllDie(iGroup, oAgent):
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLineNode = oLevelCtrl.GetLineNode(oOwner.m_LineIdx)
        if not oLineNode:
            return False
        oMonsterCtrl = oLineNode.m_MonsterCtrl
        return oMonsterCtrl.IsGroupAllDie(iGroup)

    IsGroupAllDie = staticmethod(IsGroupAllDie)
    
    def ChooseShotPF(iType, oAgent):
        oOwner = oAgent.m_OwnerObj
        dCanUse = { }
        lstAllPerform = oOwner.m_Perform.GetAllPerform()
        for oPerform in lstAllPerform:
            if oPerform.m_PFType != PF_TYPE_MONSTERACT:
                continue
            if oPerform.m_SkillShotType != iType:
                continue
            if not oPerform.CanUse(oOwner, { }):
                continue
            dCanUse[oPerform.m_SID] = 1
        
        if not dCanUse:
            return BT_FAILURE
        idx = oAgent.m_Game.Random(len(dCanUse))
        iPerform = list(dCanUse.keys())[idx]
        dPerform = {
            'pfid': iPerform,
            'Multi': (1, 1),
            'Type': MONSTER_PFAI_CATCH }
        oAgent.SetData('CurPFGroupType', MONSTER_PFAI_CATCH)
        oAgent.SetData('CurChosenPF', dPerform)
        oAgent.SetCurPerformDis()
        return BT_SUCCESS

    ChooseShotPF = staticmethod(ChooseShotPF)
    
    def ChooseAttack(oAgent):
        oOwner = oAgent.m_OwnerObj
        iPerform = oOwner.m_AttPerform
        oPerform = oOwner.m_Perform.GetPerform(iPerform)
        if not oPerform or not oPerform.CanUse(oOwner, { }):
            return BT_FAILURE
        dPerform = {
            'pfid': iPerform,
            'Multi': (1, 1),
            'Type': MONSTER_PFAI_CATCH }
        oAgent.SetData('CurPFGroupType', MONSTER_PFAI_CATCH)
        oAgent.SetData('CurChosenPF', dPerform)
        oAgent.SetCurPerformDis()
        return BT_SUCCESS

    ChooseAttack = staticmethod(ChooseAttack)
    
    def ChooseCertainPF(iPerform, oAgent):
        oOwner = oAgent.m_OwnerObj
        oPerform = oOwner.m_Perform.GetPerform(iPerform)
        if not oPerform:
            return BT_FAILURE
        oPerform.DelCDTime(oOwner)
        if not oPerform.CanUse(oOwner, { }):
            return BT_FAILURE
        dPerform = {
            'pfid': iPerform,
            'Multi': (1, 1),
            'Type': MONSTER_PFAI_CATCH }
        oAgent.SetData('CurPFGroupType', MONSTER_PFAI_CATCH)
        oAgent.SetData('CurChosenPF', dPerform)
        oAgent.SetCurPerformDis()
        return BT_SUCCESS

    ChooseCertainPF = staticmethod(ChooseCertainPF)
    
    def ChoosePF(iType, oAgent):
        if oAgent.m_PFAI:
            oEnemy = oAgent.GetLockEnemy()
            dExtra = { }
            if not oEnemy:
                oAgent.ChooseHateTarget(0, oAgent)
                oEnemy = oAgent.GetLockEnemy()
                if not oEnemy:
                    return BT_FAILURE
            dExtra['Enemy'] = oEnemy
            fChoosePFMinDis = oAgent.GetData('ChoosePFMinDis')
            if fChoosePFMinDis:
                oAgent.SetData('ChoosePFMinDis', 0)
                dExtra['ChoosePFMinDis'] = fChoosePFMinDis
            fChoosePFMaxDis = oAgent.GetData('ChoosePFMaxDis')
            if fChoosePFMaxDis:
                oAgent.SetData('ChoosePFMaxDis', 0)
                dExtra['ChoosePFMaxDis'] = fChoosePFMaxDis
            iBanPF = oAgent.GetData('BanFirstPF', 0)
            if iBanPF:
                oAgent.SetData('BanFirstPF', 0)
                dExtra['BanFirstPF'] = iBanPF
            oOwner = oAgent.m_OwnerObj
            dChosen = oAgent.m_PFAI.ChoosePFGroup(oOwner, iType, dExtra)
            if dChosen:
                if iType == MONSTER_PFAI_DODGE:
                    iCur = oOwner.m_Game.GetFrameNum()
                    oAgent.SetData('DodgeLastFrame', iCur)
                oAgent.SetData('CurPFGroup', dChosen)
                oAgent.SetData('PFTotal', 0)
                oAgent.SetData('CurPFGroupType', iType)
                for iPerform, iCntLower, iCntUpper, _ in dChosen.values():
                    dPerform = {
                        'pfid': iPerform,
                        'Multi': (iCntLower, iCntUpper),
                        'Type': iType }
                    oAgent.SetData('CurChosenPF', dPerform)
                    oAgent.SetCurPerformDis()
                    return BT_SUCCESS
                
        return BT_FAILURE

    ChoosePF = staticmethod(ChoosePF)
    
    def UsePerformGroup(oAgent):
        dChosen = oAgent.GetData('CurPFGroup')
        if not dChosen:
            return oAgent.Attack(oAgent)
        oAgent.AddCurNodeEndFunc(UsePerformGroupEnd)
        iTotalCnt = oAgent.GetData('PFTotal', 0)
        if iTotalCnt == -1:
            return BT_SUCCESS
        if not iTotalCnt:
            iTotalCnt = len(dChosen)
            oAgent.SetData('PFTotal', iTotalCnt)
        DelayUsePFGroup(oAgent, iTotalCnt)
        iUsedCnt = oAgent.GetData('PFUsed', 0)
        if iUsedCnt == -1:
            return BT_FAILURE
        if iUsedCnt >= iTotalCnt and not oAgent.m_OwnerObj.CheckCastingAndBackSwingByPF(oAgent.GetCurPerformSID()):
            return BT_SUCCESS
        return BT_RUNNING

    UsePerformGroup = staticmethod(UsePerformGroup)
    
    def KeepBulletFill(oAgent):
        if oAgent.m_PFAI:
            iFillPerform = oAgent.m_PFAI.GetFillBullet()
            oOwner = oAgent.m_OwnerObj
            if oOwner.CheckCastingAndBackSwingByPF(iFillPerform):
                return BT_RUNNING
            if oAgent.GetData('LastFillPerform', 0) == iFillPerform:
                oAgent.SetData('LastFillPerform', 0)
                oAgent.SetData('ShootRecord', 0)
                return BT_SUCCESS
            iShootRecord = oAgent.GetData('ShootRecord', 0)
            if oAgent.m_PFAI.NeedFillBullet(oOwner, iShootRecord, dExtraInfo = { }):
                oPerform = oOwner.GetPerformIfNoThenNew(iFillPerform)
                iRet = cl_war.UsePerform(oOwner, oPerform, { })
                if iRet and oOwner.CheckCastingAndBackSwingByPF(iFillPerform):
                    oAgent.SetData('LastFillPerform', iFillPerform)
                    return BT_RUNNING
        return BT_SUCCESS

    KeepBulletFill = staticmethod(KeepBulletFill)
    
    def IsPerformUseArea(oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return False
        oOwner = oAgent.m_OwnerObj
        oPerform = oAgent.GetCurPerform()
        if not oPerform:
            return False
        vOwner = oOwner.GetPos()
        vTarget = oEnemy.GetPos()
        iDis = cl_math.CalDistance3D(vOwner, vTarget)
        iPerformDis = oPerform.GetAttDistance()
        if iDis > iPerformDis and iPerformDis != 0:
            return False
        return True

    IsPerformUseArea = staticmethod(IsPerformUseArea)
    
    def IsPerformShotType(iType, oAgent):
        oPerform = oAgent.GetCurPerform()
        if not oPerform:
            return False
        return oPerform.m_SkillShotType == iType

    IsPerformShotType = staticmethod(IsPerformShotType)
    
    def Attack(oAgent):
        oOwner = oAgent.m_OwnerObj
        oPerform = oAgent.GetCurPerform()
        if not oPerform:
            return BT_FAILURE
        iPerform = oPerform.m_SID
        if oOwner.CheckCastingAndBackSwingByPF(iPerform):
            return BT_RUNNING
        if oAgent.GetData('LastPerform', 0) == iPerform:
            oAgent.SetData('LastPerform', 0)
            oAgent.SetData('CurChosenPF', { })
            if oAgent.GetData('CurPFGroupType') == MONSTER_PFAI_CATCH:
                oAgent.m_CatchStartFrame = oAgent.m_Game.GetFrameNum()
            oAgent.SetData('LastSucceededPF', iPerform)
            return BT_SUCCESS
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return BT_FAILURE
        if oPerform.m_PFType == PF_TYPE_MONSTERACT:
            vEnd = oAgent.GetData('vEnd', ())
            if not vEnd:
                vEnd = oTarget.GetPos()
            else:
                oAgent.SetData('vEnd', ())
            dData = {
                'VID': oTarget.m_ID,
                'vEnd': vEnd,
                'CastingEndFunc': Functor(SkillCastingEndFunc, oOwner, iPerform) }
            dPerform = oAgent.GetData('CurChosenPF', { })
            (iCntLower, iCntUpper) = dPerform['Multi']
            if iCntUpper > 1:
                iUseTimes = oAgent.m_Game.Random((iCntUpper - iCntLower) + 1) + iCntLower
            else:
                iUseTimes = 1
            dData['Custom'] = {
                'BallisticType': iUseTimes,
                'FromAI': True }
            if iPerform in oAgent.m_PFAI.m_UseBulletPF:
                oAgent.UpdateData('ShootRecord', iUseTimes)
                oAgent.SetData('StartAttackResult', None)
            if oAgent.GetData('BanCurPerform', 0):
                oAgent.SetData('BanFirstPF', iPerform)
            iRet = cl_war.UsePerform(oOwner, oPerform, dData)
            dPFRecord = oAgent.GetData('PFRecord', { })
            iOldTimes = dPFRecord[iPerform] if iPerform in dPFRecord else 0
            dPFRecord[iPerform] = iOldTimes + 1
            oAgent.SetData('PFRecord', dPFRecord)
        else:
            return BT_FAILURE
        if iRet:
            if oOwner.CheckCastingAndBackSwingByPF(iPerform):
                oAgent.SetData('LastPerform', iPerform)
                return BT_RUNNING
            oAgent.SetData('CurChosenPF', { })
            if dPerform['Type'] == MONSTER_PFAI_CATCH:
                oAgent.m_CatchStartFrame = oAgent.m_Game.GetFrameNum()
            oAgent.SetData('LastSucceededPF', iPerform)
            return BT_SUCCESS
        return BT_FAILURE

    Attack = staticmethod(Attack)
    
    def RegisterSyncAttack(iPerform, iTime, oAgent):
        oAgent.m_SceneData.RegisterSyncAttack(oAgent, iPerform, Time2Frame(iTime))
        return BT_RUNNING

    RegisterSyncAttack = staticmethod(RegisterSyncAttack)
    
    def SyncAttack(self, iPerform):
        oOwner = self.m_OwnerObj
        if oOwner.m_CastingSkill or oOwner.m_Side == SIDE_TYPE_VERTIGO:
            return None
        if self.ChooseCertainPF(iPerform, self) == BT_SUCCESS:
            self.Attack(self)
            self.SetData('LastPerform', 0)
            self.SetData('CurChosenPF', { })

    
    def HaltPerform(oAgent):
        oOwner = oAgent.m_OwnerObj
        cl_action.HaltAllCasting(oOwner, 'BehaviorTree')
        oAgent.Remove_Call_Out('DelayUsePFGroup')
        oAgent.SetData('PFTotal', -1)
        oAgent.SetData('PFUsed', 0)
        oAgent.SetData('NextPFFrame', 0)
        return BT_SUCCESS

    HaltPerform = staticmethod(HaltPerform)
    
    def GetChoosePF(oAgent):
        return oAgent.GetCurPerformSID()

    GetChoosePF = staticmethod(GetChoosePF)
    
    def GetLastSucceededPF(oAgent):
        return oAgent.GetData('LastSucceededPF', 0)

    GetLastSucceededPF = staticmethod(GetLastSucceededPF)
    
    def LimitChoosePFDistance(fMinDis, fMaxDis, oAgent):
        if fMinDis > 0:
            oAgent.SetData('ChoosePFMinDis', fMinDis)
        if fMaxDis > 0:
            oAgent.SetData('ChoosePFMaxDis', fMaxDis)
        return BT_SUCCESS

    LimitChoosePFDistance = staticmethod(LimitChoosePFDistance)
    
    def BanCurPerformAfterUsing(oAgent):
        oAgent.SetData('BanCurPerform', 1)
        return BT_SUCCESS

    BanCurPerformAfterUsing = staticmethod(BanCurPerformAfterUsing)
    
    def UseMovePosAsSkillEnd(oAgent):
        vPos = oAgent.GetData('ArrivePos', None)
        if not vPos:
            return BT_FAILURE
        oAgent.SetData('vEnd', vPos)
        return BT_SUCCESS

    UseMovePosAsSkillEnd = staticmethod(UseMovePosAsSkillEnd)
    
    def DashToPos(iPerform, oAgent):
        oOwner = oAgent.m_OwnerObj
        oPerform = oOwner.m_Perform.GetPerform(iPerform)
        if not oPerform:
            return BT_FAILURE
        if oOwner.CheckCastingAndBackSwingByPF(iPerform):
            return BT_RUNNING
        if oAgent.GetData('LastPerform', 0) == iPerform:
            oAgent.SetData('LastPerform', 0)
            oAgent.SetData('CurChosenPF', { })
            if oAgent.GetData('CurPFGroupType') == MONSTER_PFAI_CATCH:
                oAgent.m_CatchStartFrame = oAgent.m_Game.GetFrameNum()
            oAgent.SetData('LastSucceededPF', iPerform)
            return BT_SUCCESS
        if oPerform.m_PFType != PF_TYPE_MONSTERACT:
            return BT_FAILURE
        vPos = oAgent.GetData('ArrivePos', None)
        if not vPos:
            return BT_FAILURE
        dData = {
            'vEnd': vPos,
            'CastingEndFunc': Functor(SkillCastingEndFunc, oOwner, iPerform) }
        iRet = cl_war.UsePerform(oOwner, oPerform, dData)
        if iRet:
            if oOwner.CheckCastingAndBackSwingByPF(iPerform):
                oAgent.SetData('LastPerform', iPerform)
                return BT_RUNNING
            oAgent.SetData('CurChosenPF', { })
            oAgent.SetData('LastSucceededPF', iPerform)
            return BT_SUCCESS
        return BT_FAILURE

    DashToPos = staticmethod(DashToPos)
    
    def CheckChooseMovingCastPF(oAgent):
        iPerform = oAgent.GetCurPerformSID()
        if not iPerform:
            return False
        oPerform = oAgent.m_OwnerObj.m_Perform.GetPerform(iPerform)
        if not oPerform:
            return False
        if not oPerform.GetArgValue('MovingCast'):
            return False
        return True

    CheckChooseMovingCastPF = staticmethod(CheckChooseMovingCastPF)
    
    def ComboUsePerform(iPerform, iInterval, iSID, oAgent):
        iCanUseCombo = 1
        oMonster = oAgent.m_OwnerObj
        oGame = oAgent.m_Game
        lstMonster = []
        for iMonsterSummon in oMonster.m_MonsterSummon:
            oMonsterSummon = oGame.GetObject(iMonsterSummon, PY_FLAG_DEAD)
            if not oMonsterSummon:
                continue
            if oMonsterSummon.m_DataSID != iSID:
                continue
            if oMonsterSummon.m_CastingSkill or oMonsterSummon.m_Side == SIDE_TYPE_VERTIGO:
                iCanUseCombo = 0
                oMonsterSummon.m_Agent.SetData('Flag', MONSTERAGENT_FLAG_NOCOMBAUSEPF)
                continue
            lstMonster.append(oMonsterSummon.m_ID)
        
        if not iCanUseCombo:
            return BT_RUNNING
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return BT_FAILURE
        vEnd = oAgent.GetData('vEnd', ())
        if not vEnd:
            vEnd = oTarget.GetPos()
        dData = {
            'VID': oTarget.m_ID,
            'vEnd': vEnd }
        lstMonster.insert(0, oMonster.m_ID)
        iAllNum = len(lstMonster)
        iCurNum = 0
        dCustom = {
            'Interval': iInterval,
            'AllNum': iAllNum }
        dData['Custom'] = dCustom
        for iMonster in lstMonster:
            oMonster = oGame.GetObject(iMonster)
            if not oMonster:
                continue
            oPerform = oMonster.GetPerform(iPerform)
            if not oPerform:
                continue
            if not oPerform.m_PFType & PF_TYPE_ATIVE == PF_TYPE_ATIVE:
                return BT_FAILURE
            iCurNum += 1
            dCustom['CurNum'] = iCurNum
            oMonster.m_Agent.SetData('Flag', 0)
            oMonster.m_Agent.SetData('LastPerform', 0)
            oMonster.m_Agent.SetData('CurChosenPF', { })
            cl_war.UsePerform(oMonster, oPerform, dData)
        
        return BT_SUCCESS

    ComboUsePerform = staticmethod(ComboUsePerform)
    
    def GetCurPerform(self):
        dPerform = self.GetData('CurChosenPF', { })
        if not dPerform:
            return None
        iPerform = dPerform['pfid']
        oPerform = self.m_OwnerObj.GetPerform(iPerform)
        return oPerform

    
    def GetCurPerformSID(self):
        dPerform = self.GetData('CurChosenPF', { })
        if not dPerform:
            return 0
        return dPerform['pfid']

    
    def CurPerformDis(self):
        oPerform = self.GetCurPerform()
        if not oPerform:
            return -1
        return oPerform.GetAttDistance()

    
    def SetCurPerformDis(self):
        oPerform = self.GetCurPerform()
        if not oPerform:
            self.SetData('CurPerformUseDis', 0)
            self.m_CurPerformUseHeight = 0
        else:
            self.SetData('CurPerformUseDis', oPerform.GetAttDistance())
            self.m_CurPerformUseHeight = oPerform.m_UseHeight

    
    def GetPhase(oAgent):
        return oAgent.m_OwnerObj.Phase()

    GetPhase = staticmethod(GetPhase)
    
    def SetPhase(iPhase, oAgent):
        oAgent.m_OwnerObj.SetPhase(iPhase)
        return BT_SUCCESS

    SetPhase = staticmethod(SetPhase)
    
    def GetGuerrillaInterval(oAgent):
        return oAgent.GetConfig('GuerrillaInterval', 0)

    GetGuerrillaInterval = staticmethod(GetGuerrillaInterval)
    
    def GetGuardWaitTime(oAgent):
        return oAgent.GetConfig('GuardTime', 0)

    GetGuardWaitTime = staticmethod(GetGuardWaitTime)
    
    def PlayGuardAct(oAgent):
        iTime = CAgent.GetGuardWaitTime(oAgent)
        oTarget = oAgent.m_OwnerObj
        if not oAgent.Stop():
            return BT_FAILURE
        oState = cl_state.AddState(oTarget, STATE_GUARD_ACT, STATE_TIME_LIMIT, iTime, {
            'AID': oTarget.m_ID,
            'RS': cl_object.reason.CStrReason('警戒动作') })
        if not oState:
            return BT_FAILURE
        oState.Enable(oTarget)
        return BT_SUCCESS

    PlayGuardAct = staticmethod(PlayGuardAct)
    
    def GetHPPercent(sHPAttr, oAgent):
        oTarget = oAgent.m_OwnerObj
        if not oTarget.ValidHPAttr(sHPAttr):
            return 0
        iMax = oTarget.QueryAttr('%sMax' % sHPAttr)
        if iMax <= 0:
            return 0
        sKey = 'm_%s' % sHPAttr
        iNow = oTarget.__dict__[sKey]
        return iNow * 100 / iMax

    GetHPPercent = staticmethod(GetHPPercent)
    
    def GetTotalHPPercent(oAgent):
        oOwner = oAgent.m_OwnerObj
        iTotalHP = oOwner.HP()
        iTotalHPMax = oOwner.QueryAttr('HPMax')
        if oOwner.m_DefendTrend == DEFEND_TREND_SHIELD:
            iTotalHPMax += oOwner.QueryAttr('ShieldMax')
            iTotalHP += oOwner.Shield()
        elif oOwner.m_DefendTrend == DEFEND_TREND_ARMOR:
            iTotalHPMax += oOwner.QueryAttr('ArmorMax')
            iTotalHP += oOwner.Armor()
        return iTotalHP * 100 / iTotalHPMax

    GetTotalHPPercent = staticmethod(GetTotalHPPercent)
    
    def GetRandom(iMin, iMax, oAgent):
        return iMin + oAgent.m_Game.Random(max(0, iMax - iMin))

    GetRandom = staticmethod(GetRandom)
    
    def GetGapRandomNum(iMin, iMax, iGap, oAgent):
        iCnt = (iMax - iMin) // iGap
        if iCnt <= 0:
            return iMin
        iRet = iMin + oAgent.m_Game.Random(iCnt + 1) * iGap
        return iRet

    GetGapRandomNum = staticmethod(GetGapRandomNum)
    
    def UpdateInAdvance(oAgent):
        oAgent.m_GameSpace.CallDelayUpdate(oAgent, iFrame = 1)
        return BT_SUCCESS

    UpdateInAdvance = staticmethod(UpdateInAdvance)
    
    def AddState(iState, iTime, oAgent):
        if iTime:
            iTimeType = STATE_TIME_LIMIT
        else:
            iTimeType = STATE_TIME_FOREVER
        oTarget = oAgent.m_OwnerObj
        oState = cl_state.AddState(oTarget, iState, iTimeType, Time2Frame(iTime), {
            'AID': oTarget.m_ID,
            'RS': cl_object.reason.CStrReason('BehaviorTree') })
        if not oState:
            return BT_FAILURE
        oState.Enable(oTarget)
        return BT_SUCCESS

    AddState = staticmethod(AddState)
    
    def RemoveState(iState, oAgent):
        oTarget = oAgent.m_OwnerObj
        cl_state.RemoveState(oTarget, iState)
        return BT_SUCCESS

    RemoveState = staticmethod(RemoveState)
    
    def CheckHasState(iState, oAgent):
        if oAgent.m_OwnerObj.m_State.GetItemBySID(iState):
            return True
        return False

    CheckHasState = staticmethod(CheckHasState)
    
    def GetCustomData(sKey, oAgent):
        dCustomData = oAgent.GetData('CustomData', { })
        if sKey in dCustomData:
            return dCustomData[sKey]
        return 0

    GetCustomData = staticmethod(GetCustomData)
    
    def SetCustomData(sKey, iValue, oAgent):
        dCustomData = oAgent.GetData('CustomData', { })
        dCustomData[sKey] = iValue
        oAgent.SetData('CustomData', dCustomData)

    SetCustomData = staticmethod(SetCustomData)
    
    def BornAction(oAgent):
        oOwner = oAgent.m_OwnerObj
        iEndFrame = oOwner.m_BornActionEndFrame
        if iEndFrame:
            iCurFrame = oAgent.m_Game.GetFrameNum()
            if iCurFrame >= iEndFrame:
                oOwner.m_BornActionEndFrame = 0
                return BT_SUCCESS
            oAgent.AddCurNodeEndFunc(ClearBornActionEndFrame)
            oAgent.m_GameSpace.CallDelayUpdate(oAgent, iEndFrame - iCurFrame)
            return BT_RUNNING
        return BT_SUCCESS

    BornAction = staticmethod(BornAction)
    
    def AddPatrolEvents(oAgent):
        oAgent.ClearCheckVal(oAgent)
        oAgent.ClearAgentEvent(oAgent)
        oAgent.AddEventDamCheckVal(oAgent)
        oAgent.AddEventAttCheckVal(oAgent)
        oAgent.AddEventMoveCheckVal(oAgent)
        oAgent.AddEventUsePerformCheckVal(oAgent)
        oAgent.AddEventThrowCheckVal(oAgent)
        oAgent.AddEventAttDodgeVal(oAgent)
        oAgent.AddEventDamDodgeVal(oAgent)
        oAgent.AddEventGroupHateVal(oAgent)
        oAgent.AddEventServantPerformCheckVal(oAgent)
        return BT_SUCCESS

    AddPatrolEvents = staticmethod(AddPatrolEvents)
    
    def AddAttackEvents(oAgent):
        oAgent.ClearAgentEvent(oAgent)
        oAgent.AddEventDamHateVal(oAgent)
        oAgent.AddEventAttDodgeVal(oAgent)
        oAgent.AddEventDamDodgeVal(oAgent)
        AddPetActCheckVal(oAgent.m_OwnerObj)
        return BT_SUCCESS

    AddAttackEvents = staticmethod(AddAttackEvents)
    
    def SetActionSMPatrol(oAgent):
        oOwner = oAgent.m_OwnerObj
        oOwner.Set('CacheMoveStatus', STATUS_PATROL)
        if oOwner.Query('ForceMoveStatus'):
            return BT_SUCCESS
        oOwner.m_MoveStatusMgr.ChangeStatus(oOwner, STATUS_PATROL)
        oOwner.AttrClear('MoveSpeed', 'MonsterAgent')
        return BT_SUCCESS

    SetActionSMPatrol = staticmethod(SetActionSMPatrol)
    
    def SetActionSMRun(oAgent):
        oOwner = oAgent.m_OwnerObj
        oOwner.Set('CacheMoveStatus', STATUS_RUN)
        if oOwner.Query('ForceMoveStatus'):
            return BT_SUCCESS
        oOwner.m_MoveStatusMgr.ChangeStatus(oOwner, STATUS_RUN)
        return BT_SUCCESS

    SetActionSMRun = staticmethod(SetActionSMRun)
    
    def SetActionSMSprint(oAgent):
        oOwner = oAgent.m_OwnerObj
        oOwner.Set('CacheMoveStatus', STATUS_SPRINT)
        if oOwner.Query('ForceMoveStatus'):
            return BT_SUCCESS
        oOwner.m_MoveStatusMgr.ChangeStatus(oOwner, STATUS_SPRINT)
        return BT_SUCCESS

    SetActionSMSprint = staticmethod(SetActionSMSprint)
    
    def ClearAgentEvent(oAgent):
        oAgent.ClearAgentAttention()
        oAgent.SetData('MoveCheck', False)
        return BT_SUCCESS

    ClearAgentEvent = staticmethod(ClearAgentEvent)
    
    def AddEventDamCheckVal(oAgent):
        if not oAgent.AgentAddAttention('受伤侦察事件'):
            return BT_FAILURE
        return BT_SUCCESS

    AddEventDamCheckVal = staticmethod(AddEventDamCheckVal)
    
    def AddEventThrowCheckVal(oAgent):
        if not oAgent.AgentAddAttention('投掷技能侦察事件'):
            return BT_FAILURE
        return BT_SUCCESS

    AddEventThrowCheckVal = staticmethod(AddEventThrowCheckVal)
    
    def AddEventUsePerformCheckVal(oAgent):
        if not oAgent.AgentAddAttention('职业技能侦察事件'):
            return BT_FAILURE
        return BT_SUCCESS

    AddEventUsePerformCheckVal = staticmethod(AddEventUsePerformCheckVal)
    
    def AddEventAttCheckVal(oAgent):
        if not oAgent.AgentAddAttention('开枪侦察事件'):
            return BT_FAILURE
        return BT_SUCCESS

    AddEventAttCheckVal = staticmethod(AddEventAttCheckVal)
    
    def AddEventMoveCheckVal(oAgent):
        oAgent.SetData('MoveCheck', True)
        oAgent.SetData('MCPos', { })
        oAgent.CalMoveCheckVal()
        return BT_SUCCESS

    AddEventMoveCheckVal = staticmethod(AddEventMoveCheckVal)
    
    def AddEventJumpCheckVal(oAgent):
        if not oAgent.AgentAddAttention('跳跃侦察事件'):
            return BT_FAILURE
        return BT_SUCCESS

    AddEventJumpCheckVal = staticmethod(AddEventJumpCheckVal)
    
    def AddEventAttDodgeVal(oAgent):
        if not oAgent.AgentAddAttention('开枪闪避事件'):
            return BT_FAILURE
        return BT_SUCCESS

    AddEventAttDodgeVal = staticmethod(AddEventAttDodgeVal)
    
    def AddEventDamDodgeVal(oAgent):
        if not oAgent.AgentAddAttention('受伤闪避事件'):
            return BT_FAILURE
        return BT_SUCCESS

    AddEventDamDodgeVal = staticmethod(AddEventDamDodgeVal)
    
    def AddEventDamBlinkVal(oAgent):
        if not oAgent.AgentAddAttention('受伤瞬移事件'):
            return BT_FAILURE
        return BT_SUCCESS

    AddEventDamBlinkVal = staticmethod(AddEventDamBlinkVal)
    
    def AddEventDamHateVal(oAgent):
        if not oAgent.AgentAddAttention('受伤仇恨事件'):
            return BT_FAILURE
        return BT_SUCCESS

    AddEventDamHateVal = staticmethod(AddEventDamHateVal)
    
    def AddEventGroupHateVal(oAgent):
        iUseGroupHate = oAgent.GetConfig('UseGroupHate', 1)
        if iUseGroupHate and not oAgent.AgentAddAttention('小队仇恨侦察事件'):
            return BT_FAILURE
        return BT_SUCCESS

    AddEventGroupHateVal = staticmethod(AddEventGroupHateVal)
    
    def AddEventServantPerformCheckVal(oAgent):
        if not oAgent.AgentAddAttention('仆从技能侦察事件'):
            return BT_FAILURE
        return BT_SUCCESS

    AddEventServantPerformCheckVal = staticmethod(AddEventServantPerformCheckVal)
    
    def ChoosePsychTarget(fDistance, oAgent):
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        iTarget = oAgent.GetData('PsychTarget', 0)
        if not oGame.GetObject(iTarget, PY_FLAG_DEAD):
            oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
            lstTarget = []
            lstMonster = oScene.GetObjectsByType('Monster')
            for iID in lstMonster:
                if iID == oOwner.m_ID:
                    continue
                oTarget = oGame.GetObject(iID, PY_FLAG_DEAD)
                if not oTarget:
                    continue
                lstTarget.append(iID)
            
            dDis = oGame.Scene_GetTargetDisMap(oOwner.m_ID, lstTarget)
            iNearest = 0
            fMinDis = 999
            for iID, fDis in dDis.items():
                if fDis <= fDistance and fDis < fMinDis:
                    fMinDis = fDis
                    iNearest = iID
            
            iTarget = iNearest
        if iTarget:
            oAgent.SetLockEnemy(iTarget)
            return BT_SUCCESS
        return BT_FAILURE

    ChoosePsychTarget = staticmethod(ChoosePsychTarget)
    
    def SetChooseCrazyTargetNoHate(oAgent):
        oGame = oAgent.m_Game
        dHateData = oAgent.GetData('HateData', { })
        iCurFrame = oGame.GetFrameNum()
        for iHero, dData in dHateData.items():
            dData['Hate'] = [
                0,
                iCurFrame]
            dData['Dam'] = { }
        
        return BT_SUCCESS

    SetChooseCrazyTargetNoHate = staticmethod(SetChooseCrazyTargetNoHate)
    
    def ChooseCrazyTarget(fDistance, iInterval, iCoefficient, oAgent):
        oGame = oAgent.m_Game
        iOldFrame = oAgent.GetData('ChooseCrazyFrame', 0)
        if iOldFrame and oGame.GetFrameNum() - iOldFrame < Time2Frame(iInterval):
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        lstTarget = []
        lstMonster = oScene.GetObjectsByType('Monster')
        for iID in lstMonster:
            if iID == oOwner.m_ID:
                continue
            oTarget = oGame.GetObject(iID, PY_FLAG_DEAD)
            if not oTarget:
                continue
            lstTarget.append(iID)
        
        dDis = oGame.Scene_GetTargetDisMap(oOwner.m_ID, lstTarget)
        iMonster = 0
        fMinDis = fDistance
        for iID, fDis in dDis.items():
            if fDis < fMinDis:
                fMinDis = fDis
                iMonster = iID
        
        iMonsterWeight = 0 if not iMonster else 3000 - fMinDis * 270
        iHeroWeight = 0
        dHateData = oAgent.GetData('HateData', { })
        oNowTarget = oAgent.GetLockEnemy()
        iHero = oNowTarget.m_ID if oNowTarget and oNowTarget.m_FightType & WARRIOR_HERO else 0
        if iHero:
            iDis = cl_math.CalDistance3D(oOwner.GetPos(), oNowTarget.GetPos())
            iHate = dHateData[iHero]['Hate'][0] if iHero in dHateData else 0
            if iDis <= 2:
                iHeroWeight = 3500
            else:
                x = cl_math.math.sqrt(3000 / (iDis - 2))
                iHeroWeight = iHate * iCoefficient // 100 + x
        if iMonsterWeight > iHeroWeight and iMonster:
            oAgent.SetData('ChooseCrazyFrame', oGame.GetFrameNum())
            oAgent.SetLockEnemy(iMonster)
            return BT_SUCCESS
        return BT_FAILURE

    ChooseCrazyTarget = staticmethod(ChooseCrazyTarget)
    
    def FuzzyFarCharge(oAgent):
        return cl_betree.fuzzy.CreateFuzzy('FarCharge')

    FuzzyFarCharge = staticmethod(FuzzyFarCharge)
    
    def FuzzyFarSquareGuerrilla(oAgent):
        return cl_betree.fuzzy.CreateFuzzy('FarSquareGuerrilla')

    FuzzyFarSquareGuerrilla = staticmethod(FuzzyFarSquareGuerrilla)
    
    def FuzzyFarGuerrilla(oAgent):
        return cl_betree.fuzzy.CreateFuzzy('FarGuerrilla')

    FuzzyFarGuerrilla = staticmethod(FuzzyFarGuerrilla)
    
    def FuzzyFarHide(oAgent):
        return cl_betree.fuzzy.CreateFuzzy('FarHide')

    FuzzyFarHide = staticmethod(FuzzyFarHide)
    
    def FuzzyGrenadeHide(oAgent):
        return cl_betree.fuzzy.CreateFuzzy('GrenadeHide')

    FuzzyGrenadeHide = staticmethod(FuzzyGrenadeHide)
    
    def FuzzyGrenadeGuerrilla(oAgent):
        return cl_betree.fuzzy.CreateFuzzy('GrenadeGuerrilla')

    FuzzyGrenadeGuerrilla = staticmethod(FuzzyGrenadeGuerrilla)
    
    def FuzzyOverallCharge(oAgent):
        return cl_betree.fuzzy.CreateFuzzy('OverallCharge')

    FuzzyOverallCharge = staticmethod(FuzzyOverallCharge)
    
    def FuzzyOverallGuerrilla(oAgent):
        return cl_betree.fuzzy.CreateFuzzy('OverallGuerrilla')

    FuzzyOverallGuerrilla = staticmethod(FuzzyOverallGuerrilla)
    
    def FuzzyOverallAwait(oAgent):
        return cl_betree.fuzzy.CreateFuzzy('OverallAwait')

    FuzzyOverallAwait = staticmethod(FuzzyOverallAwait)
    
    def GetLockEnemyPastSightFrame(self):
        iNowFrame = self.m_Game.GetFrameNum()
        oTarget = self.GetLockEnemy()
        dLastSee = self.GetData('LastSee', { })
        if oTarget and oTarget.m_ID in dLastSee:
            iLastSee = dLastSee[oTarget.m_ID]
        else:
            iLastSee = 0
        return iNowFrame - iLastSee

    
    def StateTransition(iState, oAgent):
        oOwner = oAgent.m_OwnerObj
        bBackSwing = False
        if oOwner.m_BackSwingSkill:
            iCurFrame = oAgent.m_Game.GetFrameNum()
            for _, iFrame in oOwner.m_BackSwingSkill.items():
                if iFrame - iCurFrame > 0:
                    bBackSwing = True
                    break
            
        if oOwner.Query('UnusedSkill'):
            return BT_SUCCESS
        if not oOwner.m_CastingSkill:
            pass
        if not bBackSwing and oOwner.m_State.GetItemBySID(iState):
            return BT_FAILURE
        return BT_SUCCESS

    StateTransition = staticmethod(StateTransition)
    
    def ApplyOccupyAttackToken(oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return False
        if not oTarget.m_FightType & WARRIOR_HERO:
            return True
        oGame = oAgent.m_Game
        oSurvivorElement = oGame.m_WarMgr.GetComponent('SurvivorElement')
        if not oSurvivorElement:
            return False
        (iTarget, iAttackCost) = oAgent.GetData('AttackCost', (0, 0))
        if iTarget:
            oSurvivorElement.AddTokenCost(iTarget, -iAttackCost)
            oAgent.SetData('AttackCost', (0, 0))
        iRemainToken = oSurvivorElement.GetRemainTokenNumber(oTarget)
        oOwner = oAgent.m_OwnerObj
        clsData = cl_platformdata.GetMonsterConfig(oOwner.m_DataSID)
        if iRemainToken >= clsData.m_AttackCost:
            oAgent.SetData('AttackCost', (oTarget.m_ID, clsData.m_AttackCost))
            oSurvivorElement.AddTokenCost(oTarget.m_ID, clsData.m_AttackCost)
            return True
        return False

    ApplyOccupyAttackToken = staticmethod(ApplyOccupyAttackToken)
    
    def ReleaseAttackToken(oAgent):
        oGame = oAgent.m_Game
        oSurvivorElement = oGame.m_WarMgr.GetComponent('SurvivorElement')
        if not oSurvivorElement:
            return BT_FAILURE
        (iTarget, iAttackCost) = oAgent.GetData('AttackCost', (0, 0))
        if not iTarget:
            return BT_SUCCESS
        oSurvivorElement.AddTokenCost(iTarget, -iAttackCost)
        oAgent.SetData('AttackCost', (0, 0))
        return BT_SUCCESS

    ReleaseAttackToken = staticmethod(ReleaseAttackToken)
    
    def ForceOccupyAttackToken(oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return BT_FAILURE
        if not oTarget.m_FightType & WARRIOR_HERO:
            return BT_SUCCESS
        oGame = oAgent.m_Game
        oSurvivorElement = oGame.m_WarMgr.GetComponent('SurvivorElement')
        if not oSurvivorElement:
            return BT_FAILURE
        iRemainToken = oSurvivorElement.GetRemainTokenNumber(oTarget)
        if iRemainToken <= 0:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        clsData = cl_platformdata.GetMonsterConfig(oOwner.m_DataSID)
        if iRemainToken >= clsData.m_AttackCost:
            oAgent.SetData('AttackCost', (oTarget.m_ID, clsData.m_AttackCost))
            oSurvivorElement.AddTokenCost(oTarget.m_ID, clsData.m_AttackCost)
        else:
            oAgent.SetData('AttackCost', (oTarget.m_ID, iRemainToken))
            oSurvivorElement.AddTokenCost(oTarget.m_ID, iRemainToken)
        return BT_SUCCESS

    ForceOccupyAttackToken = staticmethod(ForceOccupyAttackToken)
    
    def SetPyFlag(iFlag, iAdd, oAgent):
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        oGame.SetPyFlag(oOwner.m_ID, iFlag, iAdd)
        return BT_SUCCESS

    SetPyFlag = staticmethod(SetPyFlag)
    
    def SetLowHPChaseAsTarget(iState, oAgent):
        oOwner = oAgent.m_OwnerObj
        oState = oOwner.m_State.GetItemBySID(iState)
        if not oState:
            return BT_FAILURE
        if 'ChaseTarget' not in oState.m_Data:
            return BT_FAILURE
        iChaseTarget = oState.m_Data['ChaseTarget']
        if not iChaseTarget:
            return BT_FAILURE
        oAgent.SetLockEnemy(iChaseTarget)
        return BT_SUCCESS

    SetLowHPChaseAsTarget = staticmethod(SetLowHPChaseAsTarget)
    
    def ResetCatchStartFrame(oAgent):
        oAgent.m_CatchStartFrame = oAgent.m_Game.GetFrameNum()
        return BT_SUCCESS

    ResetCatchStartFrame = staticmethod(ResetCatchStartFrame)
    
    def UseCertainPFToPos(iPerform, fPosx, fPosy, fPosz, oAgent):
        oOwner = oAgent.m_OwnerObj
        oPerform = oOwner.GetPerform(iPerform)
        if not oPerform:
            return BT_FAILURE
        if oOwner.CheckCastingAndBackSwingByPF(iPerform):
            return BT_RUNNING
        if oAgent.GetData('LastPerform', 0) == iPerform:
            oAgent.SetData('LastPerform', 0)
            oAgent.SetData('CurChosenPF', { })
            if oAgent.GetData('CurPFGroupType') == MONSTER_PFAI_CATCH:
                oAgent.m_CatchStartFrame = oAgent.m_Game.GetFrameNum()
            oAgent.SetData('LastSucceededPF', iPerform)
            return BT_SUCCESS
        if oPerform.m_PFType == PF_TYPE_MONSTERACT:
            vPos = (fPosx, fPosy, fPosz)
            oAgent.SetData('vEnd', ())
            dData = {
                'VID': 0,
                'vEnd': vPos,
                'CastingEndFunc': Functor(SkillCastingEndFunc, oOwner, iPerform) }
            iUseTimes = 1
            dData['Custom'] = {
                'BallisticType': 1,
                'FromAI': True,
                'CertainPos': True }
            if iPerform in oAgent.m_PFAI.m_UseBulletPF:
                oAgent.UpdateData('ShootRecord', iUseTimes)
                oAgent.SetData('StartAttackResult', None)
            if oAgent.GetData('BanCurPerform', 0):
                oAgent.SetData('BanFirstPF', iPerform)
            oAgent.m_PFAI.m_CurGroup = -1
            iRet = cl_war.UsePerform(oOwner, oPerform, dData)
            dPFRecord = oAgent.GetData('PFRecord', { })
            iOldTimes = dPFRecord[iPerform] if iPerform in dPFRecord else 0
            dPFRecord[iPerform] = iOldTimes + 1
            oAgent.SetData('PFRecord', dPFRecord)
        else:
            return BT_FAILURE
        if iRet:
            if oOwner.CheckCastingAndBackSwingByPF(iPerform):
                oAgent.SetData('LastPerform', iPerform)
                return BT_RUNNING
            oAgent.SetData('CurChosenPF', { })
            oAgent.SetData('LastSucceededPF', iPerform)
            return BT_SUCCESS
        return BT_FAILURE

    UseCertainPFToPos = staticmethod(UseCertainPFToPos)
    
    def CheckArriveShowPos(oAgent):
        if not oAgent.GetConfig('ShowPosID', []) and not oAgent.GetConfig('ShowPos', None):
            return True
        if oAgent.m_OwnerObj.m_State.GetItemBySID(TOSHOWPOS_STATE):
            return True
        return False

    CheckArriveShowPos = staticmethod(CheckArriveShowPos)
    
    def ZigFlyToLockTarget(fCatchDis, fIntervalDis, iShiftAngle, fMinHigh, fMaxHigh, oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return BT_FAILURE
        iTarget = oTarget.m_ID
        vTarget = oTarget.GetPos()
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        if cl_math.CheckDistance3D(vOwner, vTarget, fCatchDis):
            if oAgent.Stop():
                return BT_SUCCESS
            if not oOwner.IsStop():
                return BT_RUNNING
            return BT_FAILURE
        oAgent.AddCurNodeEndFunc(ZigFlyToLockTargetEnd)
        if iTarget == oAgent.GetData('ZigFlyTarget'):
            return BT_RUNNING
        return KeepZigFlying(oAgent, iTarget, fCatchDis, fIntervalDis, iShiftAngle, fMinHigh, fMaxHigh)

    ZigFlyToLockTarget = staticmethod(ZigFlyToLockTarget)
    
    def CheckLockNavMeshRayCast(fCheckDis, oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return False
        oOwner = oAgent.m_OwnerObj
        vStartPos = oOwner.GetPos()
        vEndPos = oTarget.GetPos()
        vPos = oAgent.m_Game.Scene_NavMeshRayCast(oOwner.m_Scene, vStartPos, vEndPos)
        iRealDis = cl_math.CalDistance(vStartPos, vPos)
        return iRealDis >= fCheckDis

    CheckLockNavMeshRayCast = staticmethod(CheckLockNavMeshRayCast)
    
    def SetDivePathPos(fMinDis, fMaxDis, fOffset, oAgent):
        oOwner = oAgent.m_OwnerObj
        oPerform = oOwner.m_Perform.GetPerform(FLYINGKNIGHT_DROP_BOMB)
        if not oPerform:
            return BT_FAILURE
        iLiftHeigh = oPerform.GetArgValue('LiftHeigh')
        iFirstSpeed = oPerform.GetArgValue('FirstSpeed')
        iVerticalSpeed = oPerform.GetArgValue('VerticalSpeed')
        if not iLiftHeigh and iFirstSpeed and iVerticalSpeed:
            BehaviorLog.Alert(f'''怪物{oOwner.m_SID}技能{FLYINGKNIGHT_DROP_BOMB}参数配置错误，请检查''')
            return BT_FAILURE
        oGame = oOwner.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        if not oScene:
            return BT_FAILURE
        lstLive = []
        for iHero in oScene.m_Heros:
            if oGame.GetObject(iHero, PY_FLAG_DEAD):
                lstLive.append(iHero)
        
        if not lstLive:
            return BT_FAILURE
        dDis = oGame.Scene_GetTargetDisMap(oOwner.m_ID, list(lstLive))
        if not dDis:
            return BT_FAILURE
        lstSorted = sorted(dDis, key = dDis.get, reverse = True)
        oTargetHero = oGame.GetObject(lstSorted[0])
        if not oTargetHero:
            return BT_FAILURE
        vTargetHeroPos = oTargetHero.GetPos()
        vOwnPos = oOwner.GetPos()
        vLiftPos = cl_math.Vec3Add(vOwnPos, (0, iLiftHeigh, 0))
        fFirstVerticalDis = (fMinDis / iFirstSpeed) * -iVerticalSpeed
        vFirstVerticalPos = cl_math.Vec3Add(vLiftPos, (0, fFirstVerticalDis, 0))
        tDir = cl_math.Vec3Minus(vTargetHeroPos, vOwnPos)
        vFirstDestPos = cl_math.Vec3DisplaceDir(vFirstVerticalPos, tDir, fMinDis)
        fDis = cl_math.CalDistance(vOwnPos, vTargetHeroPos)
        if fDis <= fMinDis:
            fDis = fMinDis + fOffset
        elif fDis <= fMaxDis - fOffset:
            fDis += fOffset
        vDest = cl_math.Vec3HorizonDisplacePos(vOwnPos, vTargetHeroPos, fDis)
        vTargetPos = (vDest[0], vTargetHeroPos[1], vDest[2])
        oAgent.SetData('LstSubductionPos', [
            vFirstDestPos,
            vTargetPos])
        oAgent.SetData('LstPathPos', [
            vLiftPos,
            vFirstDestPos,
            vTargetPos])
        return BT_SUCCESS

    SetDivePathPos = staticmethod(SetDivePathPos)
    
    def CheckVolumePathValid(oAgent):
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        iScene = oOwner.m_Scene
        fModelRadius = oOwner.m_ModelRadius
        fVerticalOffset = oOwner.m_ModelHeight / 2
        vOwnPos = oOwner.GetPos()
        vCurPos = (vOwnPos[0], vOwnPos[1] + fVerticalOffset, vOwnPos[2])
        lstPathPos = oAgent.GetData('LstPathPos', [])
        index = 0
        for vPos in lstPathPos:
            index += 1
            vPos = (vPos[0], vPos[1] + fVerticalOffset, vPos[2])
            vDir = cl_math.Vec3Minus(vPos, vCurPos)
            fDistance = cl_math.CalDistance3D(vCurPos, vPos)
            lstVictim = oGame.Scene_SweepMultiple(iScene, vCurPos, fModelRadius, vDir, fDistance, PXMASK_GROUNDBLK, {
                'BlockMask': PXMASK_GROUNDBLK })
            if lstVictim:
                return False
            vCurPos = vPos
        
        fGroundDis = oGame.Scene_GroundDistance(iScene, vCurPos, oOwner.m_GroundMaxDis, PXMASK_GROUNDBLK, oOwner.m_ID)
        vCurPos = (vCurPos[0], vCurPos[1] - fGroundDis, vCurPos[2])
        (iRet, _) = oGame.Scene_GetSpace(iScene, vCurPos)
        if not iRet:
            return False
        return True

    CheckVolumePathValid = staticmethod(CheckVolumePathValid)


def DelayUsePFGroup(oAgent, iTotalCnt):
    if not oAgent.IsActive():
        oAgent.SetData('PFUsed', -1)
        return None
    iUsedCnt = oAgent.GetData('PFUsed', 0)
    if iUsedCnt >= iTotalCnt:
        return None
    iCurFrame = oAgent.m_Game.GetFrameNum()
    if iUsedCnt >= 1:
        iNextPFFrame = oAgent.GetData('NextPFFrame', 0)
        if iNextPFFrame:
            if iNextPFFrame <= iCurFrame:
                oAgent.SetData('NextPFFrame', 0)
                dPFGroup = oAgent.GetData('CurPFGroup')
                (iPerform, iCntLower, iCntUpper, _) = dPFGroup[iUsedCnt]
                dPerform = {
                    'pfid': iPerform,
                    'Multi': (iCntLower, iCntUpper),
                    'Type': oAgent.GetData('CurPFGroupType') }
                oAgent.SetData('CurChosenPF', dPerform)
                pfobj = oAgent.GetCurPerform()
                if not pfobj:
                    oAgent.SetData('PFUsed', -1)
                    return None
                pfobj.DelCDTime(oAgent.m_OwnerObj)
            else:
                return None
    iRet = CAgent.Attack(oAgent)
    if iRet == BT_FAILURE:
        oAgent.SetData('PFUsed', -1)
        return None
    if iRet == BT_SUCCESS:
        iUsedCnt += 1
        oAgent.SetData('PFUsed', iUsedCnt)
        if iUsedCnt >= iTotalCnt:
            return None
        dPFGroup = oAgent.GetData('CurPFGroup')
        if iUsedCnt not in dPFGroup:
            oCurrentBT = oAgent.PYGetCurrentBT()
            if oCurrentBT:
                sInfo = oCurrentBT.GetPathName()
                BehaviorLog.Alert('%s err used cnt %s %s %s' % (sInfo, iUsedCnt, iTotalCnt, dPFGroup))
        (_, _, _, iDelayFrame) = dPFGroup[iUsedCnt]
        oAgent.Remove_Call_Out('DelayUsePFGroup')
        if iDelayFrame:
            oAgent.SetData('NextPFFrame', iCurFrame + iDelayFrame)
            oAgent.Call_Out(Functor(DelayUsePFGroup, oAgent, iTotalCnt), iDelayFrame, 'DelayUsePFGroup')
        else:
            oAgent.SetData('NextPFFrame', 1)
            DelayUsePFGroup(oAgent, iTotalCnt)

