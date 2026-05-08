# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39028.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39028.pyc
# Source Generated with Decompyle++
# File: p39028.pyc (Python 3.6)

from cl_only import SendAlert
from cl_commondefines import MODEL_TYPE_BOX
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_modeldefine
from cl_perform.cartoon.defines import CircumPathCartoon
from cl_commondefines import CRT_CHECK_SERVER, DAM_USE_HP, OBJ_ALL, SKILLCACHE_RANDOM, WARRIOR_BUILD, WARRIOR_HERO

class CCartoon2(CircumPathCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerAddState(skill, 8100, 0, 0, { })

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.BuildPushMoveServant(skill, 50, 10, 2)
        if not cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ALL) or cl_action.CheckWarriorHasState(skill, cl_action.GetCurVID(skill), 8088):
            cl_action.VictimAddState(skill, 8088, 50, 0, { })
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetTrapPerformCustomParam(skill, 'damage_to_hero', 3000) * (cl_action.GetPlayRound(skill) * cl_action.GetTrapPerformCustomParam(skill, 'damage_round_percentage', 0.25) + 1) })
        elif cl_action.CheckVictimType(skill, WARRIOR_BUILD, OBJ_ALL):
            if cl_action.CheckVictimSID(skill, 1184):
                cl_action.ChangeVictimDefValue(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * -1, DAM_USE_HP)
            elif cl_action.CheckVictimSID(skill, 1185):
                cl_action.ChangeVictimDefValue(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * -1, DAM_USE_HP)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'LuoHouSealWallPos'), 90, (0, 0, 0), 10, 5, 15, cl_action.GetSkillVarCache(skill, 'SealWallID')[0])

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(CircumPathCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.BuildPushMoveServant(skill, 50, 10, 0)
        if not cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ALL) or cl_action.CheckWarriorHasState(skill, cl_action.GetCurVID(skill), 8088):
            cl_action.VictimAddState(skill, 8088, 50, 0, { })
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetTrapPerformCustomParam(skill, 'damage_to_hero', 3000) * (cl_action.GetPlayRound(skill) * cl_action.GetTrapPerformCustomParam(skill, 'damage_round_percentage', 0.25) + 1) })
        elif cl_action.CheckVictimType(skill, WARRIOR_BUILD, OBJ_ALL):
            if cl_action.CheckVictimSID(skill, 1184):
                cl_action.ChangeVictimDefValue(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * -1, DAM_USE_HP)
            elif cl_action.CheckVictimSID(skill, 1185):
                cl_action.ChangeVictimDefValue(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * -1, DAM_USE_HP)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'LuoHouSealWallPos'), -90, (0, 0, 0), 10, 5, 15, cl_action.GetSkillVarCache(skill, 'SealWallID')[1])

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(CircumPathCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.BuildPushMoveServant(skill, 50, 7, 3)
        if not cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ALL) or cl_action.CheckWarriorHasState(skill, cl_action.GetCurVID(skill), 8088):
            cl_action.VictimAddState(skill, 8088, 50, 0, { })
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetTrapPerformCustomParam(skill, 'damage_to_hero', 3000) * (cl_action.GetPlayRound(skill) * cl_action.GetTrapPerformCustomParam(skill, 'damage_round_percentage', 0.25) + 1) })
        elif cl_action.CheckVictimType(skill, WARRIOR_BUILD, OBJ_ALL):
            if cl_action.CheckVictimSID(skill, 1184):
                cl_action.ChangeVictimDefValue(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * -1, DAM_USE_HP)
            elif cl_action.CheckVictimSID(skill, 1185):
                cl_action.ChangeVictimDefValue(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * -1, DAM_USE_HP)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSceneObjPos(skill, cl_action.GetSkillVarCache(skill, 'SealWallID')[0]), 30, (0, 0, 0), 2, 1, 5, cl_action.GetSkillVarCache(skill, 'SealWallID')[0])

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(CircumPathCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.BuildPushMoveServant(skill, 50, 10, 1)
        if not cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ALL) or cl_action.CheckWarriorHasState(skill, cl_action.GetCurVID(skill), 8088):
            cl_action.VictimAddState(skill, 8088, 50, 0, { })
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetTrapPerformCustomParam(skill, 'damage_to_hero', 3000) * (cl_action.GetPlayRound(skill) * cl_action.GetTrapPerformCustomParam(skill, 'damage_round_percentage', 0.25) + 1) })
        elif cl_action.CheckVictimType(skill, WARRIOR_BUILD, OBJ_ALL):
            if cl_action.CheckVictimSID(skill, 1184):
                cl_action.ChangeVictimDefValue(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * -1, DAM_USE_HP)
            elif cl_action.CheckVictimSID(skill, 1185):
                cl_action.ChangeVictimDefValue(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * -1, DAM_USE_HP)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSceneObjPos(skill, cl_action.GetSkillVarCache(skill, 'SealWallID')[1]), -30, (0, 0, 0), 2, 1, 5, cl_action.GetSkillVarCache(skill, 'SealWallID')[1])

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AttackerAddState(skill, 8093, 500, 1, { })
    cl_action.SetSkillVarCache(skill, 'SealWallID', [
        0,
        0])
    cl_action.SetSkillVarCache(skill, 'LuoHouSealWallPos', (0, 0, 0))
    cl_action.AssignBuildDie(skill, 1184)
    if cl_action.GetAttackerStateCount(skill, 8083, dState = { }) == 0:
        cl_action.CustomPerformAction(skill, 39028, 'RandomFirstPos', [])
        cl_action.CustomPerformAction(skill, 39028, 'CustomCreateBuild', [
            1187])
        cl_action.CustomPerformAction(skill, 39028, 'SealWallInfo2VarCache', [])
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
    else:
        cl_action.CustomPerformAction(skill, 39028, 'SealWallInfo2VarCache', [])
        if cl_action.CheckSkillRandomInRange(skill, 0, 50):
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_RANDOM]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39028
    m_Name = '罗睺封印墙移动'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_Resend = 1
    m_CacheAttr = [
        'DebuffProb']


