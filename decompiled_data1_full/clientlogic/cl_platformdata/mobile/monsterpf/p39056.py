# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39056.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39056.pyc
# Source Generated with Decompyle++
# File: p39056.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, RayCastCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_RANDOM

class CCartoon5(TimerCartoon):
    m_SID = 5
    
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
        cl_action.AddClientEffect(skill, 1009, cl_math.Vec3Add(cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'EndPos'), (0, 2, 0)), cl_math.Vec3MulV(cl_action.GetSkillVarCache(skill, 'Dir'), (cl_action.GetTimerCartoonCurTimes(skill, 5) * 5, cl_action.GetTimerCartoonCurTimes(skill, 5) * 5, cl_action.GetTimerCartoonCurTimes(skill, 5) * 5))), time = cl_action.ToInt(skill, 180 - cl_action.GetPlayRound(skill) * 20))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 10, 11)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 60 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetCartoonEnd(skill, 0), (0, 0, 0), [
                5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(RayCastCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'EndPos'), cl_math.Vec3MulV(cl_action.GetSkillVarCache(skill, 'Dir'), (cl_action.GetTimerCartoonCurTimes(skill, 2) * 5, cl_action.GetTimerCartoonCurTimes(skill, 2) * 5, cl_action.GetTimerCartoonCurTimes(skill, 2) * 5))), (0, 80, 0)), cl_math.Vec3Add(cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'EndPos'), cl_math.Vec3MulV(cl_action.GetSkillVarCache(skill, 'Dir'), (cl_action.GetTimerCartoonCurTimes(skill, 2) * 5, cl_action.GetTimerCartoonCurTimes(skill, 2) * 5, cl_action.GetTimerCartoonCurTimes(skill, 2) * 5))), (0, 80, 0)), cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'EndPos'), cl_math.Vec3MulV(cl_action.GetSkillVarCache(skill, 'Dir'), (cl_action.GetTimerCartoonCurTimes(skill, 2) * 5, cl_action.GetTimerCartoonCurTimes(skill, 2) * 5, cl_action.GetTimerCartoonCurTimes(skill, 2) * 5))), 1, 200, 80, targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = None, effectLiveTime = 0, radius = 0, flyoverdis = 0)

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
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 10, 11)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
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
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 80 - cl_action.GetPlayRound(skill) * 20), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
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
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 15, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableCtrl(skill, 8, cl_action.ToInt(skill, 6 - cl_action.GetPlayRound(skill)))

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableCtrl(skill, 8, 5)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'EndPos', cl_math.Vec3Add(cl_math.Vec3MulV(cl_action.CrtArgTargetPos(skill, notContainDying = False), (0, 0, 1)), cl_math.Vec3Add(cl_math.Vec3MulV((32.5, 2, 22.41), (1, 1, 0)), (30 * (1 if cl_action.CheckSkillRandomInRange(skill, 0, 50) else -1) * -1, 0, 0))))
    cl_action.SetSkillVarCache(skill, 'Dir', (1 if cl_action.CheckSkillRandomInRange(skill, 0, 50) else -1, 0, 0))
    if cl_action.CheckSkillRandomInRange(skill, 0, 50):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)
    else:
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_RANDOM]

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import CLOSE_DISTANCE, DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 39056
    m_Name = '海船-直线轰炸'
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
        'ColdTime': 500,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = CLOSE_DISTANCE
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

