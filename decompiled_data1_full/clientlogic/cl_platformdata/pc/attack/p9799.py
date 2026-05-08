# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9799.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9799.pyc
# Source Generated with Decompyle++
# File: p9799.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, MONSTER_PART_UNTAGGED

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
        for i1 in range(cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 3) - 1), cl_action.ToInt(skill, len(cl_action.GetSkillVarCache(skill, 'FlagTarget')) if cl_action.GetTimerCartoonCurTimes(skill, 3) == 10 else len(cl_action.GetSkillVarCache(skill, 'FlagTarget')) if cl_action.GetTimerCartoonCurTimes(skill, 3) > len(cl_action.GetSkillVarCache(skill, 'FlagTarget')) else cl_action.GetTimerCartoonCurTimes(skill, 3)), 1):
            cl_action.SetSkillVarCache(skill, 'TargetCount', cl_action.GetTargetStateCount(skill, 8139, cl_action.GetSkillVarCache(skill, 'FlagTarget')[i1], False, False, bFromWeapon = True))
            cl_action.SetSkillServerCache(skill, 'statecount_9799', cl_action.GetSkillVarCache(skill, 'TargetCount'))
            cl_action.SetCurVictim(skill, cl_action.GetSkillVarCache(skill, 'FlagTarget')[i1])
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.SetCurCartoonCurPos(skill, 3, cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillVarCache(skill, 'FlagTarget')[i1]))
            cl_action.ModifySkillHitPos(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillVarCache(skill, 'FlagTarget')[i1]))
            if cl_action.GetPerformArgValue(skill, 'Probability', iDefault = 0) > 0:
                cl_action.SetSkillServerCache(skill, 'MergeTimes', cl_action.GetProbabilityThroughTimes(skill, cl_action.GetPerformArgValue(skill, 'Probability', iDefault = 0), cl_action.GetSkillVarCache(skill, 'TargetCount')) + cl_action.GetSkillVarCache(skill, 'TargetCount'))
                for i2 in range(0, cl_action.GetSkillServerCache(skill, 'MergeTimes') // 4, 1):
                    cl_action.SetWeaponDamageMergeTimes(skill, 3)
                    cl_action.WeaponDamage(skill, {
                        'Att': cl_action.GetValueFromDict(skill, cl_action.GetSkillServerCache(skill, 'statecount_9799'), {
                            1: 100,
                            2: 110,
                            3: 120,
                            4: 130,
                            5: 140,
                            6: 150,
                            7: 160,
                            8: 170 }, 300) }, { }, sendPFMsg = True)
                    cl_action.RemoveTargetSourceWeaponState(skill, cl_action.GetSkillVarCache(skill, 'FlagTarget')[i1], 8139)
                
                if cl_action.GetSkillServerCache(skill, 'MergeTimes') % 4 > 0:
                    cl_action.SetWeaponDamageMergeTimes(skill, cl_action.GetSkillServerCache(skill, 'MergeTimes') % 4 - 1)
                    cl_action.WeaponDamage(skill, {
                        'Att': cl_action.GetValueFromDict(skill, cl_action.GetSkillServerCache(skill, 'statecount_9799'), {
                            1: 100,
                            2: 110,
                            3: 120,
                            4: 130,
                            5: 140,
                            6: 150,
                            7: 160,
                            8: 170 }, 300) }, { }, sendPFMsg = True)
                    cl_action.RemoveTargetSourceWeaponState(skill, cl_action.GetSkillVarCache(skill, 'FlagTarget')[i1], 8139)
                    continue
            cl_action.SetSkillServerCache(skill, 'MergeTimes', cl_action.GetSkillVarCache(skill, 'TargetCount'))
            for i3 in range(0, cl_action.GetSkillServerCache(skill, 'MergeTimes') // 4, 1):
                cl_action.SetWeaponDamageMergeTimes(skill, 3)
                cl_action.WeaponDamage(skill, {
                    'Att': cl_action.GetValueFromDict(skill, cl_action.GetSkillServerCache(skill, 'statecount_9799'), {
                        1: 100,
                        2: 110,
                        3: 120,
                        4: 130,
                        5: 140,
                        6: 150,
                        7: 160,
                        8: 170 }, 300) }, { }, sendPFMsg = True)
                cl_action.RemoveTargetSourceWeaponState(skill, cl_action.GetSkillVarCache(skill, 'FlagTarget')[i1], 8139)
            
            if cl_action.GetSkillServerCache(skill, 'MergeTimes') % 4 > 0:
                cl_action.SetWeaponDamageMergeTimes(skill, cl_action.GetSkillServerCache(skill, 'MergeTimes') % 4 - 1)
                cl_action.WeaponDamage(skill, {
                    'Att': cl_action.GetValueFromDict(skill, cl_action.GetSkillServerCache(skill, 'statecount_9799'), {
                        1: 100,
                        2: 110,
                        3: 120,
                        4: 130,
                        5: 140,
                        6: 150,
                        7: 160,
                        8: 170 }, 300) }, { }, sendPFMsg = True)
                cl_action.RemoveTargetSourceWeaponState(skill, cl_action.GetSkillVarCache(skill, 'FlagTarget')[i1], 8139)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 10)

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
        cl_action.ModifySkillCache(skill, 'DebuffProb', 0)
        cl_action.SetSkillVarCache(skill, 'FlagTarget', cl_action.GetWeaponFlagTargetByKey(skill, 'PF_5316'))
        cl_action.ClearWeaponFlagTarget(skill, 'PF_5316')
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 40, 1)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 70, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 5, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)
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

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9799
    m_Name = '#NT#s验证用法杖'
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
        1801: 1 }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 115,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClassifyTag = (1,)
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 1099
    m_CheckForbid = 1019

