# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39060.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39060.pyc
# Source Generated with Decompyle++
# File: p39060.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_BALLISTICTYPE

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
        cl_action.WarriorUsePerform(skill, cl_action.GetSkillVarCache(skill, 'CannonID'), 39061, { }, True)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 44 if cl_action.GetPlayRound(skill) >= 3 else 52 if cl_action.GetPlayRound(skill) >= 2 else 60, cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'CannonID', cl_action.ChooseValidCannonID(skill, 39061))
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def GetSkillCacheIndex():
    return [
        SKILLCACHE_BALLISTICTYPE]


def Halt(skill):
    pass


def End(skill):
    pass

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39060
    m_Name = '海船-小炮'
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
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

