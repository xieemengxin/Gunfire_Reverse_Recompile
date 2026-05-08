# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1728.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1728.pyc
# Source Generated with Decompyle++
# File: p1728.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, EntityParabolaCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY

class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] }, dArgs = { })

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
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(EntityParabolaCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

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
        cl_action.DeleteClientEffect(skill)
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-1, 2.7, -1.5)), cl_action.CrtArgGetCustomDir(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-1, 2.7, -1.5)), cl_action.CrtArgTargetPos(skill, notContainDying = False), (45, 0, 0), baseHorizontal = False), cl_action.CalParabolaSpeed(cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-1, 2.7, -1.5)), cl_action.CrtArgTargetPos(skill, notContainDying = False), -18, 45) * cl_action.GetPerformArgValue(skill, 'SpeedMul', iDefault = 1), 0.5, (0, cl_action.GetPerformArgValue(skill, 'Acceleration', iDefault = 0), 0), (0, 0), (0, 0), 800, True, True, 0, True, 0, 1021, targetType = OBJ_ENEMY, maxDistance = 0, hitHeroOver = False, forceSpeed = False, innerRadius = 0, scale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(DirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] }, dArgs = { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 5), (0, 0, 0), [
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(EntityParabolaCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.DeleteClientEffect(skill)
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.DeleteClientEffect(skill)
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.DeleteClientEffect(skill)
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (1, 2.7, -1.5)), cl_action.CrtArgGetCustomDir(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (1, 2.7, -1.5)), cl_action.CrtArgTargetPos(skill, notContainDying = False), (45, 0, 0), baseHorizontal = False), cl_action.CalParabolaSpeed(cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (1, 2.7, -1.5)), cl_action.CrtArgTargetPos(skill, notContainDying = False), -18, 45) * cl_action.GetPerformArgValue(skill, 'SpeedMul', iDefault = 1), 0.5, (0, cl_action.GetPerformArgValue(skill, 'Acceleration', iDefault = 0), 0), (0, 0), (0, 0), 800, True, True, 0, True, 0, 1021, targetType = OBJ_ENEMY, maxDistance = 0, hitHeroOver = False, forceSpeed = False, innerRadius = 0, scale = 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheExtraTrajectory(skill, cl_action.GetSkillCustomData(skill, 'IsRight', defaultValue = 0))
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) == 1:
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
    else:
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE

class CPerform(CCustomPerform):
    m_SID = 1728
    m_Name = '#NT#妖灵獒龙'
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

