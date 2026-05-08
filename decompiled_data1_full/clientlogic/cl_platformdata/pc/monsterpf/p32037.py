# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p32037.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p32037.pyc
# Source Generated with Decompyle++
# File: p32037.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, RayCastCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT

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
            'Att': 100 }, { }, sendPFMsg = False)

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
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 5)

    InitSuccess = classmethod(InitSuccess)


class CCartoon14(DirectPosCartoon):
    m_SID = 14
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 25 }, { }, sendPFMsg = False)

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
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 5)

    InitSuccess = classmethod(InitSuccess)


class CCartoon13(TimerCartoon):
    m_SID = 13
    
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
        CCartoon14.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 7)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon13.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)

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
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 5)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(RayCastCartoon):
    m_SID = 0
    
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
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i2, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'PosList')[i2], (0, cl_action.GetSkillVarCache(skill, 'HightList')[i2], 0)), cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'PosList')[i2], (0, cl_action.GetSkillVarCache(skill, 'HightList')[i2], 0)), cl_action.GetSkillVarCache(skill, 'PosList')[i2], 1, 200, 80, targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = None, effectLiveTime = 0, radius = 0, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        for i2 in range(0, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 1):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i2)
        

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
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'PosList', cl_action.CreateAolongRectanglePosList(skill, 1045, 6, 4.3, 15, 20))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, len(cl_action.GetSkillVarCache(skill, 'PosList')))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_INT])
    cl_action.SetSkillVarCache(skill, 'HightList', [])
    cl_action.SetSkillVarCache(skill, 'HightList', cl_action.CrtArgRandomIntList(skill, 80, 120, len(cl_action.GetSkillVarCache(skill, 'PosList'))))
    for i1 in range(0, len(cl_action.GetSkillVarCache(skill, 'PosList')), 1):
        cl_action.AddClientEffect(skill, 1009, cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'PosList')[i1], (0, 0, 0)), cl_action.ToInt(skill, cl_action.GetSkillVarCache(skill, 'HightList')[i1] / 0.8 + 100), (0, 0, 0))
    
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 32037
    m_Name = '【第三幕】重型火炮兵开场轰炸'
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
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

