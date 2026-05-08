# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39244.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39244.pyc
# Source Generated with Decompyle++
# File: p39244.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateCurveCartoon, DirectPosCartoon, FlyingMuzzleCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, CRT_LINELOCK, OBJ_ALL, OBJ_ENEMY, SKILLCACHE_LSTINT

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            if cl_action.GetPlayRound(skill) > 1:
                if cl_action.GetPlayRound(skill) > 2:
                    pass
                
            
            if cl_action.GetPlayRound(skill) > 1:
                if cl_action.GetPlayRound(skill) > 2:
                    pass
                
            
            cl_action.ToInt(skill, 40 + (8 if cl_action.CheckHasState(skill, 7999) else 4) * 20 + 60(60 + 70, 30 + 35), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

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
        cl_action.AttackerAddState(skill, 8027, 0, 0, { })

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            if cl_action.GetPlayRound(skill) > 1:
                if cl_action.GetPlayRound(skill) > 2:
                    pass
                
            
            if cl_action.GetPlayRound(skill) > 1:
                if cl_action.GetPlayRound(skill) > 2:
                    pass
                
            
            cl_action.ToInt(skill, 40 + (8 if cl_action.CheckHasState(skill, 7999) else 4) * 20 + 60(60 + 70, 30 + 35 + 100), 1)

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
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'randomstart')[cl_action.GetSkillVarCache(skill, 'xlist')[i1]]), cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'randomstart')[cl_action.GetSkillVarCache(skill, 'xlist')[i1]]), [
                1], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon11(TimerCartoon):
    m_SID = 11
    
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
        for i1 in range(0, 4, 1):
            cartoon = { }
            CCartoon8.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            if cl_action.GetPlayRound(skill) > 1:
                if cl_action.GetPlayRound(skill) > 2:
                    pass
                
            
            skill(cl_action.ToInt, skill(40 + (8 if cl_action.CheckHasState(skill, 7999) else 4) * 20, 60 + 70 + 60 + 16), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(DirectPosCartoon):
    m_SID = 10
    
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
            cls.EnableCtrl(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'randomstart')[cl_action.GetSkillVarCache(skill, 'xlist')[cl_action.GetTimerCartoonCurTimes(skill, 6) + -1]]), cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'randomstart')[cl_action.GetSkillVarCache(skill, 'xlist')[cl_action.GetTimerCartoonCurTimes(skill, 6) + -1]]), [
                1], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

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
        CCartoon10.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 10, 4)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
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
            if cl_action.GetPlayRound(skill) > 1:
                if cl_action.GetPlayRound(skill) > 2:
                    pass
                
            
            if cl_action.GetPlayRound(skill) > 1:
                if cl_action.GetPlayRound(skill) > 2:
                    pass
                
            
            cl_action.ToInt(skill, 30(35, 60 + 70), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(DelegateCurveCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 15 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetCartoonEnd(skill, 5), cl_action.CrtArgBodyPos(skill, 0, 0, 0, 0), 1, 100, 60, 18 if cl_action.CheckHasState(skill, 7999) else 12, 0.6, targettype = OBJ_ENEMY, liveTime = 0, defLockPos = (0, 0, 0), weakdis = 0, weakangle = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(FlyingMuzzleCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

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
        if cl_action.CheckTargetAlive(skill, cl_action.GetSkillVID(skill)):
            cartoon = { }
            CCartoon9.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.SkillHaltSelf(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            if cl_action.GetPlayRound(skill) > 1:
                if cl_action.GetPlayRound(skill) > 2:
                    pass
                
            
            if cl_action.GetPlayRound(skill) > 1:
                if cl_action.GetPlayRound(skill) > 2:
                    pass
                
            
            cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'randomstart')[cl_action.GetSkillVarCache(skill, 'xlist')[cl_action.GetCartoonLoopID(skill, 5)]])(cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'randomstart')[cl_action.GetSkillVarCache(skill, 'xlist')[cl_action.GetCartoonLoopID(skill, 5)]]), 30, 35, cl_math.Vec3Minus(cl_action.CrtArgTargetPos(skill, notContainDying = False), cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'randomstart')[cl_action.GetSkillVarCache(skill, 'xlist')[cl_action.GetCartoonLoopID(skill, 5)]])), (4 - cl_action.GetTimerCartoonCurTimes(skill, 7)) * 10 + 60, 60, 70, 8 if cl_action.CheckHasState(skill, 7999) else 4, 20, 0, 0, cl_action.GetSkillVID(skill), CRT_LINELOCK, (0, 0, 0), cl_action.CrtArgTargetPos(skill, notContainDying = False))

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
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
        CCartoon5.Init(skill, cartoon, casting = 1, index = cl_action.GetTimerCartoonCurTimes(skill, 7) + -1)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 10, 4)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

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
        CCartoon7.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 35, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
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
        cl_action.SetSkillVarCache(skill, 'xlist', cl_action.RandomNumberList(skill, 8, 7))
        cl_action.SetSkillVarCache(skill, 'randomstart', [
            (-1.39, 8.9, -0.74),
            (-4.75, 6.81, 3.34),
            (4.26, 5.72, 1.35),
            (2.43, 9.39, -1.15),
            (-4.51, 9.93, 1.08),
            (0.85, 10.58, -2.5),
            (-7.47, 6.11, -0.74),
            (4.21, 10.44, 0.83)])
        cl_action.SetSkillVarCache(skill, 'model', cl_action.CreateWarriorList(skill, {
            0: 1,
            1: 1,
            2: 1 }, {
            0: 1,
            1: 1,
            2: 1 }, 4))
        cl_action.SetSkillVarCache(skill, 'muzzle', cl_action.GetMonsterMuzzlePos(skill, (0, 0, 0)))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillVarCache(skill, 'model'))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_LSTINT])
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'perform', cl_action.GetMonsterPerformRecord(skill, 39244))
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, FAR_DISTANCE, MONSTERPF_TYPE_OTHER

class CPerform(CCustomPerform):
    m_SID = 39244
    m_Name = '妖王-混沌之雨'
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
        'ColdTime': 300,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = FAR_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

