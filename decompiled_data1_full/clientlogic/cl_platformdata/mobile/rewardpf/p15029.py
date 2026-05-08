# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15029.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15029.pyc
# Source Generated with Decompyle++
# File: p15029.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1305, 'AddStateTime', 0, 300)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDEROVER, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), 1500, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), 0, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


class CPerform(CCustomPerform):
    m_SID = 15029
    m_Name = '电流屏障'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

