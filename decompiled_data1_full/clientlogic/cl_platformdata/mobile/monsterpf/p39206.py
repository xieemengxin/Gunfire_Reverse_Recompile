# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39206.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39206.pyc
# Source Generated with Decompyle++
# File: p39206.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, WARRIOR_MONSTER

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
            cl_action.GetSkillServerCache(skill, 'lstpos')[cl_action.GetTimerCartoonCurTimes(skill, 1) - 1]], WARRIOR_MONSTER, {
            39211: 1 }, {
            'FollowDie': 1 })
        cl_action.WarriorUsePerform(skill, cl_action.GetSkillSummonCreate(skill)[cl_action.GetTimerCartoonCurTimes(skill, 1) - 1], 39216, { }, False)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 40, 3)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'lstpos', cl_action.ChooseTentacleRoundPos(skill, 60, 30, 3, 11, 19, -5, 10))
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return [
        39211]

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39206
    m_Name = '海怪-召唤强化插击'
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
        'ColdTime': 1200,
        'AttDistance': 200,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

