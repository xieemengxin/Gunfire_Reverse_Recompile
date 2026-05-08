# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petpf/p7350.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petpf/p7350.pyc
# Source Generated with Decompyle++
# File: p7350.pyc (Python 3.6)

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
from cl_commondefines import DAM_TYPE_CORRISION, PETPF_ACTIVE_ATTACK

class CPerform(CCustomPerform):
    m_SID = 7350
    m_Name = '剧毒沙蜥普攻'
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
        'ColdTime': 200,
        'AttDistance': 30,
        'ChargeTime': 0,
        'DebuffProb': 3300,
        'MaxCover': 1,
        'Radius': 0 }
    m_ElementType = DAM_TYPE_CORRISION
    m_ClientNeed = 0
    m_PFSubType = PETPF_ACTIVE_ATTACK
    m_SpellPower = 0
    m_NeedTarget = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'TrowFireBall': 1 }
    m_Resend = 1

