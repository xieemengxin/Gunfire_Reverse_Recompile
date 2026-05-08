# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1962.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1962.pyc
# Source Generated with Decompyle++
# File: p1962.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, EntityCurveCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALL_PLAYER, SKILLCACHE_INT, SKILLCACHE_LSTINT, WARRIOR_SUMMON
from cl_only import PY_FLAG_MONSTERTARGET

class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'ComAtt': 80 }, { }, sendPFMsg = False)

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
                1.5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL_PLAYER, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

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
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), cl_action.CrtArgMissingPos(skill, 0), 0.3, 1037, 180, 10, 60, 0.5, targettype = OBJ_ALL_PLAYER, summonID = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetTimerCartoonCurTimes(skill, 5) - 1], forceDel = True, iPyFlag = PY_FLAG_MONSTERTARGET)

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
        cl_action.SetSkillVictim(skill, cl_action.GetRandomLivePlayer(skill, 360, bNotContainDying = False, fMaxDis = 0, bSkillVIDSecond = False, iFlag = PY_FLAG_MONSTERTARGET, bResetVID = False))
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cl_action.BindSummonFollowTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT), True)

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
        cl_action.BindSummonFollowTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT), False)
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 180, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.CreateBoxPosList(skill, cl_math.Vec3Add(cl_action.CrtArgSelfPos(skill), (0, 4.2, 0)), (0.6, 0.8, 0.8), 1, 0.3, 0), WARRIOR_SUMMON, {
        1037: 10 }, {
        'Radius': 0.3 })
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
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE

class CPerform(CCustomPerform):
    m_SID = 1962
    m_Name = '火焰元素球'
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
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 10000 }

