# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9502.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9502.pyc
# Source Generated with Decompyle++
# File: p9502.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import SpiralRayCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_ATTACKSTATUS

class CCartoon1(SpiralRayCartoon):
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
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 0.35, skill.m_Cache['BulletSpeed'], 270, -1500, cl_action.GetWeaponAttDis(skill), skill.m_Cache['Pierce'], targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = 0, effectLiveTime = 2, damradius = 0.3)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(SpiralRayCartoon):
    m_SID = 2
    
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
            cls.EnableShow(skill, 0.35, skill.m_Cache['BulletSpeed'], 90, -1500, cl_action.GetWeaponAttDis(skill), skill.m_Cache['Pierce'], targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = 0, effectLiveTime = 2, damradius = 0.3)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableShow(skill, 15, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_ATTACKSTATUS]

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9502
    m_Name = '爆裂双星'
    m_ExtPerform = (4010,)
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
    m_BulletUse = 2
    m_ForbidRule = 0
    m_CheckForbid = 1001

