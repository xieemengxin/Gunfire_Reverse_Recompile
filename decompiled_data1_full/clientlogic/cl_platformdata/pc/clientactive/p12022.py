# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12022.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12022.pyc
# Source Generated with Decompyle++
# File: p12022.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, RayCastCartoon, TraceCartoon
from cl_commondefines import ATT_SHAPE_SECTOR, ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, MONSTER_PART_UNTAGGED, OBJ_ENEMY, SKILLCACHE_INT

class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': cl_action.GetPerformArgValue(skill, 'Att', iDefault = 0) }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 1), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(RayCastCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = (cl_action.GetSkillCustomArg(skill, 'StartX') / 100, cl_action.GetSkillCustomArg(skill, 'StartY') / 100, cl_action.GetSkillCustomArg(skill, 'StartZ') / 100)):
                return None
            cls.EnableShow(skill, 1, 50, 25, targettype = OBJ_ENEMY, liveTime = 0, radius = 0.5, flyoverdis = 0, passid = cl_action.GetSkillCustomArg(skill, 'MainTarget'), extCheck = CRT_EXTCHECK_NONE)

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
            'Att': cl_action.GetPerformArgValue(skill, 'Att', iDefault = 0) }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 2), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(RayCastCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetStartPositionInCrt(skill, 6)):
                return None
            cls.EnableShow(skill, 1, 50, 25, targettype = OBJ_ENEMY, liveTime = 0, radius = 0, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': cl_action.GetPerformArgValue(skill, 'Att', iDefault = 0) }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 4), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TraceCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetStartPositionInCrt(skill, 6)):
                return None
            cls.EnableShow(skill, 1, 25, 20, showstart = cl_action.GetStartPositionInCrt(skill, 6), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 0, angle = 25, lockDis = 0, IgnoreDefalutDis = 0, iIgnoreMonsterID = cl_action.GetSkillCustomArg(skill, 'MainTarget'), FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(DirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetCartoonHitTargetCount(skill, 6) == 0:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 6))
        else:
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 6))

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
    
    def InitSuccess(cls, skill, i2, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = (cl_action.GetSkillCustomArg(skill, 'StartX') / 100, cl_action.GetSkillCustomArg(skill, 'StartY') / 100, cl_action.GetSkillCustomArg(skill, 'StartZ') / 100), end = cl_action.CrtArgDestPosDirPlane(skill, (cl_action.GetSkillCustomArg(skill, 'StartX') / 100, cl_action.GetSkillCustomArg(skill, 'StartY') / 100, cl_action.GetSkillCustomArg(skill, 'StartZ') / 100), (cl_action.GetSkillCustomArg(skill, 'DirX') / 100, cl_action.GetSkillCustomArg(skill, 'DirY') / 100, cl_action.GetSkillCustomArg(skill, 'DirZ') / 100), 99, i2 * (360 / skill.m_Cache['MaxCover']))):
                return None
            cls.EnableShow(skill, [
                25,
                5,
                20], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_INT)
    cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
    cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)))
    cl_action.SetDirectHitInfo(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
    cl_action.WeaponDamage(skill, {
        'Att': cl_action.GetPerformArgValue(skill, 'Att', iDefault = 0) }, { }, sendPFMsg = True)
    cl_action.AddIgnoreTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
    if skill.m_Cache['AttDistance'] == 0:
        for i1 in range(0, skill.m_Cache['MaxCover'], 1):
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = i1)
        
    else:
        for i2 in range(0, skill.m_Cache['MaxCover'], 1):
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = i2)
        


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.clientactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE

class CPerform(CCustomPerform):
    m_SID = 12022
    m_Name = '秘能觉醒元素之环二-火球'
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
        'ChargeTime': 0,
        'MaxCover': 1 }
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'Att': 100,
        'CrazyEff': 20000,
        'DebuffProb': 1200 }

