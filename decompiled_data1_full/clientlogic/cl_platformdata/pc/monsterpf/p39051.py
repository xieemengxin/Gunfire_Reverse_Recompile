# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39051.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39051.pyc
# Source Generated with Decompyle++
# File: p39051.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import EntityParabolaCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, WARRIOR_SUMMON

class CCartoon0(EntityParabolaCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetRigidbodySimulation(skill, cl_action.GetCartoonEntityID(skill, 0), False)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetCartoonEntityID(skill, 0), 3000)
        cl_action.WarriorUsePerform(skill, cl_action.GetCartoonEntityID(skill, 0), 39052, { }, True)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), (0, 0, -1), (40 if cl_action.GetPlayRound(skill) >= 3 else 35 if cl_action.GetPlayRound(skill) >= 2 else 30) / 10, 0, (0, 18, 0), (0, 0), (0, 0), cl_action.CrtArgRandomNum(skill, 340 if cl_action.GetPlayRound(skill) >= 3 else 385 if cl_action.GetPlayRound(skill) >= 2 else 450, 900 if cl_action.GetPlayRound(skill) >= 3 else 1030 if cl_action.GetPlayRound(skill) >= 2 else 1200), False, False, 0, True, cl_action.GetSkillSummonCreate(skill)[i1], 1024, targetType = OBJ_ENEMY, maxDistance = 0, hitHeroOver = False, forceSpeed = False, innerRadius = 0, scale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
            cl_action.CreateRandomNumWarriorAtPointPos(skill, [
                cl_math.Vec3Add((32, 1.38, 54), (i1 * 15 + -22, 3.5, 0))], WARRIOR_SUMMON, {
                1024: 10 }, {
                'Radius': 0.5 })
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, 1)

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
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 22, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39051
    m_Name = '海船-鱼雷'
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
        'ColdTime': 1200,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 10000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_CORRISION
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

