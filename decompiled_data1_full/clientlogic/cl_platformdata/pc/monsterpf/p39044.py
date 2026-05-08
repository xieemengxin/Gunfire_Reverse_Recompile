# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39044.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39044.pyc
# Source Generated with Decompyle++
# File: p39044.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_LSTPOS
from cl_only import PY_FLAG_MONSTERTARGET

class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            'Relic': 1 })

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
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon11(TimerCartoon):
    m_SID = 11
    
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
        cl_action.UnlockMonsterAttackerFace(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 440, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.CustomPerformAction(skill, 39026, 'BalanceChoosePos', [
            cl_action.GetSkillVarCache(skill, 'RemainCnt') if cl_action.GetSkillVarCache(skill, 'RemainCnt') >= 2 else 2])
        cl_action.AttackerUsePerform(skill, 39047, {
            'LaunchCnt': cl_action.GetSkillVarCache(skill, 'RemainCnt') if cl_action.GetSkillVarCache(skill, 'RemainCnt') >= 2 else 2,
            'LaunchStartPosList': cl_action.GetSkillServerCache(skill, 'LaunchStartPosList'),
            'HeroDir': cl_action.GetSkillVarCache(skill, 'HeroDir') }, 0, 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 15, 1)

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
        cl_action.SetSkillVarCache(skill, 'HeroDir', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS))
        cl_action.SetSkillVarCache(skill, 'RemainCnt', cl_action.ToInt(skill, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)) * 2))
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.LockMonsterAttackerFace(skill)
    cl_action.SetSkillServerCache(skill, 'LeftPosList', cl_action.GetListByShuffleAndNumber(skill, [
        (-29, 42, -11),
        (-29, 53, -11),
        (-29, 31, -11),
        (-18, 42, -11),
        (-40, 42, -11)], 0))
    cl_action.SetSkillServerCache(skill, 'RightPosList', cl_action.GetListByShuffleAndNumber(skill, [
        (29, 42, -11),
        (29, 53, -11),
        (29, 31, -11),
        (18, 42, -11),
        (40, 42, -11)], 0))
    cl_action.SetSkillVarCache(skill, 'HeroDir', [])
    for i1 in range(0, 1, 1):
        cl_action.GetSkillVarCache(skill, 'HeroDir').append(cl_action.CrtArgWarriorPos(skill, [
            cl_action.GetRandomLivePlayer(skill, 360, bNotContainDying = False, fMaxDis = 0, bSkillVIDSecond = False, iFlag = PY_FLAG_MONSTERTARGET, bResetVID = True)][i1]))
    
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillVarCache(skill, 'HeroDir'))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_LSTPOS])
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39044
    m_Name = '罗睺轮回10-扫射激光'
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
        'ColdTime': 0,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

