# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9801.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9801.pyc
# Source Generated with Decompyle++
# File: p9801.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, HIT_OVER_NORMAL, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY, WARRIOR_OBSTACLE_NORMAL

class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
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
            if not cls.EnableCheck(skill, start = cl_action.GetSkillVarCache(skill, 'victimPos'), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius'] * (0.6 if cl_action.CheckHasInscription(skill, 13064) else 1)], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = True, multipleExplode = True, explosionDelay = 10)

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
        cl_action.PushVictim(skill, cl_action.GetEndPositionInCrt(skill, 6), 20, 4, 10000, angle = 0, iCartoonSID = -1, iIgnoreStruckCD = 0, iClient = 0)
        cl_action.WeaponDamage(skill, {
            'Att': 50 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 5), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                0.6], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = True, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(ThrowByPowerCartoon):
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
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i2, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'victimPos'), (0, 0.4, 0))):
                return None
            cls.EnableShow(skill, 0.1, (0, -6, 0), (0, 0), 200, False, False, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, iTriggerBullet = 0, checkWeaknessAngle = 0, checkWeaknessDis = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(DirectPosCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 25 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSkillVarCache(skill, 'victimPos'), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                ((skill.m_Cache['Radius'] - 4) * 0.6 + 3) * (0.6 if cl_action.CheckHasInscription(skill, 13064) else 1)], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = True, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        if cl_action.CheckHasInscription(skill, 13063):
            for i2 in range(0, 3, 1):
                cartoon = { }
                CCartoon5.Init(skill, cartoon, casting = 0, index = i2)
            

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
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 80, 3)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(ThrowByPowerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckMonsterType(skill, WARRIOR_OBSTACLE_NORMAL, cl_action.GetCurVID(skill)):
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)
        else:
            cl_action.SetSkillVarCache(skill, 'victimPos', cl_action.CrtArgWarriorPos(skill, cl_action.GetCurVID(skill)))
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SetSkillVarCache(skill, 'victimPos', cl_action.GetEndPositionInCrt(skill, 1))
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 0.5, (0, -3, 0), (0, 0), 500, True, True, 0, innerRadius = 0.01, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, iTriggerBullet = 0, checkWeaknessAngle = 0, checkWeaknessDis = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    for i1 in range(0, (2 if cl_action.CheckHasInscription(skill, 13064) else 0) + cl_action.GetTrajectory(skill), 1):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = i1)
    


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
    m_SID = 9801
    m_Name = '蜥燚（测试）'
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
    m_ForbidRule = 0
    m_CheckForbid = 1001

