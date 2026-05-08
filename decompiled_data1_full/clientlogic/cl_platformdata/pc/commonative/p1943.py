# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1943.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1943.pyc
# Source Generated with Decompyle++
# File: p1943.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateDirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_ELEMENTTYPE, SKILLCACHE_INT

class CCartoon1(DelegateDirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            cl_action.ModifySkillCache(skill, 'ElementType', cl_action.GetSkillCacheData(skill, SKILLCACHE_ELEMENTTYPE))
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_ELEMENTTYPE) == 1024:
            cl_action.ModifySkillCache(skill, 'ElementType', 1024)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_ELEMENTTYPE) == 512:
            cl_action.ModifySkillCache(skill, 'ElementType', 512)
        else:
            cl_action.ModifySkillCache(skill, 'ElementType', 256)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgCustomPos(skill, cartoon), (0, 0, 0), [
                cl_action.GetAttackerPerformAttr(skill, 1943, 'Radius')], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, useclientpos = False)

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
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_ELEMENTTYPE, cl_action.GetSkillCustomData(skill, 'Element', defaultValue = 512))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'ExtraElement', defaultValue = 0))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_ELEMENTTYPE,
        SKILLCACHE_INT])
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_ELEMENTTYPE,
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1943
    m_Name = '#NT#套装元素脉冲'
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
        'ChargeTime': 0,
        'DebuffProb': 3000,
        'Att': 35000,
        'Radius': 5 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

