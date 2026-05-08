# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/suitactive/p51101.pyc
# RelativePath: clientlogic/cl_platformdata/pc/suitactive/p51101.pyc
# Source Generated with Decompyle++
# File: p51101.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_LSTINT

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
        cl_action.TargetAddState(skill, 33436, 600, 0, { }, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0])
        cl_action.TargetAddState(skill, 33437, 600, 0, {
            'StateCount': cl_action.GetAttackerPerformAttr(skill, 51101, 'Radius') }, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0])

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_LSTINT)
    if not cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0] == 0:
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.suitactive import CPerform as CCustomPerform
from cl_commondefines import SUIT_PERFORM_POS_CONTROL

class CPerform(CCustomPerform):
    m_SID = 51101
    m_Name = '风行草偃套装技能'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = 0
    m_BaseAttrData = {
        'ColdTime': 1000,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'Att': 1000,
        'Radius': 0,
        'MaxCover': 1 }
    m_SourceSuit = 15111
    m_Pos = SUIT_PERFORM_POS_CONTROL
    m_ForbidRule = 0

