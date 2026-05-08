# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1925.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1925.pyc
# Source Generated with Decompyle++
# File: p1925.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, MONSTER_PART_UNTAGGED, SKILLCACHE_INT

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
        cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVID(skill))
        cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
        cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVID(skill)))
        for i1 in range(0, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 1):
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1324, 'Att') })
            if cl_action.CheckWarriorHasState(skill, cl_action.GetSkillVID(skill), 1854):
                cl_action.SubAttackerCareerPerformColdTime(skill, 0, iTime = cl_action.GetPerformArgValue(skill, 'SubCD', iDefault = 100))
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 9, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'damtimes', defaultValue = 0))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_INT])
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1925
    m_Name = '#NT#处决额外伤害'
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
    m_ClientNeed = 1
    m_UseCurWeapon = 0
    m_ForbidRule = 0

