# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1986.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1986.pyc
# Source Generated with Decompyle++
# File: p1986.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, S6_BLOOM_DICE_DAMAGE, SKILLCACHE_INT, SKILLCACHE_RANDOM

class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SetSkillCustomDataInt(skill, 'HasHit', 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSkillCustomDataInt(skill, 'BaseDam', cl_action.ToInt(skill, cl_action.GetSkillCustomData(skill, 'BaseDam', defaultValue = 0) * cl_action.GetSkillCustomData(skill, 'AttRatio', defaultValue = 1) // 100))
        if cl_action.GetSkillCustomData(skill, 'HasHit', defaultValue = 0) == 0:
            cl_action.SkillHaltSelf(skill)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, cl_action.GetSkillCustomData(skill, 'BaseDam', defaultValue = 0) * cl_action.GetSkillCustomData(skill, 'AttRatio', defaultValue = 1) // 100) })
        cl_action.SetSkillCustomDataInt(skill, 'HasHit', 1)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCustomData(skill, 'vStart', defaultValue = (0, 0, 0)), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

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
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), cl_action.GetSkillCacheData(skill, SKILLCACHE_RANDOM))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'IntervalTime', defaultValue = 0))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_RANDOM, cl_action.GetSkillCustomData(skill, 'LoopTimes', defaultValue = 0))
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        S6_BLOOM_DICE_DAMAGE][0])
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_RANDOM]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_TRUE

class CPerform(CCustomPerform):
    m_SID = 1986
    m_Name = '骰子绽放'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_TRUE
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 10,
        'ChargeTime': 0,
        'Radius': 3 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

