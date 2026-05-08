# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p32822.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p32822.pyc
# Source Generated with Decompyle++
# File: p32822.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_BALLISTICTYPE, WARRIOR_MONSTER

class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.GetSummonPosByBoxSplit(skill, 12, 4, cl_action.GetWarriorModelRadius(skill, WARRIOR_MONSTER, 32822, 'NavMesh'), True, {
            cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE) + 2 if cl_action.GetAllHeroCnt(skill, False) > 2 else cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE): 10 }, { }, False), WARRIOR_MONSTER, {
            32822: 10 }, {
            'FollowDie': 1,
            'SameGrade': 1 })
        cl_action.AttackerAddState(skill, 7094, 0, 0, { })
        cl_action.AttackerAddState(skill, 7098, 100, 0, { })
        cl_action.StartBackSwing(skill, 50)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.LockMonsterAttackerFace(skill)
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_BALLISTICTYPE]


def GetOtherMonster():
    return [
        32822]

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 32822
    m_Name = '【第三幕】精英召唤法师怪-精英召唤'
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
        'ColdTime': 1500,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_UseHeight = 1.5
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 1050
    m_CacheAttr = [
        'DebuffProb']

