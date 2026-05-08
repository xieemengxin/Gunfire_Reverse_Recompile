# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9402.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9402.pyc
# Source Generated with Decompyle++
# File: p9402.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import CastingRayCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon0(CastingRayCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.VictimAddState(skill, 1071, 50, 0, { })
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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), targettype = OBJ_ENEMY, CanWheel = False, UseLineRender = True, issecondaryskill = False)

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

from cl_perform.attack import CContinuousPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9402
    m_Name = '镭射手套'
    m_ExtPerform = ()
    m_HaltInfo = {
        40108: 1,
        30108: 1,
        10214: 1,
        143: 1 }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_BulletUse = 1
    m_ForbidRule = 0
    m_CheckForbid = 1001

