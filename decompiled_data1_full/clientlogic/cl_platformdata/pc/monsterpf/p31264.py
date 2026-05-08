# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p31264.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p31264.pyc
# Source Generated with Decompyle++
# File: p31264.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateThrowCartoon, DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_LSTINT, SKILLCACHE_RANDOM

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 4), (0, 0, 0), [
                3], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(DelegateThrowCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cl_action.StartBackSwing(skill, 137)

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
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-4, 0.82, 0)), cl_action.CrtArgGetCustomDir(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-4, 0.82, 0)), cl_action.GetSkillVarCache(skill, 'summonpos')[cl_action.GetCartoonLoopID(skill, 4)], (50, 0, 0), baseHorizontal = False), cl_action.CalParabolaSpeed(cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-4, 0.82, 0)), cl_action.GetSkillVarCache(skill, 'summonpos')[cl_action.GetCartoonLoopID(skill, 4)], -12, 50), 0.1, (0, 0, 0), (0.45, 0.45), 200, False, liveTime = 0, innerRadius = 0.1, pierce = 0)

    InitSuccess = classmethod(InitSuccess)


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
        for i1 in range(0, cl_action.GetRandomInRange(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[1], cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[2]), 1):
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 160, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 81, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, [
        cl_action.GetPerformArgValue(skill, 'PosNum', iDefault = 15),
        cl_action.GetPerformArgValue(skill, 'MinNum', iDefault = 7),
        cl_action.GetPerformArgValue(skill, 'MaxNum', iDefault = 9)])
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_LSTINT])
    cl_action.SetSkillVarCache(skill, 'summonpos', cl_action.GetSummonPosByBoxSplit(skill, 40, 9, 1, False, {
        cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0]: 10 }, { }, True, iAngle = 0))
    cl_action.SetSkillCacheExtraTrajectory(skill, len(cl_action.GetSkillVarCache(skill, 'summonpos')))
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_LSTINT,
        SKILLCACHE_RANDOM]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 31264
    m_Name = '【第三幕】精英中型近战-全垒打地雷'
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
        'ColdTime': 500,
        'AttDistance': 30,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_CDPerform = 31262
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 1050
    m_CacheAttr = [
        'DebuffProb']

