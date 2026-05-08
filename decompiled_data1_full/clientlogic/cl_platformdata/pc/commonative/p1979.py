# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1979.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1979.pyc
# Source Generated with Decompyle++
# File: p1979.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, INK_DAMAGE, OBJ_ALL, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_INT, WARRIOR_MONSTER

class CCartoon6(DirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_MONSTER, OBJ_ALL):
            cl_action.SetSkillServerCache(skill, 'ExShowTips', [
                INK_DAMAGE][0])
            cl_action.PerformDamage(skill, {
                'Att': cl_action.ToInt(skill, cl_action.GetAttackerPerformAttr(skill, 1434, 'Att') * cl_action.GetSkillCustomData(skill, 'AttRatio', defaultValue = 100) / 100) }, dArgs = { })
            if cl_action.CrtArgRandomNum(skill, 0, 100) < cl_action.GetSkillCustomData(skill, 'AddStateRatio', defaultValue = 0):
                cl_action.LionAddLockStateToTarget(skill, cl_action.GetCurVID(skill), cl_action.GetAttackerPerformAttr(skill, 1434, 'AddStateTime'), False, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVID(skill)), (0, 0, 0), [
                cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) - 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'ExplosionRadius', defaultValue = 0))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY, cl_action.GetSkillCustomData(skill, 'ExplosionTimes', defaultValue = 0))
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) > 1:
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
    else:
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1979
    m_Name = '#NT#狮子劫印焚虚天赋爆炸'
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
        'AttDistance': 99,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

