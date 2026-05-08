# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9592.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9592.pyc
# Source Generated with Decompyle++
# File: p9592.pyc (Python 3.6)

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
from cl_commondefines import DPSUBMSG_DEFAULT

class CPerform(CCustomPerform):
    m_SID = 9592
    m_Name = '#NT#龙息QTE'
    m_ExtPerform = (4378,)
    m_HaltInfo = {
        40108: 1,
        10149: 1,
        20149: 1,
        143: 1 }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 30,
        'AttDistance': 10,
        'ChargeTime': 0 }
    m_DPSubMsg = DPSUBMSG_DEFAULT
    m_ClassifyTag = ()
    m_BulletUse = 1
    m_IsMinor = 1
    m_ForbidRule = 1086
    m_CheckForbid = 1028

