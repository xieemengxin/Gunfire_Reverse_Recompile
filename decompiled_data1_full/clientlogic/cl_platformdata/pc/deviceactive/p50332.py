# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/deviceactive/p50332.pyc
# RelativePath: clientlogic/cl_platformdata/pc/deviceactive/p50332.pyc
# Source Generated with Decompyle++
# File: p50332.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_POS

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
        cl_action.SetDeviceMovePos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.IsHeroCtrl(skill):
        cl_action.AddSkillCacheData(skill, SKILLCACHE_POS)
        cl_action.SwitchDeviceFollowMoveStatus(skill, 0)
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.deviceactive import CPerform as CCustomPerform
from cl_commondefines import DEVICE_PERFORM_POS_COMMAND

class CPerform(CCustomPerform):
    m_SID = 50332
    m_Name = '炮台命令'
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
    m_BaseAttrData = {
        'ColdTime': 250,
        'AttDistance': 0,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'Att': 0,
        'Radius': 0 }
    m_Pos = DEVICE_PERFORM_POS_COMMAND
    m_ForbidRule = 1091

