# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9492.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9492.pyc
# Source Generated with Decompyle++
# File: p9492.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import CastingTraceRayCartoon, TimerCartoon, TraceIntensifyLineCartoon
from cl_commondefines import CRT_CHECK_SERVER, MONSTER_PART_WEAKNESS, OBJ_ENEMY, SKILLCACHE_PERFORMMODE

class CCartoon0(CastingTraceRayCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetSkillVarCache(skill, 'HitWeakness'):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
            cl_action.WeaponDamage(skill, {
                'Att': cl_action.GetSkillVarCache(skill, 'dam') }, {
                'SubTrajectory': 1 }, sendPFMsg = False)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': cl_action.GetSkillVarCache(skill, 'dam') }, {
                'SubTrajectory': 1 }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 6, cl_action.GetWeaponAttDis(skill), targettype = OBJ_ENEMY, effect = 0, UseLineRender = True, searchDis = cl_action.GetSkillVarCache(skill, 'searchDis'), searchNum = cl_action.GetSkillVarCache(skill, 'searchNum'), heightThreshold = 5)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TraceIntensifyLineCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSkillVarCache(skill, 'HitWeakness', cl_action.CheckHitWeakness(skill))
        cl_action.WeaponDamage(skill, {
            'Att': cl_action.GetSkillVarCache(skill, 'dam') }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 2, cl_action.GetWeaponAttDis(skill), targettype = OBJ_ENEMY, effect = 0 if cl_action.IsHeroCtrl(skill) else None, radius = 0.2, lockTeamer = False, needCheckBuff = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableShow(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'HitWeakness', False)
    cl_action.SetSkillVarCache(skill, 'searchDis', [
        6,
        6][cl_action.GetPerformMode(skill) - 1])
    cl_action.SetSkillVarCache(skill, 'searchNum', [
        3,
        3][cl_action.GetPerformMode(skill) - 1])
    cl_action.SetSkillVarCache(skill, 'dam', [
        200,
        200][cl_action.GetPerformMode(skill) - 1])
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.attack import CContinuousPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9492
    m_Name = 's毒手套左键'
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
        'ColdTime': 0,
        'AttDistance': 10,
        'ChargeTime': 0 }
    m_ClassifyTag = ()
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 0
    m_CheckForbid = 1036

