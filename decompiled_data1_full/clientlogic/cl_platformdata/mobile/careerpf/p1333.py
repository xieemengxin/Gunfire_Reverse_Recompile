# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p1333.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p1333.pyc
# Source Generated with Decompyle++
# File: p1333.pyc (Python 3.6)

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
    m_SID = 1333
    m_Name = '木灵召唤'
    m_ExtPerform = (12032, 8506)
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
        'ColdTime': 800,
        'AttDistance': 0,
        'MaxCover': 2,
        'UseInterval': 0,
        'AddStateTime': 1,
        'Att': 4000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 3000,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 500,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_BaseArgData = {
        'EvolveNum': 0,
        'CatalyzeNum': 1 }
    m_AIPerformDam = 1600

