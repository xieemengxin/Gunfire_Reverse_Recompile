# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/watchpf/p1791.pyc
# RelativePath: clientlogic/cl_platformdata/pc/watchpf/p1791.pyc
# Source Generated with Decompyle++
# File: p1791.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    pass


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCache():
    return []

from cl_perform.watchactive import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 1791
    m_Name = '附身冲击波'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = { }
    m_ForbidRule = 0

