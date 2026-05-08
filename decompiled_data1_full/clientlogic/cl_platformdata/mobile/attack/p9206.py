# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9206.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9206.pyc
# Source Generated with Decompyle++
# File: p9206.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon2(RayCastCartoon):
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
        cl_action.VictimAddState(skill, 1075, 500, 0, {
            'Cache': 1 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.CrtArgCameraCenterPos(skill, cartoon), (0.08, 0, 0))):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttackDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = None, effectLiveTime = 0, radius = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(RayCastCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)
        cl_action.VictimAddState(skill, 1075, 500, 0, {
            'Cache': 1 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.CrtArgCameraCenterPos(skill, cartoon), (0, 0.1, 0))):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttackDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = None, effectLiveTime = 0, radius = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(RayCastCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)
        cl_action.VictimAddState(skill, 1075, 500, 0, {
            'Cache': 1 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.CrtArgCameraCenterPos(skill, cartoon), (-0.08, 0, 0))):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttackDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = None, effectLiveTime = 0, radius = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def GetSkillCacheIndex():
    return []


def Halt(skill):
    pass


def End(skill):
    pass

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9206
    m_Name = '天眼'
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

