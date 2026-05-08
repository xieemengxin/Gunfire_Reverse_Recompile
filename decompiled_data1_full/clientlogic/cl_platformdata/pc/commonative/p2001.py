# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p2001.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p2001.pyc
# Source Generated with Decompyle++
# File: p2001.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, SendDataCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTPOS

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'ComAtt': 100 })
        cl_action.VictimAddState(skill, 8168, 60, 0, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[cl_action.GetCartoonLoopID(skill, 3) - 1], (0, 0, 0), [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckWarriorHasState(skill, cl_action.GetCurVID(skill), 8168):
            cl_action.PerformDamage(skill, {
                'ComAtt': 100 })
            cl_action.VictimAddState(skill, 8168, 60, 0, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[cl_action.GetCartoonLoopID(skill, 3) - 1], (0, 0, 0), [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'PerformLastPos', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[cl_action.GetCartoonLoopID(skill, 3) - 1])
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 5)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(SendDataCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = cl_action.GetTimerCartoonCurTimes(skill, 1))

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
            cls.EnableCtrl(skill)

    InitSuccess = classmethod(InitSuccess)


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
        cl_action.SetSkillServerCache(skill, 'PerformNextPos', cl_action.RefreshStepPerformNextPos(skill, cl_action.GetGroundPos(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillAID(skill))), cl_action.GetSkillVarCache(skill, 'PerformLastPos'), cl_action.GetSkillCustomData(skill, 'LimitDis', defaultValue = 400) / 100, cl_action.GetSkillCustomData(skill, 'Disoffset', defaultValue = 40) / 100, cl_action.GetSkillCustomData(skill, 'PosLiveTime', defaultValue = 300) / 100))
        cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS).append(cl_action.GetSkillServerCache(skill, 'PerformNextPos'))
        if cl_action.GetAttackerCustomData(skill, 'IsDashing', iDefault = 0) == 1:
            if cl_action.CheckVectorIsZero(skill, cl_action.GetSkillServerCache(skill, 'PerformNextPos')):
                pass
            
        
        skill(SKILLCACHE_INT, 1, 0)
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_LSTPOS,
            SKILLCACHE_INT])
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 8, 50)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'PerformLastPos', cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillAID(skill)))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, [])
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 2001
    m_Name = '#NT#通用移动路径留下岩浆'
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

