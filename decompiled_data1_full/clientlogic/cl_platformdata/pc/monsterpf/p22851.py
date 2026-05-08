# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p22851.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p22851.pyc
# Source Generated with Decompyle++
# File: p22851.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_INT, SKILLCACHE_LSTPOS

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, 0)

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
        for i1 in range(0, cl_action.ToInt(skill, cl_action.GetPerformArgValue(skill, 'BuildCount', iDefault = 12) - cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)) >= cl_action.ToInt(skill, cl_action.GetPerformArgValue(skill, 'BuildCount', iDefault = 12) - cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) else len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)), 1):
            cl_action.CreateMonsterHinder(skill, 1213, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[i1], cl_action.GetOneListFromRandonList(skill, [
                [
                    1,
                    4,
                    5,
                    7,
                    9],
                [
                    1,
                    4,
                    7,
                    8,
                    9],
                [
                    2,
                    3,
                    4,
                    6,
                    7,
                    9],
                [
                    2,
                    5,
                    7,
                    8,
                    9],
                [
                    4,
                    6,
                    7,
                    8,
                    9],
                [
                    5,
                    7,
                    8,
                    9],
                [
                    4,
                    5,
                    6,
                    7,
                    9],
                [
                    1,
                    4,
                    5,
                    6,
                    9],
                [
                    3,
                    5,
                    6,
                    7,
                    9],
                [
                    1,
                    4,
                    5,
                    6,
                    7,
                    9],
                [
                    3,
                    5,
                    6,
                    7,
                    8,
                    9],
                [
                    2,
                    4,
                    5,
                    6,
                    7,
                    8],
                [
                    2,
                    4,
                    5,
                    7,
                    9],
                [
                    1,
                    2,
                    4,
                    6,
                    7,
                    8,
                    9],
                [
                    1,
                    2,
                    3,
                    4,
                    6,
                    7]]), { })
        
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.RandomPointSectorInMeshList(skill, cl_action.CrtArgSelfPos(skill), (1, 0, 0), 3, 15, 0, 80, 4))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetMonsterHinderNum(skill))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_LSTPOS,
        SKILLCACHE_INT])
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 22851
    m_Name = '【新第三幕】明雷法师怪-阻挡物召唤'
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
    m_ElementType = DAM_TYPE_FIRE
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 1050
    m_BaseArgData = {
        'BuildCount': 12 }
    m_CacheAttr = [
        'DebuffProb']

