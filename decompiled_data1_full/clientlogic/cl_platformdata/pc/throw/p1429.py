# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p1429.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p1429.pyc
# Source Generated with Decompyle++
# File: p1429.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, HIT_OVER_NORMAL, OBJ_ALL, OBJ_ENEMY, OBJ_FRIEND, WARRIOR_MONSTER

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimSideType(skill, OBJ_ENEMY):
            if cl_action.CheckMonsterType(skill, WARRIOR_MONSTER, cl_action.GetCurVID(skill)):
                cl_action.VictimAddState(skill, 1860, cl_action.GetPerformArgValue(skill, 'SlowDownTime', iDefault = 200), 0, { })
                cl_action.PerformDamage(skill, {
                    'Att': skill.m_Cache['Att'] })
            else:
                cl_action.PerformDamage(skill, {
                    'Att': skill.m_Cache['Att'] })
        elif cl_action.GetSkillCustomData(skill, 'HasP3518', defaultValue = False) and cl_action.CheckVictimSideType(skill, OBJ_FRIEND):
            cl_action.VictimAddState(skill, 33041, 500, 0, {
                'TalentLevel': cl_action.GetSkillCustomData(skill, '3518PFLV', defaultValue = 1) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_math.Vec3Add(cl_action.GetEndPositionInCrt(skill, 1), (0, 0.1, 0)), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = True, multipleExplode = True, explosionDelay = 0)
        else:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.GetEndPositionInCrt(skill, 1), (0, 0.1, 0)), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = True, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(ThrowByPowerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0.1, 0.7))):
                return None
            cls.EnableShow(skill, 0.1, (0, skill.m_Cache['BulletVerticalAcc'], 0), (0.3, 0.3), skill.m_Cache['ExplodeDelay'], True, True, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, iTriggerBullet = 0, checkWeaknessAngle = 0, checkWeaknessDis = 0)
        else:
            cls.EnableCtrl(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0.1, 0.7)), cl_action.CrtArgGetCustomDir(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0.1, 0.7)), cl_action.GetSceneCenterPosition(skill, cartoon), cl_math.Vec3Add((0, (cl_action.GetSkillVarCache(skill, 'index') - 1) * 15, 0), (3, 0, 0)), baseHorizontal = False), skill.m_Cache['BulletSpeed'], 0.1, (0, skill.m_Cache['BulletVerticalAcc'], 0), (0.3, 0.3), skill.m_Cache['ExplodeDelay'], True, True, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, ignorePetrochemical = False, iTriggerBullet = 0, ignoreShield = False, checkWeaknessAngle = 0, checkWeaknessDis = 0, canPierceWeakness = False, hitFallAcc = 0, verticalThreshold = 0.7)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        if skill.m_Cache['Pierce'] <= 1:
            cl_action.SetSkillVarCache(skill, 'index', 1)
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        else:
            for i2 in range(0, skill.m_Cache['Pierce'], 1):
                cl_action.SetSkillVarCache(skill, 'index', i2)
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
            

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
        if skill.m_Cache['Pierce'] <= 1:
            cl_action.SetSkillVarCache(skill, 'index', 1)
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        else:
            for i3 in range(0, skill.m_Cache['Pierce'], 1):
                cl_action.SetSkillVarCache(skill, 'index', i3)
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
            

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 5, skill.m_Cache['TriggerTimes'] - 1)
        else:
            cls.EnableCtrl(skill, 5, skill.m_Cache['TriggerTimes'] - 1)

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
        if 1 == skill.m_Cache['TriggerTimes']:
            if skill.m_Cache['Pierce'] <= 1:
                cl_action.SetSkillVarCache(skill, 'index', 1)
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
            else:
                for i1 in range(0, skill.m_Cache['Pierce'], 1):
                    cl_action.SetSkillVarCache(skill, 'index', i1)
                    cartoon = { }
                    CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
                
        else:
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 10, 1)
        else:
            cls.EnableCtrl(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 20, 1)
        else:
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseThrowPFMsg(skill)
    cl_action.CachePFTransDamFactor(skill, 300)
    cartoon = { }
    CCartoon4.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1429
    m_Name = '霜冻手雷'
    m_ExtPerform = (8010, 8015, 1432, 1433)
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
        'ColdTime': 50,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 4508,
        'Att': 50000,
        'CrazyEff': 0,
        'BulletSpeed': 45,
        'DebuffProb': 1500,
        'ExplodeDelay': 500,
        'Radius': 5,
        'BulletVerticalAcc': 0,
        'AddStateTime': 300,
        'KeepTime': 300,
        'DamInterval': 100,
        'Pierce': 1,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1010
    m_BaseArgData = {
        'SlowDownTime': 200 }
    m_AIPerformDam = 2000

