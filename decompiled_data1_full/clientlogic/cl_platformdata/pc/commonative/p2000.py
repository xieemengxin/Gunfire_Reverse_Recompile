# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p2000.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p2000.pyc
# Source Generated with Decompyle++
# File: p2000.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_INT, SKILLCACHE_POS

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'Radius', defaultValue = 8))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetGroundPos(skill, cl_action.GetSkillCustomData(skill, 'TargetPos', defaultValue = (0, 0, 0))))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY, cl_action.GetSkillCustomData(skill, 'ExtraDiffuse', defaultValue = 0))
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) == 1:
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_INT,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 2000
    m_Name = '#NT#棱刺扩散特效技能'
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
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

