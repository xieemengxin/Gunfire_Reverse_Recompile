# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9510.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9510.pyc
# Source Generated with Decompyle++
# File: p9510.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ChargeCartoon, SplitTraceCartoon, ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, HIT_OVER_NORMAL, OBJ_ALL, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY, WARRIOR_BOSS, WARRIOR_OBSTACLE_BROKENPILLAR

class CCartoon1(SplitTraceCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 200 if cl_action.GetSkillServerCache(skill, '1510') or cl_action.CheckHasState(skill, 1265) else 50 }, {
            'CrazyEff': 10000,
            'Weapon': 1510 }, sendPFMsg = False)
        if cl_action.CheckHasInscription(skill, 13023):
            if not cl_action.CheckVictimType(skill, WARRIOR_BOSS, OBJ_ALL) or cl_action.CheckVictimType(skill, WARRIOR_OBSTACLE_BROKENPILLAR, OBJ_ALL):
                cl_action.VictimAddState(skill, 1497, 1000, 0, { })

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
            cls.EnableShow(skill, 1, 40 if cl_action.CheckHasInscription(skill, 4948) else 30, 55, targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 0, angle = 0, nullLockAngle = 20, lockWeakness = False, forwardModel = True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(ThrowByPowerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckWarriorHasState(skill, cl_action.GetCurVID(skill), 1497):
            cl_action.AttackerAddState(skill, 1496, 0, 0, { })
        cl_action.SetSkillServerCache(skill, '1510', cl_action.CheckHitWeakness(skill))
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)
        for i2 in range(0, 3, 1):
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 0.25, (0, 16, 0), (1, 1), 500, True, True, 0, innerRadius = 0.05, pierce = skill.m_Cache['Pierce'], ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, iTriggerBullet = 0, checkWeaknessAngle = 0, checkWeaknessDis = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        cl_action.SendTriggerBurstMsg(skill)

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
        for i3 in range(0, cl_action.GetTrajectory(skill), 1):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i3)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 15, cl_action.GetAttackerAttr(skill, 'BurstCount'))

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(ChargeCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.AttackerAddState(skill, 1136, 0, 1, { })

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveState(skill, 1136, bSameItem = False)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        for i1 in range(0, cl_action.GetTrajectory(skill), 1):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
        
        if cl_action.GetAttackerAttr(skill, 'BurstCount') > 0:
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 5, 10, 0, False, False, halfEnd = False, offsetTime = 0, breaktips = True, allowMaxChargeLowAmmo = False)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.attack import CChargePerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9510
    m_Name = '分裂弓'
    m_ExtPerform = (4185,)
    m_HaltInfo = {
        108: 1,
        40108: 1,
        30108: 1,
        10214: 1,
        143: 1,
        286: 1 }
    m_IgnoreHalt = {
        1310: 1,
        1801: 1,
        1301: 1 }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_BulletUse = 1
    m_ForbidRule = 1045
    m_CheckForbid = 1001

