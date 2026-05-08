# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p23415.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p23415.pyc
# Source Generated with Decompyle++
# File: p23415.pyc (Python 3.6)

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
        cl_action.SkillForbid(skill, False, 1053)
        cl_action.SwitchAttackerPhyAble(skill, True)
        cl_action.SwitchTargetsNavAble(skill, True, cl_action.GetSkillSummonCreate(skill))
        cl_action.UnlockMonsterAttackerFace(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

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
        cl_action.SetSkillVarCache(skill, 'sk23415MirrorPos', cl_action.ChooseMonsterMirrorPos(skill, {
            1: 0,
            2: 20 }, {
            1: [
                3],
            2: [
                1,
                2,
                3] }, 4))
        cl_action.MonsterTeleportToPos(skill, cl_action.PopSkillVarCache(skill, 'sk23415MirrorPos'))
        if cl_action.GetNowLayer(skill) == 1:
            cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.GetSkillVarCache(skill, 'sk23415MirrorPos'), WARRIOR_MONSTER, {
                23412: 10 }, {
                'FollowDie': 1,
                'NoEnemyNotify': 1,
                'SameGrade': 1 })
            cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetMonsterSummonPosList(skill))
            cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS).append(cl_action.CrtArgSelfPos(skill))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_LSTPOS])
            cl_action.SwitchTargetsPhyAble(skill, False, cl_action.GetSkillSummonCreate(skill))
            cl_action.SetAsAttackerSameAttrRatio(skill, cl_action.GetSkillSummonCreate(skill), DAM_USE_ALL)
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 1, index = 0)
        elif cl_action.GetNowLayer(skill) == 2:
            cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.GetSkillVarCache(skill, 'sk23415MirrorPos'), WARRIOR_MONSTER, {
                23422: 10 }, {
                'FollowDie': 1,
                'NoEnemyNotify': 1,
                'SameGrade': 1 })
            cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetMonsterSummonPosList(skill))
            cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS).append(cl_action.CrtArgSelfPos(skill))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_LSTPOS])
            cl_action.SwitchTargetsPhyAble(skill, False, cl_action.GetSkillSummonCreate(skill))
            cl_action.SetAsAttackerSameAttrRatio(skill, cl_action.GetSkillSummonCreate(skill), DAM_USE_ALL)
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 1, index = 0)
        elif cl_action.GetNowLayer(skill) == 3:
            cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.GetSkillVarCache(skill, 'sk23415MirrorPos'), WARRIOR_MONSTER, {
                23432: 10 }, {
                'FollowDie': 1,
                'NoEnemyNotify': 1,
                'SameGrade': 1 })
            cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetMonsterSummonPosList(skill))
            cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS).append(cl_action.CrtArgSelfPos(skill))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_LSTPOS])
            cl_action.SwitchTargetsPhyAble(skill, False, cl_action.GetSkillSummonCreate(skill))
            cl_action.SetAsAttackerSameAttrRatio(skill, cl_action.GetSkillSummonCreate(skill), DAM_USE_ALL)
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.GetSkillVarCache(skill, 'sk23415MirrorPos'), WARRIOR_MONSTER, {
                23412: 10 }, {
                'FollowDie': 1,
                'NoEnemyNotify': 1,
                'SameGrade': 1 })
            cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetMonsterSummonPosList(skill))
            cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS).append(cl_action.CrtArgSelfPos(skill))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_LSTPOS])
            cl_action.SwitchTargetsPhyAble(skill, False, cl_action.GetSkillSummonCreate(skill))
            cl_action.SetAsAttackerSameAttrRatio(skill, cl_action.GetSkillSummonCreate(skill), DAM_USE_ALL)
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

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
        cl_action.SkillForbid(skill, True, 1053)
        cl_action.SwitchAttackerPhyAble(skill, False)
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.HaltTargetAllCasting(skill, [
        cl_action.GetSkillAID(skill)])
    cl_action.LockMonsterAttackerFace(skill)
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return [
        23412,
        23422,
        23432]

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 23415
    m_Name = '宝箱怪-分身'
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

