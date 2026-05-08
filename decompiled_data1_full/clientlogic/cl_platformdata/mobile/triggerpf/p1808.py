# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/triggerpf/p1808.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/triggerpf/p1808.pyc
# Source Generated with Decompyle++
# File: p1808.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    cl_action.AttackerAddState(skill, 1147, 1500, 0, { })


def GetSkillCacheIndex():
    return []


def Halt(skill):
    pass


def End(skill):
    pass

from cl_perform.triggerpf import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 1808
    m_Name = '爆发buff'
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
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_DropShape = 5513
    m_WaitPickTime = 0
    m_ForbidRule = 0

