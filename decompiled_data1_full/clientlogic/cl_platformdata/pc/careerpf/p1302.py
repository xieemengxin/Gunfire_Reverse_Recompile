# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1302.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1302.pyc
# Source Generated with Decompyle++
# File: p1302.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, HIT_OVER_NORMAL, OBJ_ENEMY, SKILLCACHE_RANDOM

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.VictimAddState(skill, 32101, skill.m_Cache['AddStateTime'], 0, { })
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] })

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
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = cl_action.CheckHasTalent(skill, 2103), explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 1), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = cl_action.CheckHasTalent(skill, 2103), explosion = False, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon11(DirectPosCartoon):
    m_SID = 11
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.VictimAddState(skill, 32101, skill.m_Cache['AddStateTime'], 0, { })
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCartoonHitPosLst(skill, 1)[cl_action.GetCartoonLoopID(skill, 0)], end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = cl_action.CheckHasTalent(skill, 2103), explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetCartoonHitPosLst(skill, 1)[cl_action.GetCartoonLoopID(skill, 0)], (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = cl_action.CheckHasTalent(skill, 2103), explosion = False, extCheck = CRT_EXTCHECK_NONE)

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
        if cl_action.CheckHasTalent(skill, 5004):
            cartoon = { }
            CCartoon11.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 50, 1 if cl_action.CheckSkillRandomInRange(skill, 51, 100) else 0)
        elif cl_action.CheckSkillRandomInRange(skill, 61, 100):
            pass
        
        skill(50, 1, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(DirectPosCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.VictimAddState(skill, 32101, skill.m_Cache['AddStateTime'], 0, { })
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCartoonHitPosLst(skill, 1)[cl_action.GetCartoonLoopID(skill, 5)], end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = cl_action.CheckHasTalent(skill, 2103), explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetCartoonHitPosLst(skill, 1)[cl_action.GetCartoonLoopID(skill, 5)], (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = cl_action.CheckHasTalent(skill, 2103), explosion = False, extCheck = CRT_EXTCHECK_NONE)

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
        if cl_action.CheckHasTalent(skill, 5004):
            cartoon = { }
            CCartoon8.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 50, 1 if cl_action.CheckSkillRandomInRange(skill, 51, 100) else 2 if cl_action.CheckSkillRandomInRange(skill, 31, 50) else 0)
        else:
            cls.EnableCtrl(skill, 50, 1 if cl_action.CheckSkillRandomInRange(skill, 51, 100) else 2 if cl_action.CheckSkillRandomInRange(skill, 31, 50) else 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(DirectPosCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.VictimAddState(skill, 32101, skill.m_Cache['AddStateTime'], 0, { })
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCartoonHitPosLst(skill, 1)[cl_action.GetCartoonLoopID(skill, 6)], end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = cl_action.CheckHasTalent(skill, 2103), explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetCartoonHitPosLst(skill, 1)[cl_action.GetCartoonLoopID(skill, 6)], (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = cl_action.CheckHasTalent(skill, 2103), explosion = False, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
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
        if cl_action.CheckHasTalent(skill, 5004):
            cartoon = { }
            CCartoon9.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 50, 1 if cl_action.CheckSkillRandomInRange(skill, 51, 100) else 2 if cl_action.CheckSkillRandomInRange(skill, 16, 50) else 3 if cl_action.CheckSkillRandomInRange(skill, 1, 15) else 0)
        else:
            cls.EnableCtrl(skill, 50, 1 if cl_action.CheckSkillRandomInRange(skill, 51, 100) else 2 if cl_action.CheckSkillRandomInRange(skill, 16, 50) else 3 if cl_action.CheckSkillRandomInRange(skill, 1, 15) else 0)

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
        if cl_action.CheckHasTalent(skill, 2105):
            if cl_action.GetTalentLevel(skill, 2105) == 1 or (1 if cl_action.CheckSkillRandomInRange(skill, 51, 100) else 0) > 0:
                cartoon = { }
                CCartoon0.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonHitTimes(skill, 1) - 1)
            elif cl_action.GetTalentLevel(skill, 2105) == 2 or (1 if cl_action.CheckSkillRandomInRange(skill, 51, 100) else 2 if cl_action.CheckSkillRandomInRange(skill, 31, 50) else 0) > 0:
                cartoon = { }
                CCartoon5.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonHitTimes(skill, 1) - 1)
            elif cl_action.GetTalentLevel(skill, 2105) == 3 and (1 if cl_action.CheckSkillRandomInRange(skill, 51, 100) else 2 if cl_action.CheckSkillRandomInRange(skill, 16, 50) else 3 if cl_action.CheckSkillRandomInRange(skill, 1, 15) else 0) > 0:
                cartoon = { }
                CCartoon6.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonHitTimes(skill, 1) - 1)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)
        if cl_action.CheckHasTalent(skill, 2105):
            if cl_action.GetTalentLevel(skill, 2105) == 1 or (1 if cl_action.CheckSkillRandomInRange(skill, 51, 100) else 0) > 0:
                cartoon = { }
                CCartoon0.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonHitTimes(skill, 1) - 1)
            elif cl_action.GetTalentLevel(skill, 2105) == 2 or (1 if cl_action.CheckSkillRandomInRange(skill, 51, 100) else 2 if cl_action.CheckSkillRandomInRange(skill, 31, 50) else 0) > 0:
                cartoon = { }
                CCartoon5.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonHitTimes(skill, 1) - 1)
            elif cl_action.GetTalentLevel(skill, 2105) == 3 and (1 if cl_action.CheckSkillRandomInRange(skill, 51, 100) else 2 if cl_action.CheckSkillRandomInRange(skill, 16, 50) else 3 if cl_action.CheckSkillRandomInRange(skill, 1, 15) else 0) > 0:
                cartoon = { }
                CCartoon6.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonHitTimes(skill, 1) - 1)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (-0.3, 0, 1.5))):
                return None
            cls.EnableShow(skill, 1, (0, 0, 0), (0.2, 0.2), skill.m_Cache['ExplodeDelay'], True, True, 0, innerRadius = 0.05, pierce = skill.m_Cache['Pierce'], ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, iTriggerBullet = 0)
        else:
            cls.EnableCtrl(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (-0.3, 0, 1.5)), cl_action.CrtArgGetCustomDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), cl_action.GetSceneCenterPosition(skill, cartoon), cl_math.Vec3Add((0, (cl_action.GetSkillVarCache(skill, 'index') - 1) * 15, 0), (0, 0, 0))), skill.m_Cache['BulletSpeed'], 1, (0, 0, 0), (0.2, 0.2), skill.m_Cache['ExplodeDelay'], True, True, cl_action.ObjectBranchBySkillElementType(skill, None, None, None, None), 0, cl_action.ObjectBranchBySkillElementType(skill, None, None, None, None), 1, innerRadius = 0.05, pierce = skill.m_Cache['Pierce'], ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, ignorePetrochemical = False)

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
        if cl_action.CheckHasBenediction(skill, 13504):
            for i1 in range(0, 3, 1):
                cl_action.SetSkillVarCache(skill, 'index', i1)
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
            
        else:
            cl_action.SetSkillVarCache(skill, 'index', 1)
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 25, 1)
        else:
            cls.EnableCtrl(skill, 25, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
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
            cls.EnableShow(skill, 15, 1)
        else:
            cls.EnableCtrl(skill, 15, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 60, 1)
        else:
            cls.EnableCtrl(skill, 60, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseCareerPFMsg(skill)
    cartoon = { }
    CCartoon4.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_RANDOM]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1302
    m_Name = '源力法球'
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
        'ColdTime': 1500,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 200,
        'Att': 40000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 10000,
        'ExplodeDelay': 280,
        'Radius': 3,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1013
    m_AIPerformDam = 3000

