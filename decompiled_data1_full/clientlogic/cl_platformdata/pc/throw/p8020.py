# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p8020.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p8020.pyc
# Source Generated with Decompyle++
# File: p8020.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import LockTargetCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_INT, WARRIOR_ELITE

class CCartoon0(LockTargetCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.LionAddLockStateToTarget(skill, cl_action.GetCurVID(skill), cl_action.GetSkillCustomData(skill, 'StateTime', defaultValue = 0), True, {
            'LockStateKeepTime': cl_action.GetSkillCustomData(skill, 'LockStateKeepTime', defaultValue = 0) })
        cl_action.TargetAddState(skill, 8153, cl_action.ToInt(skill, cl_action.GetSkillCustomData(skill, 'StateTime', defaultValue = 0) / 3) if cl_action.CheckMonsterType(skill, WARRIOR_ELITE, cl_action.GetCurVID(skill)) else cl_action.GetSkillCustomData(skill, 'StateTime', defaultValue = 0), 0, { }, cl_action.GetCurVID(skill))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        if len(cl_action.LionThrowPfSearchEnemy(skill, 50, cl_action.CrtArgSelfPos(skill), 1, True, True, True, { }, iIgnWudi = True)) >= 1:
            cl_action.SetCrtValue(skill, 0, 'LockTarget', iDefault = cl_action.LionThrowPfSearchEnemy(skill, 50, cl_action.CrtArgSelfPos(skill), 1, True, True, True, { }, iIgnWudi = True)[0])
            cl_action.SkillMarkTarget(skill, 'WeakLock', cl_action.GetCrtValue(skill, 0, 'LockTarget', 0), True)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)), cl_action.GetTargetCenterPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)), cl_action.GetSkillVID(skill), 999, 30, liveTime = 0, isLockCenter = True)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SkillMarkTarget(skill, 'WeakLock', cl_action.GetSkillVID(skill), True)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'Source', defaultValue = 0))
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 8020
    m_Name = '#NT#被动强化锁云诀转移'
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
        'Att': 60000,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 0,
        'ExplodeDelay': 0,
        'Radius': 1.5,
        'BulletVerticalAcc': 0,
        'AddStateTime': 200,
        'KeepTime': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_PassRule = {
        1012: 1 }
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000

