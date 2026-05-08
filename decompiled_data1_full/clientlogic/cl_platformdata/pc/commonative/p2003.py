# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p2003.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p2003.pyc
# Source Generated with Decompyle++
# File: p2003.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    cl_action.AttackerRemoveState(skill, 39731, bSameItem = False)
    cl_action.SkillHaltOther(skill, 12043)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_MASK_ELEMENT

class CPerform(CCustomPerform):
    m_SID = 2003
    m_Name = '#NT#打断飞行'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_MASK_ELEMENT
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 1
    m_UseCurWeapon = 0
    m_ForbidRule = 0

