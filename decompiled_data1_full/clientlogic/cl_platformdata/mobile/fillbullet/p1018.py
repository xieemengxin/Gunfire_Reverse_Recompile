# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/fillbullet/p1018.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/fillbullet/p1018.pyc
# Source Generated with Decompyle++
# File: p1018.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import PF_SUBMSG_COMMON
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_INT

class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.FillBullet(skill, cl_action.GetWeaponIntAttr(skill, 'MaxBullet'), 0)

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
            cls.EnableShow(skill, cl_action.GetWeaponIntAttr(skill, 'FillTime'), 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 0:
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.fillbullet import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 1018
    m_Name = '织云双持换弹'
    m_ExtPerform = ()
    m_HaltInfo = {
        40108: 1,
        10149: 1,
        20149: 1,
        143: 1 }
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
        'HPConsumption': 0 }
    m_ForbidRule = 1035
    m_CheckForbid = 0
    m_SubMsg = PF_SUBMSG_COMMON

