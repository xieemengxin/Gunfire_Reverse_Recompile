# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9503.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9503.pyc
# Source Generated with Decompyle++
# File: p9503.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ChargeCartoon, RayCastCartoon, TimerCartoon, TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, CRT_EXTCHECK_PENETRATION, NWARRIOR_DROP, OBJ_ENEMY, SKILLCACHE_ATTACKSTATUS, SKILLCACHE_EXTRATRAJECTORY

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
            cls.EnableShow(skill, skill.m_Cache['ChargeTime'] * 8, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TraceCartoon):
    m_SID = 7
    
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
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), skill.m_Cache['BulletSpeed'], showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 180, lockDis = 100, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = False, searchByDistance = False, canLockMoreTimes = False, scale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(RayCastCartoon):
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
    
    def InitSuccess(cls, skill, i2, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), 120, targettype = OBJ_ENEMY, liveTime = 0, radius = (cl_action.GetCartoonChargeLevel(skill, 4) - 3) * 0.2 + 0.45, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_PENETRATION)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cl_action.SendTriggerBurstMsg(skill)

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
                for i5 in range(0, cl_action.GetTrajectory(skill), 1):
                    cartoon = { }
                    CCartoon7.Init(skill, cartoon, casting = 0, index = i5)
                
            else:
                cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                for i6 in range(0, cl_action.GetTrajectory(skill), 1):
                    cartoon = { }
                    CCartoon3.Init(skill, cartoon, casting = 0, index = i6)
                
        elif cl_action.CheckHasInscription(skill, 4896):
            for i7 in range(0, cl_action.GetTrajectory(skill), 1):
                cartoon = { }
                CCartoon7.Init(skill, cartoon, casting = 0, index = i7)
            
        else:
            cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
            for i8 in range(0, cl_action.GetTrajectory(skill), 1):
                cartoon = { }
                CCartoon3.Init(skill, cartoon, casting = 0, index = i8)
            

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 15, cl_action.GetAttackerAttr(skill, 'BurstCount'))

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(ChargeCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

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
        if cl_action.IsHeroCtrl(skill):
            if cl_action.GetCartoonChargeLevel(skill, 4) == 2:
                if cl_action.GetCartoonChargeLevel(skill, 4) >= 3:
                    cl_action.ModifySkillCache(skill, 'CrazyEff', (cl_action.GetCartoonChargeLevel(skill, 4) - 3) * 10000 + cl_action.GetWeaponIntAttr(skill, 'CrazyEff'))
                if cl_action.GetPerformArgValue(skill, 'CalLucky', iDefault = 0) > 0:
                    cl_action.ModifySkillCache(skill, 'LuckyHit', (100 if cl_action.GetCartoonChargeLevel(skill, 4) >= 7 else 14 * cl_action.GetCartoonChargeLevel(skill, 4)) + skill.m_Cache['LuckyHit'])
                if cl_action.IsOpenSnipe(skill):
                    if cl_action.CheckHasInscription(skill, 4896):
                        for i1 in range(0, cl_action.GetTrajectory(skill), 1):
                            cartoon = { }
                            CCartoon7.Init(skill, cartoon, casting = 0, index = i1)
                        
                    else:
                        cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                        for i2 in range(0, cl_action.GetTrajectory(skill), 1):
                            cartoon = { }
                            CCartoon3.Init(skill, cartoon, casting = 0, index = i2)
                        
                elif cl_action.CheckHasInscription(skill, 4896):
                    for i3 in range(0, cl_action.GetTrajectory(skill), 1):
                        cartoon = { }
                        CCartoon7.Init(skill, cartoon, casting = 0, index = i3)
                    
                else:
                    cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                    for i4 in range(0, cl_action.GetTrajectory(skill), 1):
                        cartoon = { }
                        CCartoon3.Init(skill, cartoon, casting = 0, index = i4)
                    
                if cl_action.GetAttackerAttr(skill, 'BurstCount') > 0:
                    cartoon = { }
                    CCartoon5.Init(skill, cartoon, casting = 0, index = 0)
                if cl_action.CheckHasState(skill, 39706):
                    cl_action.AddAttackerStateCount(skill, 39706, -1, iTime = 0, bFromAttack = True, bFromWeapon = True)
                
            if cl_action.GetCartoonChargeLevel(skill, 4) == 3:
                if cl_action.GetCartoonChargeLevel(skill, 4) >= 3:
                    cl_action.ModifySkillCache(skill, 'CrazyEff', (cl_action.GetCartoonChargeLevel(skill, 4) - 3) * 10000 + cl_action.GetWeaponIntAttr(skill, 'CrazyEff'))
                if cl_action.GetPerformArgValue(skill, 'CalLucky', iDefault = 0) > 0:
                    cl_action.ModifySkillCache(skill, 'LuckyHit', (100 if cl_action.GetCartoonChargeLevel(skill, 4) >= 7 else 14 * cl_action.GetCartoonChargeLevel(skill, 4)) + skill.m_Cache['LuckyHit'])
                if cl_action.IsOpenSnipe(skill):
                    if cl_action.CheckHasInscription(skill, 4896):
                        for i9 in range(0, cl_action.GetTrajectory(skill), 1):
                            cartoon = { }
                            CCartoon7.Init(skill, cartoon, casting = 0, index = i9)
                        
                    else:
                        cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                        for i10 in range(0, cl_action.GetTrajectory(skill), 1):
                            cartoon = { }
                            CCartoon3.Init(skill, cartoon, casting = 0, index = i10)
                        
                elif cl_action.CheckHasInscription(skill, 4896):
                    for i11 in range(0, cl_action.GetTrajectory(skill), 1):
                        cartoon = { }
                        CCartoon7.Init(skill, cartoon, casting = 0, index = i11)
                    
                else:
                    cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                    for i12 in range(0, cl_action.GetTrajectory(skill), 1):
                        cartoon = { }
                        CCartoon3.Init(skill, cartoon, casting = 0, index = i12)
                    
                if cl_action.GetAttackerAttr(skill, 'BurstCount') > 0:
                    cartoon = { }
                    CCartoon5.Init(skill, cartoon, casting = 0, index = 0)
                if cl_action.CheckHasState(skill, 39706):
                    cl_action.AddAttackerStateCount(skill, 39706, -1, iTime = 0, bFromAttack = True, bFromWeapon = True)
                
            if cl_action.GetCartoonChargeLevel(skill, 4) == 4:
                if cl_action.GetCartoonChargeLevel(skill, 4) >= 3:
                    cl_action.ModifySkillCache(skill, 'CrazyEff', (cl_action.GetCartoonChargeLevel(skill, 4) - 3) * 10000 + cl_action.GetWeaponIntAttr(skill, 'CrazyEff'))
                if cl_action.GetPerformArgValue(skill, 'CalLucky', iDefault = 0) > 0:
                    cl_action.ModifySkillCache(skill, 'LuckyHit', (100 if cl_action.GetCartoonChargeLevel(skill, 4) >= 7 else 14 * cl_action.GetCartoonChargeLevel(skill, 4)) + skill.m_Cache['LuckyHit'])
                if cl_action.IsOpenSnipe(skill):
                    if cl_action.CheckHasInscription(skill, 4896):
                        for i17 in range(0, cl_action.GetTrajectory(skill), 1):
                            cartoon = { }
                            CCartoon7.Init(skill, cartoon, casting = 0, index = i17)
                        
                    else:
                        cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                        for i18 in range(0, cl_action.GetTrajectory(skill), 1):
                            cartoon = { }
                            CCartoon3.Init(skill, cartoon, casting = 0, index = i18)
                        
                elif cl_action.CheckHasInscription(skill, 4896):
                    for i19 in range(0, cl_action.GetTrajectory(skill), 1):
                        cartoon = { }
                        CCartoon7.Init(skill, cartoon, casting = 0, index = i19)
                    
                else:
                    cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                    for i20 in range(0, cl_action.GetTrajectory(skill), 1):
                        cartoon = { }
                        CCartoon3.Init(skill, cartoon, casting = 0, index = i20)
                    
                if cl_action.GetAttackerAttr(skill, 'BurstCount') > 0:
                    cartoon = { }
                    CCartoon5.Init(skill, cartoon, casting = 0, index = 0)
                if cl_action.CheckHasState(skill, 39706):
                    cl_action.AddAttackerStateCount(skill, 39706, -1, iTime = 0, bFromAttack = True, bFromWeapon = True)
                
            if cl_action.GetCartoonChargeLevel(skill, 4) == 5:
                if cl_action.GetCartoonChargeLevel(skill, 4) >= 3:
                    cl_action.ModifySkillCache(skill, 'CrazyEff', (cl_action.GetCartoonChargeLevel(skill, 4) - 3) * 10000 + cl_action.GetWeaponIntAttr(skill, 'CrazyEff'))
                if cl_action.GetPerformArgValue(skill, 'CalLucky', iDefault = 0) > 0:
                    cl_action.ModifySkillCache(skill, 'LuckyHit', (100 if cl_action.GetCartoonChargeLevel(skill, 4) >= 7 else 14 * cl_action.GetCartoonChargeLevel(skill, 4)) + skill.m_Cache['LuckyHit'])
                if cl_action.IsOpenSnipe(skill):
                    if cl_action.CheckHasInscription(skill, 4896):
                        for i25 in range(0, cl_action.GetTrajectory(skill), 1):
                            cartoon = { }
                            CCartoon7.Init(skill, cartoon, casting = 0, index = i25)
                        
                    else:
                        cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                        for i26 in range(0, cl_action.GetTrajectory(skill), 1):
                            cartoon = { }
                            CCartoon3.Init(skill, cartoon, casting = 0, index = i26)
                        
                elif cl_action.CheckHasInscription(skill, 4896):
                    for i27 in range(0, cl_action.GetTrajectory(skill), 1):
                        cartoon = { }
                        CCartoon7.Init(skill, cartoon, casting = 0, index = i27)
                    
                else:
                    cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                    for i28 in range(0, cl_action.GetTrajectory(skill), 1):
                        cartoon = { }
                        CCartoon3.Init(skill, cartoon, casting = 0, index = i28)
                    
                if cl_action.GetAttackerAttr(skill, 'BurstCount') > 0:
                    cartoon = { }
                    CCartoon5.Init(skill, cartoon, casting = 0, index = 0)
                if cl_action.CheckHasState(skill, 39706):
                    cl_action.AddAttackerStateCount(skill, 39706, -1, iTime = 0, bFromAttack = True, bFromWeapon = True)
                
            if cl_action.GetCartoonChargeLevel(skill, 4) == 6:
                if cl_action.GetCartoonChargeLevel(skill, 4) >= 3:
                    cl_action.ModifySkillCache(skill, 'CrazyEff', (cl_action.GetCartoonChargeLevel(skill, 4) - 3) * 10000 + cl_action.GetWeaponIntAttr(skill, 'CrazyEff'))
                if cl_action.GetPerformArgValue(skill, 'CalLucky', iDefault = 0) > 0:
                    cl_action.ModifySkillCache(skill, 'LuckyHit', (100 if cl_action.GetCartoonChargeLevel(skill, 4) >= 7 else 14 * cl_action.GetCartoonChargeLevel(skill, 4)) + skill.m_Cache['LuckyHit'])
                if cl_action.IsOpenSnipe(skill):
                    if cl_action.CheckHasInscription(skill, 4896):
                        for i33 in range(0, cl_action.GetTrajectory(skill), 1):
                            cartoon = { }
                            CCartoon7.Init(skill, cartoon, casting = 0, index = i33)
                        
                    else:
                        cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                        for i34 in range(0, cl_action.GetTrajectory(skill), 1):
                            cartoon = { }
                            CCartoon3.Init(skill, cartoon, casting = 0, index = i34)
                        
                elif cl_action.CheckHasInscription(skill, 4896):
                    for i35 in range(0, cl_action.GetTrajectory(skill), 1):
                        cartoon = { }
                        CCartoon7.Init(skill, cartoon, casting = 0, index = i35)
                    
                else:
                    cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                    for i36 in range(0, cl_action.GetTrajectory(skill), 1):
                        cartoon = { }
                        CCartoon3.Init(skill, cartoon, casting = 0, index = i36)
                    
                if cl_action.GetAttackerAttr(skill, 'BurstCount') > 0:
                    cartoon = { }
                    CCartoon5.Init(skill, cartoon, casting = 0, index = 0)
                if cl_action.CheckHasState(skill, 39706):
                    cl_action.AddAttackerStateCount(skill, 39706, -1, iTime = 0, bFromAttack = True, bFromWeapon = True)
                
            if cl_action.GetCartoonChargeLevel(skill, 4) == 7:
                if cl_action.GetCartoonChargeLevel(skill, 4) >= 3:
                    cl_action.ModifySkillCache(skill, 'CrazyEff', (cl_action.GetCartoonChargeLevel(skill, 4) - 3) * 10000 + cl_action.GetWeaponIntAttr(skill, 'CrazyEff'))
                if cl_action.GetPerformArgValue(skill, 'CalLucky', iDefault = 0) > 0:
                    cl_action.ModifySkillCache(skill, 'LuckyHit', (100 if cl_action.GetCartoonChargeLevel(skill, 4) >= 7 else 14 * cl_action.GetCartoonChargeLevel(skill, 4)) + skill.m_Cache['LuckyHit'])
                if cl_action.IsOpenSnipe(skill):
                    if cl_action.CheckHasInscription(skill, 4896):
                        for i41 in range(0, cl_action.GetTrajectory(skill), 1):
                            cartoon = { }
                            CCartoon7.Init(skill, cartoon, casting = 0, index = i41)
                        
                    else:
                        cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                        for i42 in range(0, cl_action.GetTrajectory(skill), 1):
                            cartoon = { }
                            CCartoon3.Init(skill, cartoon, casting = 0, index = i42)
                        
                elif cl_action.CheckHasInscription(skill, 4896):
                    for i43 in range(0, cl_action.GetTrajectory(skill), 1):
                        cartoon = { }
                        CCartoon7.Init(skill, cartoon, casting = 0, index = i43)
                    
                else:
                    cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                    for i44 in range(0, cl_action.GetTrajectory(skill), 1):
                        cartoon = { }
                        CCartoon3.Init(skill, cartoon, casting = 0, index = i44)
                    
                if cl_action.GetAttackerAttr(skill, 'BurstCount') > 0:
                    cartoon = { }
                    CCartoon5.Init(skill, cartoon, casting = 0, index = 0)
                if cl_action.CheckHasState(skill, 39706):
                    cl_action.AddAttackerStateCount(skill, 39706, -1, iTime = 0, bFromAttack = True, bFromWeapon = True)
                elif cl_action.GetCartoonChargeLevel(skill, 4) >= 3:
                    cl_action.ModifySkillCache(skill, 'CrazyEff', (cl_action.GetCartoonChargeLevel(skill, 4) - 3) * 10000 + cl_action.GetWeaponIntAttr(skill, 'CrazyEff'))
                if cl_action.GetPerformArgValue(skill, 'CalLucky', iDefault = 0) > 0:
                    cl_action.ModifySkillCache(skill, 'LuckyHit', (100 if cl_action.GetCartoonChargeLevel(skill, 4) >= 7 else 14 * cl_action.GetCartoonChargeLevel(skill, 4)) + skill.m_Cache['LuckyHit'])
                if cl_action.IsOpenSnipe(skill):
                    if cl_action.CheckHasInscription(skill, 4896):
                        for i49 in range(0, cl_action.GetTrajectory(skill), 1):
                            cartoon = { }
                            CCartoon7.Init(skill, cartoon, casting = 0, index = i49)
                        
                    else:
                        cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                        for i50 in range(0, cl_action.GetTrajectory(skill), 1):
                            cartoon = { }
                            CCartoon3.Init(skill, cartoon, casting = 0, index = i50)
                        
                elif cl_action.CheckHasInscription(skill, 4896):
                    for i51 in range(0, cl_action.GetTrajectory(skill), 1):
                        cartoon = { }
                        CCartoon7.Init(skill, cartoon, casting = 0, index = i51)
                    
                else:
                    cl_action.SetSkillVarCache(skill, 'BulletFrameStart', cl_action.GetMuzzlePos(skill))
                    for i52 in range(0, cl_action.GetTrajectory(skill), 1):
                        cartoon = { }
                        CCartoon3.Init(skill, cartoon, casting = 0, index = i52)
                    
                if cl_action.GetAttackerAttr(skill, 'BurstCount') > 0:
                    cartoon = { }
                    CCartoon5.Init(skill, cartoon, casting = 0, index = 0)
                if cl_action.CheckHasState(skill, 39706):
                    cl_action.AddAttackerStateCount(skill, 39706, -1, iTime = 0, bFromAttack = True, bFromWeapon = True)
        return 100

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, skill.m_Cache['ChargeTime'], 7, 0, False, True, halfEnd = False, offsetTime = 0, breaktips = True, allowMaxChargeLowAmmo = False)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon4.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_ATTACKSTATUS,
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

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

