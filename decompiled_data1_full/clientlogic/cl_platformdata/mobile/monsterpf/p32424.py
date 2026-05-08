# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p32424.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p32424.pyc
# Source Generated with Decompyle++
# File: p32424.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, EntityCurveCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.DeleteClientEffect(skill)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 200 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetCartoonEnd(skill, 3), (0, 0, 0), [
                5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(EntityCurveCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cl_action.AddClientEffect(skill, 1006, cl_action.CrtArgTargetPos(skill, notContainDying = False), time = 0)
        cl_action.StartBackSwing(skill, 176)

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
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 5, 0)), cl_action.CrtArgTargetBodyShiftPos(skill, 1, 0, 0, 0, 0, 0, 1.5, 1.5), 1.5, 1018, 150, 12, 0, 1.5, targettype = OBJ_ENEMY, summonID = 0, forceDel = False)

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
        for i1 in range(0, 1, 1):
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 260, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import CLOSE_DISTANCE, DAM_TYPE_FIRE

class CPerform(CCustomPerform):
    m_SID = 32424
    m_Name = '【第二幕】精英投射怪-大法球术'
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
        'ColdTime': 800,
        'AttDistance': 30,
        'ChargeTime': 0,
        'DebuffProb': 10000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_FIRE
    m_SkillShotType = CLOSE_DISTANCE
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

