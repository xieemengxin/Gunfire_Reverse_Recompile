# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9708.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9708.pyc
# Source Generated with Decompyle++
# File: p9708.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon, TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon3(TraceCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.ModifySkillCache(skill, 'ElementType', 256)
        cl_action.ModifySkillCache(skill, 'DebuffProb', 2500)
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_math.Vec3Add(cl_action.GetCameraCenterPosition(skill, cartoon), (0, -0.7, 0))):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), skill.m_Cache['BulletSpeed'], showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 2, angle = 20, lockDis = 70, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0)

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
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 25, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TraceCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.ModifySkillCache(skill, 'ElementType', 512)
        cl_action.ModifySkillCache(skill, 'DebuffProb', 2500)
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_math.Vec3Add(cl_action.GetCameraCenterPosition(skill, cartoon), (0, -0.7, 0))):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), skill.m_Cache['BulletSpeed'], showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 2, angle = 20, lockDis = 70, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0)

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
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 25, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TraceCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.ModifySkillCache(skill, 'ElementType', 1024)
        cl_action.ModifySkillCache(skill, 'DebuffProb', 2500)
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_math.Vec3Add(cl_action.GetCameraCenterPosition(skill, cartoon), (0, -0.7, 0))):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), skill.m_Cache['BulletSpeed'], showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 2, angle = 20, lockDis = 70, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0)

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
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 25, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9708
    m_Name = '#NT#散射法杖'
    m_ExtPerform = (5314,)
    m_HaltInfo = {
        10214: 1,
        143: 1 }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_BulletUse = 1
    m_ForbidRule = 1095
    m_CheckForbid = 1001

