# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p1303.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p1303.pyc
# Source Generated with Decompyle++
# File: p1303.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ChargeCartoon, WinkPosCartoon
from cl_commondefines import ATT_SHAPE_LINE, CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon1(WinkPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.AttackerAddState(skill, 32208, 20, 0, { })

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': ((5 if cl_action.CheckHasTalent(skill, 2201) else cl_action.GetCartoonChargeLevel(skill, 0)) / 5 + 0.1) * skill.m_Cache['Att'] })
        cl_action.PushVictim(skill, cl_action.GetCartoonEnd(skill, 1), 20, 4, 10000, angle = 45 if cl_action.CheckHasTalent(skill, 2215) else 0)
        cl_action.ChangeAttackerShield(skill, skill.m_Cache['ShieldMax'])

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 0, 100, [], [], dashshape = ATT_SHAPE_LINE, acceleration = 0, decrease = 0, targettype = OBJ_ENEMY, hitOver = not cl_action.CheckHasTalent(skill, 2215), bWaitOverTime = False, upSpeed = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(ChargeCartoon):
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
        cl_action.SetSkillCartoonCheckData(skill, {
            'WinkMoveLen': ((5 if cl_action.CheckHasTalent(skill, 2201) else cl_action.GetCartoonChargeLevel(skill, 0)) / 5 + 1) * skill.m_Cache['AttDistance'] })
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 20, 5, 0, False, True, effect = None, halfEnd = False, offsetTime = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.CheckHasTalent(skill, 2201):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
    else:
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1303
    m_Name = '冲锋（废弃）'
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
        'ColdTime': 1000,
        'AttDistance': 10,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 40000,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 0,
        'ExplodeDelay': 0,
        'Radius': 0,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 1013
    m_AIPerformDam = 0

