# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1947.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1947.pyc
# Source Generated with Decompyle++
# File: p1947.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import CurveCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ALL, SKILLCACHE_ELEMENTTYPE, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_PERFORMMODE

class CCartoon0(CurveCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.VictimAddState(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE), 500, 0, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)), cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1]), 1, 300, 30, 360, 1, targettype = OBJ_ALL, pierceblock = True, liveTime = 0, hittarger = False, iVictim = cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), lockPos = (0, 0, 0), bLockDeadPos = False)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillCustomData(skill, 'LockTarget'))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'SourceVID', defaultValue = 0))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_PERFORMMODE, cl_action.GetSkillCustomData(skill, 'ElementExceptionSID', defaultValue = 0))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_ELEMENTTYPE])
    for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)), 1):
        cl_action.SetSkillVictim(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1])
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1947
    m_Name = '元素奥能(套装)'
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
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

