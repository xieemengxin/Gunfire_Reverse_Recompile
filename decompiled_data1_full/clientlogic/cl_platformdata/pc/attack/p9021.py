# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9021.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9021.pyc
# Source Generated with Decompyle++
# File: p9021.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, MONSTER_PART_BARRIAR, MONSTER_PART_SHIELD, OBJ_ENEMY

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, int(30 / skill.m_Cache['AttSpeed'] / 250), 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(RayCastCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckHitPointArea(skill, MONSTER_PART_SHIELD):
            cl_action.SetSkillVarCache(skill, 'isHitBarriar', cl_action.CheckHitPointArea(skill, MONSTER_PART_BARRIAR))
            cl_action.WeaponDamage(skill, {
                'Att': 400 }, { }, sendPFMsg = False)

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
    cl_action.SetSkillCustomDataInt(skill, 'EnhanceShoot', 0)
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 0, index = 0)


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
    m_SID = 9021
    m_Name = '#NT#双发步枪终结攻击'
    m_ExtPerform = ()
    m_HaltInfo = {
        40108: 1,
        30108: 1,
        10214: 1,
        143: 1 }
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
    m_BulletUse = 2
    m_ForbidRule = 1028
    m_CheckForbid = 1001

