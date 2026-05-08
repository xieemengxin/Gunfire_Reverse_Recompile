# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9599.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9599.pyc
# Source Generated with Decompyle++
# File: p9599.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ChargeCartoon
from cl_commondefines import CRT_CHECK_SERVER

class CCartoon0(ChargeCartoon):
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
            cls.EnableShow(skill, 10, 10, 0, False, False, effect = None, halfEnd = True, offsetTime = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []

from cl_perform.attack import CChargePerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9599
    m_Name = 's金陵长弓'
    m_ExtPerform = ()
    m_HaltInfo = {
        108: 1,
        40108: 1,
        30108: 1,
        10214: 1,
        10149: 1,
        143: 1,
        286: 1 }
    m_IgnoreHalt = {
        1310: 1,
        8001: 1,
        1801: 1,
        1413: 1,
        1670: 1,
        1312: 1,
        1313: 1,
        8503: 1,
        8504: 1,
        8004: 1 }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 43,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClassifyTag = ()
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 1045
    m_CheckForbid = 1019

