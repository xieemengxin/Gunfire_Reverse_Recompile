# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p1330.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p1330.pyc
# Source Generated with Decompyle++
# File: p1330.pyc (Python 3.6)

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

from cl_perform.careerpf import CPFEnergyPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1330
    m_Name = '#NT#基础式'
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
        'ColdTime': 4,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 30000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 2000,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1098
    m_CheckForbid = 1013
    m_BaseArgData = {
        'EnergyCost3': -1000,
        'EnergyCost4': -1000,
        'EnergyRecoverL3': 1000,
        'L3Mul': 3,
        'RecoverMul': 100 }
    m_AIPerformDam = 1200

