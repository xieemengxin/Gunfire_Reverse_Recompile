# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39158.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39158.pyc
# Source Generated with Decompyle++
# File: p39158.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, MonsterDashCartoon, SubductionCartoon, TimerCartoon, WinkPosCartoon
from cl_commondefines import ATT_SHAPE_LINE, ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, FIGHT3_KEY_IGNOREUNBALANCE, OBJ_ALL, OBJ_ENEMY, SKILLCACHE_POS, STATE_EFF_DEBAR, WARRIOR_SUMMON
from cl_only import PY_FLAG_EXCLUDEMONSTERHATE

class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cl_action.ClearSkillSummonCreateCollect(skill)
        cl_action.SetSkillServerCache(skill, 'lsthero', cl_action.GetNavMeshHero(skill, (135, 1.5, 135), True))
        cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.GetPosByRelativePosition(skill, [
            (6, 0, 3),
            (6, 0, -3),
            (4, 0, 6),
            (4, 0, -6)], len(cl_action.GetSkillServerCache(skill, 'lsthero')) - 1), WARRIOR_SUMMON, {
            1029: 10 }, {
            'Capsule': 0 }, (0, 0, 0))
        for i1 in range(0, len(cl_action.GetSkillSummonCreate(skill)), 1):
            cl_action.SetSummonLifeTime(skill, cl_action.GetSkillSummonCreate(skill)[i1], cl_action.GetPlayRound(skill) * 500 + 2000)
            cl_action.RandomTraceUnLockHero(skill, cl_action.GetSkillSummonCreate(skill)[i1], cl_action.GetSkillServerCache(skill, 'lsthero'), True)
        

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
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon20(DirectPosCartoon):
    m_SID = 20
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 50 }, { }, sendPFMsg = False)
        if not cl_action.CheckWarriorHasState(skill, cl_action.GetSkillVID(skill), 7963):
            cl_action.PushHeroVictim(skill, cl_action.CrtArgSelfPos(skill), 8, 8, 10000, downSpeed = 9, fGravaty = 9.8, angle = 0, bDirectRotation = False)
            cl_action.VictimAddState(skill, 7963, 200, 1, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False), [
                7], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon19(TimerCartoon):
    m_SID = 19
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon20.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon20.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 20)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(MonsterDashCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.StartBackSwing(skill, 100)
        cl_action.SkillHaltSelf(skill)

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
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'CenterPos'), (cl_action.CountDistance3D(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetSkillVarCache(skill, 'CenterPos')) / 50) * 100, 0, 50, False, False, False, checkDis = 0, start = cl_action.CrtArgSelfPos(skill), offSetY = 0, staticbreak = False, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ENEMY, Collision = False, BulletHeightScale = 1, BulletRadiusScale = 1)

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
        cartoon = { }
        CCartoon9.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 130, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(MonsterDashCartoon):
    m_SID = 4
    
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
            cls.EnableCtrl(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), 1000, 0, 50, False, False, False, checkDis = 0, start = cl_action.CrtArgSelfPos(skill), offSetY = 0, staticbreak = False, CheckTime = 10, StopDis = 1, CheckHalt = False, targettype = OBJ_ENEMY, Collision = False, BulletHeightScale = 1, BulletRadiusScale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
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
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 130, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(MonsterDashCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon19.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetTornadoDashPos(skill, cl_action.GetSkillVarCache(skill, 'CenterPos'), 70, PY_FLAG_EXCLUDEMONSTERHATE))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_POS])
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), 1000, 0, 50, False, False, False, checkDis = 0, start = cl_action.CrtArgSelfPos(skill), offSetY = 0, staticbreak = False, CheckTime = 10, StopDis = 1, CheckHalt = False, targettype = OBJ_ENEMY, Collision = False, BulletHeightScale = 1, BulletRadiusScale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
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
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 130, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
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
        cl_action.SetSkillServerCache(skill, 'TargetHeroID', cl_action.GetRandomNavMeshPlayer(skill, cl_action.GetSkillVarCache(skill, 'CenterPos'), True))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSceneObjPos(skill, cl_action.GetSkillServerCache(skill, 'TargetHeroID')) if cl_action.GetSkillServerCache(skill, 'TargetHeroID') > 0 else cl_action.CrtArgTargetPos(skill, notContainDying = False))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_POS])
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        cl_action.AssignSummonDie(skill, cl_action.GetSummonByDistance(skill, 20 - cl_action.GetPlayRound(skill), 1028), 0)
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 130, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon17(TimerCartoon):
    m_SID = 17
    
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
        cl_action.UnlockMonsterAttackerFace(skill)
        cl_action.MonsterFaceTarget(skill, cl_action.GetSkillVID(skill), 20, 1)
        cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREUNBALANCE)
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 75, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon18(TimerCartoon):
    m_SID = 18
    
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
        CCartoon17.Init(skill, cartoon, casting = 13, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 8, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon16(SubductionCartoon):
    m_SID = 16
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon18.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), [
                cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'CenterPos'), (0, 5, 0))], [
                80])

    InitSuccess = classmethod(InitSuccess)


class CCartoon15(TimerCartoon):
    m_SID = 15
    
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
        CCartoon16.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 6, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon14(TimerCartoon):
    m_SID = 14
    
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
        CCartoon15.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon13(TimerCartoon):
    m_SID = 13
    
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
        cl_action.LockMonsterAttackerFace(skill)
        cartoon = { }
        CCartoon14.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 32, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
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
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon12(TimerCartoon):
    m_SID = 12
    
    def Active(cls, skill):
        cl_action.RemoveIgnoreStateEffect(skill, STATE_EFF_DEBAR)
        cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREUNBALANCE)
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(WinkPosCartoon):
    m_SID = 10
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon12.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'CenterPos'), 0, 40, [], [], dashshape = ATT_SHAPE_LINE, acceleration = 0, decrease = 0, targettype = OBJ_ALL, hitOver = True, bWaitOverTime = False, upSpeed = 0, needHitQingYanLayer = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon11(TimerCartoon):
    m_SID = 11
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

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
        CCartoon10.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 75, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AttackerAddState(skill, 1009, 0, 1, { })
    cl_action.AttackerAddState(skill, 8141, 0, 1, { })
    cl_action.SetSkillVarCache(skill, 'CenterPos', (139.33, 1.5, 141.75))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.CrtArgSelfPos(skill))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_POS])
    if cl_action.CountDistance3D(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_action.GetGroundPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS))) > 3:
        cl_action.MonsterAttackerFacePos(skill, cl_action.GetSkillVarCache(skill, 'CenterPos'), 360)
        cartoon = { }
        CCartoon13.Init(skill, cartoon, casting = 1, index = 0)
    elif cl_action.CountDistance(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (139.33, 1.5, 141.75)) > 7:
        cl_action.AddIgnoreStateEffect(skill, STATE_EFF_DEBAR)
        cl_action.MonsterAttackerFacePos(skill, cl_action.GetSkillVarCache(skill, 'CenterPos'), 360)
        cartoon = { }
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)
    else:
        cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREUNBALANCE)
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39158
    m_Name = '风神-旋转冲锋'
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
        'ColdTime': 4500,
        'AttDistance': 25,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

