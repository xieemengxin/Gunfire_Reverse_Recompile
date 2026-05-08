# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9211.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9211.pyc
# Source Generated with Decompyle++
# File: p9211.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ChargeCartoon, DirectPosCartoon, SkillSummonCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, DAM_USE_SHIELD, OBJ_ENEMY, SKILLCACHE_INT

class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.BreakVictimProtection(skill, DAM_USE_SHIELD, True, True)
        cl_action.WeaponDamage(skill, {
            'Att': skill.m_Cache['SnipeTime'] }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCartoonEnd(skill, 2), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

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
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 10, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(SkillSummonCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimTouch(skill):
            if skill.m_Cache['EnergyBar'] == 0:
                cl_action.BreakVictimProtection(skill, DAM_USE_SHIELD, True, True)
                cl_action.WeaponDamage(skill, {
                    'Att': skill.m_Cache['SnipeFov'] }, { }, sendPFMsg = False)
            else:
                cl_action.WeaponDamage(skill, {
                    'Att': skill.m_Cache['SnipeFov'] }, { }, sendPFMsg = False)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': skill.m_Cache['SnipeFov'] }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, skill.m_Cache['Pierce'], 5530, 1027, 0.5, 50, 25, 0, effect = None, hitInterval = 14, reboundCnt = 0, driveSpeed = 0, driveAccSpeed = 0, targettype = OBJ_ENEMY)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(ChargeCartoon):
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
        for i1 in range(0, 1, 1):
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 50, 2, 0, False, False, effect = None, halfEnd = False, offsetTime = 0, breaktips = True)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.attack import CChargePerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9211
    m_Name = '特斯拉'
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
        'ChargeTime': 20 }
    m_BulletUse = 1
    m_ForbidRule = 1045
    m_CheckForbid = 1001

