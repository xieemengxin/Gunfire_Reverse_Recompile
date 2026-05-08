# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39024.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39024.pyc
# Source Generated with Decompyle++
# File: p39024.pyc (Python 3.6)

from cl_only import SendAlert, OutputPos
from cl_pxlayer import PXMASK_BLOCK
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_RECTANGLE, ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, MODEL_TYPE_BOX, MODEL_TYPE_CAPSULE, OBJ_ALL, OBJ_ENEMY, SKILLCACHE_LSTPOS, WARRIOR_HERO

class CCartoon9(DirectPosCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.CustomPerformAction(skill, 39024, 'CustomWalk', [
            1])
        cl_action.PushHeroVictim(skill, (0, 0, 0), 10, 10, 10000, downSpeed = 5, fGravaty = 9.8, angle = 0)
        cl_action.WeaponDamage(skill, {
            'Att': 50 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgDestPosDir(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgSelfFace(skill), 25, 0), (0, 0, 0), [
                10], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon9.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 150, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(TimerCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 450, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 10, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(TimerCartoon):
    m_SID = 10
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.MonsterFaceTarget(skill, cl_action.GetSkillVID(skill), 50, 1)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PushHeroVictim(skill, cl_action.GetSkillVarCache(skill, 'EndPos'), 10, 3, 10000, downSpeed = 0, fGravaty = 9.8, angle = 0)
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetTrapPerformCustomParam(skill, 'damage_to_hero', 3000) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'EndPos'), (0, 0, 0), [
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        for i3 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)), 1):
            cl_action.SetSkillVarCache(skill, 'EndPos', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[i3])
            cl_action.PerformCreateBuild(skill, 1185, MODEL_TYPE_CAPSULE, cl_action.GetSkillVarCache(skill, 'EndPos'), 0, 0, {
                'FollowDie': 1,
                'OffsetCenterHeight': -0.5 })
            cl_action.AddClientEffect(skill, 2028, cl_action.GetSkillVarCache(skill, 'EndPos'), 0, (0, 0, 0))
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.CustomPerformAction(skill, 39024, 'UpdateFinalWarnPos', [
            62,
            50,
            9])

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 8, 12)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.PerformCreateBuild(skill, 1184, MODEL_TYPE_BOX, cl_action.GetSkillVarCache(skill, 'BlockMidPos'), cl_action.GetSkillVarCache(skill, 'BlockAngle'), 700, {
            'FollowDie': 1 })

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ALL):
            cl_action.PushHeroVictim(skill, cl_action.GetSkillVarCache(skill, 'BlockStartPos'), 10, 3, 10000, downSpeed = 0, fGravaty = 9.8, angle = 0)
            cl_action.WeaponDamage(skill, {
                'Att': 50 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'BlockStartPos'), cl_action.GetSkillVarCache(skill, 'BlockEndPos'), [
                30,
                3,
                2], attshape = ATT_SHAPE_RECTANGLE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon10.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillServerCache(skill, 'FinalWarnPosList'))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_LSTPOS])
        for i2 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)), 1):
            cl_action.AddClientEffect(skill, 2026, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[i2], 100, (0, 0, 0))
            cl_action.AddClientEffect(skill, 2027, cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[i2], (0, 10, 0)), 100, (0, 0, 0))
        
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        if cl_action.GetTimerCartoonCurTimes(skill, 2) == 1:
            for i4 in range(0, 8, 1):
                cl_action.AddClientEffect(skill, 2022, cl_action.GetSkillVarCache(skill, 'LuoHouBlockMidPos')[i4], 100, cl_action.GetSkillVarCache(skill, 'LuoHouBlockFace')[i4])
            
        elif cl_action.GetTimerCartoonCurTimes(skill, 2) == 3:
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 0, index = 0)
            for i6 in range(0, 8, 1):
                cl_action.SetSkillVarCache(skill, 'BlockStartPos', cl_action.GetSkillVarCache(skill, 'LuoHouBlockStartPos')[i6])
                cl_action.SetSkillVarCache(skill, 'BlockEndPos', cl_action.GetSkillVarCache(skill, 'LuoHouBlockEndPos')[i6])
                cl_action.SetSkillVarCache(skill, 'BlockMidPos', cl_action.GetSkillVarCache(skill, 'LuoHouBlockMidPos')[i6])
                cl_action.SetSkillVarCache(skill, 'BlockAngle', cl_action.GetSkillVarCache(skill, 'LuoHouBlockAngle')[i6])
                cartoon = { }
                CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
            

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 4)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'LuoHouBlockStartPos', [
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0)])
    cl_action.SetSkillVarCache(skill, 'LuoHouBlockMidPos', [
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0)])
    cl_action.SetSkillVarCache(skill, 'LuoHouBlockEndPos', [
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0)])
    cl_action.SetSkillVarCache(skill, 'LuoHouBlockFace', [
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0)])
    cl_action.SetSkillVarCache(skill, 'LuoHouBlockCentrePos', [
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0)])
    cl_action.SetSkillVarCache(skill, 'LuoHouBlockAngle', [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0])
    cl_action.CustomPerformAction(skill, 39024, 'BlockInfo2VarCache', [])
    cl_action.MonsterAttackerFaceLeastAnglePos(skill, cl_action.GetSkillVarCache(skill, 'LuoHouBlockCentrePos'), 20)
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39024
    m_Name = '罗睺双手砸地'
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
        'ColdTime': 1500,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']


