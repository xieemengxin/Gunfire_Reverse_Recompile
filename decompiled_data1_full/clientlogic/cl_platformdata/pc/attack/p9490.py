# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9490.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9490.pyc
# Source Generated with Decompyle++
# File: p9490.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import FORBID_OPSKILL
from cl_perform.cartoon.defines import AnnulusChangeCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_INT

class CCartoon0(AnnulusChangeCartoon):
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
            cls.EnableShow(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 2, (skill.m_Cache['AttSpeed'] / 100) * (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 16), (skill.m_Cache['AttSpeed'] / 100) * (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 16), 0, True, 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.attack import CContinuousPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9490
    m_Name = '#NT#磁暴线圈扩张'
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
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_BulletUse = 0
    m_ForbidRule = 1094
    m_CheckForbid = 1028
    m_CheckForbid = FORBID_OPSKILL
    
    def WeaponFire(self, oWarrior, oSkill):
        pass


