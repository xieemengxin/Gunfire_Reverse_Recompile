# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9505.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9505.pyc
# Source Generated with Decompyle++
# File: p9505.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ChargeCartoon, DirectPosCartoon, ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, HIT_OVER_NORMAL, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY

class CCartoon5(TimerCartoon):
    m_SID = 5
    
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


class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.CustomPerformAction(skill, 4887, 'CustomDamage', [
            100])

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgGetStickerPos(skill, 0), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                6], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, multipleExplode = True, explosionDelay = 10)

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
        if cl_action.CheckTargetAlive(skill, cl_action.GetCartoonHitTargetInOrder(skill, 0)):
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
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
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(ThrowByPowerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetCartoonChargeLevel(skill, 2) >= 10:
            cl_action.ModifySkillCache(skill, 'ThumpProb', 10000)
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)
            if cl_action.CheckHasInscription(skill, 4887):
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
            else:
                cl_action.WeaponDamage(skill, {
                    'Att': 100 }, { }, sendPFMsg = False)
                if cl_action.CheckHasInscription(skill, 4887):
                    cartoon = { }
                    CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        if cl_action.CheckHasInscription(skill, 4887):
            cl_action.CustomPerformAction(skill, 4887, 'HitStatic', [])
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 0.25, (0, cl_action.GetCartoonChargeLevel(skill, 2) + 5, 0), (1, 1), 300, True, True, 0, innerRadius = 0.05, pierce = skill.m_Cache['Pierce'], ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, iTriggerBullet = 0, checkWeaknessAngle = 3, checkWeaknessDis = 50)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
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
        for i2 in range(0, cl_action.GetTrajectory(skill), 1):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i2)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 15, cl_action.GetAttackerAttr(skill, 'BurstCount'))

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(ChargeCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        if cl_action.CheckHasInscription(skill, 4934):
            cl_action.AttackerAddState(skill, 1163, 0, 1, { })
            cl_action.AttackerAddState(skill, 1136, 0, 1, { })
            cl_action.AttackerAddState(skill, 1341, 0, 1, { })
            if cl_action.IsHeroCtrl(skill):
                cartoon = { }
                CCartoon5.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cl_action.AttackerAddState(skill, 1136, 0, 1, { })
                cl_action.AttackerAddState(skill, 1341, 0, 1, { })
                if cl_action.IsHeroCtrl(skill):
                    cartoon = { }
                    CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveState(skill, 1136, bSameItem = False)
        cl_action.AttackerRemoveState(skill, 1163, bSameItem = False)
        cl_action.AttackerRemoveState(skill, 1341, bSameItem = False)

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
            CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
        
        if cl_action.GetAttackerAttr(skill, 'BurstCount') > 0:
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, int(4 / skill.m_Cache['AttSpeed'] / 250), 10, 0, False, True, halfEnd = False, offsetTime = 0, breaktips = True, allowMaxChargeLowAmmo = False)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
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

from cl_perform.attack import CChargePerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9505
    m_Name = '金陵长弓'
    m_ExtPerform = (4028,)
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
        'ChargeTime': 0 }
    m_BulletUse = 1
    m_ForbidRule = 1045
    m_CheckForbid = 1001

