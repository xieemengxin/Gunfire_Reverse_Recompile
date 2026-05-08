# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p8503.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p8503.pyc
# Source Generated with Decompyle++
# File: p8503.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_perform
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_LSTINT, SKILLCACHE_LSTINTSPECIAL

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
        for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)), 1):
            cl_action.SetSkillVarCache(skill, 'CurVictim', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1])
            cl_action.SetSkillVarCache(skill, 'CurCount', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[i1])
            cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVarCache(skill, 'CurVictim'))
            for i2 in range(0, cl_action.GetSkillVarCache(skill, 'CurCount'), 1):
                cl_action.PerformDamage(skill, {
                    'Att': skill.m_Cache['Att'] * cl_action.GetSkillCustomData(skill, 'MulAtt') })
            
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 55, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTINTSPECIAL]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 8503
    m_Name = '#被动剑雨飞弹'
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
        'ColdTime': 10,
        'AttDistance': 100,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 200,
        'Att': 20000,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 1000,
        'ExplodeDelay': 0,
        'Radius': 3,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 0
    
    def UsePerform(self, oWarrior, oSkill):
        cl_perform.skillcache.SetSkillCacheByIndex(oSkill, SKILLCACHE_LSTINT, oSkill.m_Custom['lstHitVictim'])
        oSkill.m_Collect['8503-TotalCount'] = len(oSkill.m_Custom['lstHitVictim'])
        super().UsePerform(oWarrior, oSkill)


