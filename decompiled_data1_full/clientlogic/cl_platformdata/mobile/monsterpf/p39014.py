# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39014.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39014.pyc
# Source Generated with Decompyle++
# File: p39014.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import MonsterJumpCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, SKILLCACHE_EXTRATRAJECTORY, STATE_EFF_DEBAR

class CCartoon5(TimerCartoon):
    m_SID = 5
    
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
            cls.EnableCtrl(skill, 183, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
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
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 83, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(MonsterJumpCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.RemoveIgnoreStateEffect(skill, STATE_EFF_DEBAR)

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
            cls.EnableCtrl(skill, cl_action.ChooseLevelPosLineNear(skill, [
                'bossleave1',
                'bossleave2',
                'bossleave3'], (0, 0, 0)), 30, 3, 68, 188, 48, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
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
        cl_action.AddIgnoreStateEffect(skill, STATE_EFF_DEBAR)
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 310, 1)

    InitSuccess = classmethod(InitSuccess)


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
        cl_action.AddIgnoreStateEffect(skill, STATE_EFF_DEBAR)
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 710 - cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) * 100, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

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
        cl_action.SummonAreaMonster(skill, 2, {
            (8 if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) + cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) >= 4 else (cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) + cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True)) * 2) + 1: 100,
            8 if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) + cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) >= 4 else (cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) + cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True)) * 2: 100 }, {
            (4 if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) + cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) >= 4 else cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) * 2 + cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True)) + cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) + 2 + 1: 100,
            (4 if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) + cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) >= 4 else cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) * 2 + cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True)) + cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) + 2: 100 })
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) + 1 >= (4 if cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) >= 2 else 3):
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.AttackerAddState(skill, 7014, 710 - cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) * 100, 0, { })
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(MonsterJumpCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.RemoveIgnoreStateEffect(skill, STATE_EFF_DEBAR)
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, cl_action.ChooseLevelPosLineNear(skill, [
                'bossfire',
                'bossfire1',
                'bossfire2'], (0, 0, 0)), 30, 3, 68, 188, 48, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheExtraTrajectory(skill, cl_action.GetMonsterPerformRecord(skill, 0))
    cl_action.AttackerAddState(skill, 7017, 1000, 0, { })
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNORETHUMP)
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.AddIgnoreStateEffect(skill, STATE_EFF_DEBAR)
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


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
from cl_commondefines import CLOSE_DISTANCE, DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 39014
    m_Name = 'boss陆吾-召唤'
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
        'ColdTime': 4500,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = CLOSE_DISTANCE
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

