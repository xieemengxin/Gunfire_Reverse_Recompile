# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9514.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9514.pyc
# Source Generated with Decompyle++
# File: p9514.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import LightningChainCartoon, ThrowByPowerCartoon, TimerCartoon, TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, HIT_OVER_NORMAL, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY

class CCartoon6(TraceCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 150 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCartoonEnd(skill, 3)):
                return None
            cls.EnableShow(skill, 1, 50, 50, targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 0, angle = 180, lockWeakness = False, lockAngle = 0, lockDis = 0, IgnoreDefalutDis = 0, iIgnoreMonsterID = cl_action.GetCartoonHitTargetInOrder(skill, 3), FilterDie = True, lockFromCartoon = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(LightningChainCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 1, index = cl_action.GetCartoonLoopID(skill, 1))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 2, 10, 10, cl_action.GetCartoonHitTargetInOrder(skill, 3), '', 1, bKeepStart = True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TraceCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 150 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCartoonEnd(skill, 4)):
                return None
            cls.EnableShow(skill, 1, 50, 50, targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 0, angle = 180, lockWeakness = False, lockAngle = 0, lockDis = 0, IgnoreDefalutDis = 0, iIgnoreMonsterID = cl_action.GetCartoonHitTargetInOrder(skill, 4), FilterDie = True, lockFromCartoon = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(LightningChainCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 1, index = cl_action.GetCartoonLoopID(skill, 2))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 2, 10, 10, cl_action.GetCartoonHitTargetInOrder(skill, 4), '', 1, bKeepStart = True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TraceCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.FillPFBullet(skill, 9594, cl_action.GetAttackerWeaponPerformAttr(skill, 9594, 'PFBulletRecover'))
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)
        if cl_action.CheckVictimHasBeaconSunmon(skill, cl_action.GetCartoonHitTargetInOrder(skill, 4)):
            cl_action.TriggerVictimBeaconSummon(skill, 1)
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 1, index = cl_action.GetCartoonLoopID(skill, 4))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCartoonEnd(skill, 3)):
                return None
            cls.EnableShow(skill, 1, 50, 30, targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 0, angle = 180, lockWeakness = cl_action.GetSkillVarCache(skill, 'isHitWeakness'), lockAngle = 0, lockDis = 0, IgnoreDefalutDis = 0, iIgnoreMonsterID = cl_action.GetCartoonHitTargetInOrder(skill, 3), FilterDie = True, lockFromCartoon = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(LightningChainCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = cl_action.GetCartoonLoopID(skill, 0))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 2 if cl_action.CheckHasInscription(skill, 13040) else 1, 10, 10, cl_action.GetCartoonHitTargetInOrder(skill, 3), '', 1, bKeepStart = True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(ThrowByPowerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSkillVarCache(skill, 'isHitWeakness', cl_action.CheckHitWeakness(skill))
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)
        if cl_action.CheckVictimHasBeaconSunmon(skill, cl_action.GetCartoonHitTargetInOrder(skill, 3)):
            cl_action.TriggerVictimBeaconSummon(skill, 1)
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 1, index = cl_action.GetCartoonLoopID(skill, 3))
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = cl_action.GetCartoonLoopID(skill, 3))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgMuzzlePos(skill, cartoon)):
                return None
            cls.EnableShow(skill, 0.4, (0, 16, 0), (0.99, 0.99), 300, True, True, 0, innerRadius = 0.1, pierce = 1, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3)

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
        for i1 in range(0, cl_action.GetTrajectory(skill), 1):
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 8, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon5.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9514
    m_Name = '电镖'
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
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_BulletUse = 1
    m_ForbidRule = 0
    m_CheckForbid = 1001

