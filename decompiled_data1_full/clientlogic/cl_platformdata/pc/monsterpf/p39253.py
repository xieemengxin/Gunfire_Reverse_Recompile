# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39253.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39253.pyc
# Source Generated with Decompyle++
# File: p39253.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, RayCastCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_INT

class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        if cl_action.CrtArgRandomNum(skill, 0, 100) > 50:
            cl_action.SendCurCartoonTriggerMsg(skill)

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
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 0), (0, 0, 0), [
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

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
        if cl_action.CrtArgRandomNum(skill, 0, 100) > 50:
            cl_action.SendCurCartoonTriggerMsg(skill)
            cl_action.WeaponDamage(skill, {
                'Att': 40 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'randomstart')[cl_action.GetSkillVarCache(skill, 'index')], cl_action.GetSkillVarCache(skill, 'randomstart')[cl_action.GetSkillVarCache(skill, 'index')], cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillVarCache(skill, 'lsthero')[i1]), 1, 200, 90, targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = None, effectLiveTime = 0, radius = 0.1, flyoverdis = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        if cl_action.CrtArgRandomNum(skill, 0, 100) > 50:
            cl_action.SendCurCartoonTriggerMsg(skill)

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
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 8), (0, 0, 0), [
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(RayCastCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CrtArgRandomNum(skill, 0, 100) > 50:
            cl_action.SendCurCartoonTriggerMsg(skill)
            cl_action.WeaponDamage(skill, {
                'Att': 40 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i2, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'randomstart')[cl_action.GetSkillVarCache(skill, 'randomnumber')], cl_action.GetSkillVarCache(skill, 'randomstart')[cl_action.GetSkillVarCache(skill, 'randomnumber')], cl_action.GetSkillVarCache(skill, 'lstpos')[i2], 1, 200, 90, targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = 0, effectLiveTime = 0, radius = 0.1, flyoverdis = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'randomstart', [
        (1537.5, 575.4, 1369.41),
        (1486.8, 575.4, 1301.1),
        (1483.6, 567.4, 1218),
        (1739.9, 575.4, 1323.9),
        (1740.2, 578.7, 1252.9),
        (1732.8, 575.3, 1218)])
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, 0)
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_INT])
    if 0 == cl_action.GetSkillCacheData(skill, SKILLCACHE_INT):
        cl_action.SetSkillVarCache(skill, 'lsthero', cl_action.GetLiveHeroID(skill, False))
        for i1 in range(0, len(cl_action.GetSkillVarCache(skill, 'lsthero')), 1):
            cl_action.SetSkillVarCache(skill, 'index', cl_action.CrtArgRandomNum(skill, 0, 5))
            cl_action.AddClientEffect(skill, 1023, cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillVarCache(skill, 'lsthero')[i1]), time = 500)
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
        
    else:
        cl_action.SetSkillVarCache(skill, 'lstpos', cl_action.GetListByShuffleAndNumber(skill, cl_action.CreateRectanglePosList(skill, (1610.38, 500.31, 1263.58), (60, 0, 60), 144, 4, 0), 2))
        for i2 in range(0, len(cl_action.GetSkillVarCache(skill, 'lstpos')), 1):
            cl_action.SetSkillVarCache(skill, 'randomnumber', cl_action.CrtArgRandomNum(skill, 0, 5))
            cl_action.AddClientEffect(skill, 1023, cl_action.GetSkillVarCache(skill, 'lstpos')[i2], time = 500)
            cartoon = { }
            CCartoon8.Init(skill, cartoon, casting = 0, index = i2)
        


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39253
    m_Name = '美术测试-妖王-混沌之雨无怪'
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
    m_CacheAttr = [
        'DebuffProb']

