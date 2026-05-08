# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39249.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39249.pyc
# Source Generated with Decompyle++
# File: p39249.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, FlyingMuzzleCartoon, RayCastCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, CRT_LINELOCK, OBJ_ALL, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_LSTINTSPECIAL, SKILLCACHE_LSTPOS, SKILLCACHE_RANDOM
from cl_only import PY_FLAG_EXCLUDEMONSTERHATE, PY_FLAG_MONSTERTARGET

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
        CCartoon10.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 15, cl_action.GetSkillCustomData(skill, 'number', defaultValue = 0))

    InitSuccess = classmethod(InitSuccess)


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
            'Att': 40 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 11), (0, 0, 0), [
                4 if cl_action.CheckHasState(skill, 7999) else 2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon11(RayCastCartoon):
    m_SID = 11
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 20 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 5), cl_action.GetEndPositionInCrt(skill, 5), cl_action.GetVct3LstSubscript(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS), 0), 99, 100, 60, targettype = OBJ_ENEMY, liveTime = 0, radius = 0.1, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(FlyingMuzzleCartoon):
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
        if cl_action.GetSkillCustomData(skill, 'change', defaultValue = 0) == 1:
            cl_action.SetSkillVarCache(skill, 'skilltarget', cl_action.GetRandomLivePlayer(skill, 360, bNotContainDying = True, fMaxDis = 0, bSkillVIDSecond = False, iFlag = PY_FLAG_EXCLUDEMONSTERHATE, bResetVID = True))
            if cl_action.CheckTargetAlive(skill, cl_action.GetSkillVarCache(skill, 'skilltarget')):
                cl_action.SetSkillVictim(skill, cl_action.GetSkillVarCache(skill, 'skilltarget'))
                cl_action.ChangeFlyingMuzzleTarget(skill, 5, cl_action.GetSkillVarCache(skill, 'skilltarget'))
                cl_action.SetSkillVarCache(skill, 'number', 1)
                cl_action.SetSkillCacheData(skill, SKILLCACHE_RANDOM, len(cl_action.GetSummonPosByBoxSplit(skill, 8, 8, 0.1, False, {
                    cl_action.GetSkillVarCache(skill, 'number'): 1 }, { }, True, iAngle = 0)))
                cl_action.ServerSendSkillCache(skill, [
                    SKILLCACHE_RANDOM])
                if not cl_action.GetSkillCacheData(skill, SKILLCACHE_RANDOM) == 0:
                    cl_action.SetSkillVarCache(skill, 'lstpos', cl_action.ChangePosListToCloseGround(skill, cl_action.GetSummonPosByBoxSplit(skill, 8, 8, 0.1, False, {
                        cl_action.GetSkillVarCache(skill, 'number'): 1 }, { }, True, iAngle = 0)))
                    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillVarCache(skill, 'lstpos'))
                    cl_action.ServerSendSkillCache(skill, [
                        SKILLCACHE_LSTPOS])
                    cl_action.SetSkillServerCache(skill, 'index', 0)
                    cartoon = { }
                    CCartoon11.Init(skill, cartoon, casting = 1, index = 0)
        elif cl_action.CheckTargetAlive(skill, cl_action.GetIntLstSubscript(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL), cl_action.GetCartoonLoopID(skill, 5))):
            cl_action.SetSkillVictim(skill, cl_action.GetIntLstSubscript(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL), cl_action.GetCartoonLoopID(skill, 5)))
            cl_action.SetSkillVarCache(skill, 'number', 1)
            cl_action.SetSkillCacheData(skill, SKILLCACHE_RANDOM, len(cl_action.GetSummonPosByBoxSplit(skill, 8, 8, 0.1, False, {
                cl_action.GetSkillVarCache(skill, 'number'): 1 }, { }, True, iAngle = 0)))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_RANDOM])
            if not cl_action.GetSkillCacheData(skill, SKILLCACHE_RANDOM) == 0:
                cl_action.SetSkillVarCache(skill, 'lstpos', cl_action.ChangePosListToCloseGround(skill, cl_action.GetSummonPosByBoxSplit(skill, 8, 8, 0.1, False, {
                    cl_action.GetSkillVarCache(skill, 'number'): 1 }, { }, True, iAngle = 0)))
                cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillVarCache(skill, 'lstpos'))
                cl_action.ServerSendSkillCache(skill, [
                    SKILLCACHE_LSTPOS])
                cl_action.SetSkillServerCache(skill, 'index', 0)
                cartoon = { }
                CCartoon11.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cl_action.SetSkillVarCache(skill, 'skilltarget', cl_action.GetRandomLivePlayer(skill, 360, bNotContainDying = True, fMaxDis = 0, bSkillVIDSecond = False, iFlag = PY_FLAG_EXCLUDEMONSTERHATE, bResetVID = True))
                if cl_action.CheckTargetAlive(skill, cl_action.GetSkillVarCache(skill, 'skilltarget')):
                    cl_action.SetSkillVictim(skill, cl_action.GetSkillVarCache(skill, 'skilltarget'))
                    cl_action.ChangeFlyingMuzzleTarget(skill, 5, cl_action.GetSkillVarCache(skill, 'skilltarget'))
                    cl_action.SetSkillVarCache(skill, 'number', 1)
                    cl_action.SetSkillCacheData(skill, SKILLCACHE_RANDOM, len(cl_action.GetSummonPosByBoxSplit(skill, 8, 8, 0.1, False, {
                        cl_action.GetSkillVarCache(skill, 'number'): 1 }, { }, True, iAngle = 0)))
                    cl_action.ServerSendSkillCache(skill, [
                        SKILLCACHE_RANDOM])
                    if not cl_action.GetSkillCacheData(skill, SKILLCACHE_RANDOM) == 0:
                        cl_action.SetSkillVarCache(skill, 'lstpos', cl_action.ChangePosListToCloseGround(skill, cl_action.GetSummonPosByBoxSplit(skill, 8, 8, 0.1, False, {
                            cl_action.GetSkillVarCache(skill, 'number'): 1 }, { }, True, iAngle = 0)))
                        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillVarCache(skill, 'lstpos'))
                        cl_action.ServerSendSkillCache(skill, [
                            SKILLCACHE_LSTPOS])
                        cl_action.SetSkillServerCache(skill, 'index', 0)
                        cartoon = { }
                        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            if cl_action.GetPlayRound(skill) > 1:
                if cl_action.GetPlayRound(skill) > 2:
                    pass
                
            
            if cl_action.GetPlayRound(skill) > 1:
                if cl_action.GetPlayRound(skill) > 2:
                    pass
                
            
            cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'randomstart')[cl_action.GetSkillVarCache(skill, 'xlist')[cl_action.GetCartoonLoopID(skill, 5)]])(cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'randomstart')[cl_action.GetSkillVarCache(skill, 'xlist')[cl_action.GetCartoonLoopID(skill, 5)]]), 30, 35, cl_math.Vec3Minus(cl_action.CrtArgWarriorPos(skill, cl_action.GetIntLstSubscript(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL), cl_action.GetTimerCartoonCurTimes(skill, 0) + -1)), cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'randomstart')[cl_action.GetSkillVarCache(skill, 'xlist')[cl_action.GetCartoonLoopID(skill, 5)]])), 20, 60, 70, 600, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 0, 0, cl_action.GetIntLstSubscript(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL), cl_action.GetTimerCartoonCurTimes(skill, 0) + -1), CRT_LINELOCK, (0, 0, 0), cl_action.CrtArgWarriorPos(skill, cl_action.GetIntLstSubscript(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL), cl_action.GetTimerCartoonCurTimes(skill, 0) + -1)))

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
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = cl_action.GetTimerCartoonCurTimes(skill, 0) + -1)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 15, cl_action.GetSkillVarCache(skill, 'looptimes'))

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
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
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 35, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
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
        2: 1 }, cl_action.GetSkillCustomData(skill, 'number', defaultValue = 0)))
    cl_action.SetSkillVarCache(skill, 'muzzle', cl_action.GetMonsterMuzzlePos(skill, (0, 0, 0)))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillVarCache(skill, 'model'))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL, cl_action.GetAllHeroIDByPyFlag(skill, PY_FLAG_MONSTERTARGET))
    cl_action.SetSkillVarCache(skill, 'looptimes', len(cl_action.GetAllHeroIDByPyFlag(skill, PY_FLAG_MONSTERTARGET)) if cl_action.GetSkillCustomData(skill, 'number', defaultValue = 0) > len(cl_action.GetAllHeroIDByPyFlag(skill, PY_FLAG_MONSTERTARGET)) else cl_action.GetSkillCustomData(skill, 'number', defaultValue = 0))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'time', defaultValue = 0))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTINTSPECIAL,
        SKILLCACHE_INT])
    if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)) > 0:
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTINTSPECIAL,
        SKILLCACHE_LSTPOS,
        SKILLCACHE_RANDOM]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39249
    m_Name = '妖王-单体混沌'
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
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_Resend = 1
    m_CacheAttr = [
        'DebuffProb']

