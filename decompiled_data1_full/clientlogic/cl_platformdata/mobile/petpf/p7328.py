# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petpf/p7328.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petpf/p7328.pyc
# Source Generated with Decompyle++
# File: p7328.pyc (Python 3.6)

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

from cl_perform.petactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_THUNDER, PETPF_ACTIVE_SLIP_SPELL

class CPerform(CCustomPerform):
    m_SID = 7328
    m_Name = '#NT#妖灵电球'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 20,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1,
        'Radius': 0 }
    m_ElementType = DAM_TYPE_THUNDER
    m_ClientNeed = 0
    m_PFSubType = PETPF_ACTIVE_SLIP_SPELL
    m_SpellPower = 0
    m_NeedTarget = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 2000 }

