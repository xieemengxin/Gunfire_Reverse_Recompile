# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1913.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1913.pyc
# Source Generated with Decompyle++
# File: p1913.pyc (Python 3.6)

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

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 1913
    m_Name = '秘能觉醒元素之环二-剑气'
    m_ExtPerform = ()
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
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0,
        'DebuffProb': 3000,
        'Att': 0 }
    m_ClientNeed = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'Att': 0,
        'Trajectory': 0,
        'ExtEffect': 0 }

