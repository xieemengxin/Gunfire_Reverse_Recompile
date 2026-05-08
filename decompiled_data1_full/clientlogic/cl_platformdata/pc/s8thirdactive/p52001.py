# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s8thirdactive/p52001.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s8thirdactive/p52001.pyc
# Source Generated with Decompyle++
# File: p52001.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    cl_action.S8ThirdActiveAddState(skill, cl_action.GetSkillAID(skill), 39739, { })


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.s8thirdactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 52001
    m_Name = '临时护盾'
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
        'AttDistance': 0,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'Att': 0,
        'Radius': 0,
        'AddStateTime': 700 }
    m_ElementType = DAM_TYPE_NORMAL
    m_ClientNeed = (0,)
    m_ForbidRule = 0

