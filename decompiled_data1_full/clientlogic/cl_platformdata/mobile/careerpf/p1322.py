# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p1322.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p1322.pyc
# Source Generated with Decompyle++
# File: p1322.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_INT, SKILLCACHE_POS

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 35, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
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
        cl_action.SkillForbid(skill, False, 1085)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 45, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cl_action.SkillForbid(skill, True, 1085)

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
        cl_action.ServantUsePerform(skill, 7154, {
            'EndPos': cl_action.GetSkillCacheData(skill, SKILLCACHE_POS) })
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 25, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
            cl_action.ServantUsePerform(skill, 7154, {
                'EndPos': cl_action.GetSkillCacheData(skill, SKILLCACHE_POS) })
        else:
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 70, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_INT)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_POS)
    if cl_math.CalDistance3D(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, -10000, 0)) > 0.1:
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.SkillForbid(skill, False, 1085)


def End(skill):
    cl_action.SkillForbid(skill, False, 1085)


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1322
    m_Name = '重新部署'
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
        'ColdTime': 1200,
        'AttDistance': 25,
        'MaxCover': 3,
        'UseInterval': 0,
        'AddStateTime': 1,
        'Att': 0,
        'CrazyEff': 0,
        'BulletSpeed': 50,
        'DebuffProb': 0,
        'ExplodeDelay': 200,
        'Radius': 15,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 4,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1084
    m_CheckForbid = 1013
    m_AIPerformDam = 0

