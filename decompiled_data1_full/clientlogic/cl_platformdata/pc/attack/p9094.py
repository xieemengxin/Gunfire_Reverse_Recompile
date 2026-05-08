# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9094.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9094.pyc
# Source Generated with Decompyle++
# File: p9094.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_PERFORMMODE

class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.AttackerAddState(skill, 1902, 0, 1, { })
        cl_action.AttackerAddState(skill, 1523, 0, 0, {
            'GainEffect': cl_action.GetPerformArgValue(skill, 'InsEnhance', iDefault = 0) })
        cl_action.SetCartoonDependState(skill, 1, 1902)

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
            cls.EnableShow(skill, 200, 20)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 0:
        cl_action.SkillHaltOther(skill, 9094)
        cl_action.AttackerRemoveState(skill, 1523, bSameItem = False)
    else:
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.AttackerRemoveState(skill, 1523, bSameItem = False)


def End(skill):
    cl_action.AttackerRemoveState(skill, 1523, bSameItem = False)


def GetSkillCacheIndex():
    return [
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform
from cl_commondefines import DPSUBMSG_NOFIRE

class CPerform(CCustomPerform):
    m_SID = 9094
    m_Name = 's六方'
    m_ExtPerform = (5305, 5309)
    m_HaltInfo = {
        40108: 1,
        30108: 1,
        10108: 1,
        10149: 1,
        143: 1,
        286: 1,
        377: 1 }
    m_IgnoreHalt = {
        1312: 1 }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 50,
        'AttDistance': 0,
        'ChargeTime': 700,
        'MaxPFBullet': 26000,
        'PFBulletUse': 3250,
        'PFBulletRecover': 650,
        'CostPFBulletDuringUse': 0,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_DPSubMsg = DPSUBMSG_NOFIRE
    m_ClassifyTag = (4,)
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 1074
    m_CheckForbid = 1014

