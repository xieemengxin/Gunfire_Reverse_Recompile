# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1674.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1674.pyc
# Source Generated with Decompyle++
# File: p1674.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALL

class CCartoon14(RayCastCartoon):
    m_SID = 14
    
    def Active(cls, skill):
        cl_action.SetCurVictim(skill, cl_action.GetSkillCustomData(skill, 'curvid', defaultValue = 0))
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetSkillCustomData(skill, 'att', defaultValue = 0) }, dArgs = {
            'IgnoreShield': 0,
            'IgnoreArmor': 0 })

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
            cls.EnableCtrl(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillCustomData(skill, 'curvid', defaultValue = 0)), (0, 0, 0), cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillCustomData(skill, 'curvid', defaultValue = 0)), 0, 0, 0, targettype = OBJ_ALL, liveTime = 0, radius = 0, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        if cl_action.CheckTargetAlive(skill, cl_action.GetSkillCustomData(skill, 'curvid', defaultValue = 0)):
            cartoon = { }
            CCartoon14.Init(skill, cartoon, casting = 0, index = 0)

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
        if cl_action.CheckTargetAlive(skill, cl_action.GetSkillCustomData(skill, 'curvid', defaultValue = 0)):
            cartoon = { }
            CCartoon14.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCustomData(skill, 'waitTime', defaultValue = 0), cl_action.GetSkillCustomData(skill, 'triggerTimes', defaultValue = 0))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1674
    m_Name = '流血技能'
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
        'AttDistance': 99,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

