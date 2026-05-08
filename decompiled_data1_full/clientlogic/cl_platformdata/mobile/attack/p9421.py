# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9421.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9421.pyc
# Source Generated with Decompyle++
# File: p9421.pyc (Python 3.6)

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

from cl_perform.attack import CContinuousPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9421
    m_Name = '#NT#龙息激光'
    m_ExtPerform = (5348,)
    m_HaltInfo = {
        108: 1,
        40108: 1,
        30108: 1,
        10214: 1,
        143: 1,
        286: 1 }
    m_IgnoreHalt = {
        1310: 1,
        1301: 1,
        1801: 1 }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 60 }
    m_BulletUse = 0
    m_ForbidRule = 1086
    m_CheckForbid = 1001

