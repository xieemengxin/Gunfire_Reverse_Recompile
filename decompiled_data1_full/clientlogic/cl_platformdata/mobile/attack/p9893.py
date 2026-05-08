# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9893.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9893.pyc
# Source Generated with Decompyle++
# File: p9893.pyc (Python 3.6)

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
from cl_commondefines import DPSUBMSG_NOFIRE

class CPerform(CCustomPerform):
    m_SID = 9893
    m_Name = 's追龙新迭代'
    m_ExtPerform = (4381,)
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 50,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_DPSubMsg = DPSUBMSG_NOFIRE
    m_ClassifyTag = ()
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 0
    m_CheckForbid = 1019

