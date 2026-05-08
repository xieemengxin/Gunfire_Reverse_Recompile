# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9792.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9792.pyc
# Source Generated with Decompyle++
# File: p9792.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon, TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, MONSTER_PART_UNTAGGED, MONSTER_PART_WEAKNESS, NWARRIOR_DROP, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_INT

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
            cls.EnableShow(skill, 40, 1)

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
        if cl_action.CheckHitPointArea(skill, MONSTER_PART_WEAKNESS):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgHitPos(skill)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), 25, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 360, lockDis = 70, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 15, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = False, searchByDistance = False, canLockMoreTimes = False, scale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TraceCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckHitPointArea(skill, MONSTER_PART_WEAKNESS):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)
        cl_action.IgnoreCurVictimOnceAfterHit(skill)
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            cartoon = { }
            CCartoon7.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgHitPos(skill)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), 25, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 360, lockDis = 70, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 15, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = False, searchByDistance = False, canLockMoreTimes = False, scale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TraceCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckHitPointArea(skill, MONSTER_PART_WEAKNESS):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)
        cl_action.IgnoreCurVictimOnceAfterHit(skill)
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgHitPos(skill)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), 25, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 360, lockDis = 70, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 15, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = False, searchByDistance = False, canLockMoreTimes = False, scale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TraceCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckHitPointArea(skill, MONSTER_PART_WEAKNESS):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)
        cl_action.IgnoreCurVictimOnceAfterHit(skill)
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgHitPos(skill)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), 25, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 360, lockDis = 70, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 15, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = False, searchByDistance = False, canLockMoreTimes = False, scale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TraceCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckHitPointArea(skill, MONSTER_PART_WEAKNESS):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)
        cl_action.IgnoreCurVictimOnceAfterHit(skill)
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgHitPos(skill)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), 25, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 360, lockDis = 70, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 15, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = False, searchByDistance = False, canLockMoreTimes = False, scale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TraceCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckHitPointArea(skill, MONSTER_PART_WEAKNESS):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)
        if cl_action.CheckHasInscription(skill, 4967):
            cl_action.IgnoreCurVictimOnceAfterHit(skill)
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
            cl_action.TargetAddState(skill, 1896, 0, 0, { }, cl_action.GetNearestMonsterInRange(skill, 8, 1, 0, 0, 0, 0, iUseVictim = 1, iExcludeState = 1896, iExcludeStateCountMin = 1, iExcludeStateFromAttack = 1))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_math.Vec3Add(cl_action.GetCameraDirPos(skill, 0), cl_action.CrtArgToCameraRotation(skill, (0.414, -0.266, 2.276)))):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), skill.m_Cache['BulletSpeed'], showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 0, angle = 360 if cl_math.CalDistance3D(cl_action.GetCameraCenterPosition(skill, cartoon), cl_action.GetSceneObjPos(skill, 0)) <= 5 else 18, lockDis = 70, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 15, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = False, searchByDistance = False, canLockMoreTimes = False, scale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

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
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 28, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(TimerCartoon):
    m_SID = 8
    
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
            cls.EnableShow(skill, 18, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon8.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9792
    m_Name = '#NT#标记法杖2'
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
    m_ForbidRule = 1095
    m_CheckForbid = 1001

