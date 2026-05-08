# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/throw/p1417.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/throw/p1417.pyc
# Source Generated with Decompyle++
# File: p1417.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, HIT_OVER_NORMAL, OBJ_ENEMY

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.SetSkillServerCache(skill, 'iHit', 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSkillServerCache(skill, 'iHit', 1)
        if cl_action.GetTalentLevel(skill, 2806) == 1:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerAttr(skill, 'Energy') * 3 })
            cl_action.VictimAddState(skill, 32425, skill.m_Cache['AddStateTime'], 0, {
                'TalentLevel': cl_action.GetTalentLevel(skill, 2805) })
            cl_action.VictimAddState(skill, 32429, skill.m_Cache['AddStateTime'], 0, { })
            cl_action.VictimAddState(skill, 32484, skill.m_Cache['AddStateTime'], 0, { })
            cl_action.AttackerAddState(skill, 32432, 0, 0, { })
        elif cl_action.GetTalentLevel(skill, 2806) == 2:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerAttr(skill, 'Energy') * 4 })
            cl_action.VictimAddState(skill, 32425, skill.m_Cache['AddStateTime'], 0, {
                'TalentLevel': cl_action.GetTalentLevel(skill, 2805) })
            cl_action.VictimAddState(skill, 32429, skill.m_Cache['AddStateTime'], 0, { })
            cl_action.VictimAddState(skill, 32484, skill.m_Cache['AddStateTime'], 0, { })
            cl_action.AttackerAddState(skill, 32432, 0, 0, { })
        elif cl_action.GetTalentLevel(skill, 2806) == 3:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerAttr(skill, 'Energy') * 5 })
            cl_action.VictimAddState(skill, 32425, skill.m_Cache['AddStateTime'], 0, {
                'TalentLevel': cl_action.GetTalentLevel(skill, 2805) })
            cl_action.VictimAddState(skill, 32429, skill.m_Cache['AddStateTime'], 0, { })
            cl_action.VictimAddState(skill, 32484, skill.m_Cache['AddStateTime'], 0, { })
            cl_action.AttackerAddState(skill, 32432, 0, 0, { })
        else:
            cl_action.VictimAddState(skill, 32425, skill.m_Cache['AddStateTime'], 0, {
                'TalentLevel': cl_action.GetTalentLevel(skill, 2805) })
            cl_action.VictimAddState(skill, 32429, skill.m_Cache['AddStateTime'], 0, { })
            cl_action.VictimAddState(skill, 32484, skill.m_Cache['AddStateTime'], 0, { })
            cl_action.AttackerAddState(skill, 32432, 0, 0, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCartoonEnd(skill, 1), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(ThrowByPowerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.CrtArgCameraCenterPos(skill, cartoon), (0, 0.1, 0.7))):
                return None
            cls.EnableShow(skill, 1, (0, skill.m_Cache['BulletVerticalAcc'], 0), (0.3, 0.3), skill.m_Cache['ExplodeDelay'], True, True, 0, 0, None, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3)

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
            cls.EnableShow(skill, 5, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
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
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 28, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon4.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1417
    m_Name = '诅咒'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_NORMAL
    m_BaseAttrData = {
        'ColdTime': 50,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 4508,
        'Att': 0,
        'CrazyEff': 0,
        'BulletSpeed': 70,
        'DebuffProb': 10000,
        'ExplodeDelay': 500,
        'Radius': 5,
        'BulletVerticalAcc': 0,
        'AddStateTime': 600,
        'KeepTime': 600,
        'DamInterval': 100,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1010
    m_AIPerformDam = 2000

