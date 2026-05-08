# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1938.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1938.pyc
# Source Generated with Decompyle++
# File: p1938.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import AnnulusDiffuseCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_RANDOM

class CCartoon3(AnnulusDiffuseCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        if cl_action.GetSkillVarCache(skill, 'ElementNum') == 1:
            cl_action.SetSkillVarCache(skill, 'ElementStateSID', 20026)
        elif cl_action.GetSkillVarCache(skill, 'ElementNum') == 2:
            cl_action.SetSkillVarCache(skill, 'ElementStateSID', 20027)
        elif cl_action.GetSkillVarCache(skill, 'ElementNum') == 3:
            cl_action.SetSkillVarCache(skill, 'ElementStateSID', 20028)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.VictimAddState(skill, cl_action.GetSkillVarCache(skill, 'ElementStateSID'), 500, 0, {
            '': 0 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), 0, cl_action.GetAttackerPerformAttr(skill, 1938, 'Radius'), 10, 4, targettype = OBJ_ENEMY, liveTime = 0, pierceStatic = True)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'ElementNum', cl_action.GetRandomInRange(skill, 1, 3))
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_RANDOM]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_ELEMENT

class CPerform(CCustomPerform):
    m_SID = 1938
    m_Name = '无伤随机元素脉冲'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_ELEMENT
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0,
        'DebuffProb': 10000,
        'Radius': 10 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

