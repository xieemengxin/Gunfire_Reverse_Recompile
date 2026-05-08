# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p1329.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p1329.pyc
# Source Generated with Decompyle++
# File: p1329.pyc (Python 3.6)

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
    m_SID = 1329
    m_Name = '怒罡化形'
    m_ExtPerform = (5327,)
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
        'ColdTime': 300,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 200,
        'Att': 30000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 3300,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 6000,
        'MaxPFBullet': 1000,
        'PFBulletUse': 1000,
        'CostPFBulletDuringUse': 0,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_ForbidRule = 1012
    m_CheckForbid = 1013
    m_AIPerformDam = 600

