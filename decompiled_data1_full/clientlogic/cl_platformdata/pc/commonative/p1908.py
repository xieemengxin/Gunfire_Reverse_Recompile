# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1908.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1908.pyc
# Source Generated with Decompyle++
# File: p1908.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_ELEMENTTYPE

class CCartoon4(DirectPosCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetSkillCustomData(skill, 'pf50010Extra', defaultValue = 0) < cl_action.GetSkillCustomData(skill, 'pf50010MaxExtra', defaultValue = 0):
            cl_action.EndDelayAttackUsePerform(skill, 1908, {
                'pf50010MaxExtra': cl_action.GetSkillCustomData(skill, 'pf50010MaxExtra', defaultValue = 0),
                'pf50010Extra': cl_action.GetSkillCustomData(skill, 'pf50010Extra', defaultValue = 0) + 1,
                'TargetID': cl_action.GetSkillCustomData(skill, 'TargetID', defaultValue = 0),
                'Element': cl_action.GetSkillCustomData(skill, 'Element', defaultValue = 0) }, 30, cl_action.GetSkillCustomData(skill, 'TargetID', defaultValue = 0), True)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetPerformArgValue(skill, 'Att', iDefault = 0) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillCustomData(skill, 'TargetID', defaultValue = 0)) if cl_action.GetSkillCustomData(skill, 'pf50010Extra', defaultValue = 0) > 0 else cl_action.CrtArgCustomPos(skill, cartoon), (0, 0, 0), [
                skill.m_Cache['AttDistance']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

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
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ModifySkillCache(skill, 'ElementType', cl_action.GetSkillCustomData(skill, 'Element', defaultValue = 512))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_ELEMENTTYPE, cl_action.GetSkillCustomData(skill, 'Element', defaultValue = 512))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_ELEMENTTYPE])
    cl_action.SetSkillVarCache(skill, 'NowElement', cl_action.GetSkillCacheData(skill, SKILLCACHE_ELEMENTTYPE))
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_ELEMENTTYPE]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_pxlayer import PXMASK_BOX
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1908
    m_Name = '秘能觉醒元素之环'
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
        'AttDistance': 6,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_IgnoreLayer = (PXMASK_BOX,)
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 3000,
        'Att': 40000 }

