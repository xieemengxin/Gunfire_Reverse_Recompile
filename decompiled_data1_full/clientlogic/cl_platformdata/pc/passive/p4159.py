# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4159.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4159.pyc
# Source Generated with Decompyle++
# File: p4159.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ARMOR_RADIO_SUB

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 1, ARMOR_RADIO_SUB, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetPhase(oWarrior, oEventCB, 2)


class CPerform(CCustomPerform):
    m_SID = 4159
    m_Name = '一幕精英右矛兵-阶段1'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