def CustomCreateBuild(oSkill, *args):
    oGame = oSkill.m_Game
    iObjSID = args[0][0]
    oObstacle = oGame.m_WarData.GetBuildData(iObjSID)
    if not oObstacle:
        SendAlert('err', '技能%d 在战场%d创建%d建筑失败' % (oSkill.m_Base['pfid'], oGame.m_WarMgr.m_SID, iObjSID))
        return None
    oAttack = oSkill.GetAttack()
    iScene = oSkill.m_Base['Scene']
    vCenterPos = oAttack.GetPos()
    vPos = oSkill.m_VarCache['LuoHouSealWallPos']
    lstSeal = []
    iSealNum = 2
    lstArgs = cl_modeldefine.GetModelDefine(oObstacle.m_Shape, 'Box')
    vFace = cl_math.Vec3Minus(vPos, vCenterPos)
    iFlag = 1
    for _ in range(iSealNum):
        fAngle = cl_math.CalRotate2D(cl_math.RotateAroundVector(vFace, (0, iFlag, 0), 90))
        iFlag = -iFlag
        dAddData = {
            'Angle': [
                0,
                fAngle,
                0],
            'Center': [
                0,
                lstArgs[1] * 0.5,
                0],
            'Origin': vPos,
            'SID': iObjSID,
            'Scale': [
                1,
                1,
                1],
            'Shape': MODEL_TYPE_BOX,
            'Size': lstArgs }
        oBuild = oGame.m_ResMgr.CreateBuild(iScene, iObjSID, dAddData)
        lstSeal.append(oBuild.m_ID)
        oAttack.m_FollowDieObjs[oBuild.m_ID] = 1
    
    oAttack.Set('SealWallID', lstSeal)


def SealWallInfo2VarCache(oSkill, *args):
    oAttack = oSkill.GetAttack()
    oSkill.m_VarCache['SealWallID'] = oAttack.Query('SealWallID')


def RandomFirstPos(oSkill, *args):
    oAttack = oSkill.GetAttack()
    oGame = oAttack.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oAttack.m_Scene)
    if 'LuoHouBlockData' not in oScene.m_CustomData:
        SendAlert('err', '39028技能数据缺失,请尽量在罗睺关测试')
        return None
    lstBlockData = oScene.m_CustomData['LuoHouBlockData']
    lstPos = []
    for dBlockData in lstBlockData:
        lstPos.append(dBlockData['lstPos'][1])
    
    vSealWallPos = None
    iSelect = 0
    fMaxDis = -1
    for idx, vPos in enumerate(lstPos):
        fHeroMinDis = 999
        for iHero in oScene.GetHeros():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            fDis = cl_math.CalDistance(oHero.GetPos(), vPos)
            if fDis < fHeroMinDis:
                fHeroMinDis = fDis
        
        if fHeroMinDis > fMaxDis:
            fMaxDis = fHeroMinDis
            iSelect = idx
    
    vSealWallPos = lstPos[iSelect]
    iAssignGroup = oGame.GetWarMgr().Query('AssignGroup')
    if iAssignGroup:
        vSealWallPos = lstPos[iAssignGroup]
    oAttack.Set('FirstSealWallPos', vSealWallPos)
    oSkill.m_VarCache['LuoHouSealWallPos'] = vSealWallPos


def CreateBuildPosBySealWall(oSkill, *args):
    oAttack = oSkill.GetAttack()
    vPos = oAttack.GetPos()
    fDis = args[0][0]
    lstSealWallID = oAttack.Query('SealWallID')
    if not lstSealWallID:
        SendAlert('err', '获取罗睺封印墙信息失败')
        return None
    oGame = oAttack.m_Game
    lstFace = []
    for iSealWall in lstSealWallID:
        oSealWall = oGame.GetObject(iSealWall)
        vFinalPos = oSealWall.Query('CircumPathFinalPos')
        if not vFinalPos:
            SendAlert('err', '获取封印墙最终位置失败。')
            vFinalPos = oSealWall.GetPos()
        lstFace.append(cl_math.Vec3Minus(vFinalPos, vPos))
    
    iAngle = cl_math.CalAngle2D(lstFace[0], lstFace[1])
    iOffsetAngle = iAngle // 3
    lstBuildPos = []
    iFlag = 1
    for vFace in lstFace:
        vFace = cl_math.RotateAroundVector(vFace, (0, 1, 0), iFlag * iOffsetAngle)
        iFlag = -iFlag
        vBuildPos = cl_math.Vec3DisplaceDir(vPos, vFace, fDis)
        lstBuildPos.append(vBuildPos)
    
    oSkill.m_VarCache['StonePillarPosList'] = lstBuildPos

