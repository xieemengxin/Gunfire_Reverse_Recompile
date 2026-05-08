# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1677.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1677.pyc
# Source Generated with Decompyle++
# File: p1677.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import CurveCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon1(CurveCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetTalentLevel(skill, 2506) == 1:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.ToInt(skill, cl_action.GetAttackerAttr(skill, 'EnergyMax') * 1) })
        elif cl_action.GetTalentLevel(skill, 2506) == 2:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.ToInt(skill, cl_action.GetAttackerAttr(skill, 'EnergyMax') * 2) })
        elif cl_action.GetTalentLevel(skill, 2506) == 3:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.ToInt(skill, cl_action.GetAttackerAttr(skill, 'EnergyMax') * 4) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetAttackerCustomPos(skill, 'BarriarPos'), cl_action.CrtArgRandomAngle(skill, cartoon, cl_action.GetAttackerCustomPos(skill, 'BarriarPos'), cl_action.CrtArgBodyPos(skill, 0, 0, 0, 0), 20, 30, 20, 30, False), 1, 50, 25, 270, 0.7, targettype = OBJ_ENEMY, pierceblock = True, effect = 0, liveTime = 0, trailEffect = 0, effectLiveTime = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 15, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1677
    m_Name = '反射光墙弹道追踪'
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
    m_BaseArgData = {
        'DebuffProb': 1200,
        'Att': 0 }

