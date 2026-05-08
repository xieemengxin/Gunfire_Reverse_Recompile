# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p7114.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p7114.pyc
# Source Generated with Decompyle++
# File: p7114.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, ThrowByPowerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, HIT_OVER_NORMAL, OBJ_ENEMY

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
            cls.EnableCtrl(skill, cl_action.GetCartoonEnd(skill, 1), (0, 0, 0), [
                2.5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False)

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
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMuzzlePos(skill, cartoon), cl_action.CrtArgSetParabolaSpeed(skill, cartoon, cl_action.CrtArgMuzzlePos(skill, cartoon), cl_action.CrtArgRandomPosInCircle(skill, cartoon, 10, 4), 20, -18, 0), 20, 0.25, (0, 0, 0), (0.2, 0.2), 500, True, False, 0, 0, None, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    for i1 in range(0, 6, 1):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = i1)
    


def GetSkillCacheIndex():
    return []


def Halt(skill):
    pass


def End(skill):
    pass

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, NONE_DISTANCE
from cl_pxlayer import PXMASK_BARRIER

class CPerform(CCustomPerform):
    m_SID = 7114
    m_Name = '首层boss-地雷'
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
        'ColdTime': 1000,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 2000 }
    m_ElementType = DAM_TYPE_NORMAL
    m_IgnoreLayer = (PXMASK_BARRIER,)
    m_SkillShotType = NONE_DISTANCE
    m_ForbidRule = 0

