# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39047.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39047.pyc
# Source Generated with Decompyle++
# File: p39047.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateThrowCartoon, DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, DAM_USE_HP, OBJ_ALL, OBJ_ENEMY, SKILLCACHE_CHARGELEVEL, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_LSTPOS, WARRIOR_BUILD

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
        cl_action.AddClientEffect(skill, 2023, cl_action.VectorShiftForAttDir(skill, cl_action.GetMonsterMuzzlePos(skill, (0, 0, 0)), cl_action.GetSkillVarCache(skill, 'LaunchStartPosList')[cl_action.GetCartoonLoopID(skill, 3)]), 200, (0, 0, 0))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_BUILD, OBJ_ALL) or cl_action.CheckVictimSID(skill, 1185):
            cl_action.ChangeVictimDefValue(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * cl_action.GetPerformArgValue(skill, 'buildatk', iDefault = 10) * -0.01), DAM_USE_HP)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 50 }, { }, sendPFMsg = False)

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
                3.1], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(DelegateThrowCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.AddClientEffect(skill, 0, cl_action.GetSkillVarCache(skill, 'LaunchEndPosList'), 100, (0, 0, 0))
        cl_action.AddClientEffect(skill, 2025, cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'LaunchStartPosList')[cl_action.ToInt(skill, cl_action.ToInt(skill, (cl_action.GetTimerCartoonCurTimes(skill, 4) + cl_action.GetSkillVarCache(skill, 'RandomLR')[cl_action.GetCartoonLoopID(skill, 0)]) % 2) + cl_action.GetCartoonLoopID(skill, 0) * 2)]), 200, cl_action.CrtArgGetCustomDir(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'LaunchStartPosList')[cl_action.ToInt(skill, cl_action.ToInt(skill, (cl_action.GetTimerCartoonCurTimes(skill, 4) + cl_action.GetSkillVarCache(skill, 'RandomLR')[cl_action.GetCartoonLoopID(skill, 0)]) % 2) + cl_action.GetCartoonLoopID(skill, 0) * 2)]), cl_action.GetSkillVarCache(skill, 'LaunchEndPosList'), (0, 0, 0), baseHorizontal = False))

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
    
    def InitSuccess(cls, skill, i2, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'LaunchStartPosList')[cl_action.ToInt(skill, cl_action.ToInt(skill, (cl_action.GetTimerCartoonCurTimes(skill, 4) + cl_action.GetSkillVarCache(skill, 'RandomLR')[cl_action.GetCartoonLoopID(skill, 0)]) % 2) + cl_action.GetCartoonLoopID(skill, 0) * 2)]), cl_action.CrtArgGetCustomDir(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetSkillVarCache(skill, 'muzzle'), cl_action.GetSkillVarCache(skill, 'LaunchStartPosList')[cl_action.ToInt(skill, cl_action.ToInt(skill, (cl_action.GetTimerCartoonCurTimes(skill, 4) + cl_action.GetSkillVarCache(skill, 'RandomLR')[cl_action.GetCartoonLoopID(skill, 0)]) % 2) + cl_action.GetCartoonLoopID(skill, 0) * 2)]), cl_action.GetSkillVarCache(skill, 'LaunchEndPosList'), (0, 0, 0), baseHorizontal = False), 110 if cl_action.GetMonsterPhase(skill) >= 3 else 110, 0.3, (0, 18, 0), (0.5, 0.5), 0, True, liveTime = 0, innerRadius = 0.2, pierce = 1)

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
        for i2 in range(0, len(cl_action.GetSkillVarCache(skill, 'RandomLR')), 1):
            if len(cl_action.GetSkillCustomData(skill, 'HeroDir', defaultValue = [])) == 0:
                cl_action.SetSkillVarCache(skill, 'muzzle', cl_action.GetMonsterMuzzlePos(skill, (0, 0, 0)))
                cartoon = { }
                CCartoon0.Init(skill, cartoon, casting = 0, index = i2)
                continue
            cl_action.SetSkillVarCache(skill, 'LaunchEndPosList', cl_action.ChangePosListToCloseGround(skill, [
                cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetSkillCustomData(skill, 'HeroDir', defaultValue = [])[i2], cl_action.GetTimerCartoonCurTimes(skill, 4) * 2.2 + 30, 0), cl_action.GetSkillCustomData(skill, 'HeroDir', defaultValue = [])[i2], 3.35, cl_action.ToInt(skill, 90 * (1 if cl_action.ToInt(skill, (cl_action.GetTimerCartoonCurTimes(skill, 4) + cl_action.GetSkillVarCache(skill, 'RandomLR')[i2]) % 2) == 0 else -1)))])[0])
            cl_action.SetSkillVarCache(skill, 'muzzle', cl_action.GetMonsterMuzzlePos(skill, (0, 0, 0)))
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i2)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 35, cl_action.ToInt(skill, 6.77419 + cl_action.ToInt(skill, 6.27419)))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_CHARGELEVEL, 1)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'LaunchCnt', defaultValue = 0))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillCustomData(skill, 'LaunchStartPosList', defaultValue = []))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.CrtArgRandomIntList(skill, 0, 1, len(cl_action.GetSkillCustomData(skill, 'HeroDir', defaultValue = []))))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_INT,
        SKILLCACHE_LSTPOS,
        SKILLCACHE_LSTINT])
    cl_action.SetSkillVarCache(skill, 'LaunchStartPosList', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS))
    cl_action.SetSkillVarCache(skill, 'RandomLR', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT))
    for i1 in range(0, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 1):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = i1)
    
    cartoon = { }
    CCartoon4.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_CHARGELEVEL,
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39047
    m_Name = '罗睺扫射激光射击'
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
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_FIRE
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_BaseArgData = {
        'buildatk': 10 }
    m_Resend = 1
    m_CacheAttr = [
        'DebuffProb']

