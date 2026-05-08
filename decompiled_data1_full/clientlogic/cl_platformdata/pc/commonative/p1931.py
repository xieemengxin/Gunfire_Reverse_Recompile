# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1931.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1931.pyc
# Source Generated with Decompyle++
# File: p1931.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER

class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSkillServerCache(skill, 'lstPos', cl_action.GetPosIncisedCircle(skill, 5, 8, 18))
        for i1 in range(0, 5, 1):
            cl_action.SetSkillCustomDataInt(skill, 'Random', cl_action.CrtArgRandomNum(skill, 0, 2))
            if cl_action.GetSkillCustomData(skill, 'Random', defaultValue = 0) >= 2:
                cl_action.AttackerUsePerform(skill, 1932, {
                    'vEnd': cl_action.GetSkillServerCache(skill, 'lstPos')[i1] }, 0, cl_action.GetSkillVID(skill))
                continue
            if cl_action.GetSkillCustomData(skill, 'Random', defaultValue = 0) <= 0:
                cl_action.AttackerUsePerform(skill, 1933, {
                    'vEnd': cl_action.GetSkillServerCache(skill, 'lstPos')[i1] }, 0, cl_action.GetSkillVID(skill))
                continue
            cl_action.AttackerUsePerform(skill, 1934, {
                'vEnd': cl_action.GetSkillServerCache(skill, 'lstPos')[i1] }, 0, cl_action.GetSkillVID(skill))
        

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
            cls.EnableCtrl(skill, 145, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 55, 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


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
    m_SID = 1931
    m_Name = '#NT#妖化怪随机元素球*5'
    m_ExtPerform = (1932, 1934, 1933)
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
        'ChargeTime': 0,
        'Radius': 12 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

