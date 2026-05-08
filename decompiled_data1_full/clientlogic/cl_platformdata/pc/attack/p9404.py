# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9404.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9404.pyc
# Source Generated with Decompyle++
# File: p9404.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, ThrowByPowerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, HIT_OVER_NORMAL, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY, WARRIOR_OBSTACLE_NORMAL

class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSkillVarCache(skill, 'HitNum', cl_action.GetSkillVarCache(skill, 'HitNum') + 1)
        cl_action.SetSkillVarCache(skill, 'JumpNum', cl_action.GetSkillVarCache(skill, 'JumpNum') + 2)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PushVictim(skill, cl_action.GetEndPositionInCrt(skill, 3), 20, 3, 10000, angle = 0, iCartoonSID = -1, iIgnoreStruckCD = 0, iClient = 0)
        cl_action.WeaponDamage(skill, {
            'Att': 100 - cl_action.GetSkillVarCache(skill, 'HitNum') * 25 if cl_action.GetPerformArgValue(skill, 'AttrIncrease', iDefault = 0) == 0 else 100 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 1), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                cl_action.GetSkillVarCache(skill, 'Rad')], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = True, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSkillVarCache(skill, 'Rad', cl_action.GetSkillVarCache(skill, 'Rad') + 0)
        if cl_action.GetCartoonHitTargetCount(skill, 2) > 0:
            cl_action.SetSkillVarCache(skill, 'HitNum', cl_action.GetSkillVarCache(skill, 'HitNum') + 1)
            cl_action.SetSkillVarCache(skill, 'JumpNum', cl_action.GetSkillVarCache(skill, 'JumpNum') + (2 if cl_action.GetCartoonHitTargetCount(skill, 2) > 0 else 1))
        elif cl_action.GetCartoonHitTargetCount(skill, 2) > 0:
            pass
        
        skill('JumpNum', cl_action.GetSkillVarCache(skill, 'JumpNum'), 2 + 1)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PushVictim(skill, cl_action.GetEndPositionInCrt(skill, 2), 20, 3, 10000, angle = 0, iCartoonSID = -1, iIgnoreStruckCD = 0, iClient = 0)
        cl_action.WeaponDamage(skill, {
            'Att': 100 - cl_action.GetSkillVarCache(skill, 'HitNum') * 25 if cl_action.GetPerformArgValue(skill, 'AttrIncrease', iDefault = 0) == 0 else 100 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 1), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                cl_action.GetSkillVarCache(skill, 'Rad')], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = True, multipleExplode = True, explosionDelay = 10)

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
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Radius'] if cl_action.CheckHasInscription(skill, 13025) else 0.4, (0, 0, 0), (0.6, 0.75), 6000 if cl_action.CheckHasInscription(skill, 13025) else 300, False, False, 0, innerRadius = 0.1, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0.1, 0.1), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0.7, maxRadius = 3, iTriggerBullet = 0, checkWeaknessAngle = 0, checkWeaknessDis = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'Rad', skill.m_Cache['Radius'])
    cl_action.SetSkillVarCache(skill, 'JumpNum', 0)
    cl_action.SetSkillVarCache(skill, 'HitNum', 0)
    for i1 in range(0, cl_action.GetTrajectory(skill), 1):
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
    m_SID = 9404
    m_Name = '狂鲨'
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

