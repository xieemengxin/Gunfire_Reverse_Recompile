# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39029.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39029.pyc
# Source Generated with Decompyle++
# File: p39029.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateThrowCartoon, DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, DAM_USE_HP, OBJ_ALL, OBJ_ENEMY, SKILLCACHE_CHARGELEVEL, SKILLCACHE_INT, SKILLCACHE_LSTPOS, WARRIOR_BUILD

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
        cl_action.AddClientEffect(skill, 2023, cl_action.VectorShiftForAttDir(skill, cl_action.GetMonsterMuzzlePos(skill, (0, 0, 0)), cl_action.GetSkillVarCache(skill, 'LaunchStartPosList')[cl_action.GetCartoonLoopID(skill, 3)]), 200, (0, 0, 0))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_BUILD, OBJ_ALL) or cl_action.CheckVictimSID(skill, 1185):
            cl_action.ChangeVictimDefValue(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * cl_action.GetPerformArgValue(skill, 'buildatk', iDefault = 10) * -0.01), DAM_USE_HP)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 50 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetCartoonEnd(skill, 0), (0, 0, 0), [
                3], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(DelegateThrowCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.AddClientEffect(skill, 2024, cl_action.GetSkillVarCache(skill, 'LaunchEndPosList')[cl_action.GetSkillVarCache(skill, 'LaunchList')[cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 2) - 1)] if cl_action.ToInt(skill, len(cl_action.GetSkillVarCache(skill, 'LaunchEndPosList')) - 1) >= cl_action.GetSkillVarCache(skill, 'LaunchList')[cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 2) - 1)] else 0], 150, (0, 0, 0))
        cl_action.AddClientEffect(skill, 2025, cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'LaunchStartPosList')[cl_action.GetSkillVarCache(skill, 'LaunchList')[cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 2) - 1)]]), 200, cl_action.CrtArgGetCustomDir(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'LaunchStartPosList')[cl_action.GetSkillVarCache(skill, 'LaunchList')[cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 2) - 1)]]), cl_action.GetSkillVarCache(skill, 'LaunchEndPosList')[cl_action.GetSkillVarCache(skill, 'LaunchList')[cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 2) - 1)] if cl_action.ToInt(skill, len(cl_action.GetSkillVarCache(skill, 'LaunchEndPosList')) - 1) >= cl_action.GetSkillVarCache(skill, 'LaunchList')[cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 2) - 1)] else 0], (0, 0, 0)))

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'LaunchStartPosList')[cl_action.GetSkillVarCache(skill, 'LaunchList')[cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 2) - 1)]]), cl_action.CrtArgGetCustomDir(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'LaunchStartPosList')[cl_action.GetSkillVarCache(skill, 'LaunchList')[cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 2) - 1)]]), cl_action.GetSkillVarCache(skill, 'LaunchEndPosList')[cl_action.GetSkillVarCache(skill, 'LaunchList')[cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 2) - 1)] if cl_action.ToInt(skill, len(cl_action.GetSkillVarCache(skill, 'LaunchEndPosList')) - 1) >= cl_action.GetSkillVarCache(skill, 'LaunchList')[cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 2) - 1)] else 0], (0, 0, 0)), 80 if cl_action.GetMonsterPhase(skill) >= 3 else 75 if cl_action.GetMonsterPhase(skill) >= 2 else 70, 0.3, (0, 18, 0), (0.5, 0.5), 0, True, liveTime = 0, innerRadius = 0.2, pierce = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'LaunchList', cl_action.RandomNumberList(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)))
        cl_action.SetSkillVarCache(skill, 'LaunchEndPosList', cl_action.GetSummonPosByBoxSplit(skill, 10 if cl_action.GetMonsterPhase(skill) >= 3 else 15 if cl_action.GetMonsterPhase(skill) >= 2 else 20, 5, 1, False, {
            cl_action.ToInt(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) - 1): 100 }, { }, True))
        cl_action.GetSkillVarCache(skill, 'LaunchEndPosList').append(cl_action.CrtArgTargetPos(skill, notContainDying = True))
        cl_action.SetSkillVarCache(skill, 'LaunchEndPosList', cl_action.ChangePosListToCloseGround(skill, cl_action.GetSkillVarCache(skill, 'LaunchEndPosList')))

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
        cl_action.SetSkillVarCache(skill, 'muzzle', cl_action.GetMonsterMuzzlePos(skill, (0, 0, 0)))
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = cl_action.GetSkillVarCache(skill, 'LaunchList')[cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 2) - 1)])

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
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
        cl_action.SetSkillVictim(skill, cl_action.GetRandomLivePlayer(skill, 120, bNotContainDying = True))
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) * 30 + 20), cl_action.GetSkillCacheData(skill, SKILLCACHE_CHARGELEVEL))

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
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
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 15, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_CHARGELEVEL, cl_action.GetPerformArgValue(skill, 'TrajectoryCnt', iDefault = 7))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'LaunchCnt'))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillCustomData(skill, 'LaunchStartPosList'))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_INT,
        SKILLCACHE_LSTPOS])
    cl_action.SetSkillVarCache(skill, 'LaunchStartPosList', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS))
    for i1 in range(0, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 1):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = i1)
    
    cartoon = { }
    CCartoon5.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_CHARGELEVEL,
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39029
    m_Name = '罗睺远程光波射击'
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
    m_ElementType = DAM_TYPE_FIRE
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_BaseArgData = {
        'buildatk': 10 }
    m_Resend = 1
    m_CacheAttr = [
        'DebuffProb']

