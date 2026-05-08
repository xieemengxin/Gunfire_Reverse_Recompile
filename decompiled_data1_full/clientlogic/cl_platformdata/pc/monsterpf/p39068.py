# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39068.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39068.pyc
# Source Generated with Decompyle++
# File: p39068.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, EntityParabolaCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY

class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            'Attack': 1 })

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
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 0), (0, 0, 0), [
                12], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(EntityParabolaCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.StartBackSwing(skill, cl_action.ToInt(skill, 264 - cl_action.GetPlayRound(skill) * 16))

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.DeleteClientEffect(skill)
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.DeleteClientEffect(skill)
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, [
                (27.32, 15.11, 55.78),
                (32.04, 15.25, 53.89),
                (37.412, 15.28, 55.32)][cl_action.GetTimerCartoonCurTimes(skill, 4)], cl_action.CrtArgGetCustomDir(skill, [
                (27.32, 15.11, 55.78),
                (32.04, 15.25, 53.89),
                (37.412, 15.28, 55.32)][cl_action.GetTimerCartoonCurTimes(skill, 4)], [
                (10, 3.27, 18),
                (32, 3.25, 18),
                (54, 3.38, 18)][cl_action.GetTimerCartoonCurTimes(skill, 4)], (60, 0, 0), baseHorizontal = False), cl_action.CalParabolaSpeed([
                (27.32, 15.11, 55.78),
                (32.04, 15.25, 53.89),
                (37.412, 15.28, 55.32)][cl_action.GetTimerCartoonCurTimes(skill, 4)], [
                (10, 3.27, 18),
                (32, 3.25, 18),
                (54, 3.38, 18)][cl_action.GetTimerCartoonCurTimes(skill, 4)], -11 - cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True), 50), 0.5, (0, 0, 0), (0, 0), (0, 0), 800, True, True, 0, True, 0, 1022, targetType = OBJ_ENEMY, maxDistance = 0, hitHeroOver = True, forceSpeed = False, innerRadius = 0, scale = 1, hitmonsterover = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.CheckTargetAlive(skill, cl_action.GetSkillAID(skill)):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.MonsterAttackerFacePos(skill, (31, 4, 4), 10)

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
            cls.EnableCtrl(skill, 50, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cl_action.MonsterAttackerFacePos(skill, [
            (10, 3.27, 18),
            (32, 3.25, 18),
            (54, 3.38, 18)][cl_action.GetTimerCartoonCurTimes(skill, 4)], 5)
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.MonsterAttackerFacePos(skill, [
            (10, 3.27, 18),
            (32, 3.25, 18),
            (54, 3.38, 18)][cl_action.GetTimerCartoonCurTimes(skill, 4)], 5)
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 80, 2)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39068
    m_Name = '海船-火力全开'
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
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

