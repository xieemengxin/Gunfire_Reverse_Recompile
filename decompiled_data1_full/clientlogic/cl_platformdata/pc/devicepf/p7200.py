# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicepf/p7200.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicepf/p7200.pyc
# Source Generated with Decompyle++
# File: p7200.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateRayCastCartoon, DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, MONSTER_PART_UNTAGGED, OBJ_ENEMY, SKILLCACHE_BALLISTICTYPE, SKILLCACHE_BEACONCOUNT, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_PERFORMMODE

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


class CCartoon0(DelegateRayCastCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.StartBackSwing(skill, int(10000 / cl_action.GetAttackerAttr(skill, 'AttSpeed')))

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 1:
            cl_action.IgnoreCurVictimOnceAfterHit(skill)
            cl_action.VictimAddState(skill, 33130, cl_action.GetSkillCustomData(skill, 'MultiLock', defaultValue = 0), 0, { })
            cl_action.VictimAddState(skill, 33131, cl_action.GetSkillCustomData(skill, 'MultiLock', defaultValue = 0), 0, { })
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE) == 2:
            cl_action.ModifySkillCache(skill, 'CrazyEff', 20000)
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)
        else:
            cl_action.PerformDamage(skill, {
                'Att': skill.m_Cache['Att'] })
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_BEACONCOUNT) == 1:
            cl_action.VictimAddState(skill, 33131, cl_action.GetSkillCustomData(skill, 'SingleLock', defaultValue = 0), 0, { })
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 1:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 1:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 1.5, -3.6) if cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE) == 2 else (0, 1.7, -0.6)), cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 1.5, -3.6) if cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE) == 2 else (0, 1.7, -0.6)), (0, 0, 0), 1, 90, 80, targettype = OBJ_ENEMY, liveTime = 0.1, radius = 0.25, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE, iLockTarget = cl_action.GetSkillVID(skill))

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(DelegateRayCastCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 1:
            cl_action.IgnoreCurVictimOnceAfterHit(skill)
            cl_action.VictimAddState(skill, 33130, cl_action.GetSkillCustomData(skill, 'MultiLock', defaultValue = 0), 0, { })
            cl_action.VictimAddState(skill, 33131, cl_action.GetSkillCustomData(skill, 'MultiLock', defaultValue = 0), 0, { })
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE) == 2:
            cl_action.ModifySkillCache(skill, 'CrazyEff', 20000)
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)
        else:
            cl_action.PerformDamage(skill, {
                'Att': skill.m_Cache['Att'] })
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_BEACONCOUNT) == 1:
            cl_action.VictimAddState(skill, 33131, cl_action.GetSkillCustomData(skill, 'SingleLock', defaultValue = 0), 0, { })
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 1:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 1:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 1.5, -3.6) if cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE) == 2 else (0, 1.7, -0.6)), cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 1.5, -3.6) if cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE) == 2 else (0, 1.7, -0.6)), (0, 0, 0), 1, 90, 80, targettype = OBJ_ENEMY, liveTime = 0.1, radius = 0.25, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE, iLockTarget = cl_action.GetSkillVID(skill))

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
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE) == 2:
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
            for i1 in range(0, cl_action.GetSkillCacheExtraTrajectory(skill), 1):
                cartoon = { }
                CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
            
        else:
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
            for i2 in range(0, cl_action.GetSkillCacheExtraTrajectory(skill), 1):
                cartoon = { }
                CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
            

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE, cl_action.GetArgDataCache(skill, 'BulletType', iDefault = 1))
    cl_action.SetSkillCacheExtraTrajectory(skill, cl_action.GetPerformArgValue(skill, 'ExtTrajectoryNum', iDefault = 0))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_PERFORMMODE, 1 if cl_action.GetSkillCustomData(skill, 'MultiLock', defaultValue = 0) > 0 else 0)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_BEACONCOUNT, 1 if cl_action.GetSkillCustomData(skill, 'SingleLock', defaultValue = 0) > 0 else 0)
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_PERFORMMODE,
        SKILLCACHE_BEACONCOUNT,
        SKILLCACHE_BALLISTICTYPE])
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_BALLISTICTYPE,
        SKILLCACHE_BEACONCOUNT,
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.deviceactive import CDeviceActive as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL
from cl_pxlayer import PXMASK_BARRIER

class CPerform(CCustomPerform):
    m_SID = 7200
    m_Name = '致命装置-炮台攻击'
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
        'AttDistance': 50,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1,
        'EnergyCost': 500,
        'Radius': 0 }
    m_ElementType = DAM_TYPE_NORMAL
    m_UseHeight = 1.6
    m_IgnoreLayer = (PXMASK_BARRIER,)
    m_ClientNeed = (0,)
    m_ForbidRule = 0

