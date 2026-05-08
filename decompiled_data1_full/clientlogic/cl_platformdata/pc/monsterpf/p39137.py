# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39137.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39137.pyc
# Source Generated with Decompyle++
# File: p39137.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, EntityParabolaCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_BALLISTICTYPE, SKILLCACHE_EXTRATRAJECTORY

class CCartoon16(TimerCartoon):
    m_SID = 16
    
    def Active(cls, skill):
        cl_action.StartBackSwing(skill, 150)

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
        cl_action.UnlockMonsterAttackerFace(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(DirectPosCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 25 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 3), (0, 0, 0), [
                5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 15)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(EntityParabolaCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 30 }, { }, sendPFMsg = False)
        cl_action.SendCurCartoonTriggerMsg(skill)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
        cl_action.SendCurCartoonTriggerMsg(skill)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-2, 5, -5)), cl_action.CrtArgGetCustomDir(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-2, 5, -5)), cl_action.CrtArgTargetPos(skill, notContainDying = False), (50, 0, 0)), cl_action.CalParabolaSpeed(cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-2, 5, -5)), cl_action.CrtArgTargetPos(skill, notContainDying = False), -20 if cl_action.GetPlayRound(skill) >= 3 else -18 if cl_action.GetPlayRound(skill) >= 2 else -16, 50), 0.5, (0, 0, 0), (0, 0), (0, 0), 1000, True, True, 0, True, 0, 1016, targetType = OBJ_ENEMY, maxDistance = 0, hitHeroOver = False, forceSpeed = False, innerRadius = 0, scale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 25 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 17), (0, 0, 0), [
                5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
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
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 15)

    InitSuccess = classmethod(InitSuccess)


class CCartoon17(EntityParabolaCartoon):
    m_SID = 17
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 30 }, { }, sendPFMsg = False)
        cl_action.SendCurCartoonTriggerMsg(skill)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)
        cl_action.SendCurCartoonTriggerMsg(skill)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-2, 5, -5)), cl_action.CrtArgGetCustomDir(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-2, 5, -5)), cl_action.GetSkillVarCache(skill, 'summonpos')[cl_action.GetCartoonLoopID(skill, 17)], (50, 0, 0)), cl_action.CalParabolaSpeed(cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-2, 5, -5)), cl_action.GetSkillVarCache(skill, 'summonpos')[cl_action.GetCartoonLoopID(skill, 17)], -20 if cl_action.GetPlayRound(skill) >= 3 else -18 if cl_action.GetPlayRound(skill) >= 2 else -16, 50), 0.5, (0, 0, 0), (0, 0), (0, 0), 1000, True, True, 0, True, 0, 1016, targetType = OBJ_ENEMY, maxDistance = 0, hitHeroOver = False, forceSpeed = False, innerRadius = 0, scale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        for i2 in range(0, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY), 1):
            cartoon = { }
            CCartoon17.Init(skill, cartoon, casting = 0, index = i2)
        

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SetSkillVarCache(skill, 'summonpos', cl_action.GetSummonPosByBoxSplit(skill, (cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) - 1) * 10 + 30, (cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) - 1) + 5, 1, False, {
            cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE) + (cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) - 1) * 2: 10 }, { }, True))
        cl_action.SetSkillCacheExtraTrajectory(skill, len(cl_action.GetSkillVarCache(skill, 'summonpos')))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(TimerCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon16.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
        for i1 in range(0, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY), 1):
            cartoon = { }
            CCartoon17.Init(skill, cartoon, casting = 0, index = i1)
        
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 0, index = 0)
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 167, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 67, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'summonpos', cl_action.GetSummonPosByBoxSplit(skill, (cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) - 1) * 10 + 30, (cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) - 1) + 5, 1, False, {
        cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE) + (cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) - 1) * 2: 10 }, { }, True))
    cl_action.SetSkillCacheExtraTrajectory(skill, len(cl_action.GetSkillVarCache(skill, 'summonpos')))
    cl_action.LockMonsterAttackerFace(skill)
    cartoon = { }
    CCartoon6.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_BALLISTICTYPE,
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39137
    m_Name = '二幕boss-纵向远程子弹攻击'
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
        'ColdTime': 600,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 10000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_CORRISION
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

