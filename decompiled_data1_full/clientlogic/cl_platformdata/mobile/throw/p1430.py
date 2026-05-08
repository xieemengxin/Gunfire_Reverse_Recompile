# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/throw/p1430.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/throw/p1430.pyc
# Source Generated with Decompyle++
# File: p1430.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import BranchCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_RECTANGLE, CRT_CHECK_SERVER

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 8, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(BranchCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetTalentLevel(skill, 3015) >= 3 or cl_action.CheckHasBenediction(skill, 13531):
            cl_action.AttackerAddState(skill, 1521, skill.m_Cache['AddStateTime'], 0, { })
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetAttackerPerformAttr(skill, 1422, 'Att') })
        cl_action.AttackerAddState(skill, 1520, skill.m_Cache['AddStateTime'], 0, { })
        if cl_action.CheckHasSkillVarCache(skill, 'p3012_hit'):
            cl_action.SetSkillVarCache(skill, 'p3012_hit', int(cl_action.GetSkillVarCache(skill, 'p3012_hit') + 1))
            if cl_action.GetSkillVarCache(skill, 'p3012_hit') >= (3 if cl_action.GetTalentLevel(skill, 3012) >= 3 else 5) and cl_action.CheckTargetAlive(skill, cl_action.GetCurVID(skill)):
                cl_action.SetSkillVarCache(skill, 'p3012_hit', 0)
                cartoon = { }
                CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
            cl_action.SetAttackerStateCount(skill, 32656, cl_action.GetSkillVarCache(skill, 'p3012_hit'))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        for i1 in range(0, len(cl_action.GetCartoonHitTarget(skill, 5)), 1):
            cl_action.TargetAddState(skill, 32714, 25, 0, { }, cl_action.GetCartoonHitTarget(skill, 5)[i1])
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, (cl_action.GetSkillCustomArg(skill, 'SX') / 100, cl_action.GetSkillCustomArg(skill, 'SY') / 100, cl_action.GetSkillCustomArg(skill, 'SZ') / 100), (cl_action.GetSkillCustomArg(skill, 'EX') / 100, cl_action.GetSkillCustomArg(skill, 'EY') / 100, cl_action.GetSkillCustomArg(skill, 'EZ') / 100), ATT_SHAPE_RECTANGLE, [
                8,
                6,
                40], cl_action.GetAttackerPerformAttr(skill, 1422, 'DamInterval'), 0.25)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.CheckHasTalent(skill, 3012):
        cl_action.SetSkillVarCache(skill, 'p3012_hit', cl_action.GetAttackerStateCount(skill, 32656, dState = { }))
    cartoon = { }
    CCartoon5.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.throw import CUseCountPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1430
    m_Name = '秘卷觉醒镇妖'
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
        'CrazyEff': 10000,
        'BulletSpeed': 25,
        'DebuffProb': 0,
        'ExplodeDelay': 0,
        'Radius': 0,
        'BulletVerticalAcc': 0,
        'AddStateTime': 600,
        'KeepTime': 0,
        'DamInterval': 4,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000

