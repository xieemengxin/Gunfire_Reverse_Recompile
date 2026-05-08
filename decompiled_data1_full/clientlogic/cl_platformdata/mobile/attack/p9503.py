# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9503.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9503.pyc
# Source Generated with Decompyle++
# File: p9503.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ChargeCartoon, RayCastCartoon, TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_ATTACKSTATUS, SKILLCACHE_EXTRATRAJECTORY

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
            'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgMuzzlePos(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttackDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = 0, effectLiveTime = 0, lineDistance = 1, angle = 180, lockWeakness = True, lockAngle = 10, lockDis = 100, IgnoreDefalutDis = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(RayCastCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i2, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgCameraCenterPos(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttackDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = 0, effectLiveTime = 2, radius = 0.45, flyoverdis = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(ChargeCartoon):
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
        if cl_action.IsOpenSnipe(skill):
            if cl_action.CheckHasInscription(skill, 4896):
                for i1 in range(0, cl_action.GetTrajectory(skill), 1):
                    cartoon = { }
                    CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
                
            else:
                for i2 in range(0, cl_action.GetTrajectory(skill), 1):
                    cartoon = { }
                    CCartoon1.Init(skill, cartoon, casting = 0, index = i2)
                
        elif cl_action.CheckHasInscription(skill, 4896):
            for i3 in range(0, cl_action.GetTrajectory(skill), 1):
                cartoon = { }
                CCartoon0.Init(skill, cartoon, casting = 0, index = i3)
            
        else:
            for i4 in range(0, cl_action.GetTrajectory(skill), 1):
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = i4)
            

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, skill.m_Cache['ChargeTime'], 2, 0, False, False, effect = None, halfEnd = False, offsetTime = 0)

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
        SKILLCACHE_ATTACKSTATUS,
        SKILLCACHE_EXTRATRAJECTORY]

from cl_perform.attack import CChargePerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9503
    m_Name = '苍鹰'
    m_ExtPerform = ()
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
        'ChargeTime': 10 }
    m_BulletUse = 1
    m_ForbidRule = 1045
    m_CheckForbid = 1001

