# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4161.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4161.pyc
# Source Generated with Decompyle++
# File: p4161.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DUAL_STATE_BEGIN, DUAL_STATE_END

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'FillTime', 0, 50000)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'FillTime', 0, 0)


class CPerform(CCustomPerform):
    m_SID = 4161
    m_Name = '1302双持改换弹时间'
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

