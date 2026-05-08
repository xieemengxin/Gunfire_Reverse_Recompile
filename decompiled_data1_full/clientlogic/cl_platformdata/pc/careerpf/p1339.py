# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1339.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1339.pyc
# Source Generated with Decompyle++
# File: p1339.pyc (Python 3.6)

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
    m_SID = 1339
    m_Name = '#NT#重新部署'
    m_ExtPerform = (8507,)
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
        'ColdTime': 1200,
        'AttDistance': 25,
        'MaxCover': 3,
        'UseInterval': 0,
        'AddStateTime': 1,
        'Att': 0,
        'CrazyEff': 0,
        'BulletSpeed': 50,
        'DebuffProb': 0,
        'ExplodeDelay': 200,
        'Radius': 15,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 4,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1084
    m_CheckForbid = 1013
    m_AIPerformDam = 0

