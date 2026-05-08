# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9394.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9394.pyc
# Source Generated with Decompyle++
# File: p9394.pyc (Python 3.6)

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

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9394
    m_Name = 's毒手套'
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
        'ColdTime': 100,
        'AttDistance': 10,
        'ChargeTime': 0 }
    m_CheckForbid = 1019
    m_BulletUse = 1
    m_IsMinor = 1
    m_ForbidRule = 1045

