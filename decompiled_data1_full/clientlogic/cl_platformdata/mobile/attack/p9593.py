# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9593.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9593.pyc
# Source Generated with Decompyle++
# File: p9593.pyc (Python 3.6)

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
    m_SID = 9593
    m_Name = '速射弓左键弹道'
    m_ExtPerform = ()
    m_HaltInfo = {
        40108: 1,
        10108: 1,
        10214: 1,
        143: 1,
        286: 1,
        377: 1 }
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
    m_ClassifyTag = ()
    m_BulletUse = 1
    m_IsMinor = 1
    m_ForbidRule = 0
    m_CheckForbid = 1036

