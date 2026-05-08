# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/deviceactive/p50303.pyc
# RelativePath: clientlogic/cl_platformdata/pc/deviceactive/p50303.pyc
# Source Generated with Decompyle++
# File: p50303.pyc (Python 3.6)

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
    m_SID = 50303
    m_Name = '毒气部署-毒气专属2'
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
    m_Pos = DEVICE_PERFORM_POS_ARRANGE
    m_ForbidRule = 0
    m_CheckForbid = 1035

