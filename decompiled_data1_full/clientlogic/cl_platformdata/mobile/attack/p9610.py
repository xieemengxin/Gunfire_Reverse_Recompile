# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9610.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9610.pyc
# Source Generated with Decompyle++
# File: p9610.pyc (Python 3.6)

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
    m_SID = 9610
    m_Name = '#NT#双刀-3'
    m_ExtPerform = ()
    m_HaltInfo = {
        10214: 1,
        143: 1 }
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
        'ChargeTime': 0,
        'MinUseEnergy': 0,
        'Att': 200,
        'PFBulletRecover': 1500 }
    m_BulletUse = 1
    m_ForbidRule = 1113
    m_CheckForbid = 1001
    m_BaseArgData = {
        'ExtraAttMul': 5000 }

