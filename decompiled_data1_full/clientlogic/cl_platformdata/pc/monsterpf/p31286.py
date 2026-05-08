# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p31286.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p31286.pyc
# Source Generated with Decompyle++
# File: p31286.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, GroundFlyCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, WARRIOR_SUMMON

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
        cl_action.MonsterTeleportToPos(skill, cl_action.GetEndPositionInCrt(skill, 5))
        cl_action.StartBackSwing(skill, 300)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(DirectPosCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.CreateRandomNumWarriorAtPointPos(skill, [
            cl_math.Vec3Add(cl_action.GetEndPositionInCrt(skill, 5), (0, 2, 0))], WARRIOR_SUMMON, {
            1063: 10 }, {
            'FollowDie': 1 })

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.AddClientEffect(skill, 1017, (0, 0, 0), 100, (0, 0, 0))
        cl_action.WeaponDamage(skill, {
            'Att': 80 }, { }, sendPFMsg = False)
        cl_action.PushHeroVictim(skill, (0, 0, 0), 9, 3, 10000, downSpeed = 4, fGravaty = 9.8, angle = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.AddClientEffect(skill, 1017, (0, 0, 0), 100, (0, 0, 0))
        cl_action.WeaponDamage(skill, {
            'Att': 80 }, { }, sendPFMsg = False)
        cl_action.PushHeroVictim(skill, (0, 0, 0), 9, 3, 10000, downSpeed = 4, fGravaty = 9.8, angle = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 1), (0, 0, 0), [
                3], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(GroundFlyCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.StartBackSwing(skill, 100)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgSelfFace(skill), 40, 60, 1, 45, tolerateRadius = 0.5, climbHeight = 0, targettype = OBJ_ENEMY, effect = 0, trailEffect = None, HitHero = True, pierceMonster = False)

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
        for i1 in range(0, 1, 1):
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.LockMonsterAttackerFace(skill)
    cl_action.UnlockMonsterAttackerFace(skill)
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

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 31286
    m_Name = '【第四幕】精英弱点怪-冰刃斩'
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
        'AttDistance': 25,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 1038
    m_CacheAttr = [
        'DebuffProb']

