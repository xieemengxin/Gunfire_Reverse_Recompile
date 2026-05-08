# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9799.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9799.pyc
# Source Generated with Decompyle++
# File: p9799.pyc (Python 3.6)

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
    m_SID = 9799
    m_Name = '#NT#s验证用法杖'
    m_ExtPerform = ()
    m_HaltInfo = {
        108: 1,
        40108: 1,
        30108: 1,
        10214: 1,
        10149: 1,
        143: 1,
        286: 1 }
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
        'ColdTime': 115,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClassifyTag = (1,)
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 1099
    m_CheckForbid = 1019

