# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39213.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39213.pyc
# Source Generated with Decompyle++
# File: p39213.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import SectorRotateCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, MODEL_TYPE_BOX, OBJ_ENEMY, SKILLCACHE_INT

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
            cls.EnableCtrl(skill, cl_action.ToInt(skill, cl_action.GetPlayRound(skill) * -7 + 187), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

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
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_INT])

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(TimerCartoon):
    m_SID = 9
    
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
            cls.EnableCtrl(skill, 10, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon9.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.ClearAttackerForceDistance(skill)
        cl_action.AttackerRemoveState(skill, 20026, bSameItem = False)
        cl_action.AttackerRemoveState(skill, 20030, bSameItem = False)
        cl_action.RemovePhyModel(skill, 'PF39213_UP')

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
            cls.EnableCtrl(skill, 150, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveSelf(skill)

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
            cls.EnableCtrl(skill, 200, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(SectorRotateCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 80 }, { }, sendPFMsg = False)
        cl_action.PushHeroVictim(skill, (0, 0, 0), 10, 5, 10000, downSpeed = 5, fGravaty = 9.8, angle = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), cl_math.Vec3Minus(cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_math.Vec3Minus(cl_action.GetMapCenterPos(skill), cl_action.CrtArgSelfPos(skill)), 60, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) * 60), cl_action.CrtArgSelfPos(skill)), (0, 3, 0), 120, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) * (cl_action.GetPlayRound(skill) * 20 + 60), 3.6, 60, targettype = OBJ_ENEMY, innerRadius = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(SectorRotateCartoon):
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), cl_math.Vec3Minus(cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_math.Vec3Minus(cl_action.GetMapCenterPos(skill), cl_action.CrtArgSelfPos(skill)), 60, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) * 60), cl_action.CrtArgSelfPos(skill)), (0, 3, 0), 120, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) * (cl_action.GetPlayRound(skill) * 20 + 60), 10, 60, targettype = OBJ_ENEMY, innerRadius = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 167, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.CalTargetClockWise(skill, cl_action.CrtArgSelfPos(skill), (0, 0, 0)))
        cl_action.MonsterAttackerFacePos(skill, cl_action.GetMapCenterPos(skill), 0)
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

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
        cl_action.SetAttackerForceDistance(skill, 10)
        cl_action.CreatePhyModel(skill, 'PF39213_UP', MODEL_TYPE_BOX, 2, 6, [
            4,
            1,
            (cl_action.CountDistance(skill, (33.5, 3.4, -0.51), cl_action.CrtArgSelfPos(skill)) - 28) / 2], (0, 3, (cl_action.CountDistance(skill, (33.5, 3.4, -0.51), cl_action.CrtArgSelfPos(skill)) - 28) / 2))
        cl_action.SetExtraModelDistance(skill, cl_action.CountDistance(skill, (33.5, 3.4, -0.51), cl_action.CrtArgSelfPos(skill)) - 28)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon7.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39213
    m_Name = '触手-横扫'
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
        'ColdTime': 1000,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

