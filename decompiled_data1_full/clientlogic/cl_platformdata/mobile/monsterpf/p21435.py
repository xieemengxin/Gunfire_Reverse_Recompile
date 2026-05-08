# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p21435.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p21435.pyc
# Source Generated with Decompyle++
# File: p21435.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon1(RayCastCartoon):
    m_SID = 1
    
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
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 1, -0.7)), cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 1, -0.7)), cl_action.CrtArgShiftAngle(skill, cartoon, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 1, -0.7)), cl_action.CrtArgTargetBodyShiftPos(skill, 1, 0, 0, 0, 0, 0, 0, 0), 5 - i1 * 5, 0), 1, 45, 35, targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = 0, effectLiveTime = 5, radius = 0)

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
        for i1 in range(0, 3, 1):
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = i1)
        
        cl_action.StartBackSwing(skill, 70)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 95, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def End(skill):
    pass


def Halt(skill):
    pass


def GetSkillCacheIndex():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_THUNDER, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 21435
    m_Name = '【第三幕】中型远程-三箭齐发'
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
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_THUNDER
    m_UseHeight = 1.5
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 1038
    m_CacheAttr = [
        'DebuffProb']

