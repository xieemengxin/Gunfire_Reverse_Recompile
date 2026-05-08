# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39209.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39209.pyc
# Source Generated with Decompyle++
# File: p39209.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, WARRIOR_SUMMON

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
        cl_action.CreateRandomNumWarriorAtPointPos(skill, [
            cl_action.GetSkillServerCache(skill, 'pos')[cl_action.GetTimerCartoonCurTimes(skill, 0)]], WARRIOR_SUMMON, {
            1053: 1 }, {
            'FollowDie': 1,
            'Radius': 0.3 })
        cl_action.WarriorUsePerform(skill, cl_action.GetSkillSummonCreate(skill)[cl_action.GetTimerCartoonCurTimes(skill, 0)], 39218, { }, False)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.AddClientEffect(skill, 1020, cl_action.GetSkillServerCache(skill, 'pos')[cl_action.GetTimerCartoonCurTimes(skill, 0)], time = 50)
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
        cl_action.AddClientEffect(skill, 1020, cl_action.GetSkillServerCache(skill, 'pos')[cl_action.GetTimerCartoonCurTimes(skill, 0)], time = 50)
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 65, cl_action.ToInt(skill, (3 if cl_action.GetAllHeroCnt(skill, False) > 2 else 2) + -1))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.GetSummonCnt(skill, 1053) < cl_action.GetPlayRound(skill) + 3 + (7 if cl_action.GetAllHeroCnt(skill, False) > 2 else 5):
        cl_action.SetSkillServerCache(skill, 'pos', cl_action.AdjustTentaclePos(skill, cl_action.ChooseTentacleRoundPos(skill, cl_action.CrtArgRandomNum(skill, 0, 5) + 23, 30, 3 if cl_action.GetAllHeroCnt(skill, False) > 2 else 2, 5, 7.5, 0, 0), (1, 0, 0), 1053, 30, 5, 180, 0, lastDirOnly = False, heightOffset = 3.7))
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39209
    m_Name = '海怪-强化拍击-运营用'
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
        'ColdTime': 2600,
        'AttDistance': 200,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

