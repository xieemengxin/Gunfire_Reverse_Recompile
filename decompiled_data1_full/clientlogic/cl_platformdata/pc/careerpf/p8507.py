# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p8507.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p8507.pyc
# Source Generated with Decompyle++
# File: p8507.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_INT, SKILLCACHE_POS

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
            cls.EnableCtrl(skill, 1000, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
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
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 45, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
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
        cl_action.HaltTargetAllCasting(skill, [
            cl_action.GetAttackerServantID(skill)])
        cl_action.ServantUsePerform(skill, 7153, {
            'vEnd': cl_action.GetSkillCacheData(skill, SKILLCACHE_POS),
            'AddStateTime': skill.m_Cache['AddStateTime'],
            'TransDamFactor': cl_action.GetTransDamFactor(skill) })
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 25, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
            cl_action.HaltTargetAllCasting(skill, [
                cl_action.GetAttackerServantID(skill)])
            cl_action.ServantUsePerform(skill, 7153, {
                'vEnd': cl_action.GetSkillCacheData(skill, SKILLCACHE_POS),
                'AddStateTime': skill.m_Cache['AddStateTime'],
                'TransDamFactor': cl_action.GetTransDamFactor(skill) })
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
                cartoon = { }
                CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 70, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseCareerPFMsg(skill)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, 1 if cl_action.CheckHasState(skill, 32810) else 0)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetTargetRandomAccessiblePos(skill, cl_action.GetAttackerServantID(skill), cl_action.GetSkillVID(skill), cl_action.GetAttackerFacing(skill), 20, 2, 4, 40, 140, cl_action.GetTargetNearestSpace(skill, cl_action.GetSkillVID(skill), True, 1)))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_INT,
        SKILLCACHE_POS])
    if cl_math.CalDistance3D(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, -10000, 0)) > 0.1:
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 8507
    m_Name = '#NT#天降神兵（被动）'
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
        'ColdTime': 1500,
        'AttDistance': 25,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 300,
        'Att': 80000,
        'CrazyEff': 0,
        'BulletSpeed': 40,
        'DebuffProb': 10000,
        'ExplodeDelay': 200,
        'Radius': 10,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 4,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1084
    m_PassRule = {
        1066: 1 }
    m_CheckForbid = 1013
    m_AIPerformDam = 3000

