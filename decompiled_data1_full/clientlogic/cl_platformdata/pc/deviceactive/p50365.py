# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/deviceactive/p50365.pyc
# RelativePath: clientlogic/cl_platformdata/pc/deviceactive/p50365.pyc
# Source Generated with Decompyle++
# File: p50365.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    if cl_action.CheckDeciveStatus(skill, False, True):
        cl_action.SetDeciveAcitveStatus(skill, False)
    elif cl_action.CheckDeciveStatus(skill, False, False):
        cl_action.SetDeciveAcitveStatus(skill, True)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.deviceactive import CPerform as CCustomPerform
from cl_commondefines import DEVICE_PERFORM_POS_ARRANGE

class CPerform(CCustomPerform):
    m_SID = 50365
    m_Name = '屏障部署-屏障专属1'
    m_ExtPerform = (12025,)
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
    m_Pos = DEVICE_PERFORM_POS_ARRANGE
    m_ForbidRule = 1091
    m_CheckForbid = 1035

