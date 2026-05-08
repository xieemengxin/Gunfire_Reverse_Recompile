# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/deviceactive/p50360.pyc
# RelativePath: clientlogic/cl_platformdata/pc/deviceactive/p50360.pyc
# Source Generated with Decompyle++
# File: p50360.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, HIT_OVER_GROUND, OBJ_ENEMY

class CCartoon1(ThrowByPowerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.ArrangeDevice(skill, cl_action.GetEndPositionInCrt(skill, 1), cl_action.CrtArgSelfFace(skill), {
            'WidthScale': cl_action.GetPerformArgValue(skill, 'WidthScale', iDefault = 100) }, 0)
        cl_action.SetDeciveAcitveStatus(skill, True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.ArrangeDevice(skill, cl_action.GetEndPositionInCrt(skill, 1), cl_action.CrtArgSelfFace(skill), {
            'WidthScale': cl_action.GetPerformArgValue(skill, 'WidthScale', iDefault = 100) }, 0)
        cl_action.SetDeciveAcitveStatus(skill, True)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (-0.25, -0.05, 0.2))):
                return None
            cls.EnableShow(skill, 0.1, (0, 5, 0), (0.12, 0.14), 300, False, False, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_GROUND, changeRadius = 0, maxRadius = 3)

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
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 65, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.RecycleDevice(skill)
    cl_action.SetDeciveAcitveStatus(skill, False)
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

from cl_perform.deviceactive import CPerform as CCustomPerform
from cl_commondefines import DEVICE_PERFORM_POS_COMMAND

class CPerform(CCustomPerform):
    m_SID = 50360
    m_Name = '屏障开/关(废弃)'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = 0
    m_BaseAttrData = { }
    m_Pos = DEVICE_PERFORM_POS_COMMAND
    m_ForbidRule = 0

