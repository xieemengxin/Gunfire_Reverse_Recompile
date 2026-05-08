# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12041.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12041.pyc
# Source Generated with Decompyle++
# File: p12041.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, NWARRIOR_DROP, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT

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
            'Att': cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) })
        if cl_action.GetSkillCustomArg(skill, 'SpeedTimes') != 0:
            if cl_action.CheckHasStateFromAttacker(skill, cl_action.GetCurVID(skill), 33830):
                cl_action.AddFromAttackerStateCount(skill, 33830, 500, iTime = cl_action.GetSkillCustomArg(skill, 'SpeedTimes'))
                if cl_action.CheckHasState(skill, 33831):
                    cl_action.AddAttackerStateCount(skill, 33831, 500, iTime = cl_action.GetSkillCustomArg(skill, 'SpeedTimes'))
                else:
                    cl_action.TargetAddState(skill, 33831, cl_action.GetSkillCustomArg(skill, 'SpeedTimes'), 0, { }, cl_action.GetSkillAID(skill))
                    cl_action.AddAttackerStateCount(skill, 33831, 500, iTime = cl_action.GetSkillCustomArg(skill, 'SpeedTimes'))
            else:
                cl_action.VictimAddState(skill, 33830, cl_action.GetSkillCustomArg(skill, 'SpeedTimes'), 0, { })
                cl_action.AddFromAttackerStateCount(skill, 33830, 500, iTime = cl_action.GetSkillCustomArg(skill, 'SpeedTimes'))
                if cl_action.CheckHasState(skill, 33831):
                    cl_action.AddAttackerStateCount(skill, 33831, 500, iTime = cl_action.GetSkillCustomArg(skill, 'SpeedTimes'))
                else:
                    cl_action.TargetAddState(skill, 33831, cl_action.GetSkillCustomArg(skill, 'SpeedTimes'), 0, { }, cl_action.GetSkillAID(skill))
                    cl_action.AddAttackerStateCount(skill, 33831, 500, iTime = cl_action.GetSkillCustomArg(skill, 'SpeedTimes'))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgHitPos(skill)):
                return None
            cls.EnableShow(skill, 999, 70, 30, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 180, lockDis = 12, IgnoreDefalutDis = 9999, iIgnoreMonsterID = cl_action.GetCurVID(skill), FilterDie = True, lockFromCartoon = True, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 15, traceTimes = cl_action.GetSkillCustomArg(skill, 'AttCnt'), maskFightType = NWARRIOR_DROP, noTargetOver = True, searchByDistance = True, canLockMoreTimes = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TraceCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSkillVarCache(skill, 'isHitWeakness', cl_action.CheckHitWeakness(skill))
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) })
        if cl_action.GetSkillCustomArg(skill, 'SpeedTimes') != 0:
            if cl_action.CheckHasStateFromAttacker(skill, cl_action.GetCurVID(skill), 33830):
                cl_action.AddFromAttackerStateCount(skill, 33830, 500, iTime = cl_action.GetSkillCustomArg(skill, 'SpeedTimes'))
                if cl_action.CheckHasState(skill, 33831):
                    cl_action.AddAttackerStateCount(skill, 33831, 500, iTime = cl_action.GetSkillCustomArg(skill, 'SpeedTimes'))
                else:
                    cl_action.TargetAddState(skill, 33831, cl_action.GetSkillCustomArg(skill, 'SpeedTimes'), 0, { }, cl_action.GetSkillAID(skill))
                    cl_action.AddAttackerStateCount(skill, 33831, 500, iTime = cl_action.GetSkillCustomArg(skill, 'SpeedTimes'))
            else:
                cl_action.VictimAddState(skill, 33830, cl_action.GetSkillCustomArg(skill, 'SpeedTimes'), 0, { })
                cl_action.AddFromAttackerStateCount(skill, 33830, 500, iTime = cl_action.GetSkillCustomArg(skill, 'SpeedTimes'))
                if cl_action.CheckHasState(skill, 33831):
                    cl_action.AddAttackerStateCount(skill, 33831, 500, iTime = cl_action.GetSkillCustomArg(skill, 'SpeedTimes'))
                else:
                    cl_action.TargetAddState(skill, 33831, cl_action.GetSkillCustomArg(skill, 'SpeedTimes'), 0, { }, cl_action.GetSkillAID(skill))
                    cl_action.AddAttackerStateCount(skill, 33831, 500, iTime = cl_action.GetSkillCustomArg(skill, 'SpeedTimes'))
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 1, 70, 30, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 180, lockDis = 50, IgnoreDefalutDis = 9999, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = True, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 15, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = True, searchByDistance = True, canLockMoreTimes = False)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.IsHeroCtrl(skill):
        cl_action.SetSkillCustomDataInt(skill, 'Att', cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
        if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) > 0:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 1, index = 0)
        elif len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) > 0:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.clientactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 12041
    m_Name = '#NT#通用弹射发射'
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
        'ChargeTime': 0 }
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'Radius': 3 }

