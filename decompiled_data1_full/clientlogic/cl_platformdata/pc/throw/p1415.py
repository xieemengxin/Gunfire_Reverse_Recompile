# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p1415.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p1415.pyc
# Source Generated with Decompyle++
# File: p1415.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ChargeCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, WARRIOR_BARRIER

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
        cl_action.SetSkillServerCache(skill, 'GainEffect', cl_action.CostAttackerEnergy(skill, cl_action.GetCartoonChargeLevel(skill, 0), 1.3, 0.5))
        cl_action.SetSkillServerCache(skill, 'KeepTime', cl_action.ToInt(skill, skill.m_Cache['AddStateTime'] * (cl_action.GetSkillServerCache(skill, 'GainEffect') / 10000 + 1)))
        cl_action.AttackerAddState(skill, 32363, cl_action.ToInt(skill, skill.m_Cache['AddStateTime'] * (cl_action.GetSkillServerCache(skill, 'GainEffect') / 10000 + 1)), 0, {
            'GainEffect': cl_action.GetSkillServerCache(skill, 'GainEffect'),
            'Att': cl_action.GetAttackerPerformAttr(skill, 1415, 'Att') })
        if cl_action.GetAttackerAttr(skill, 'Energy') <= 0:
            cl_action.AssignSummonDie(skill, cl_action.GetAttackSummon(skill, WARRIOR_BARRIER), 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 60, 0)

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
        cl_action.SetSkillServerCache(skill, 'GainEffect', cl_action.CostAttackerEnergy(skill, cl_action.GetCartoonChargeLevel(skill, 0), 1.3, 0.5))
        cl_action.SetSkillServerCache(skill, 'KeepTime', cl_action.ToInt(skill, skill.m_Cache['AddStateTime'] * (cl_action.GetSkillServerCache(skill, 'GainEffect') / 10000 + 1)))
        cl_action.AttackerAddState(skill, 32363, cl_action.ToInt(skill, skill.m_Cache['AddStateTime'] * (cl_action.GetSkillServerCache(skill, 'GainEffect') / 10000 + 1)), 0, {
            'GainEffect': cl_action.GetSkillServerCache(skill, 'GainEffect'),
            'Att': cl_action.GetAttackerPerformAttr(skill, 1415, 'Att') })
        if cl_action.GetAttackerAttr(skill, 'Energy') <= 0:
            cl_action.AssignSummonDie(skill, cl_action.GetAttackSummon(skill, WARRIOR_BARRIER), 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(ChargeCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetCartoonChargeLevel(skill, 0) < 10:
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 4, 1000000, 0, True, True, effect = None, halfEnd = False, offsetTime = 0.1)

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
        cl_action.AttackerAddState(skill, 32363, skill.m_Cache['AddStateTime'], 0, {
            'Att': cl_action.GetAttackerPerformAttr(skill, 1415, 'Att') })
        cl_action.SetSkillServerCache(skill, 'GainEffect', 0)
        cl_action.SetSkillServerCache(skill, 'KeepTime', skill.m_Cache['AddStateTime'])

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 10, 1)

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
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 70, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.CheckHasTalent(skill, 2515):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
    else:
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1415
    m_Name = '肾上腺素'
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
        'ColdTime': 100,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 4508,
        'Att': 2000,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 0,
        'ExplodeDelay': 0,
        'Radius': 0,
        'BulletVerticalAcc': 0,
        'AddStateTime': 600,
        'KeepTime': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1010
    m_AIPerformDam = 2000

