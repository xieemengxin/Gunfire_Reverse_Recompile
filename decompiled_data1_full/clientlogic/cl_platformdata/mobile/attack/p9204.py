# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9204.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9204.pyc
# Source Generated with Decompyle++
# File: p9204.pyc (Python 3.6)

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
    m_SID = 9204
    m_Name = '#NT#s炸弹魔'
    m_ExtPerform = (1027, 5319)
    m_HaltInfo = {
        10214: 1,
        10149: 1 }
    m_IgnoreHalt = {
        1310: 1,
        1801: 1 }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 40,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_CheckForbid = 1019
    m_ClassifyTag = (1,)
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 1048

