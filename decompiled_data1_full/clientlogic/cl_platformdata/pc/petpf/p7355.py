# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petpf/p7355.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petpf/p7355.pyc
# Source Generated with Decompyle++
# File: p7355.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, HIT_OVER_NORMAL, OBJ_ENEMY, S6_DICE_DAMAGE, SKILLCACHE_LSTINT

class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetAttackerAttr(skill, 'HPMax') * (((cl_action.GetSkillCustomData(skill, 'DiceLevel', defaultValue = 1) if cl_action.GetSkillCustomData(skill, 'DiceLevel', defaultValue = 1) < 5 else 7) * 50 + 50) / 100) }, dArgs = { })
        if not cl_action.GetSkillCustomData(skill, 'DiceLevel', defaultValue = 1) < 3:
            cl_action.VictimAddState(skill, 33909, 500, 0, {
                'DiceLevel': cl_action.GetSkillCustomData(skill, 'DiceLevel', defaultValue = 1) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.SkillStartPos(skill), (0, 0.1, 0)), (0, 0, 0), [
                8], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

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
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetAttackerAttr(skill, 'HPMax') * (((cl_action.GetSkillCustomData(skill, 'DiceLevel', defaultValue = 1) if cl_action.GetSkillCustomData(skill, 'DiceLevel', defaultValue = 1) < 5 else 7) * 50 + 50) / 100) }, dArgs = { })
        if not cl_action.GetSkillCustomData(skill, 'DiceLevel', defaultValue = 1) < 3:
            cl_action.VictimAddState(skill, 33909, 500, 0, {
                'DiceLevel': cl_action.GetSkillCustomData(skill, 'DiceLevel', defaultValue = 1) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill) if cl_action.GetSkillVarCache(skill, 'SelfBoom') == 1 else cl_action.GetEndPositionInCrt(skill, 0), (0, 0, 0), [
                5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
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
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 5)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
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
        cl_action.AttackerRemoveState(skill, 33908, bSameItem = False)
        cl_action.AssignWarriorDie(skill, cl_action.GetSkillAID(skill))
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        if cl_action.GetSkillVarCache(skill, 'FireRing') == 1:
            cartoon = { }
            CCartoon7.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 10 / cl_action.GetSkillVarCache(skill, 'AttackSpeed')), 0)

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
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 60 / cl_action.GetSkillVarCache(skill, 'AttackSpeed')), 0)

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
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetAttackerAttr(skill, 'HPMax') * (((cl_action.GetSkillCustomData(skill, 'DiceLevel', defaultValue = 1) if cl_action.GetSkillCustomData(skill, 'DiceLevel', defaultValue = 1) < 5 else 7) * 50 + 50) / 100) }, dArgs = { })
        if not cl_action.GetSkillCustomData(skill, 'DiceLevel', defaultValue = 1) < 3:
            cl_action.VictimAddState(skill, 33909, 500, 0, {
                'DiceLevel': cl_action.GetSkillCustomData(skill, 'DiceLevel', defaultValue = 1) })

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
                8], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

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
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)
        if cl_action.GetSkillVarCache(skill, 'FireRing') == 1:
            cartoon = { }
            CCartoon7.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetMuzzlePosition(skill, cartoon), cl_math.Vec3MulV(cl_action.CrtArgGetCustomDir(skill, cl_action.CrtArgCustomPos(skill, cartoon), cl_action.CrtArgCustomStartPos(skill, cartoon), (0, 0, 0), baseHorizontal = False), (1, 0, 1)), 10, 0.33, (0, 0, 0), (0.4, 0.4), 100, False, False, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, ignorePetrochemical = False, iTriggerBullet = 0, ignoreShield = False, checkWeaknessAngle = 0, checkWeaknessDis = 0, canPierceWeakness = False, hitFallAcc = 0, verticalThreshold = 0.7)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'S6DiceSkill', 1)
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        S6_DICE_DAMAGE][0])
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, [
        cl_action.GetSkillCustomData(skill, 'SelfBoom', defaultValue = 1),
        cl_action.GetSkillCustomData(skill, 'FireRing', defaultValue = 0)])
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_LSTINT])
    cl_action.SetSkillVarCache(skill, 'SelfBoom', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0])
    cl_action.SetSkillVarCache(skill, 'FireRing', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[1])
    cl_action.SetSkillVarCache(skill, 'AttackSpeed', cl_action.Clamp(skill, 70 / (skill.m_Cache['AttSpeed'] if skill.m_Cache['AttSpeed'] > 0 else 70), 1, 2.5))
    if cl_action.GetSkillVarCache(skill, 'SelfBoom') == 1:
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)
    else:
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.petactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE, PETPF_ACTIVE_ATTACK

class CPerform(CCustomPerform):
    m_SID = 7355
    m_Name = '第六赛季硝石勇士自爆'
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
        'ColdTime': 300,
        'AttDistance': 4.5,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1,
        'Radius': 0 }
    m_ElementType = DAM_TYPE_FIRE
    m_ClientNeed = 0
    m_PFSubType = PETPF_ACTIVE_ATTACK
    m_SpellPower = 0
    m_NeedTarget = 0
    m_ForbidRule = 1021

