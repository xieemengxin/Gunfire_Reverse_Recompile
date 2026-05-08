# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p7153.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p7153.pyc
# Source Generated with Decompyle++
# File: p7153.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateDirectPosCartoon, DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, LEVEL_TYPE_BOSS, OBJ_ALL, OBJ_ENEMY, SKILLCACHE_INT, WARRIOR_BOSS, WARRIOR_ELITE

class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cl_action.SkillHaltTargetPerform(skill, cl_action.GetAttackerOwnerID(skill), 1321)

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
        cl_action.UnlockMonsterAttackerFace(skill)
        cl_action.MonsterResumeAgent(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4 if int(8600 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else int(8600 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(DelegateDirectPosCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        if cl_action.CheckPointSkillIsEnable(skill, 7150):
            cl_action.AttackerAddState(skill, 32816, 0, 0, { })
        cl_action.SendCurCartoonTriggerMsg(skill)
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckVictimType(skill, WARRIOR_BOSS, OBJ_ALL) or cl_action.CheckVictimType(skill, WARRIOR_ELITE, OBJ_ALL):
            cl_action.VictimAddState(skill, 20039, cl_action.GetSkillCustomData(skill, 'AddStateTime', defaultValue = 0), 0, { })
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetAttackerAttr(skill, 'Att') * 1.5 * (cl_action.GetSummonOwnerTalentLevel(skill, 3304) * 1.5 + 1) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), (0, 0, 0), [
                10], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, useclientpos = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        if cl_action.CheckPointSkillIsEnable(skill, 7150):
            cl_action.AttackerAddState(skill, 32816, 0, 0, { })
        cl_action.SendCurCartoonTriggerMsg(skill)
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckVictimType(skill, WARRIOR_BOSS, OBJ_ALL) or cl_action.CheckVictimType(skill, WARRIOR_ELITE, OBJ_ALL):
            cl_action.VictimAddState(skill, 20039, cl_action.GetSkillCustomData(skill, 'AddStateTime', defaultValue = 0), 0, { })
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetAttackerAttr(skill, 'Att') * 1.5 * (cl_action.GetSummonOwnerTalentLevel(skill, 3304) * 1.5 + 1) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), (0, 0, 0), [
                10], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

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
        if cl_action.CheckCurLevelType(skill, LEVEL_TYPE_BOSS):
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4 if int(2000 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else int(2000 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)), 1)

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
        cl_action.TeleportToNearestSpacePosByPos(skill, cl_action.GetSkillCustomData(skill, 'vEnd', defaultValue = (0, 0, 0)))
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4 if int(4000 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else int(4000 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)), 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetAttackerAttr(skill, 'AttSpeed'))
    cl_action.AddSkillCacheData(skill, SKILLCACHE_INT)
    cl_action.MonsterPauseAgent(skill)
    cl_action.MonsterAttackerFacePos(skill, cl_action.GetSkillCustomData(skill, 'vEnd', defaultValue = (0, 0, 0)), 0)
    cl_action.LockMonsterAttackerFace(skill)
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.MonsterResumeAgent(skill)
    cl_action.SkillHaltTargetPerform(skill, cl_action.GetAttackerOwnerID(skill), 1321)


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 7153
    m_Name = '#NT#木机甲人型机能爆发'
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
        'AttDistance': 300,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 80000,
        'CrazyEff': 0,
        'BulletSpeed': 5000,
        'DebuffProb': 1500,
        'ExplodeDelay': 0,
        'Radius': 0,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1038
    m_PassRule = {
        1039: 1 }
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 0

