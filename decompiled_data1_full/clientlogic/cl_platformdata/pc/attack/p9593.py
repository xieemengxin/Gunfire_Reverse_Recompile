# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9593.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9593.pyc
# Source Generated with Decompyle++
# File: p9593.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon, SplitArrowCartoon
from cl_commondefines import CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_RANDOM

class CCartoon2(SplitArrowCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 200 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_math.Vec3Add(cl_action.GetCameraCenterPosition(skill, cartoon), cl_action.CrtArgToCameraRotation(skill, (0.35, -0.2, 1.3)))):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], 3, 25, [
                (35, 0, 0),
                (-35, 0, 0),
                (0, 35, 0)], 5, 120, 25, 1, 90, 3, 1, 100, targettype = OBJ_ENEMY, accelerated = 70, lockWeakness = True, secondMaxAngle = 20, acceleratedSec = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(RayCastCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        if cl_action.CheckHasInscription(skill, 13111) and cl_action.GetRandomInRange(skill, 0, 100) <= 5:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

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
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, liveTime = 0, radius = 0.5, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_RANDOM]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9593
    m_Name = '速射弓左键弹道'
    m_ExtPerform = ()
    m_HaltInfo = {
        40108: 1,
        10108: 1,
        10214: 1,
        143: 1,
        286: 1,
        377: 1 }
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
    m_ClassifyTag = ()
    m_BulletUse = 1
    m_IsMinor = 1
    m_ForbidRule = 0
    m_CheckForbid = 1036

