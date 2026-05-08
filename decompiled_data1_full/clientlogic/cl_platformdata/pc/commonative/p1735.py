# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1735.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1735.pyc
# Source Generated with Decompyle++
# File: p1735.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, ThrowByPowerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, HIT_OVER_NORMAL, OBJ_ALL, OBJ_ENEMY, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_HERO, WARRIOR_NORMAL

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SendInteraceHitTargetMsg(skill, cl_action.GetSkillCustomData(skill, 'TriggerID', defaultValue = 0), dInfo = {
            'OriginID': cl_action.GetSkillCustomData(skill, 'OriginID', defaultValue = 0),
            'TriggerFrame': cl_action.GetSkillCustomData(skill, 'TriggerFrame', defaultValue = 0) })
        if cl_action.CheckMonsterType(skill, WARRIOR_NORMAL, cl_action.GetCurVID(skill)):
            cl_action.AssignWarriorDie(skill, cl_action.GetCurVID(skill))
        if cl_action.CheckMonsterType(skill, WARRIOR_HERO, cl_action.GetCurVID(skill)):
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0) }, dArgs = { })
        if cl_action.CheckMonsterType(skill, WARRIOR_ELITE, cl_action.GetCurVID(skill)):
            cl_action.VictimAddState(skill, 33545, cl_action.GetSpecificPerformArgValue(skill, 44002, 'EliteWeakTime', iDefault = 0), 0, {
                'DamAdd': cl_action.GetSpecificPerformArgValue(skill, 44002, 'DamAdd', iDefault = 0) })
            cl_action.TrapThumpVictim(skill, cl_action.GetCurVID(skill))
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 1000) }, dArgs = { })
        if cl_action.CheckMonsterType(skill, WARRIOR_BOSS, cl_action.GetCurVID(skill)):
            cl_action.VictimAddState(skill, 33545, cl_action.GetSpecificPerformArgValue(skill, 44002, 'BossWeakTime', iDefault = 0), 0, {
                'DamAdd': cl_action.GetSpecificPerformArgValue(skill, 44002, 'DamAdd', iDefault = 0) })
            cl_action.TrapThumpVictim(skill, cl_action.GetCurVID(skill))
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 1000) }, dArgs = { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetGroundPos(skill, cl_action.CrtArgHitPos(skill)), (0, 0, 0), [
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SendInteraceHitTargetMsg(skill, cl_action.GetSkillCustomData(skill, 'TriggerID', defaultValue = 0), dInfo = {
            'OriginID': cl_action.GetSkillCustomData(skill, 'OriginID', defaultValue = 0),
            'TriggerFrame': cl_action.GetSkillCustomData(skill, 'TriggerFrame', defaultValue = 0) })
        if cl_action.CheckMonsterType(skill, WARRIOR_NORMAL, cl_action.GetCurVID(skill)):
            cl_action.AssignWarriorDie(skill, cl_action.GetCurVID(skill))
        if cl_action.CheckMonsterType(skill, WARRIOR_HERO, cl_action.GetCurVID(skill)):
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0) }, dArgs = { })
        if cl_action.CheckMonsterType(skill, WARRIOR_ELITE, cl_action.GetCurVID(skill)):
            cl_action.VictimAddState(skill, 33545, cl_action.GetSpecificPerformArgValue(skill, 44002, 'EliteWeakTime', iDefault = 0), 0, {
                'DamAdd': cl_action.GetSpecificPerformArgValue(skill, 44002, 'DamAdd', iDefault = 0) })
            cl_action.TrapThumpVictim(skill, cl_action.GetCurVID(skill))
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 1000) }, dArgs = { })
        if cl_action.CheckMonsterType(skill, WARRIOR_BOSS, cl_action.GetCurVID(skill)):
            cl_action.VictimAddState(skill, 33545, cl_action.GetSpecificPerformArgValue(skill, 44002, 'BossWeakTime', iDefault = 0), 0, {
                'DamAdd': cl_action.GetSpecificPerformArgValue(skill, 44002, 'DamAdd', iDefault = 0) })
            cl_action.TrapThumpVictim(skill, cl_action.GetCurVID(skill))
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 1000) }, dArgs = { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 0), (0, 0, 0), [
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

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
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), (0, -1, 0), 10, 0.25, (0, 12, 0), (0, 0), 0, True, True, 0, innerRadius = 0.05, pierce = 1, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, ignorePetrochemical = False, iTriggerBullet = 0, ignoreShield = False, checkWeaknessAngle = 0, checkWeaknessDis = 0, canPierceWeakness = False)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1735
    m_Name = '吊灯陷阱主动技能'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_NORMAL
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0,
        'Radius': 10 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

