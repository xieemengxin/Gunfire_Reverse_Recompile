# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9094.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9094.pyc
# Source Generated with Decompyle++
# File: p9094.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon, TimerCartoon, TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALL, OBJ_ENEMY, SKILLCACHE_LSTINTSPECIAL, SKILLCACHE_PERFORMMODE

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
        cl_action.AttackerRemoveState(skill, 1523, bSameItem = False)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(RayCastCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetSkillServerCache(skill, 'damageCnt') < 4:
            cl_action.WeaponDamage(skill, {
                'Att': (cl_action.GetSkillServerCache(skill, 'damageCnt') * 20 + 5) * 100 }, { }, sendPFMsg = False)
        elif (cl_action.GetSkillServerCache(skill, 'damageCnt') - 3) * 5 + 65 < 100:
            cl_action.WeaponDamage(skill, {
                'Att': ((cl_action.GetSkillServerCache(skill, 'damageCnt') - 3) * 5 + 65) * 100 }, { }, sendPFMsg = False)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 10000 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgMuzzlePos(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttackDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ALL, liveTime = 0, radius = 0, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

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
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 10, 2)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TraceCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetSkillServerCache(skill, 'damageCnt') < 4:
            cl_action.WeaponDamage(skill, {
                'Att': (cl_action.GetSkillServerCache(skill, 'damageCnt') * 20 + 5) * 100 }, { }, sendPFMsg = False)
        elif (cl_action.GetSkillServerCache(skill, 'damageCnt') - 3) * 5 + 65 < 100:
            cl_action.WeaponDamage(skill, {
                'Att': ((cl_action.GetSkillServerCache(skill, 'damageCnt') - 3) * 5 + 65) * 100 }, { }, sendPFMsg = False)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 10000 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgMuzzlePos(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttackDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 50, lockWeakness = True, lockAngle = 15, lockDis = 100, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False)

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
        cl_action.SetSkillServerCache(skill, 'damageCnt', cl_action.GetTargetStateCount(skill, 1523, cl_action.GetSkillAID(skill), False, False))
        if cl_action.CheckNumberinList(skill, 13041, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)):
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = 0)
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 300, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.AttackerAddState(skill, 1523, 310, 0, { })
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 0:
        cl_action.SetSkillServerCache(skill, 'damageCnt', cl_action.GetTargetStateCount(skill, 1523, cl_action.GetSkillAID(skill), False, False))
        if cl_action.CheckNumberinList(skill, 13041, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)):
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = 0)
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 0, index = 0)
    else:
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINTSPECIAL,
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform
from cl_commondefines import DPSUBMSG_NOFIRE

class CPerform(CCustomPerform):
    m_SID = 9094
    m_Name = 's六方'
    m_ExtPerform = (5305, 5309)
    m_HaltInfo = {
        40108: 1,
        30108: 1,
        10108: 1,
        10149: 1,
        143: 1,
        286: 1,
        377: 1 }
    m_IgnoreHalt = {
        1312: 1 }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 50,
        'AttDistance': 0,
        'ChargeTime': 700,
        'MaxPFBullet': 26000,
        'PFBulletUse': 3250,
        'PFBulletRecover': 650,
        'CostPFBulletDuringUse': 0,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_DPSubMsg = DPSUBMSG_NOFIRE
    m_ClassifyTag = (4,)
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 1074
    m_CheckForbid = 1014

