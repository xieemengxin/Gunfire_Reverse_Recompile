# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39154.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39154.pyc
# Source Generated with Decompyle++
# File: p39154.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY

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
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 129 - cl_action.GetPlayRound(skill) * 5), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(RayCastCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.UnlockMonsterAttackerFace(skill)
        cl_action.StartBackSwing(skill, 83)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 80 }, { }, sendPFMsg = False)
        cl_action.PushHeroVictim(skill, (0, 0, 0), 25, 7, 10000, downSpeed = 0, fGravaty = 9.8, angle = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetMonsterMuzzlePos(skill, (0, 2, 0)), cl_action.GetMonsterMuzzlePos(skill, (0, 2, 0)), cl_action.StartAndEndAtSameHeight(skill, cl_action.GetMonsterMuzzlePos(skill, (0, 2, 0)), cl_action.CrtArgTargetPos(skill)), 10, 100, cl_action.ToInt(skill, cl_action.GetPlayRound(skill) * 5 + 50), targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = 0, effectLiveTime = 1, radius = 1.5, flyoverdis = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

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
        cl_action.LockMonsterAttackerFace(skill)
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 135 - cl_action.GetPlayRound(skill) * 5), 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import CLOSE_DISTANCE, DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 39154
    m_Name = '风神-贴地波'
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
        'ColdTime': 300,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = CLOSE_DISTANCE
    m_ForbidRule = 1038
    m_CacheAttr = [
        'DebuffProb']

