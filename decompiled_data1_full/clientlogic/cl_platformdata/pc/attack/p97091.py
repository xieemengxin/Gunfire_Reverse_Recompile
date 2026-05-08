# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p97091.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p97091.pyc
# Source Generated with Decompyle++
# File: p97091.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ExternalDriveCartoon, ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, HIT_OVER_NORMAL, MONSTER_PART_BARRIAR, MONSTER_PART_UNTAGGED, OBJ_ENEMY

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(ExternalDriveCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        if cl_action.CheckVictimInStruckCD(skill):
            cl_action.PushMoveVictim(skill, (0, 0, 0), 40, 6.4, (0, 0, 0), iCartoonSID = 4, bKnockBack = True)
        else:
            cl_action.PushVictim(skill, (0, 0, 0), 40, 6.4, 10000, angle = 0, iCartoonSID = 4, iIgnoreStruckCD = 0, iClient = 1)

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
            cls.EnableShow(skill, cl_action.GetCurVID(skill), cl_action.GetSkillHitArea(skill), 3)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(ThrowByPowerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        if cl_action.IsHeroCtrl(skill):
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckHitPointArea(skill, MONSTER_PART_BARRIAR):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
        cl_action.SetSkillVarCache(skill, 'HitNum', cl_action.GetSkillVarCache(skill, 'HitNum') + 1)
        cl_action.WeaponDamage(skill, {
            'Att': ((4 if cl_action.GetSkillVarCache(skill, 'HitNum') > 4 else cl_action.GetSkillVarCache(skill, 'HitNum')) * 25 + 100 if cl_action.CheckHasInscription(skill, 13093) else 100) * 3 }, { }, sendPFMsg = True)
        if cl_action.IsHeroCtrl(skill):
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        if cl_action.GetSkillVarCache(skill, 'isHitStatic') and cl_math.CalDistance3D(cl_action.CrtArgHitPos(skill), cl_action.GetStartPositionInCrt(skill, 3)) <= 4.8 and cl_action.IsHeroCtrl(skill):
            cl_action.SetSkillVarCache(skill, 'isHitStatic', True)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = 'muzzle'))):
                return None
            cls.EnableShow(skill, 3, (0, 0, 0), (0, 0), 200, True, False, 200, innerRadius = 0.1, pierce = 99, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, iTriggerBullet = 0, checkWeaknessAngle = 0, checkWeaknessDis = 0)

    InitSuccess = classmethod(InitSuccess)


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
        for i1 in range(0, 1, 1):
            cl_action.SetSkillVarCache(skill, 'isHitStatic', False)
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, int(66 / skill.m_Cache['AttSpeed'] / 180), 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'HitNum', 0)
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


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
    m_SID = 97091
    m_Name = '#NT#聚能法杖右键'
    m_ExtPerform = (5306,)
    m_HaltInfo = {
        40108: 1,
        30108: 1,
        10214: 1,
        143: 1 }
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
        'MaxPFBullet': 16000,
        'PFBulletUse': 16000,
        'PFBulletRecover': 1000,
        'CostPFBulletDuringUse': 1,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_ClassifyTag = (2,)
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 1099
    m_CheckForbid = 1019

