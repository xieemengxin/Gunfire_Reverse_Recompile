# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/throw/p1433.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/throw/p1433.pyc
# Source Generated with Decompyle++
# File: p1433.pyc (Python 3.6)

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

from cl_perform.throw import CUseCountPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1433
    m_Name = '#NT#13553破绽爆炸'
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
        'ColdTime': 15,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 0,
        'Att': 50000,
        'CrazyEff': 0,
        'BulletSpeed': 45,
        'DebuffProb': 1500,
        'ExplodeDelay': 500,
        'Radius': 5,
        'BulletVerticalAcc': 0,
        'AddStateTime': 300,
        'KeepTime': 300,
        'DamInterval': 100,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000

