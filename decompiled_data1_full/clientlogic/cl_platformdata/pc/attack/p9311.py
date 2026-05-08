# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9311.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9311.pyc
# Source Generated with Decompyle++
# File: p9311.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TraceLineCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY

class CCartoon2(TraceLineCartoon):
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
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), targettype = OBJ_ENEMY, effect = 0, radius = 1.5, lockTeamer = False, shootOnNoTarget = True, offsetradius = 20)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TraceLineCartoon):
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
    
    def InitSuccess(cls, skill, i2, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), targettype = OBJ_ENEMY, effect = 0, radius = 1.5, lockTeamer = False, shootOnNoTarget = True, offsetradius = 20)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TraceLineCartoon):
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

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i3, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), targettype = OBJ_ENEMY, effect = 0, radius = 1.5, lockTeamer = False, shootOnNoTarget = True, offsetradius = 20)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    for i1 in range(0, 4, 1):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = i1)
    
    if cl_action.GetTrajectory(skill) > 4:
        for i2 in range(4, 12 if cl_action.GetTrajectory(skill) > 12 else cl_action.GetTrajectory(skill), 1):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i2)
        
        if cl_action.GetTrajectory(skill) > 12:
            for i3 in range(12, 12 if cl_action.GetTrajectory(skill) > 24 else cl_action.GetTrajectory(skill), 1):
                cartoon = { }
                CCartoon3.Init(skill, cartoon, casting = 0, index = i3)
            


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.attack import CContinuousPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9311
    m_Name = '八爪鱼'
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

