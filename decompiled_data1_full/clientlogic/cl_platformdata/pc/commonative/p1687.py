# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1687.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1687.pyc
# Source Generated with Decompyle++
# File: p1687.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_INT, SKILLCACHE_LSTINT, WARRIOR_SUMMON

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
        cl_action.AttackerAddState(skill, 1363, 0, 0, { })
        if cl_action.GetNowLayer(skill) == 1:
            cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.CreateBoxPosList(skill, cl_action.CrtArgSelfTopPos(skill), (0.8, 0.8, 0.8), 1, 0.3, 0), WARRIOR_SUMMON, {
                1056: 1 }, {
                'Radius': 0.3 })
            cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, len(cl_action.GetSkillSummonCreate(skill)))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillSummonCreate(skill))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_INT,
                SKILLCACHE_LSTINT])
            cl_action.BindSummonFollowTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT), True)
        else:
            cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.CreateBoxPosList(skill, cl_action.CrtArgSelfTopPos(skill), (0.8, 0.8, 0.8), 1, 0.3, 0), WARRIOR_SUMMON, {
                1054: 1 }, {
                'Radius': 0.3 })
            cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, len(cl_action.GetSkillSummonCreate(skill)))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillSummonCreate(skill))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_INT,
                SKILLCACHE_LSTINT])
            cl_action.BindSummonFollowTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT), True)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT]

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1687
    m_Name = '每日试炼庇佑灵石水母生成'
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
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

