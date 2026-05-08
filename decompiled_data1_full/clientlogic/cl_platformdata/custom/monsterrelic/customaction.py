# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/monsterrelic/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/monsterrelic/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_only import PY_FLAG_DEAD, PY_FLAG_MONSTERTARGET, SendAlert, ShufferList, Time2Frame, Functor
from cl_commondefines import WARRIOR_HERO, SIDE_TYPE_MONSTER, MODEL_TYPE_SPHERE, MODEL_TYPE_CAPSULE, WARRIOR_MOVEEFFECT, WARRIOR_SCENEQUERY_ENTITYEFFECT
import cl_math
import cl_modeldefine
import cl_gamedebug as debug
import cl_snetwar

def CustomAction25860(oWarrior, oEventCB, dArgs):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' not in dMsgInfo or 'CostCash' not in dArgs:
        return None
    iTarget = dMsgInfo['CurVID']
    oTarget = oWarrior.m_Game.GetObject(iTarget)
    if oTarget and oTarget.m_FightType & WARRIOR_HERO:
        iCostCash = dArgs['CostCash']
        if iCostCash < 0 and -iCostCash > oTarget.m_WarCash:
            iCostCash = -(oTarget.m_WarCash)
        oTarget.AddCash(iCostCash, '25860MRelicAdd')


def CheckGapDistance(vPos, lstCur, fGap):
    for vCurPos in lstCur:
        if cl_math.CheckDistance3D(vCurPos, vPos, fGap):
            return False
    
    return True


def CustomActionBossSummon(oWarrior, oEventCB, dArgs):
    oGame = oWarrior.m_Game
    iScene = oWarrior.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    if not oWarrior.m_Agent:
        return None
    dHate = oWarrior.m_Agent.GetData('HateData', { })
    if not dHate:
        return None
    iSummonSID = dArgs['sid'] if 'sid' in dArgs else 0
    fMin = dArgs['min'] if 'min' in dArgs else 0
    fMax = dArgs['max'] if 'max' in dArgs else 0
    fGap = dArgs['gap'] if 'gap' in dArgs else 0
    iPerHeroNum = dArgs['num'] if 'num' in dArgs else 1
    iMaxNum = dArgs['maxnum'] if 'maxnum' in dArgs else 20
    iDelayTime = dArgs['delay'] if 'delay' in dArgs else 0
    iEffectSID = dArgs['effect'] if 'effect' in dArgs else 0
    iCur = 0
    lstCurPos = []
    lstSummon = oScene.GetObjectsByType('Summon')
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon, PY_FLAG_DEAD)
        if not oSummon or oSummon.m_SID != iSummonSID:
            continue
        iCur += 1
        lstCurPos.append(oSummon.GetPos())
    
    iRestNum = iMaxNum - iCur
    if iRestNum <= 0:
        return None
    dPos = { }
    dBackupPos = { }
    vDir = (1, 0, 0)
    for iHero in oScene.GetHeros():
        if iHero not in dHate:
            continue
        oHero = oGame.GetObject(iHero, PY_FLAG_MONSTERTARGET)
        if not oHero:
            continue
        dPos[iHero] = []
        dBackupPos[iHero] = []
        vCenter = oHero.GetGroundPos()
        for _i in range(iPerHeroNum):
            for _j in range(5):
                vPos = oGame.Scene_RandomPointSectorInMesh(iScene, vCenter, vDir, fMin, fMax, 0, 180)
                if not vPos:
                    continue
                if not CheckGapDistance(vPos, lstCurPos, fGap):
                    dBackupPos[iHero].append(vPos)
                    continue
                dPos[iHero].append(vPos)
                lstCurPos.append(vPos)
            
        
    
    for iHero, lstPos in dPos.items():
        iNeed = iPerHeroNum - len(lstPos)
        if iNeed <= 0:
            continue
        lstBackupPos = ShufferList(oGame, dBackupPos[iHero], iNeed)
        lstPos.extend(lstBackupPos)
    
    dEffect = { }
    if iEffectSID:
        dPlayer = oScene.GetPlayers()
        for iHero, lstPos in dPos.items():
            for vPos in lstPos:
                iEffectID = oGame.NewNoSceneObjID()
                cl_snetwar.GS2CAddEffect(oGame, iScene, iEffectID, iEffectSID, vPos, dPlayer)
                dEffect[iEffectID] = 1
            
        
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    if iDelayTime:
        func = Functor(CreateSummons, oWarrior, iSummonSID, dPos, dArgs, iPerform, dEffect)
        sKey = oEventCB.m_Key
        oWarrior.Call_Out(func, Time2Frame(iDelayTime), sKey)
    else:
        CreateSummons(oWarrior, iSummonSID, dPos, dArgs, iPerform, dEffect)


def CreateSummons(oWarrior, iSummonSID, dPos, dArgs, iPerform, dEffect):
    if not (oWarrior.m_Scene) or oWarrior.IsDead():
        return None
    oGame = oWarrior.m_Game
    clsSummonData = oGame.m_WarData.GetSummonData(iSummonSID)
    if not clsSummonData:
        SendAlert('err', '战场%s未找到召唤物配置%s' % (oGame.m_WarMgr.m_SID, iSummonSID))
        return None
    iScene = oWarrior.m_Scene
    if dEffect:
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        dPlayer = oScene.GetPlayers()
        for iEffectID in dEffect:
            cl_snetwar.GS2CDeleteEffect(oGame, iScene, iEffectID, dPlayer)
        
    iOwner = oWarrior.m_ID
    tFace = oWarrior.GetFacing()
    tLine = oWarrior.m_LineIdx
    fHeightOffSet = dArgs['height'] if 'height' in dArgs else 0
    iGrade = oWarrior.m_AddGrade if 'SameGrade' in dArgs else 1
    dShapeInfo = { }
    if 'Radius' in dArgs:
        fRadius = dArgs['Radius']
        dShapeInfo = {
            'Shape': MODEL_TYPE_SPHERE,
            'Angle': (0, 0, 0),
            'Scale': (1, 1, 1),
            'Center': (0, 0, 0),
            'Size': (fRadius, fRadius, fRadius) }
    elif 'Capsule' in dArgs:
        tModelData = cl_modeldefine.GetModelDefine(clsSummonData.m_Shape, 'NavMesh')
        dShapeInfo = {
            'Shape': MODEL_TYPE_CAPSULE,
            'Angle': (0, 0, 0),
            'Scale': (1, 1, 1),
            'Center': (0, 0, 0),
            'Size': (tModelData[1], tModelData[0], 0) }
    for iHero, lstPos in dPos.items():
        for vPos in lstPos:
            if fHeightOffSet:
                vPos = (vPos[0], vPos[1] + fHeightOffSet, vPos[2])
            dAddInfo = {
                'Owner': iOwner,
                'Side': SIDE_TYPE_MONSTER,
                'Origin': vPos,
                'Facing': tFace,
                'SrcPerform': iPerform }
            dAddInfo.update(dShapeInfo)
            oSummon = oGame.m_ResMgr.CreateSummon(iScene, iSummonSID, dAddInfo, tLine, iGrade)
            if not oSummon:
                continue
            if oSummon.m_FightType == WARRIOR_SCENEQUERY_ENTITYEFFECT or oSummon.m_PhyModel:
                oSummon.m_PhyModel.rigidbody.E_SetKinematic(True)
                continue
            if oSummon.m_FightType == WARRIOR_MOVEEFFECT:
                oSummon.StartMove(iHero)
        
    

