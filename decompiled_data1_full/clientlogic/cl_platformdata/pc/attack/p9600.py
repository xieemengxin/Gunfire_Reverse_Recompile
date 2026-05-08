# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9600.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9600.pyc
# Source Generated with Decompyle++
# File: p9600.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, ScanTargetCartoon, SendDataCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINTSPECIAL

class CCartoon9(TimerCartoon):
    m_SID = 9
    
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
        cl_action.SkillForbid(skill, False, 1069)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 40, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(DirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 450 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVarCache(skill, 'Targets')[cl_action.GetCartoonLoopID(skill, 0)]), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 2) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else cl_action.GetTimerCartoonCurTimes(skill, 0))

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
        CCartoon6.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 2) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else cl_action.GetTimerCartoonCurTimes(skill, 0))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 5, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(SendDataCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.CheckNumberinList(skill, cl_action.GetSkillVarCache(skill, 'Targets')[cl_action.GetCartoonLoopID(skill, 0)], cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)):
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
                cartoon = { }
                CCartoon2.Init(skill, cartoon, casting = 0, index = cl_action.GetTimerCartoonCurTimes(skill, 0))
            else:
                cartoon = { }
                CCartoon6.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 2) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else cl_action.GetTimerCartoonCurTimes(skill, 0))

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
            cls.EnableShow(skill)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = cl_action.GetTimerCartoonCurTimes(skill, 0))
        else:
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 2) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else cl_action.GetTimerCartoonCurTimes(skill, 0))

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
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 10, cl_action.ToInt(skill, cl_action.GetDictionaryValue(skill, cl_action.GetCartoonDict(skill, 1), cl_action.GetSkillVarCache(skill, 'Targets')[cl_action.GetCartoonLoopID(skill, 0)]) - 1))

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(DirectPosCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 450 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVarCache(skill, 'Targets')[cl_action.GetCartoonLoopID(skill, 5)]), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon7.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 5, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(DirectPosCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 450 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSkillVarCache(skill, 'TargetPos'), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'Targets', cl_action.GetDictionaryKeys(skill, cl_action.GetCartoonDict(skill, 1)))
        if len(cl_action.GetSkillVarCache(skill, 'Targets')) > 0:
            for i1 in range(0, len(cl_action.GetSkillVarCache(skill, 'Targets')), 1):
                if cl_action.GetDictionaryValue(skill, cl_action.GetCartoonDict(skill, 1), cl_action.GetSkillVarCache(skill, 'Targets')[i1]) > 1:
                    cartoon = { }
                    CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
                    continue
                if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
                    cartoon = { }
                    CCartoon5.Init(skill, cartoon, casting = 0, index = i1)
                    continue
                cl_action.SetSkillVarCache(skill, 'TargetPos', cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVarCache(skill, 'Targets')[i1]))
                cartoon = { }
                CCartoon8.Init(skill, cartoon, casting = 0, index = 0)
            

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
            cls.EnableShow(skill, 10, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(ScanTargetCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.EnableWeaponPerform(skill, 4385)
        cartoon = { }
        CCartoon9.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SetSkillScanInfo(skill, cl_action.GetCartoonDict(skill, 1))
        cl_action.SendCurCartoonTriggerMsg(skill)
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 99, 30, 0.3 * (0.3 if cl_action.CheckHasInscription(skill, 4969) else 1) * (1 - 0.5(cl_action.ToInt, (skill if cl_action.ToInt(skill, (skill.m_Cache['AttSpeed'] - 350 if skill.m_Cache['AttSpeed'] - 350 > 0 else 0) / 5) * 0.01 > 0.5 else skill.m_Cache['AttSpeed'] - 350 if skill.m_Cache['AttSpeed'] - 350 > 0 else 0) / 5) * 0.01), maxMarkNum = 3, clearTime = 1, clearIntervalTime = 0.3, maxScanNum = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SkillForbid(skill, True, 1069)
    cl_action.DisableWeaponPerform(skill, 4385)
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.SkillForbid(skill, False, 1069)
    cl_action.EnableWeaponPerform(skill, 4385)
    cl_action.AttackerRemoveState(skill, 1392, bSameItem = False)


def End(skill):
    cl_action.AttackerRemoveState(skill, 1392, bSameItem = False)


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINTSPECIAL]


def GetOtherMonster():
    return []

from cl_perform.attack import CChargePerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9600
    m_Name = '#NT#追踪导弹'
    m_ExtPerform = (4385,)
    m_HaltInfo = {
        108: 1,
        40108: 1,
        30108: 1,
        10214: 1,
        10149: 1,
        143: 1,
        286: 1 }
    m_IgnoreHalt = {
        1310: 1,
        1801: 1 }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0,
        'MaxPFBullet': 40000,
        'PFBulletUse': 40000,
        'PFBulletRecover': 200,
        'CostPFBulletDuringUse': 1,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_ClassifyTag = (1, 2)
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 0
    m_CheckForbid = 1019

