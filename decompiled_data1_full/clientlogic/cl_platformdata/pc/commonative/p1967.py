# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1967.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1967.pyc
# Source Generated with Decompyle++
# File: p1967.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, EntityCurveCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LIVEHEROCNT, SKILLCACHE_LSTINT, WARRIOR_SUMMON
from cl_only import PY_FLAG_MONSTERTARGET

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 10 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 6), (0, 0, 0), [
                5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 15)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(EntityCurveCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 20 }, { }, sendPFMsg = False)
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
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), cl_action.CrtArgTargetPos(skill, notContainDying = False), 1, 1078, 180, 20, 60, 0.3, targettype = OBJ_ENEMY, summonID = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetCartoonLoopID(skill, 0)], forceDel = True, iPyFlag = PY_FLAG_MONSTERTARGET)

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
        cl_action.SummonAttachHitTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetCartoonLoopID(skill, 0)], True, 0, (0, 0, 0), parentName = '')
        cl_action.SetSkillVictim(skill, cl_action.GetRandomLivePlayer(skill, 360, bNotContainDying = True, fMaxDis = 0, bSkillVIDSecond = False, iFlag = PY_FLAG_MONSTERTARGET, bResetVID = False))
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 150, 1)

    InitSuccess = classmethod(InitSuccess)


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
        cl_action.TargetAddState(skill, 8075, 0, 0, { }, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetTimerCartoonCurTimes(skill, 5) - 1])
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = cl_action.GetTimerCartoonCurTimes(skill, 5) - 1)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))

    InitSuccess = classmethod(InitSuccess)


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
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 60, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.PerformAddArgValue(skill, '1967_UseCnt', 1)
    cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.CreateBoxPosList(skill, cl_math.Vec3Add(cl_action.CrtArgSelfPos(skill), (cl_action.GetPerformArgValue(skill, 'OffsetX', iDefault = 0), cl_action.GetPerformArgValue(skill, 'OffsetY', iDefault = 0), cl_action.GetPerformArgValue(skill, 'OffsetZ', iDefault = 0))), (cl_action.GetPerformArgValue(skill, 'SizeX', iDefault = 12), cl_action.GetPerformArgValue(skill, 'SizeY', iDefault = 24), cl_action.GetPerformArgValue(skill, 'SizeZ', iDefault = 12)), cl_action.GetAllHeroCnt(skill, True, bUseRidingAloneCnt = False) + (1 if cl_action.GetPerformArgValue(skill, '1967_UseCnt', iDefault = 1) < 3 else cl_action.GetPerformArgValue(skill, '1967_UseCnt', iDefault = 1) if cl_action.GetPerformArgValue(skill, '1967_UseCnt', iDefault = 1) < 5 else 4) + (cl_action.GetNowLayer(skill) + -1 if cl_action.GetNowLayer(skill) + -1 < 3 else 3) * 2, 1, 0.8), WARRIOR_SUMMON, {
        1078: 10 }, {
        'Radius': 1 })
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, len(cl_action.GetSkillSummonCreate(skill)))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillSummonCreate(skill))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT])
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LIVEHEROCNT,
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1967
    m_Name = '首领遗物-鱼龙毒球'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_NORMAL
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 99,
        'ChargeTime': 0,
        'Radius': 5 }
    m_ClientNeed = 1
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'OffsetX': 0,
        'OffsetY': 20,
        'OffsetZ': 0,
        'SizeX': 12,
        'SizeY': 24,
        'SizeZ': 12 }

