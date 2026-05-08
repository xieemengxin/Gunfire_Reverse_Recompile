# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p8001.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p8001.pyc
# Source Generated with Decompyle++
# File: p8001.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY

class CCartoon5(DirectPosCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cl_action.SetSkillServerCache(skill, 'EndPos', cl_action.GetSkillVarCache(skill, 'EndPos'))
        cl_action.SendCurCartoonTriggerMsg(skill)
        cl_action.SetShapeInfo(skill, True, cl_action.GetSkillVarCache(skill, 'EndPos'), ATT_SHAPE_SPHERE, [
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'EndPos'), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

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
                'Att': skill.m_Cache['Att'] * (3 + cl_action.GetTalentLevel(skill, 2124) + (cl_action.GetCartoonLoopID(skill, 2) if cl_action.GetTalentLevel(skill, 2124) == 3 else 0) if cl_action.CheckHasTalent(skill, 2124) else 1) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'EndPos'), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SetSkillServerCache(skill, 'EndPos', cl_action.GetSkillVarCache(skill, 'EndPos'))
        cl_action.SendCurCartoonTriggerMsg(skill)
        cl_action.SetShapeInfo(skill, True, cl_action.GetSkillVarCache(skill, 'EndPos'), ATT_SHAPE_SPHERE, [
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, skill.m_Cache['DamInterval'], skill.m_Cache['KeepTime'] / skill.m_Cache['DamInterval'])

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.GetSkillCustomData(skill, 'ThrowMsg', defaultValue = 0) == 1:
        cl_action.SendUseThrowPFMsg(skill)
    cl_action.SetSkillVarCache(skill, 'EndPos', cl_math.Vec3Add(cl_action.CrtArgTargetPos(skill, notContainDying = False), (0, 0.2, 0)))
    if cl_action.CheckHasTalent(skill, 5005):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)
    else:
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


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
    m_SID = 8001
    m_Name = '烟雾手雷爆炸'
    m_ExtPerform = ()
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
        'ColdTime': 0,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 0,
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
    m_ForbidRule = 0
    m_PassRule = {
        1012: 1 }
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 400
    m_CheckForbid = 0

