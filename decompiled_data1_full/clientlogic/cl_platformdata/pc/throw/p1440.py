# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p1440.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p1440.pyc
# Source Generated with Decompyle++
# File: p1440.pyc (Python 3.6)

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

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1440
    m_Name = '#NT#硬木飞弹'
    m_ExtPerform = (8009,)
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_NORMAL
    m_BaseAttrData = {
        'ColdTime': 50,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 4508,
        'Att': 50000,
        'CrazyEff': 10000,
        'BulletSpeed': 80,
        'DebuffProb': 1500,
        'ExplodeDelay': 0,
        'Radius': 4,
        'BulletVerticalAcc': 0,
        'AddStateTime': 600,
        'KeepTime': 0,
        'DamInterval': 4,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1010
    m_AIPerformDam = 2000

