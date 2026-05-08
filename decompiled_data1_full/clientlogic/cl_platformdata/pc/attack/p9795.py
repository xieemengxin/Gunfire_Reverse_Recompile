# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9795.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9795.pyc
# Source Generated with Decompyle++
# File: p9795.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ChargeCartoon, DirectPosCartoon, SplitArrowCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, MONSTER_PART_FLAW, MONSTER_PART_WEAKNESS, MONSTER_PART_WEAKNESSFLAW, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT

class CCartoon9(DirectPosCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.GetCurVID(skill) == cl_action.GetSkillServerCache(skill, 'CurHitTarget'):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
            cl_action.WeaponDamage(skill, {
                'Att': 70 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgHitPos(skill), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon13(DirectPosCartoon):
    m_SID = 13
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.GetCurVID(skill) == cl_action.GetSkillServerCache(skill, 'CurHitTarget'):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_FLAW)
            cl_action.WeaponDamage(skill, {
                'Att': 70 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgHitPos(skill), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon14(DirectPosCartoon):
    m_SID = 14
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetCurVID(skill) == cl_action.GetSkillServerCache(skill, 'CurHitTarget'):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESSFLAW)
            cl_action.WeaponDamage(skill, {
                'Att': 70 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgHitPos(skill), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(DirectPosCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.GetCurVID(skill) == cl_action.GetSkillServerCache(skill, 'CurHitTarget'):
            cl_action.WeaponDamage(skill, {
                'Att': 70 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgHitPos(skill), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(SplitArrowCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 70 }, { }, sendPFMsg = False)
        cl_action.SetSkillServerCache(skill, 'CurHitTarget', cl_action.GetCurVID(skill))
        if cl_action.CheckHitPointArea(skill, MONSTER_PART_WEAKNESS):
            cartoon = { }
            CCartoon9.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 1))
        elif cl_action.CheckHitPointArea(skill, MONSTER_PART_FLAW):
            cartoon = { }
            CCartoon13.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 1))
        elif cl_action.CheckHitPointArea(skill, MONSTER_PART_WEAKNESSFLAW):
            cartoon = { }
            CCartoon14.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 1))
        else:
            cartoon = { }
            CCartoon8.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 1))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], 5 if cl_action.GetSkillVarCache(skill, 'SplitTimes') == 3 else 4 if cl_action.GetSkillVarCache(skill, 'SplitTimes') == 2 else 3, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0], [
                (-13, 30, 0),
                (-26, 20, 0),
                (-39, 40, 0),
                (-52, 30, 0),
                (-65, 40, 0)] if cl_action.GetSkillVarCache(skill, 'SplitTimes') == 3 else [
                (52, 30, 0),
                (65, 40, 0),
                (0, 40, 0),
                (0, 10, 0)] if cl_action.GetSkillVarCache(skill, 'SplitTimes') == 2 else [
                (13, 30, 0),
                (26, 20, 0),
                (39, 40, 0)], 3, 80, 90, 2, 180, 3, 3, 30, targettype = OBJ_ENEMY, accelerated = 50, lockWeakness = True, secondMaxAngle = 4, acceleratedSec = 50, trailLifeTime = 50)

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
        cl_action.SetSkillVarCache(skill, 'SplitTimes', 2)
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 7) if cl_action.GetSkillVarCache(skill, 'SplitTimes') == 3 else cl_action.GetCartoonLoopID(skill, 6) if cl_action.GetSkillVarCache(skill, 'SplitTimes') == 2 else cl_action.GetSkillVarCache(skill, 'TriggerTime'))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 8, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
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
        cl_action.SetSkillVarCache(skill, 'SplitTimes', 3)
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 7) if cl_action.GetSkillVarCache(skill, 'SplitTimes') == 3 else cl_action.GetCartoonLoopID(skill, 6) if cl_action.GetSkillVarCache(skill, 'SplitTimes') == 2 else cl_action.GetSkillVarCache(skill, 'TriggerTime'))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 12, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(TimerCartoon):
    m_SID = 10
    
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
        cl_action.SetSkillVarCache(skill, 'SplitTimes', 1)
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 7) if cl_action.GetSkillVarCache(skill, 'SplitTimes') == 3 else cl_action.GetCartoonLoopID(skill, 6) if cl_action.GetSkillVarCache(skill, 'SplitTimes') == 2 else cl_action.GetSkillVarCache(skill, 'TriggerTime'))
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = cl_action.ToInt(skill, cl_action.GetSkillVarCache(skill, 'TriggerTime') + 1))
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 0, index = cl_action.ToInt(skill, cl_action.GetSkillVarCache(skill, 'TriggerTime') + 2))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 48, 0)

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, 120 if skill.m_Cache['TriggerTimes'] > 1 else 76), 0)

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
        for i1 in range(0, skill.m_Cache['TriggerTimes'], 1):
            cl_action.SetSkillVarCache(skill, 'TriggerTime', cl_action.ToInt(skill, i1 * 3))
            if i1 == 0:
                cl_action.SetSkillVarCache(skill, 'SplitTimes', 1)
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 7) if cl_action.GetSkillVarCache(skill, 'SplitTimes') == 3 else cl_action.GetCartoonLoopID(skill, 6) if cl_action.GetSkillVarCache(skill, 'SplitTimes') == 2 else cl_action.GetSkillVarCache(skill, 'TriggerTime'))
                cartoon = { }
                CCartoon6.Init(skill, cartoon, casting = 0, index = cl_action.ToInt(skill, cl_action.GetSkillVarCache(skill, 'TriggerTime') + 1))
                cartoon = { }
                CCartoon7.Init(skill, cartoon, casting = 0, index = cl_action.ToInt(skill, cl_action.GetSkillVarCache(skill, 'TriggerTime') + 2))
                continue
            cartoon = { }
            CCartoon10.Init(skill, cartoon, casting = 1, index = i1)
        
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(ChargeCartoon):
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
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 20, 1, 0, False, True, halfEnd = False, offsetTime = 1, breaktips = False, allowMaxChargeLowAmmo = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, (8 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) * 100) if cl_action.ToInt(skill, (8 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) * 100) >= 4 else 4, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

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
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 100:
                if cl_action.ToInt(skill, (52 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) * 100) >= 4:
                    pass
                
            
            skill(4, 64, 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.attack import CChargePerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9795
    m_Name = 's速射弓'
    m_ExtPerform = (5315, 5340)
    m_HaltInfo = {
        40108: 1,
        143: 1 }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 43,
        'AttDistance': 0,
        'ChargeTime': 40,
        'MaxPFBullet': 30000,
        'PFBulletUse': 30000,
        'PFBulletRecover': 1500,
        'CostPFBulletDuringUse': 1,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000,
        'TriggerTimes': 1 }
    m_ClassifyTag = (2,)
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 1045
    m_CheckForbid = 1019

