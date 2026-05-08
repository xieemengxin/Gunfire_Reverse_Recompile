# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p20431.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p20431.pyc
# Source Generated with Decompyle++
# File: p20431.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateCurveCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_BALLISTICTYPE, SKILLCACHE_INT, SKILLCACHE_LSTINT

class CCartoon1(DelegateCurveCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 2, -0.5)), cl_action.CrtArgRandomAngle(skill, cartoon, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 2, -0.5)), cl_action.CrtArgTargetBodyShiftPos(skill, 1, 0, 5, 15, 0, 2, 0, 2), 0, 0, 0, 0, False), 1, 105, 35, 0, 0.4, targettype = OBJ_ENEMY, liveTime = 0, defLockPos = (0, 0, 0), weakdis = 0, weakangle = 0, resetTargetPos = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(DelegateCurveCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 2, -0.5)), cl_action.CrtArgRandomAngle(skill, cartoon, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 2, -0.5)), cl_action.CrtArgTargetBodyShiftPos(skill, 1, 0, 5, 15, 0, 2, 0, 2), 0, 0, 0, 0, False), 1, 105, 35, 0, 0.4, targettype = OBJ_ENEMY, liveTime = 0, defLockPos = (0, 0, 0), weakdis = 0, weakangle = 0, resetTargetPos = False)

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
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            cl_action.SetSkillVictim(skill, cl_action.GetSkillVarCache(skill, 'MainTarget'))
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
            if cl_action.GetTimerCartoonCurTimes(skill, 3) % 3 == 0:
                cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetHeroInSightArgs(skill, 60, 45, True, cl_action.GetSkillVarCache(skill, 'MainTarget'), (0, 0, 0)))
                cl_action.ServerSendSkillCache(skill, [
                    SKILLCACHE_LSTINT])
                for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)), 1):
                    cl_action.SetSkillVarCache(skill, 'MinorTarget', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1])
                    cl_action.SetSkillVictim(skill, cl_action.GetSkillVarCache(skill, 'MinorTarget'))
                    cartoon = { }
                    CCartoon6.Init(skill, cartoon, casting = 0, index = 0)
                
            else:
                cl_action.SetSkillVictim(skill, cl_action.GetSkillVarCache(skill, 'MainTarget'))
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.StartBackSwing(skill, 30)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetAttackerAttr(skill, 'AttSpeed'), cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE))

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
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
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetPerformArgValue(skill, 'ExtraTarget', iDefault = 0))
    cl_action.SetSkillVarCache(skill, 'MainTarget', cl_action.GetSkillVID(skill))
    cartoon = { }
    CCartoon4.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_BALLISTICTYPE,
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 20431
    m_Name = '飞行基础炮台怪-连射'
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
        'ColdTime': 200,
        'AttDistance': 45,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_ForbidRule = 0
    m_Resend = 1
    m_CacheAttr = [
        'DebuffProb']

