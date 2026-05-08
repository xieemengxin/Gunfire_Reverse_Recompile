# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1994.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1994.pyc
# Source Generated with Decompyle++
# File: p1994.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, MONSTER_PART_UNTAGGED, NWARRIOR_DROP, OBJ_ALL, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_LSTINTSPECIAL

class CCartoon0(TraceCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
        cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1]))
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) != 0:
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[i1] < cl_action.GetSkillCacheData(skill, SKILLCACHE_INT):
                pass
            
        
        skill('Att', {
            cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0): cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0) }, dArgs = { })
        if cl_action.GetSkillCustomData(skill, 'IsDebar', defaultValue = 0) == 1:
            cl_action.VictimAddState(skill, 33935, cl_action.GetSkillCustomData(skill, 'DeberTime', defaultValue = 100), 0, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetHoverObjPos(skill, cl_action.GetStateIdBySid(skill, cl_action.GetSkillAID(skill), 33934)), (0, 0, 0), 0, 100, 80, showstart = (0, 0, 0), targettype = OBJ_ALL, targetID = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1], liveTime = 300, lineDistance = 0, angle = 180, lockWeakness = False, lockAngle = 180, canDesAngle = 0, lockDis = 200, IgnoreDefalutDis = 0, IgnoreSummon = False, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = True, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0, lockSumm = False, lockCanDestroy = False, lockHideDoor = False, isBlocked = False, isMonsterFirst = False, lockExplode = False, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = False, searchByDistance = False, canLockMoreTimes = False)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetAttackerCustomData(skill, 'S7LeiRenSuperRatio', iDefault = 0))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillCustomData(skill, 'TargetList'))
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) != 0:
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL, cl_action.CrtArgRandomIntList(skill, 0, 100, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT))))
        for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)), 1):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
        
    else:
        for i2 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)), 1):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i2)
        


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTINTSPECIAL]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_THUNDER

class CPerform(CCustomPerform):
    m_SID = 1994
    m_Name = '#NT#第七赛季雷刃'
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
        'ChargeTime': 0,
        'DebuffProb': 3000 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 3000 }

