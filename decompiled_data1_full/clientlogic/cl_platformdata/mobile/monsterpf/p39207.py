# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39207.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39207.pyc
# Source Generated with Decompyle++
# File: p39207.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, WARRIOR_MONSTER

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
        cl_action.CreateRandomNumWarriorAtPointPos(skill, [
            cl_action.GetSkillServerCache(skill, 'lstpos')[cl_action.GetTimerCartoonCurTimes(skill, 2) + 3]], WARRIOR_MONSTER, {
            39211: 1 }, {
            'FollowDie': 1 })
        cl_action.WarriorUsePerform(skill, cl_action.GetSkillSummonCreate(skill)[-1], 39217, {
            'vDir': cl_math.Vec3Minus(cl_action.GetMapCenterPos(skill), cl_math.Vec3Add(cl_action.GetMapCenterPos(skill), (0, 0, 60))) }, False)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, cl_action.GetPlayRound(skill) * -5 + 60), 4)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, cl_action.GetPlayRound(skill) * -20 + 300), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

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
        cl_action.CreateRandomNumWarriorAtPointPos(skill, [
            cl_action.GetSkillServerCache(skill, 'lstpos')[cl_action.GetTimerCartoonCurTimes(skill, 0) - 1]], WARRIOR_MONSTER, {
            39211: 1 }, {
            'FollowDie': 1 })
        cl_action.WarriorUsePerform(skill, cl_action.GetSkillSummonCreate(skill)[-1], 39217, {
            'vDir': cl_math.Vec3Minus(cl_action.GetMapCenterPos(skill), cl_math.Vec3Add(cl_action.GetMapCenterPos(skill), (0, 0, 60))) }, False)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, cl_action.GetPlayRound(skill) * -5 + 60), 4)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.MonsterAttackerFacePos(skill, cl_math.Vec3Add(cl_action.CrtArgSelfPos(skill), (0, 0, -1)), 0)
    cl_action.SetSkillServerCache(skill, 'lstpos', cl_action.ChooseTentacleSequencePos(skill, cl_action.CrtArgTargetGroundPos(skill), 60, 8, 17))
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return [
        39211]

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39207
    m_Name = '海怪-召唤强化拍击'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 3000,
        'AttDistance': 200,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

