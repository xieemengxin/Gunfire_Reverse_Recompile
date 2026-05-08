# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p31641.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p31641.pyc
# Source Generated with Decompyle++
# File: p31641.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, DAM_USE_ALL, FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, SKILLCACHE_LSTPOS, STATE_CLS_ABNORMAL, WARRIOR_MONSTER

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
        cl_action.AttackerRemoveState(skill, 7085, bSameItem = False)
        cl_action.SwitchAttackerNavAble(skill, True)
        cl_action.SwitchAttackerPhyAble(skill, True)
        cl_action.SwitchTargetsPhyAble(skill, True, cl_action.GetSkillSummonCreate(skill))
        cl_action.SwitchTargetsNavAble(skill, True, cl_action.GetSkillSummonCreate(skill))
        cl_action.AttackerAddState(skill, 7120, 0, 0, { })
        cl_action.AttackerRemoveState(skill, 7122, bSameItem = False)
        cl_action.UnlockMonsterAttackerFace(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetAttackerAttr(skill, 'PostDodgeTime'), 1)

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
        cl_action.SetSkillVarCache(skill, 'sk31641MirrorPos', cl_action.ChooseMonsterMirrorPos(skill, {
            1: 0,
            2: 20 }, {
            1: [
                15],
            2: [
                4,
                16,
                11] }, 3))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillVarCache(skill, 'sk31641MirrorPos'))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_LSTPOS])
        cl_action.SetTeleportPos(skill, cl_action.PopSkillVarCache(skill, 'sk31641MirrorPos'))
        cl_action.MonsterTeleport(skill, [])
        cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.GetSkillVarCache(skill, 'sk31641MirrorPos'), WARRIOR_MONSTER, {
            31651: 10 }, {
            'FollowDie': 1,
            'NoEnemyNotify': 1,
            'SameGrade': 1,
            'SameSuper': 1 })
        cl_action.SwitchTargetsPhyAble(skill, False, cl_action.GetSkillSummonCreate(skill))
        cl_action.SwitchTargetsNavAble(skill, False, cl_action.GetSkillSummonCreate(skill))
        cl_action.AttackerAddState(skill, 7085, 0, 1, { })
        cl_action.SetAsAttackerSameAttrRatio(skill, cl_action.GetSkillSummonCreate(skill), DAM_USE_ALL)
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetAttackerAttr(skill, 'DodgeTime'), 1)

    InitSuccess = classmethod(InitSuccess)


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
        cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNORETHUMP)
        cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREKNOCKBACK)
        cl_action.RemoveTargetsAllStateByType(skill, [
            cl_action.GetSkillAID(skill)], STATE_CLS_ABNORMAL)
        cl_action.SwitchAttackerNavAble(skill, False)
        cl_action.SwitchAttackerPhyAble(skill, False)
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetAttackerAttr(skill, 'PreDodgeTime'), 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.HaltTargetAllCasting(skill, [
        cl_action.GetSkillAID(skill)])
    cl_action.LockMonsterAttackerFace(skill)
    cl_action.AttackerAddState(skill, 7122, 0, 0, { })
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetMonsterSummonPosList(skill))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_LSTPOS])
    cl_action.SetSkillVarCache(skill, 'skill31641summonpos', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS))
    cl_action.ClearMonsterSummon(skill)
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.SwitchAttackerNavAble(skill, True)
    cl_action.SwitchAttackerPhyAble(skill, True)
    cl_action.SwitchTargetsPhyAble(skill, True, cl_action.GetSkillSummonCreate(skill))
    cl_action.SwitchTargetsNavAble(skill, True, cl_action.GetSkillSummonCreate(skill))
    cl_action.AttackerAddState(skill, 7120, 0, 0, { })
    cl_action.AttackerRemoveState(skill, 7122, bSameItem = False)
    cl_action.UnlockMonsterAttackerFace(skill)


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return [
        31651]

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 31641
    m_Name = '【第四幕】精英狙击怪-移形换位'
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
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_UseHeight = 1.5
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

