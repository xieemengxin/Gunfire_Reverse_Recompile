# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicepf/p7205.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicepf/p7205.pyc
# Source Generated with Decompyle++
# File: p7205.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import CurveCartoon, DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_BEACONCOUNT, SKILLCACHE_CHARGELEVEL, SKILLCACHE_INT, SKILLCACHE_PERFORMMODE, SKILLCACHE_POS

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.VictimAddState(skill, 33130, cl_action.GetSkillCustomData(skill, 'MultiLock', defaultValue = 0), 0, { })
        cl_action.VictimAddState(skill, 33131, cl_action.GetSkillCustomData(skill, 'MultiLock', defaultValue = 0), 0, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgHitPos(skill), (0, 0, 0), [
                5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

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
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] })
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_BEACONCOUNT) == 1:
            cl_action.VictimAddState(skill, 33131, cl_action.GetSkillCustomData(skill, 'SingleLock', defaultValue = 0), 0, { })

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
                1.5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(CurveCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_CHARGELEVEL) == 1:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cl_action.PerformDamage(skill, {
                'Att': skill.m_Cache['Att'] })
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_BEACONCOUNT) == 1:
                cl_action.VictimAddState(skill, 33131, cl_action.GetSkillCustomData(skill, 'SingleLock', defaultValue = 0), 0, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_CHARGELEVEL) == 1:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0.25, 2.5, -0.55) if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 1 else (-0.4, 2.5, -0.55) if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 2 else (0.25, 2.3, -0.8) if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 3 else (-0.4, 2.3, -0.8) if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 4 else (0, 0, 0)), cl_math.Vec3Add(cl_action.GetCameraDirPos(skill, 3), (0, cl_action.CountDistance(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0.25, 2.5, -0.55) if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 1 else (-0.4, 2.5, -0.55) if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 2 else (0.25, 2.3, -0.8) if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 3 else (-0.4, 2.3, -0.8) if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 4 else (0, 0, 0)), cl_action.CrtArgTargetPos(skill, notContainDying = False) if cl_action.CheckTargetAlive(skill, cl_action.GetSkillVID(skill)) else cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)), 0)), 1, 90, 40, 800, 0.7, targettype = OBJ_ENEMY, pierceblock = False, liveTime = 0, hittarger = False, iVictim = 0, lockPos = cl_action.GetSkillCacheData(skill, SKILLCACHE_POS))

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
        cl_action.SetSkillCustomDataInt(skill, 'ChooseSelf', 1)
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSkillCustomData(skill, 'LockPos', defaultValue = (0, 0, 0)))
    cl_action.PerformAddArgValue(skill, 'AttNum', -3 if cl_action.GetPerformArgValue(skill, 'AttNum', iDefault = 0) >= 4 else 1)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_PERFORMMODE, cl_action.GetPerformArgValue(skill, 'AttNum', iDefault = 0))
    cl_action.MonsterFaceTarget(skill, cl_action.GetSkillVID(skill), 20, 0)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_CHARGELEVEL, 1 if cl_action.GetSkillCustomData(skill, 'MultiLock', defaultValue = 0) > 0 else 0)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_BEACONCOUNT, 1 if cl_action.GetSkillCustomData(skill, 'SingleLock', defaultValue = 0) > 0 else 0)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, skill.m_Cache['TriggerTimes'])
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_INT,
        SKILLCACHE_PERFORMMODE,
        SKILLCACHE_BEACONCOUNT,
        SKILLCACHE_CHARGELEVEL,
        SKILLCACHE_POS])
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_BEACONCOUNT,
        SKILLCACHE_CHARGELEVEL,
        SKILLCACHE_INT,
        SKILLCACHE_PERFORMMODE,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.deviceactive import CDeviceActive as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL
from cl_pxlayer import PXMASK_BARRIER

class CPerform(CCustomPerform):
    m_SID = 7205
    m_Name = '炮台专属2-飞弹攻击'
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
        'AttDistance': 150,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1,
        'EnergyCost': 500,
        'Radius': 0,
        'TriggerTimes': 0 }
    m_ElementType = DAM_TYPE_NORMAL
    m_IgnoreLayer = (PXMASK_BARRIER,)
    m_ClientNeed = (0,)
    m_ForbidRule = 0

