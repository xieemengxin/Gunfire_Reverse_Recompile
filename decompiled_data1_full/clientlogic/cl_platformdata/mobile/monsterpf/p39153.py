# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39153.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39153.pyc
# Source Generated with Decompyle++
# File: p39153.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, OBJ_ALL, OBJ_ALLNOSELF, OBJ_ENEMY, WARRIOR_PHYSXENTITYEFFECT, WARRIOR_SUMMON

class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_PHYSXENTITYEFFECT, OBJ_ALL):
            cl_action.WeaponDamage(skill, {
                'Att': 99999 }, { }, sendPFMsg = False)
            cl_action.AttackerAddState(skill, 7961, 0, 1, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False), [
                9], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALLNOSELF, pierceStatic = False, explosion = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckWarriorHasState(skill, cl_action.GetSkillVID(skill), 7963):
            cl_action.WeaponDamage(skill, {
                'Att': 20 }, { }, sendPFMsg = False)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 50 }, { }, sendPFMsg = False)
            cl_action.PushHeroVictim(skill, cl_action.CrtArgSelfPos(skill), 25, cl_action.GetPlayRound(skill) + 5, 10000, downSpeed = 0, fGravaty = 9.8, angle = 0)
            cl_action.VictimAddState(skill, 7963, 250, 0, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False), [
                7], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 30)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cl_action.ClearSkillSummonCreateCollect(skill)
        cl_action.SetSkillServerCache(skill, 'lsthero', cl_action.GetNavMeshHero(skill, (135, 1.5, 135), True))
        cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.GetPosByRelativePosition(skill, [
            (6, 0, 3),
            (6, 0, -3),
            (4, 0, 6),
            (4, 0, -6)], len(cl_action.GetSkillServerCache(skill, 'lsthero')) - 1), WARRIOR_SUMMON, {
            1029: 10 }, {
            'Capsule': 0 })
        for i1 in range(0, len(cl_action.GetSkillSummonCreate(skill)), 1):
            cl_action.SetSummonLifeTime(skill, cl_action.GetSkillSummonCreate(skill)[i1], cl_action.GetPlayRound(skill) * 500 + 2000)
            cl_action.RandomTraceUnLockHero(skill, cl_action.GetSkillSummonCreate(skill)[i1], cl_action.GetSkillServerCache(skill, 'lsthero'), True)
        

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
        cl_action.AttackerAddState(skill, 7961, 0, 1, { })
        cl_action.AttackerAddState(skill, 7091, 0, 1, { })
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

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
        cl_action.ClearSkillSummonCreateCollect(skill)
        cl_action.SetSkillServerCache(skill, 'lsthero', cl_action.GetNavMeshHero(skill, (135, 1.5, 135), True))
        cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.GetPosByRelativePosition(skill, [
            (6, 0, 3),
            (6, 0, -3),
            (4, 0, 6),
            (4, 0, -6)], len(cl_action.GetSkillServerCache(skill, 'lsthero')) - 1), WARRIOR_SUMMON, {
            1029: 10 }, {
            'Capsule': 0 })
        for i2 in range(0, len(cl_action.GetSkillSummonCreate(skill)), 1):
            cl_action.SetSummonLifeTime(skill, cl_action.GetSkillSummonCreate(skill)[i2], cl_action.GetPlayRound(skill) * 500 + 2000)
            cl_action.RandomTraceUnLockHero(skill, cl_action.GetSkillSummonCreate(skill)[i2], cl_action.GetSkillServerCache(skill, 'lsthero'), True)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 740, 2)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
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
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, 1)

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
        cl_action.AssignSummonDie(skill, cl_action.GetSummonByDistance(skill, 21 - cl_action.GetPlayRound(skill) * 2, 1028), 0)
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 130, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import CLOSE_DISTANCE, DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 39153
    m_Name = '风神-旋转移动'
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
        'ColdTime': 4500,
        'AttDistance': 30,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = CLOSE_DISTANCE
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

