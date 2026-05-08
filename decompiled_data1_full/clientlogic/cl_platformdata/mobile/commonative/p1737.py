# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/commonative/p1737.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/commonative/p1737.pyc
# Source Generated with Decompyle++
# File: p1737.pyc (Python 3.6)

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
from cl_pxlayer import PXMASK_BOX
from cl_commondefines import DAM_TYPE_ELEMENT

class CPerform(CCustomPerform):
    m_SID = 1737
    m_Name = '元素之环模块技能'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_ELEMENT
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0,
        'Att': 35000,
        'Radius': 10 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_IgnoreLayer = (PXMASK_BOX,)
    m_ForbidRule = 0

