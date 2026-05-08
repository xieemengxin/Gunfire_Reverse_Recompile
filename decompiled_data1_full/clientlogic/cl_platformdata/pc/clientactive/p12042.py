# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12042.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12042.pyc
# Source Generated with Decompyle++
# File: p12042.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TraceCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, COMMON_SEASON_DAMEAGE, CRT_CHECK_SERVER, NWARRIOR_DROP, OBJ_ENEMY, SKILLCACHE_ATTACKSTATUS, SKILLCACHE_BALLISTICTYPE, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_LSTINTSPECIAL, SKILLCACHE_SIGNSPEED

class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_ATTACKSTATUS) != 0:
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[cl_action.GetCartoonLoopID(skill, 6)] < cl_action.GetSkillCacheData(skill, SKILLCACHE_ATTACKSTATUS):
                pass
            
        
        skill('Att', {
            cl_action.ToInt: skill(cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) * cl_action.GetSpecificPerformArgValue(skill, 2007, 'AttRatio', iDefault = 0) / 10000) }, dArgs = { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCartoonCurPos(skill, 6), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                cl_action.GetSkillCacheData(skill, SKILLCACHE_SIGNSPEED)], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TraceCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        if cl_action.GetAttackerStateCount(skill, 33934) > 0:
            cl_action.AddAttackerStateCount(skill, 33934, -1, iTime = 0, bFromAttack = False, bFromWeapon = False)
            cl_action.UpdateDictSkillCustomData(skill, 'DamFlag', cl_action.GetCartoonLoopID(skill, 6), 1)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetDictValueFromSkillCustomData(skill, 'DamFlag', cl_action.GetCartoonLoopID(skill, 6), iDefault = 0) > 0:
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_ATTACKSTATUS) != 0:
                if cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[cl_action.GetCartoonLoopID(skill, 6)] < cl_action.GetSkillCacheData(skill, SKILLCACHE_ATTACKSTATUS):
                    pass
                
            
            skill('NextAtt', cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_ATTACKSTATUS) != 0:
                if cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[cl_action.GetCartoonLoopID(skill, 6)] < cl_action.GetSkillCacheData(skill, SKILLCACHE_ATTACKSTATUS):
                    pass
                
            
            skill('Att', {
                cl_action.GetSkillCacheData(skill, SKILLCACHE_INT): cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) }, dArgs = { })
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE) == 1:
                cl_action.VictimAddState(skill, 33935, cl_action.GetAttackerCustomData(skill, 'ST33934DeberTime', iDefault = 100), 0, { })
            if not cl_action.GetSpecificPerformArgValue(skill, 2007, 'LaunchDis', iDefault = 0) > 0 and cl_action.CheckTargetAlive(skill, cl_action.GetCurVID(skill)) or 0 == cl_action.GetDictValueFromSkillCustomData(skill, 'LaunchTarget', 0, iDefault = cl_action.GetCurVID(skill)):
                cl_action.SetSkillCustomDataV3List(skill, 'AllTagert', cl_action.GetRangeTargetByPointTarget(skill, cl_action.GetCurVID(skill), cl_action.GetSpecificPerformArgValue(skill, 2007, 'LaunchDis', iDefault = 0), True, 0, bSort = True, bChooseHero = False, bFillinList = False))
                if len(cl_action.GetSkillCustomData(skill, 'AllTagert')) > 0:
                    cl_action.UpdateDictSkillCustomData(skill, 'LaunchTarget', cl_action.GetSkillAID(skill), 1)
                    if not cl_action.GetSkillCustomData(skill, 'AllTagert')[len(cl_action.GetSkillCustomData(skill, 'AllTagert')) - 1] == cl_action.GetCurVID(skill):
                        cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 2007, {
                            'Att': cl_action.GetSkillCustomData(skill, 'NextAtt', defaultValue = 0),
                            'Super': 1 if cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[cl_action.GetCartoonLoopID(skill, 6)] < cl_action.GetSkillCacheData(skill, SKILLCACHE_ATTACKSTATUS) else 0,
                            'StartPos': cl_action.GetTargetCenterPos(skill, cl_action.GetCurVID(skill)) }, False, iTargetVID = cl_action.GetSkillCustomData(skill, 'AllTagert')[len(cl_action.GetSkillCustomData(skill, 'AllTagert')) - 1])
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_SIGNSPEED) > 0:
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetHoverObjPos(skill, cl_action.GetStateIdBySid(skill, cl_action.GetSkillAID(skill), 33934), i1)):
                return None
            cls.EnableShow(skill, 1, 70, 30, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 0.1, angle = 8, lockDis = 0, IgnoreDefalutDis = 100, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = False, searchByDistance = False, canLockMoreTimes = False, scale = 2 if cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[cl_action.GetCartoonLoopID(skill, 6)] < cl_action.GetSkillCacheData(skill, SKILLCACHE_ATTACKSTATUS) else 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        COMMON_SEASON_DAMEAGE][0])
    if cl_action.IsHeroCtrl(skill) or len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) > 0:
        for i1 in range(0, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY), 1):
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 1, index = i1)
        
    elif len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) > 0:
        for i2 in range(0, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY), 1):
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 1, index = i2)
        


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_ATTACKSTATUS,
        SKILLCACHE_BALLISTICTYPE,
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTINTSPECIAL,
        SKILLCACHE_SIGNSPEED]


def GetOtherMonster():
    return []

from cl_perform.clientactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_THUNDER

class CPerform(CCustomPerform):
    m_SID = 12042
    m_Name = 'S7雷刃发射'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_THUNDER
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 3000 }

