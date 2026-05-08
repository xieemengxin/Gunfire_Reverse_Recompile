# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9594.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9594.pyc
# Source Generated with Decompyle++
# File: p9594.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import LightningChainCartoon, ThrowByPowerCartoon, TimerCartoon, TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, HIT_OVER_NORMAL, OBJ_ENEMY

class CCartoon0(TraceCartoon):
    m_SID = 0
    
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
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 3)):
                return None
            cls.EnableShow(skill, 1, 50, 50, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 0, angle = 180, lockAngle = 0, lockDis = 0, IgnoreDefalutDis = 0, iIgnoreMonsterID = cl_action.GetCartoonHitTargetInOrder(skill, 3), FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False)

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
        CCartoon0.Init(skill, cartoon, casting = 1, index = cl_action.GetCartoonLoopID(skill, 1))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 2, 10, 10, cl_action.GetCartoonHitTargetInOrder(skill, 3), '', 1, True)

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
        if cl_action.CheckVictimHasBeaconSunmon(skill, cl_action.GetCartoonHitTargetInOrder(skill, 3)):
            cl_action.TriggerVictimBeaconSummon(skill, 1)
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 1, index = cl_action.GetCartoonLoopID(skill, 3))
        else:
            cl_action.CreateBeaconSummon(skill, 1061, cl_action.GetCartoonHitFirstTargetPos(skill, 3), 2000, 7, 3, False)
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 1, index = cl_action.GetCartoonLoopID(skill, 3))

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
            cls.EnableShow(skill, 0.2, (0, 16, 0), (0, 0), 300, True, True, 0, innerRadius = 0.1, pierce = 1, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3)

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
        for i1 in range(0, 5, 1):
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 15, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon5.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9594
    m_Name = 's雷电锁链'
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
        'ColdTime': 50,
        'AttDistance': 0,
        'ChargeTime': 0,
        'MaxPFBullet': 6000,
        'PFBulletUse': 2000,
        'PFBulletRecover': 500,
        'CostPFBulletDuringUse': 1,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_ClassifyTag = (2,)
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 0
    m_CheckForbid = 1019

