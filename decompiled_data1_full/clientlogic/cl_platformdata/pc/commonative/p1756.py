# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1756.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1756.pyc
# Source Generated with Decompyle++
# File: p1756.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALL_PLAYER, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_LSTPOS, WARRIOR_HERO

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 36, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        cl_action.DeleteClientEffect(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 175, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'ComAtt': 200 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[cl_action.GetCartoonLoopID(skill, 5)], (0, 0.1, 0)), (0, 0, 0), [
                cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL_PLAYER, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 5))

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
            cls.EnableCtrl(skill, 36, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cl_action.AddSceneEventForState(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[cl_action.GetCartoonLoopID(skill, 5)], 186, 1, {
            'Radius': cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) }, 32248, 200, 1, iFightType = WARRIOR_HERO, iLeaveSetTime = -1)
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 150, 1)

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
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 1) - 1))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'TriggerRadius', defaultValue = 3))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillCustomData(skill, 'LockTarget'))
    if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) > 0:
        for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)), 1):
            cl_action.AddItemToLstPos(skill, cl_action.GetGroundPos(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1])), bCheckSame = False)
            cl_action.SetSkillServerCache(skill, 'ExtraPos', cl_action.RandomPointSectorInMeshList(skill, cl_action.GetGroundPos(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1])), (1, 0, 1), 4, 10, 1, 179, cl_action.GetSkillCustomData(skill, 'ChooseNum', defaultValue = 0)))
            for i2 in range(0, len(cl_action.GetSkillServerCache(skill, 'ExtraPos')), 1):
                cl_action.AddItemToLstPos(skill, cl_action.GetSkillServerCache(skill, 'ExtraPos')[i2], bCheckSame = False)
            
        
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_LSTPOS])
        if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)) > 0:
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE

class CPerform(CCustomPerform):
    m_SID = 1756
    m_Name = 'S7-赛季房间挑战流星'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_FIRE
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 2000 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

