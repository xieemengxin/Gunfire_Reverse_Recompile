# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1998.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1998.pyc
# Source Generated with Decompyle++
# File: p1998.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, COMMON_SEASON_DAMEAGE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_RANDOM, WARRIOR_MONSTER

class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SetSkillCustomDataInt(skill, 'HasHit', 0)
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0] >= 1:
            cl_action.AddSceneEventForState(skill, cl_action.GetStartPositionInCrt(skill, 0), 192, 1, {
                'Radius': 4 }, 39676, 192, 1, iFightType = WARRIOR_MONSTER, iLeaveSetTime = -1)

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetSkillCustomData(skill, 'HasHit', defaultValue = 0) == 0:
            cl_action.SetSkillCustomDataInt(skill, 'SkillHalt', 1)
            if not cl_action.GetAttackerCustomValue(skill, 'SpreadRadius', iDefault = 0) == 0:
                cl_action.SetSkillCustomDataInt(skill, 'RemainTriggerTime', cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) - cl_action.GetTimerCartoonCurTimes(skill, 1))
                if cl_action.GetSkillCustomData(skill, 'RemainTriggerTime', defaultValue = 0) > 0:
                    cl_action.SetSkillCustomDataInt(skill, 'SpreadVictim', cl_action.GetNearestMonsterInRange(skill, cl_action.GetAttackerCustomValue(skill, 'SpreadRadius', iDefault = 0) / 100, 0, 0, 0, 0, 0, iUseVictim = 1, iExcludeState = 0, iExcludeStateCountMin = 0, iExcludeStateFromAttack = 0))
                    if not cl_action.GetSkillCustomData(skill, 'SpreadVictim', defaultValue = 0) == 0:
                        cl_action.AttackerUsePerform(skill, 1998, {
                            'Att': cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0),
                            'ExtraRadius': cl_action.GetSkillCustomData(skill, 'ExtraRadius', defaultValue = 0),
                            'ExtraDamRatio': cl_action.GetSkillCustomData(skill, 'ExtraDamRatio', defaultValue = 0),
                            'MaxCount': cl_action.GetSkillCustomData(skill, 'MaxCount', defaultValue = 8),
                            'TriggerFinalDam': cl_action.GetSkillCustomData(skill, 'TriggerFinalDam', defaultValue = 0),
                            'RemainTriggerTime': cl_action.GetSkillCustomData(skill, 'RemainTriggerTime', defaultValue = 0) - 1,
                            'vStart': cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillCustomData(skill, 'SpreadVictim', defaultValue = 0)) }, 0, cl_action.GetSkillCustomData(skill, 'SpreadVictim', defaultValue = 0))

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSkillCustomDataInt(skill, 'HasHit', 1)
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0) * (cl_action.GetAttackerCustomValue(skill, 'DamRatio', iDefault = 0) + 100 + cl_action.GetSkillCustomData(skill, 'ExtraDamRatio', defaultValue = 0) * min(cl_action.GetTimerCartoonCurTimes(skill, 1), cl_action.GetSkillCustomData(skill, 'MaxCount', defaultValue = 8)))) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCustomData(skill, 'vStart', defaultValue = cl_action.SkillStartPos(skill)), (0, 0, 0), [
                (cl_action.GetAttackerCustomValue(skill, 'BaseRadius', iDefault = 100) + cl_action.GetSkillCustomData(skill, 'ExtraRadius', defaultValue = 0) * min(cl_action.GetTimerCartoonCurTimes(skill, 1), cl_action.GetSkillCustomData(skill, 'MaxCount', defaultValue = 0))) / 100], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        if cl_action.GetSkillCustomData(skill, 'SkillHalt', defaultValue = 0) == 0:
            cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')
            cl_action.SetSkillCustomDataInt(skill, 'CurRadius', cl_action.GetAttackerCustomValue(skill, 'BaseRadius', iDefault = 100) + cl_action.GetSkillCustomData(skill, 'ExtraRadius', defaultValue = 0) * min(cl_action.GetTimerCartoonCurTimes(skill, 1), cl_action.GetSkillCustomData(skill, 'MaxCount', defaultValue = 0)))
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
        if cl_action.GetSkillCustomData(skill, 'SkillHalt', defaultValue = 0) == 0:
            cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')
            cl_action.SetSkillCustomDataInt(skill, 'CurRadius', cl_action.GetAttackerCustomValue(skill, 'BaseRadius', iDefault = 100) + cl_action.GetSkillCustomData(skill, 'ExtraRadius', defaultValue = 0) * min(cl_action.GetTimerCartoonCurTimes(skill, 1), cl_action.GetSkillCustomData(skill, 'MaxCount', defaultValue = 0)))
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetAttackerCustomValue(skill, 'IntervalTime', iDefault = 60), cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        COMMON_SEASON_DAMEAGE][0])
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'RemainTriggerTime', defaultValue = cl_action.GetAttackerCustomValue(skill, 'ExtraTriggerTime', iDefault = 1)))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_RANDOM, cl_action.GetSkillCustomData(skill, 'ExtraRadius', defaultValue = 0))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY, cl_action.GetAttackerCustomValue(skill, 'BaseRadius', iDefault = 100))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, [
        cl_action.GetPerformArgValue(skill, 'EnableAbsorb', iDefault = 0)])
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_INT,
        SKILLCACHE_RANDOM,
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_LSTINT])
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_RANDOM]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1998
    m_Name = '#NT#S7组件莲花绽放'
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
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'AIPerformDam': 200 }

