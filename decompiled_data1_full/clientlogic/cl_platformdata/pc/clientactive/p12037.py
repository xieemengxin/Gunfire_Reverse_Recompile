# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12037.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12037.pyc
# Source Generated with Decompyle++
# File: p12037.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon, TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, NWARRIOR_DROP, OBJ_ENEMY, S6_DICE_DAMAGE, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_INT, SKILLCACHE_LSTINT

class CCartoon6(TraceCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': (cl_action.GetDiceAbilityQuality(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) + 1) * 5 + (cl_action.GetDiceAbilityQuality(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) - 3) * (0 if cl_action.GetDiceAbilityQuality(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else 5) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 1, 70, 30, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 0.1, angle = 8, lockDis = 0, IgnoreDefalutDis = 100, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = False, searchByDistance = False)

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
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 0))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, i1 * 10), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TraceCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': (cl_action.GetDiceAbilityQuality(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) + 1) * 5 + (cl_action.GetDiceAbilityQuality(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) - 3) * (0 if cl_action.GetDiceAbilityQuality(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else 5) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 1, 70, 30, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 0.1, angle = 8, lockDis = 0, IgnoreDefalutDis = 100, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = False, searchByDistance = False)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'S6DiceSkill', 1)
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        S6_DICE_DAMAGE][0])
    if cl_action.IsHeroCtrl(skill):
        cl_action.SetSkillCustomDataInt(skill, 'DiceID', cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
        if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) > 0:
            for i1 in range(1, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY), 1):
                cartoon = { }
                CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
            
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        elif len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) > 0:
            for i2 in range(1, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY), 1):
                cartoon = { }
                CCartoon0.Init(skill, cartoon, casting = 0, index = i2)
            
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.clientactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 12037
    m_Name = 'S6腐蚀尖刺发射（队友AI）（已废弃可直接使用）'
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
        'ChargeTime': 0 }
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 10000 }