def BlockInfo2VarCache(oSkill, *args):
    oAttack = oSkill.GetAttack()
    oGame = oAttack.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oAttack.m_Scene)
    if 'LuoHouBlockData' not in oScene.m_CustomData:
        SendAlert('err', '39024技能数据缺失,请尽量在罗睺关测试')
        return None
    lstBlockData = oScene.m_CustomData['LuoHouBlockData']
    lstStartPos = []
    lstMidPos = []
    lstEndPos = []
    lstFace = []
    lstAngle = []
    lstCentrePos = []
    for dBlockData in lstBlockData:
        lstPos = dBlockData['lstPos']
        lstStartPos.append(lstPos[0])
        lstMidPos.append(lstPos[1])
        lstEndPos.append(lstPos[2])
        vFace = dBlockData['Face']
        fAngle = cl_math.CalRotate2D(vFace)
        lstAngle.append(fAngle)
        lstFace.append(vFace)
        lstCentrePos.append(dBlockData['CentrePos'])
    
    oSkill.m_VarCache['LuoHouBlockStartPos'] = lstStartPos
    oSkill.m_VarCache['LuoHouBlockMidPos'] = lstMidPos
    oSkill.m_VarCache['LuoHouBlockEndPos'] = lstEndPos
    oSkill.m_VarCache['LuoHouBlockAngle'] = lstAngle
    oSkill.m_VarCache['LuoHouBlockFace'] = lstFace
    oSkill.m_VarCache['LuoHouBlockCentrePos'] = lstCentrePos


def UpdateFinalWarnPos(oSkill, *args):
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    iMaxDis = args[0][0]
    iWarnMaxDis = args[0][1]
    iMinBlockDis = args[0][2]
    oAttack = oSkill.GetAttack()
    vAttackPos = oAttack.GetPos()
    lstPos = []
    lstHero = cl_action.GetLiveHeroID(oSkill, False, iMaxDis)
    for iHero in lstHero:
        oHero = oGame.GetObject(iHero)
        vPos = oHero.GetPos()
        if not cl_math.CheckDistance(vAttackPos, vPos, iWarnMaxDis):
            vPos = cl_math.Vec3DisplacePos(vAttackPos, vPos, iWarnMaxDis)
        vPos = UpdatePosByBlock(oSkill, vPos, iMinBlockDis)
        vRet = oGame.Scene_RaycastSingle(oSkill.m_Base['Scene'], vPos, cl_math.Vec3Add(vPos, (0, -10, 0)), PXMASK_BLOCK)
        if vRet[0] != -1:
            vPos = vRet[1]
        lstPos.append(vPos)
    
    oSkill.m_Collect['FinalWarnPosList'] = lstPos


def UpdatePosByBlock(oSkill, vPos, fMinDis):
    oGame = oSkill.m_Game
    lstBlockPos = oSkill.m_VarCache['LuoHouBlockMidPos']
    oAttack = oSkill.GetAttack()
    vAttackPos = oAttack.GetPos()
    vNearrestPos = None
    fNearrestDis = 999
    for vBlockPos in lstBlockPos:
        fDis = cl_math.CalDistance(vBlockPos, vPos)
        if fDis < fNearrestDis:
            fNearrestDis = fDis
            vNearrestPos = vBlockPos
    
    if not vNearrestPos:
        SendAlert('err', '%s获取最近隔断异常' % OutputPos(vPos))
        return vPos
    (x, z) = cl_math.GetFootPoint(vPos[0], vPos[2], vAttackPos[0], vAttackPos[2], vNearrestPos[0], vNearrestPos[2])
    vFootPos = (x, vPos[1], z)
    fFootDis = cl_math.CalDistance(vFootPos, vPos)
    if fFootDis < fMinDis:
        vDir = cl_math.Vec3Minus(vPos, vFootPos)
        vPos = cl_math.Vec3DisplaceDir(vPos, vDir, fMinDis - fFootDis)
    return vPos


def CustomWalk(oSkill, *args):
    if 'CurVID' not in oSkill.m_Update:
        return None
    fDis = args[0][0]
    oAttack = oSkill.GetAttack()
    vCenterPos = oAttack.GetPos()
    iVictim = oSkill.m_Update['CurVID']
    oVictim = oSkill.m_Game.GetObject(iVictim)
    if not oVictim:
        return None
    if oVictim.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return None
    oAttackPos = oAttack.GetPos()
    vVictimPos = oVictim.GetPos()
    vDir = cl_math.Vec3Minus(vVictimPos, oAttackPos)
    vTargetPos = cl_math.Vec3DisplaceDir(vVictimPos, vDir, fDis)
    oVictim.WalkTo(vTargetPos)

