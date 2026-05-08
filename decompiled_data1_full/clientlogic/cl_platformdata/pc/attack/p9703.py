# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9703.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9703.pyc
# Source Generated with Decompyle++
# File: p9703.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TraceCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, NWARRIOR_DROP, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY

class CCartoon4(DirectPosCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = True)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 1), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                2.5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = True, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TraceCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), skill.m_Cache['BulletSpeed'], showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 0, angle = 5 if cl_math.CalDistance3D(cl_action.GetCameraCenterPosition(skill, cartoon), cl_action.GetSceneObjPos(skill, 0)) >= 15 else 15 if cl_math.CalDistance3D(cl_action.GetCameraCenterPosition(skill, cartoon), cl_action.GetSceneObjPos(skill, 0)) <= 5 else cl_math.CalDistance3D(cl_action.GetCameraCenterPosition(skill, cartoon), cl_action.GetSceneObjPos(skill, 0)) * -1 + 20, lockDis = 70, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = cl_action.GetSkillVarCache(skill, 'offsetpos'), arriveDoTrigger = True, accelerated = 25, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = False, searchByDistance = False, canLockMoreTimes = False, scale = 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    for i1 in range(0, cl_action.GetTrajectory(skill), 1):
        cl_action.SetSkillVarCache(skill, 'targetId', 0)
        cl_action.SetSkillVarCache(skill, 'offsetpos', (0, 0, 0))
        cl_action.SetSkillVarCache(skill, 'endpos', cl_math.Vec3Add((0, 0, 0), cl_action.GetSceneObjPos(skill, 0)))
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = i1)
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9703
    m_Name = '#NT#浮游炮普攻'
    m_ExtPerform = ()
    m_HaltInfo = {
        40108: 1,
        30108: 1,
        10214: 1,
        143: 1 }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_BulletUse = 1
    m_ForbidRule = 0
    m_PassRule = {
        1012: 1,
        1051: 1,
        1062: 1,
        1064: 1,
        1065: 1,
        1085: 1 }
    m_CheckForbid = 1034

