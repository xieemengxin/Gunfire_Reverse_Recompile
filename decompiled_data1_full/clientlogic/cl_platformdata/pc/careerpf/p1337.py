# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1337.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1337.pyc
# Source Generated with Decompyle++
# File: p1337.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, LockTargetCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_ATTACKSTATUS, SKILLCACHE_INT, SKILLCACHE_LSTINT, WATER_BUBBLE_DAMAGE

class CCartoon3(LockTargetCartoon):
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSkillVarCache(skill, 'startPos')):
                return None
            cls.EnableShow(skill, cl_action.GetSkillVarCache(skill, 'startPos'), cl_action.GetSkillVarCache(skill, 'startPos'), cl_action.GetSkillVarCache(skill, 'target'), 999, 80, liveTime = 1.5, isLockCenter = False)
        else:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'startPos'), cl_action.GetSkillVarCache(skill, 'startPos'), cl_action.GetSkillVarCache(skill, 'target'), 999, 80, liveTime = 1.5, isLockCenter = False)

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
        for i2 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)), 1):
            cl_action.SetDirectHitInfo(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i2])
            cl_action.SetSkillServerCache(skill, 'ExShowTips', [
                WATER_BUBBLE_DAMAGE][0])
            cl_action.PerformDamage(skill, {
                'Att': skill.m_Cache['Att'] * 10 }, dArgs = { })
            cl_action.SendCurCartoonTriggerMsg(skill)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 20, 1)
        else:
            cls.EnableCtrl(skill, 20, 1)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 40, 1)
        else:
            cls.EnableCtrl(skill, 40, 1)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 52, 1)
        else:
            cls.EnableCtrl(skill, 52, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSkillServerCache(skill, 'ExShowTips', [
            WATER_BUBBLE_DAMAGE][0])
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] * 30 }, dArgs = { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgSelfCenterPos(skill), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 40, 1)
        else:
            cls.EnableCtrl(skill, 40, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ApplyStateTransDamFactor(skill, 33711)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_ATTACKSTATUS, cl_action.GetSkillCustomData(skill, 'Mode', defaultValue = 0))
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_ATTACKSTATUS) == 1:
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillCustomData(skill, 'VIDList'))
        if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) > 0:
            for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)), 1):
                cl_action.SetSkillVarCache(skill, 'random', cl_action.ToInt(skill, cl_action.RandomFloat(0, 5)))
                cl_action.SetSkillVarCache(skill, 'target', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1])
                cl_action.SetSkillVarCache(skill, 'startPos', cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillAID(skill)), cl_math.Vec3Minus(cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillAID(skill)), cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillVarCache(skill, 'target'))), 15, cl_action.ToInt(skill, cl_action.RandomFloat(-30, 30))))
                cl_action.SetSkillVarCache(skill, 'endPos', cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillVarCache(skill, 'target')))
                cartoon = { }
                CCartoon3.Init(skill, cartoon, casting = 1, index = 0)
            
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cl_action.SetSkillVarCache(skill, 'random', cl_action.ToInt(skill, cl_action.RandomFloat(0, 5)))
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
    else:
        cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'Radius', defaultValue = 15))
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_ATTACKSTATUS,
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1337
    m_Name = '迅影式'
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
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 30000,
        'CrazyEff': 0,
        'BulletSpeed': 5000,
        'DebuffProb': 2000,
        'ExplodeDelay': 0,
        'Radius': 15,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_AIPerformDam = 1000

