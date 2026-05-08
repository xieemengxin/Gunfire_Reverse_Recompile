# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9509.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9509.pyc
# Source Generated with Decompyle++
# File: p9509.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, HIT_OVER_NORMAL, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY

class CCartoon3(ThrowByPowerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)
        if cl_action.CheckHasInscription(skill, 4937):
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetBulletCurPos(skill, 1)):
                return None
            cls.EnableShow(skill, 0.2, (0, 16, 0), (0.99, 0.99), 300, True, False, 0, 0, None, 0, innerRadius = 0.1, pierce = 99, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(ThrowByPowerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)
        if cl_action.CheckHasInscription(skill, 4937):
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetBulletCurPos(skill, 1)):
                return None
            cls.EnableShow(skill, 0.2, (0, 16, 0), (0.99, 0.99), 300, True, False, 0, 0, None, 0, innerRadius = 0.1, pierce = 99, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(ThrowByPowerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)
        if cl_action.CheckHasInscription(skill, 4937):
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetBulletCurPos(skill, 1)):
                return None
            cls.EnableShow(skill, 0.2, (0, 16, 0), (0.99, 0.99), 300, True, False, 0, 0, None, 0, innerRadius = 0.1, pierce = 99, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(ThrowByPowerCartoon):
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
        if cl_action.CheckHasInscription(skill, 4937):
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgMuzzlePos(skill, cartoon)):
                return None
            cls.EnableShow(skill, 0.2, (0, 16, 0), (0.99, 0.99), 300, True, True, 0, 0, None, 0, innerRadius = 0.1, pierce = 99, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3)

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
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)
        if cl_action.CheckHasInscription(skill, 4937):
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)

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
            cls.EnableShow(skill, 0.2, (0, 16, 0), (0.99, 0.99), 300, True, False, 0, 0, None, 0, innerRadius = 0.1, pierce = 99, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3)

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
            if cl_action.CheckHasInscription(skill, 13026):
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
                continue
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
        

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
    m_SID = 9509
    m_Name = '棱镜'
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

