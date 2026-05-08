# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1754.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1754.pyc
# Source Generated with Decompyle++
# File: p1754.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_LSTPOS, WARRIOR_HERO, WARRIOR_MONSTER

class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)), 1):
            cl_action.AddClientEffect(skill, 1018 if cl_action.GetNowLayer(skill) == 2 else 1017, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[i1], 50, (0, 0, 0))
            cl_action.AddSceneEventForState(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[i1], 200, 1, {
                'Radius': 2 }, 32248, 50, 1, iFightType = WARRIOR_HERO, iLeaveSetTime = -1)
        

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
        cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS), WARRIOR_MONSTER, {
            cl_action.GetSkillCustomData(skill, 'CreateMonsterSID', defaultValue = 0): 100 }, { }, (0, 0, 0))
        if cl_action.CheckHasSkillCollect(skill, 'SummonCreate'):
            for i2 in range(0, len(cl_action.GetSkillServerCache(skill, 'SummonCreate')), 1):
                cl_action.TargetAddState(skill, 33963, 0, 0, { }, cl_action.GetSkillServerCache(skill, 'SummonCreate')[i2])
            

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSummonPosByBoxSplit(skill, (cl_action.GetWarriorModelRadius(skill, WARRIOR_MONSTER, cl_action.GetSkillCustomData(skill, 'CreateMonsterSID', defaultValue = 0), 'NavMesh') + 0.5) * 6, 3, cl_action.GetWarriorModelRadius(skill, WARRIOR_MONSTER, cl_action.GetSkillCustomData(skill, 'CreateMonsterSID', defaultValue = 0), 'NavMesh'), True, {
        cl_action.GetSkillCustomData(skill, 'CreateMonsterNum', defaultValue = 0): 100 }, { }, False, iAngle = 0))
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1754
    m_Name = '#NT#S7房间挑战4召唤一刀怪'
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

