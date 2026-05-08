# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p8016.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p8016.pyc
# Source Generated with Decompyle++
# File: p8016.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_POS, WARRIOR_MONSTER

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
        cl_action.AttackerUsePerform(skill, 8010, {
            'vEnd': cl_action.GetSkillVarCache(skill, 'BoomPos'),
            'TransDamFactor': cl_action.GetTransDamFactor(skill) }, 0, 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 3)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
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
        cl_action.AddSceneEventForState(skill, cl_action.GetSkillVarCache(skill, 'BoomPos'), 150, 1, {
            'Radius': 12 }, 33047, 150, 1, iFightType = WARRIOR_MONSTER, iLeaveSetTime = -1)
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseThrowPFMsg(skill)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSkillCustomData(skill, 'vEnd', defaultValue = (0, 0, 0)))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_POS])
    cl_action.SetSkillVarCache(skill, 'BoomPos', cl_action.GetSkillCacheData(skill, SKILLCACHE_POS))
    cl_action.SetCustomPos(skill, cl_action.GetSkillCustomData(skill, 'vEnd', defaultValue = (0, 0, 0)))
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 8016
    m_Name = '#NT#时空黑洞'
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
        'MaxCover': 1,
        'BulletSID': 0,
        'Att': 50000,
        'CrazyEff': 0,
        'BulletSpeed': 45,
        'DebuffProb': 1500,
        'ExplodeDelay': 500,
        'Radius': 3,
        'BulletVerticalAcc': 0,
        'AddStateTime': 300,
        'KeepTime': 300,
        'DamInterval': 100,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000

