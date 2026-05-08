# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1725.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1725.pyc
# Source Generated with Decompyle++
# File: p1725.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, EntityCurveCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT, WARRIOR_SUMMON

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
            'Att': 90 }, { }, sendPFMsg = False)

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
                1.5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

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
            cls.EnableCtrl(skill, (0, 0, 0), cl_action.CrtArgTargetPos(skill, notContainDying = False), 0.3, 1039, 180, 10, 60, 0.5, targettype = OBJ_ENEMY, summonID = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetTimerCartoonCurTimes(skill, 5) - 1], forceDel = True)

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
        cl_action.SetSkillVictim(skill, cl_action.GetSkillVID(skill))
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.CreateBoxPosList(skill, cl_math.Vec3Add(cl_action.CrtArgSelfPos(skill), (0, cl_action.GetPointTargetModelHeight(skill, cl_action.GetSkillVID(skill)) * 1.5, 0)), (0.6, 0.8, 0.8), 1, 0.3, 0), WARRIOR_SUMMON, {
        1039: 10 }, {
        'Radius': 0.3 })
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, len(cl_action.GetSkillSummonCreate(skill)))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillSummonCreate(skill))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT])
    cartoon = { }
    CCartoon5.Init(skill, cartoon, casting = 0, index = 0)


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
    m_SID = 1725
    m_Name = '#NT#妖灵火球'
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
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 10000 }

