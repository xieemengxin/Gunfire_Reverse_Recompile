# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/throw/p1410.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/throw/p1410.pyc
# Source Generated with Decompyle++
# File: p1410.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, HIT_OVER_GROUND, OBJ_ENEMY

class CCartoon7(DirectPosCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        cl_action.SetShapeInfo(skill, True, cl_action.GetCartoonEnd(skill, 1), ATT_SHAPE_SPHERE, [
            skill.m_Cache['Radius']])

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] * ((int(skill.m_Cache['KeepTime'] / skill.m_Cache['DamInterval']) + 1) * (cl_action.GetTalentLevel(skill, 2124) + 3 if cl_action.CheckHasTalent(skill, 2124) else 1) + (int(skill.m_Cache['KeepTime'] / skill.m_Cache['DamInterval']) * (int(skill.m_Cache['KeepTime'] / skill.m_Cache['DamInterval']) + 1) / 2 if cl_action.GetTalentLevel(skill, 2124) == 3 else 0)) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCartoonEnd(skill, 1), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(DirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckPointSkillIsEnable(skill, 15023) and cl_action.GetCartoonLoopID(skill, 6) == 0:
            cl_action.VictimAddState(skill, 32101, 200, 0, { })
        if not cl_action.CheckWarriorHasState(skill, cl_action.GetCurVID(skill), 1199):
            cl_action.PerformDamage(skill, {
                'Att': skill.m_Cache['Att'] * (cl_action.GetTalentLevel(skill, 2124) + 3 + (cl_action.GetCartoonLoopID(skill, 6) if cl_action.GetTalentLevel(skill, 2124) == 3 else 0) if cl_action.CheckHasTalent(skill, 2124) else 1) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSkillVarCache(skill, 'firstHitPos'), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cl_action.SetShapeInfo(skill, True, cl_action.GetSkillVarCache(skill, 'firstHitPos'), ATT_SHAPE_SPHERE, [
            skill.m_Cache['Radius']])
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = cl_action.GetTimerCartoonCurTimes(skill, 5))

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
        CCartoon6.Init(skill, cartoon, casting = 0, index = cl_action.GetTimerCartoonCurTimes(skill, 5))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, skill.m_Cache['DamInterval'], skill.m_Cache['KeepTime'] / skill.m_Cache['DamInterval'])

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckPointSkillIsEnable(skill, 15023) and cl_action.GetCartoonLoopID(skill, 2) == 0:
            cl_action.VictimAddState(skill, 32101, 200, 0, { })
        if not cl_action.CheckWarriorHasState(skill, cl_action.GetCurVID(skill), 1199):
            cl_action.PerformDamage(skill, {
                'Att': skill.m_Cache['Att'] * (cl_action.GetTalentLevel(skill, 2124) + 3 + (cl_action.GetCartoonLoopID(skill, 2) if cl_action.GetTalentLevel(skill, 2124) == 3 else 0) if cl_action.CheckHasTalent(skill, 2124) else 1) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCartoonEnd(skill, 1), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SetShapeInfo(skill, True, cl_action.GetCartoonEnd(skill, 1), ATT_SHAPE_SPHERE, [
            skill.m_Cache['Radius']])
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = cl_action.GetTimerCartoonCurTimes(skill, 0))

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetShapeInfo(skill, False, (0, 0, 0), ATT_SHAPE_SPHERE, [
            skill.m_Cache['Radius']])

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = cl_action.GetTimerCartoonCurTimes(skill, 0))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, skill.m_Cache['DamInterval'], skill.m_Cache['KeepTime'] / skill.m_Cache['DamInterval'])

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(ThrowByPowerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSkillServerCache(skill, 'EndPos', cl_action.GetCartoonEnd(skill, 1))
        cl_action.SendCurCartoonTriggerMsg(skill)
        if cl_action.CheckHasTalent(skill, 5005):
            cartoon = { }
            CCartoon7.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cl_action.SetSkillVarCache(skill, 'firstHitPos', cl_action.CrtArgWarriorPos(skill, cl_action.GetCurVID(skill)))
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SetSkillVarCache(skill, 'firstHitPos', cl_action.GetCartoonEnd(skill, 1))
        cl_action.SetSkillServerCache(skill, 'EndPos', cl_action.GetCartoonEnd(skill, 1))
        cl_action.SendCurCartoonTriggerMsg(skill)
        if cl_action.CheckHasTalent(skill, 5005):
            cartoon = { }
            CCartoon7.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.CrtArgCameraCenterPos(skill, cartoon), (-0.25, -0.05, 0.2))):
                return None
            cls.EnableShow(skill, 0.1, (0, skill.m_Cache['BulletVerticalAcc'], 0), (0.12, 0.14), skill.m_Cache['ExplodeDelay'], True, False, cl_action.ObjectBranchBySkillElementType(skill, None, None, None, None), 0, None, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_GROUND, changeRadius = 0, maxRadius = 3)

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
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 40, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon4.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 1410
    m_Name = '烟雾手雷'
    m_ExtPerform = (8001,)
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_CORRISION
    m_BaseAttrData = {
        'ColdTime': 50,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 4508,
        'Att': 10000,
        'CrazyEff': 0,
        'BulletSpeed': 45,
        'DebuffProb': 10000,
        'ExplodeDelay': 500,
        'Radius': 5,
        'BulletVerticalAcc': 0,
        'AddStateTime': 300,
        'KeepTime': 300,
        'DamInterval': 100,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1010
    m_AIPerformDam = 400

