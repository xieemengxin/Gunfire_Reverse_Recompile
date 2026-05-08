# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p2007.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p2007.pyc
# Source Generated with Decompyle++
# File: p2007.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TraceCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, COMMON_SEASON_DAMEAGE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, NWARRIOR_DROP, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_POS, SKILLCACHE_SIGNSPEED

class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, cl_action.ToInt(skill, cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0) * cl_action.GetPerformArgValue(skill, 'LaunchAtt', iDefault = 0) / 10000) * cl_action.GetPerformArgValue(skill, 'LaunchAoeAtt', iDefault = 0) / 10000) }, dArgs = { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetCartoonCurPos(skill, 6), (0, 0, 0), [
                cl_action.GetSkillCacheData(skill, SKILLCACHE_SIGNSPEED)], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TraceCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0) * cl_action.GetPerformArgValue(skill, 'LaunchAtt', iDefault = 0) / 10000) }, dArgs = { })
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVID(skill)), 1, 70, 30, showstart = (0, 0, 0), targettype = OBJ_ENEMY, targetID = cl_action.GetSkillVID(skill), liveTime = 0, lineDistance = 0.1, angle = 8, lockWeakness = False, lockAngle = 0, canDesAngle = 0, lockDis = 0, IgnoreDefalutDis = 100, IgnoreSummon = False, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0, lockSumm = False, lockCanDestroy = False, lockHideDoor = False, isBlocked = False, isMonsterFirst = False, lockExplode = False, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = False, searchByDistance = False, canLockMoreTimes = False, scale = 2 if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1 else 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        COMMON_SEASON_DAMEAGE][0])
    cl_action.SetSkillCacheData(skill, SKILLCACHE_SIGNSPEED, cl_action.GetPerformArgValue(skill, 'LaunchAoeRange', iDefault = 0) / 10)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'Super', defaultValue = 0))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSkillCustomData(skill, 'StartPos', defaultValue = (0, 0, 0)))
    cartoon = { }
    CCartoon6.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_POS,
        SKILLCACHE_SIGNSPEED]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 2007
    m_Name = '弹射雷刃'
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
        'AttDistance': 10,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

