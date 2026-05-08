# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/throw/p1436.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/throw/p1436.pyc
# Source Generated with Decompyle++
# File: p1436.pyc (Python 3.6)

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
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 1436
    m_Name = '森源法球'
    m_ExtPerform = (8019, 12031, 8015)
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_CORRISION
    m_BaseAttrData = {
        'ColdTime': 50,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 4508,
        'Att': 15000,
        'CrazyEff': 0,
        'BulletSpeed': 80,
        'DebuffProb': 1500,
        'ExplodeDelay': 500,
        'Radius': 5,
        'BulletVerticalAcc': 0,
        'AddStateTime': 600,
        'KeepTime': 80,
        'DamInterval': 3,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0,
        'CommonMaxCount': 20 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_BaseArgData = {
        'ImmobilizeTime': 25,
        'ShiftDis': -5,
        'ExtraDamRatio': 0,
        'StateTriggerInterval': 0,
        'NotReduceRatio': 0,
        'Spread': 0,
        'ParasiticMul': 10000 }
    m_AIPerformDam = 2000

