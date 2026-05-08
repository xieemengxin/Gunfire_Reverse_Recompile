# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39094.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39094.pyc
# Source Generated with Decompyle++
# File: p39094.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, MODEL_TYPE_CAPSULE, OBJ_ENEMY, WARRIOR_HERO

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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(DirectPosCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 80 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'PosList')[cl_action.GetCartoonLoopID(skill, 3)], (0, 0, 0), [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False)

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
        cl_action.CreateStonePillar(skill, 1134, 101, cl_action.GetSkillVarCache(skill, 'PosList')[cl_action.GetCartoonLoopID(skill, 3)], MODEL_TYPE_CAPSULE, [
            8,
            2,
            0], 45, 359)
        cl_action.AddClientEffect(skill, 1014, cl_action.GetSkillVarCache(skill, 'PosList')[cl_action.GetCartoonLoopID(skill, 3)], time = 100)
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 60, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'PosList', cl_action.CreateRectanglePosList(skill, (-7, 0, -6), (50, 0, 42), (10 if cl_action.GetAllHeroCnt(skill, False) >= 3 else 9 if cl_action.GetAllHeroCnt(skill, False) >= 2 else 8) + (12 if cl_action.GetPlayRound(skill) >= 3 else 11 if cl_action.GetPlayRound(skill) >= 2 else 10), (30 if cl_action.GetPlayRound(skill) >= 3 else 35 if cl_action.GetPlayRound(skill) >= 2 else 40) / 10, 2))
    for i1 in range(0, len(cl_action.GetSkillVarCache(skill, 'PosList')), 1):
        cl_action.AddClientEffect(skill, 1013, cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'PosList')[i1], (0, 2, 0)), time = 75)
        cl_action.AddSceneEventForState(skill, cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'PosList')[i1], (0, 2, 0)), 75, 1, {
            'Radius': 3 }, 32248, 75, 1, iFightType = WARRIOR_HERO, iLeaveSetTime = -1)
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = i1)
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39094
    m_Name = '石巨人-召唤石柱'
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
        'ColdTime': 1,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

