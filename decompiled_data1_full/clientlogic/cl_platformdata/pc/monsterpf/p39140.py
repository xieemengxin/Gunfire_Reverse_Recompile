# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39140.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39140.pyc
# Source Generated with Decompyle++
# File: p39140.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_EXTRATRAJECTORY

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
        if cl_action.CheckHasState(skill, 7133):
            cl_action.AttackerRemoveState(skill, 7133, bSameItem = False)
        else:
            cl_action.SummonAreaMonster(skill, 3, {
                (8 if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) + 1 >= 4 else 11 if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) + 1 >= 3 else 2) + 2: 100,
                (8 if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) + 1 >= 4 else 11 if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) + 1 >= 3 else 2) + 1: 100,
                8 if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) + 1 >= 4 else 11 if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) + 1 >= 3 else 2: 100 }, {
                cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) + 1: 100 })
            cl_action.SwitchAttackerNavAble(skill, False)
            cl_action.SwitchAttackerPhyAble(skill, False)
            cl_action.AttackerAddState(skill, 7133, 0, 0, {
                'Att': 0 })

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 150, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheExtraTrajectory(skill, cl_action.GetMonsterPerformRecord(skill, 0) + cl_action.GetMonsterPerformRecord(skill, 39141))
    cl_action.LockMonsterAttackerFace(skill)
    cl_action.SetMonsterAttackerPhase(skill, 3)
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39140
    m_Name = '二幕boss-本体潜沙技能'
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
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

