# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p1918.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p1918.pyc
# Source Generated with Decompyle++
# File: p1918.pyc (Python 3.6)

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

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1918
    m_Name = '#NT#球形浊墨领域'
    m_ExtPerform = ()
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
        'ColdTime': 0,
        'AttDistance': 99,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 7500,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 1500,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 0

