# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9609.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9609.pyc
# Source Generated with Decompyle++
# File: p9609.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import MeleeWeaponCartoon, ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, HIT_OVER_NORMAL, MONSTER_PART_BARRIAR, MONSTER_PART_UNTAGGED, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY

class CCartoon7(ThrowByPowerCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckHitPointArea(skill, MONSTER_PART_BARRIAR):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
        if cl_action.CheckHasInscription(skill, 13121) and cl_action.GetSkillServerCache(skill, 'HadRecover1') < 1:
            cl_action.AttackerAddState(skill, 33927, 1000, 0, { })
            cl_action.AddAttackerStateCount(skill, 33927, 1, iTime = 0, bFromAttack = False, bFromWeapon = False)
        if cl_action.GetAttackerWeaponPerformAttr(skill, 9609, 'MinUseEnergy') >= 1 and cl_action.GetSkillServerCache(skill, 'HadRecover1') < 1:
            cl_action.FillPFBullet(skill, 9690, cl_action.GetAttackerWeaponPerformAttr(skill, 9609, 'PFBulletRecover'), 1)
        cl_action.SetSkillServerCache(skill, 'HadRecover1', 1)
        cl_action.WeaponDamage(skill, {
            'Att': 60 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        if cl_action.GetSkillVarCache(skill, 'isHitStatic') and cl_math.CalDistance3D(cl_action.CrtArgHitPos(skill), cl_action.GetStartPositionInCrt(skill, 7)) <= 4.8 and cl_action.IsHeroCtrl(skill):
            cl_action.SetSkillVarCache(skill, 'isHitStatic', True)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 0.1, (0, 0, 0), (0.5, 0.5), 60, True, True, 0, innerRadius = 0.1, pierce = 99, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, iTriggerBullet = 0, checkWeaknessAngle = 0, checkWeaknessDis = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(ThrowByPowerCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckHitPointArea(skill, MONSTER_PART_BARRIAR):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
        if cl_action.CheckHasInscription(skill, 13121) and cl_action.GetSkillServerCache(skill, 'HadRecover2') < 1:
            cl_action.AttackerAddState(skill, 33927, 1000, 0, { })
            cl_action.AddAttackerStateCount(skill, 33927, 1, iTime = 0, bFromAttack = False, bFromWeapon = False)
        if cl_action.GetAttackerWeaponPerformAttr(skill, 9609, 'MinUseEnergy') >= 1 and cl_action.GetSkillServerCache(skill, 'HadRecover2') < 1:
            cl_action.FillPFBullet(skill, 9690, cl_action.GetAttackerWeaponPerformAttr(skill, 9609, 'PFBulletRecover'), 1)
        cl_action.SetSkillServerCache(skill, 'HadRecover2', 1)
        cl_action.WeaponDamage(skill, {
            'Att': 60 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        if cl_action.GetSkillVarCache(skill, 'isHitStatic') and cl_math.CalDistance3D(cl_action.CrtArgHitPos(skill), cl_action.GetStartPositionInCrt(skill, 6)) <= 4.8 and cl_action.IsHeroCtrl(skill):
            cl_action.SetSkillVarCache(skill, 'isHitStatic', True)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 0.1, (0, 0, 0), (0.5, 0.5), 60, True, True, 0, innerRadius = 0.1, pierce = 99, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, iTriggerBullet = 0, checkWeaknessAngle = 0, checkWeaknessDis = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        if cl_action.GetCartoonHitTargetCount(skill, 3) >= 1:
            if cl_action.CheckHasInscription(skill, 13121):
                cl_action.AttackerAddState(skill, 33927, 1000, 0, { })
                cl_action.AddAttackerStateCount(skill, 33927, 1, iTime = 0, bFromAttack = False, bFromWeapon = False)
            if not cl_action.GetAttackerWeaponPerformAttr(skill, 9609, 'MinUseEnergy') >= 1:
                cl_action.FillPFBullet(skill, 9690, cl_action.GetAttackerWeaponPerformAttr(skill, 9609, 'PFBulletRecover'), 1)

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
            cls.EnableShow(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(MeleeWeaponCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        if cl_action.CheckHasInscription(skill, 13122):
            cl_action.SetSkillVarCache(skill, 'isHitStatic', False)
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.IsHeroCtrl(skill):
            cl_action.WeaponDamage(skill, {
                'Att': cl_action.GetAttackerWeaponPerformAttr(skill, 9609, 'Att') }, { }, sendPFMsg = False)

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
            cls.EnableShow(skill, [
                skill.m_Cache['Radius'],
                0.4,
                100,
                30], meshCount = 5, totalTime = 10, targettype = OBJ_ENEMY, pierceStatic = False, left2right = False, center2around = False, canCritical = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        if cl_action.CheckHasInscription(skill, 13122):
            cl_action.SetSkillVarCache(skill, 'isHitStatic', False)
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
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, 4 if 20 / cl_action.GetAttSpeedRatio(skill) < 4 else 20 / cl_action.GetAttSpeedRatio(skill) - 20 / cl_action.GetAttSpeedRatio(skill) % 4), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(MeleeWeaponCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetCartoonHitTargetCount(skill, 0) >= 1:
            if cl_action.CheckHasInscription(skill, 13121):
                cl_action.AttackerAddState(skill, 33927, 1000, 0, { })
                cl_action.AddAttackerStateCount(skill, 33927, 1, iTime = 0, bFromAttack = False, bFromWeapon = False)
            if not cl_action.GetAttackerWeaponPerformAttr(skill, 9609, 'MinUseEnergy') >= 1:
                cl_action.FillPFBullet(skill, 9690, cl_action.GetAttackerWeaponPerformAttr(skill, 9609, 'PFBulletRecover'), 1)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.IsHeroCtrl(skill):
            cl_action.WeaponDamage(skill, {
                'Att': cl_action.GetAttackerWeaponPerformAttr(skill, 9609, 'Att') }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius'],
                0.4,
                100,
                30], meshCount = 5, totalTime = 10, targettype = OBJ_ENEMY, pierceStatic = False, left2right = False, center2around = False, canCritical = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
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
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 1, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 8, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 6, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'HadRecover1', 0)
    cl_action.SetSkillServerCache(skill, 'HadRecover2', 0)
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


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
    m_SID = 9609
    m_Name = '#NT#双刀-2'
    m_ExtPerform = ()
    m_HaltInfo = {
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
        'ChargeTime': 0,
        'MinUseEnergy': 0,
        'Att': 100,
        'PFBulletRecover': 1500 }
    m_BulletUse = 1
    m_ForbidRule = 1113
    m_CheckForbid = 1001
    m_BaseArgData = {
        'ExtraAttMul': 5000 }

