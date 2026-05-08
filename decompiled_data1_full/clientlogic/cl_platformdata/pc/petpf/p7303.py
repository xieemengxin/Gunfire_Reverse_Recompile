# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petpf/p7303.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petpf/p7303.pyc
# Source Generated with Decompyle++
# File: p7303.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER

class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.StartBackSwing(skill, cl_action.ToInt(skill, 50 / cl_action.GetSkillVarCache(skill, 'AttackSpeed')))

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
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 80 / cl_action.GetSkillVarCache(skill, 'AttackSpeed')), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
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
        cl_action.SetCurVictim(skill, cl_action.GetSkillVID(skill))
        cl_action.SetCurCartoonCurPos(skill, 0, cl_action.CrtArgHitPos(skill))
        cl_action.SetSkillServerCache(skill, 'AttSpeedMul', cl_action.GetAttackerBaseAttr(skill, 'AttSpeed') / (skill.m_Cache['AttSpeed'] if skill.m_Cache['AttSpeed'] > 0 else cl_action.GetAttackerBaseAttr(skill, 'AttSpeed')))
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, skill.m_Cache['Att'] * ((cl_action.GetSkillServerCache(skill, 'AttSpeedMul') - 2.5 if cl_action.GetSkillServerCache(skill, 'AttSpeedMul') > 2.5 else 0) / 2.5 + 1)) }, dArgs = { })

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 20 / cl_action.GetSkillVarCache(skill, 'AttackSpeed')), 1)

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
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 50 / cl_action.GetSkillVarCache(skill, 'AttackSpeed')), 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'AttackSpeed', cl_action.Clamp(skill, 150 / (skill.m_Cache['AttSpeed'] if skill.m_Cache['AttSpeed'] > 0 else 150), 1, 2.5))
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.petactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, PETPF_ACTIVE_ATTACK

class CPerform(CCustomPerform):
    m_SID = 7303
    m_Name = '长弩锐士追踪子弹'
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
        'ColdTime': 300,
        'AttDistance': 40,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1,
        'Radius': 0 }
    m_ElementType = DAM_TYPE_NORMAL
    m_ClientNeed = 0
    m_PFSubType = PETPF_ACTIVE_ATTACK
    m_SpellPower = 0
    m_NeedTarget = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'FlySpeed': 22 }

