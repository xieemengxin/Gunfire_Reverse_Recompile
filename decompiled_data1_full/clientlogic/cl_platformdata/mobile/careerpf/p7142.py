# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p7142.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p7142.pyc
# Source Generated with Decompyle++
# File: p7142.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateDirectPosCartoon, MonsterDashCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, OBJ_ALL, OBJ_ENEMY, SKILLCACHE_INT

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
        cl_action.UnlockMonsterAttackerFace(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4 if int(7000 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else int(7000 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(DelegateDirectPosCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cl_action.StartBackSwing(skill, 4 if int(9000 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else int(9000 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)))
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetAttackerAttr(skill, 'Att') * 1.5 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 0.2, -3.5)), cl_action.CrtArgSkillEndPos(skill), [
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, useclientpos = False)

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
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4 if int(3700 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else int(3700 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(MonsterDashCartoon):
    m_SID = 9
    
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'targetpos'), 4 if int(3700 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else int(3700 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)), 4 if int(2500 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else int(2500 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)), cl_action.ToInt(skill, (cl_action.CountDistance(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetSkillVarCache(skill, 'targetpos')) + (-3.5 if cl_action.CountDistance(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), cl_action.CrtArgSkillEndPos(skill)) < 0.5 else 0)) / (0.04 if 37 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) < 0.04 else 37 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))) if cl_action.ToInt(skill, (cl_action.CountDistance(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetSkillVarCache(skill, 'targetpos')) + (-3.5 if cl_action.CountDistance(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), cl_action.CrtArgSkillEndPos(skill)) < 0.5 else 0)) / (0.04 if 37 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) < 0.04 else 37 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))) > 0 else 1, True, False, True, checkDis = 0, start = (0, 0, 0), offSetY = 0, staticbreak = False, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ALL, Collision = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon13(TimerCartoon):
    m_SID = 13
    
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
        if cl_action.CountDistance(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), cl_action.CrtArgSkillEndPos(skill)) < 0.5:
            cl_action.SetSkillVarCache(skill, 'targetpos', cl_action.CrtArgTargetPos(skill, notContainDying = False))
            cl_action.LockMonsterAttackerFace(skill)
            cartoon = { }
            CCartoon9.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.SetSkillVarCache(skill, 'targetpos', cl_action.CrtArgSkillEndPos(skill))
            cl_action.LockMonsterAttackerFace(skill)
            cartoon = { }
            CCartoon9.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4 if int(1300 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else int(1300 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)), 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetAttackerAttr(skill, 'AttSpeed'))
    cl_action.AddSkillCacheData(skill, SKILLCACHE_INT)
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNORETHUMP)
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREKNOCKBACK)
    cartoon = { }
    CCartoon13.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


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
    m_SID = 7142
    m_Name = '#NT#木机甲跳砍'
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
        'ColdTime': 200,
        'AttDistance': 15,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 0,
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
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 300

