# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9400.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9400.pyc
# Source Generated with Decompyle++
# File: p9400.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon, TraceCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, DAM_USE_ARMOR, DAM_USE_SHIELD, JL_CONTINUE_DAMAGE, NWARRIOR_DROP, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_INT

class CCartoon6(DirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        if cl_action.CheckHasInscription(skill, 13131):
            cl_action.SetSkillVarCache(skill, 'RemainDamTimes', cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckHasInscription(skill, 13047):
            cl_action.BreakVictimProtection(skill, DAM_USE_SHIELD, True, True)
            cl_action.BreakVictimProtection(skill, DAM_USE_ARMOR, True, True)
            cl_action.SetSkillVarCache(skill, 'Att', (60 if cl_action.GetCartoonLoopID(skill, 6) > 0 else 200) + cl_action.GetSkillVarCache(skill, 'stateCnt') * 25)
            cl_action.WeaponDamage(skill, {
                'Att': cl_action.GetSkillVarCache(skill, 'Att') }, { }, sendPFMsg = False)
            cl_action.SetSkillServerCache(skill, 'HitTimes', int(cl_action.GetSkillServerCache(skill, 'HitTimes') + 1))
        elif cl_action.GetCartoonLoopID(skill, 6) > 0:
            pass
        
        skill('Att', 60, 200 + cl_action.GetSkillVarCache(skill, 'stateCnt') * 25)
        cl_action.WeaponDamage(skill, {
            'Att': cl_action.GetSkillVarCache(skill, 'Att') }, { }, sendPFMsg = False)
        cl_action.SetSkillServerCache(skill, 'HitTimes', int(cl_action.GetSkillServerCache(skill, 'HitTimes') + 1))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgGetTransPos(skill, cl_action.GetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetCartoonLoopID(skill, 3)))), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                cl_action.GetSkillVarCache(skill, 'stateCnt') * 0.5 + 0.4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.SetAttackerStateCount(skill, 1908, 0)

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
        if cl_action.CheckTargetAlive(skill, cl_action.GetSkillVID(skill)):
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 3))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 6, cl_action.GetSkillVarCache(skill, 'DamCnt'))

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
            'Att': cl_action.GetSkillServerCache(skill, 'AttBuff') * (45 if cl_action.GetCartoonLoopID(skill, 5) > 0 else 150) }, { }, sendPFMsg = False)
        cl_action.SetSkillServerCache(skill, 'HitTimes', int(cl_action.GetSkillServerCache(skill, 'HitTimes') + 1))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgHitPos(skill), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                0.5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)

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
        CCartoon5.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 3))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 6, cl_action.GetSkillVarCache(skill, 'DamCnt'))

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TraceCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSkillVictim(skill, cl_action.GetCurVID(skill))
        cl_action.UpdateDictSkillCustomData(skill, 'PF9400_VID', cl_action.GetCurVID(skill), 1)
        cl_action.SetSkillServerCache(skill, 'PF9400_VID', cl_action.GetSkillCustomData(skill, 'PF9400_VID', defaultValue = { }))
        cl_action.SetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetCartoonLoopID(skill, 3)), cl_action.CrtArgHitTransform(skill))
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 3))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], skill.m_Cache['EnergyBar'] * 1, 50, targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 360 if cl_math.CalDistance3D(cl_action.GetCameraCenterPosition(skill, cartoon), cl_action.GetSceneObjPos(skill, 0)) <= 5 else 5, lockDis = 20, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 100, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = False, searchByDistance = False, canLockMoreTimes = False, scale = 1)

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
        cl_action.SetSkillVarCache(skill, 'DamCnt', 2 if cl_action.CheckHasInscription(skill, 13132) else cl_action.GetTrajectory(skill))
        cl_action.SetSkillVarCache(skill, 'lockLst', cl_action.GetClosestLockTarget(skill, 3, [
            15,
            20]))
        for i1 in range(0, cl_action.GetSkillVarCache(skill, 'stateCnt') + 1 if cl_action.CheckHasInscription(skill, 13132) else 1, 1):
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'stateCnt', cl_action.GetAttackerStateCount(skill, 1908))
        cl_action.SetSkillServerCache(skill, 'HitTimes', 0)
        cl_action.SetSkillServerCache(skill, 'ExShowTips', [
            JL_CONTINUE_DAMAGE][0])
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
        cl_action.SkillForbid(skill, False, 1076)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 90, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'AttBuff', cl_action.GetSkillServerCache(skill, 'AttBuff') + 1 if cl_action.CheckHasSkillCollect(skill, 'AttBuff') else 1)
    cl_action.SkillForbid(skill, True, 1076)
    cartoon = { }
    CCartoon7.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    cl_action.SkillForbid(skill, False, 1076)


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9400
    m_Name = '#NT#锯轮 s手喷近战'
    m_ExtPerform = (1020,)
    m_HaltInfo = {
        108: 1,
        40108: 1,
        10214: 1,
        10149: 1,
        143: 1 }
    m_IgnoreHalt = {
        1310: 1,
        1801: 1,
        1020: 1 }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 90,
        'AttDistance': 20,
        'ChargeTime': 0 }
    m_ClassifyTag = ()
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 0
    m_CheckForbid = 1019

