# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/suitactive/p8602.pyc
# RelativePath: clientlogic/cl_platformdata/pc/suitactive/p8602.pyc
# Source Generated with Decompyle++
# File: p8602.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    cl_action.AttackerAddState(skill, 33408, 500, 0, { })


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.suitactive import CPerform as CCustomPerform
from cl_commondefines import SUIT_PERFORM_POS_CONTROL

class CPerform(CCustomPerform):
    m_SID = 8602
    m_Name = '#NT#安全气囊技能'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = 0
    m_BaseAttrData = {
        'ColdTime': 1000,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'Att': 0,
        'Radius': 0,
        'MaxCover': 1 }
    m_SourceSuit = 15113
    m_Pos = SUIT_PERFORM_POS_CONTROL
    m_ForbidRule = 0

