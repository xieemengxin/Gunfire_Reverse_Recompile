# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p31284.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p31284.pyc
# Source Generated with Decompyle++
# File: p31284.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, RayCastCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_LSTPOS, WARRIOR_SUMMON

class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.CreateRandomNumWarriorAtPointPos(skill, [
            cl_math.Vec3Add(cl_action.GetEndPositionInCrt(skill, 0), (0, 2, 0))], WARRIOR_SUMMON, {
            1063: 10 }, {
            'FollowDie': 1 })

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.AddClientEffect(skill, 1017, (0, 0, 0), 100, (0, 0, 0))
        cl_action.WeaponDamage(skill, {
            'Att': 80 }, { }, sendPFMsg = False)
        cl_action.PushHeroVictim(skill, cl_action.GetEndPositionInCrt(skill, 0), 9, 3, 10000, downSpeed = 4, fGravaty = 9.8, angle = 0)
        cl_action.StartBackSwing(skill, 100)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.AddClientEffect(skill, 1017, (0, 0, 0), 100, (0, 0, 0))
        cl_action.WeaponDamage(skill, {
            'Att': 80 }, { }, sendPFMsg = False)
        cl_action.PushHeroVictim(skill, cl_action.GetEndPositionInCrt(skill, 0), 9, 3, 10000, downSpeed = 4, fGravaty = 9.8, angle = 0)
        cl_action.StartBackSwing(skill, 100)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 0), cl_action.GetEndPositionInCrt(skill, 0), [
                3], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(RayCastCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.CrtArgTargetPos(skill, notContainDying = False), (0, 15, 0)), cl_math.Vec3Add(cl_action.CrtArgTargetPos(skill, notContainDying = False), (0, 15, 0)), cl_action.CrtArgTargetPos(skill, notContainDying = False), 99, 30, 10, targettype = OBJ_ENEMY, liveTime = 0, radius = 0, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(DirectPosCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.CreateRandomNumWarriorAtPointPos(skill, [
            cl_math.Vec3Add(cl_action.GetEndPositionInCrt(skill, 2), (0, 2, 0))], WARRIOR_SUMMON, {
            1063: 10 }, {
            'FollowDie': 1 })

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.AddClientEffect(skill, 1017, (0, 0, 0), 100, (0, 0, 0))
        cl_action.WeaponDamage(skill, {
            'Att': 80 }, { }, sendPFMsg = False)
        cl_action.PushHeroVictim(skill, cl_action.GetEndPositionInCrt(skill, 2), 9, 3, 10000, downSpeed = 4, fGravaty = 9.8, angle = 0)
        cl_action.StartBackSwing(skill, 100)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.AddClientEffect(skill, 1017, (0, 0, 0), 100, (0, 0, 0))
        cl_action.WeaponDamage(skill, {
            'Att': 80 }, { }, sendPFMsg = False)
        cl_action.PushHeroVictim(skill, cl_action.GetEndPositionInCrt(skill, 2), 9, 3, 10000, downSpeed = 4, fGravaty = 9.8, angle = 0)
        cl_action.StartBackSwing(skill, 100)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 2), cl_action.GetEndPositionInCrt(skill, 2), [
                3], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(RayCastCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[i1], (0, 15, 0)), cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[i1], (0, 15, 0)), cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[i1], 99, 30, 10, targettype = OBJ_ENEMY, liveTime = 0, radius = 0, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'pos', cl_action.GetSummonPosByBoxSplit(skill, 16, 4, 1, False, {
        1: 10 }, { }, True, iAngle = 0))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillVarCache(skill, 'pos'))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_LSTPOS])
    cl_action.LockMonsterAttackerFace(skill)
    cl_action.UnlockMonsterAttackerFace(skill)
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
    for i1 in range(0, 1, 1):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = i1)
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 31284
    m_Name = '【第四幕】精英弱点怪-召唤冰刃'
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
        'ColdTime': 350,
        'AttDistance': 9,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 1038
    m_CacheAttr = [
        'DebuffProb']

