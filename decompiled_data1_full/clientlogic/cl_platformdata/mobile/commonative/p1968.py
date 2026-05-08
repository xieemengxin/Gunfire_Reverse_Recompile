# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/commonative/p1968.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/commonative/p1968.pyc
# Source Generated with Decompyle++
# File: p1968.pyc (Python 3.6)

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
from cl_commondefines import DAM_TYPE_THUNDER

class CPerform(CCustomPerform):
    m_SID = 1968
    m_Name = '电容法杖电击'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_THUNDER
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0,
        'DebuffProb': 10000,
        'Att': 35000,
        'Radius': 15 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_IgnoreLayer = (PXMASK_BOX,)
    m_ForbidRule = 0

