# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13607.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13607.pyc
# Source Generated with Decompyle++
# File: p13607.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddDiceShopNpcEnergy(oWarrior, oLifeCycle, 2, 2)
    cl_action.CommonAddDiceShopNpcSpecialItem(oWarrior, oLifeCycle, 1008)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DICESHOP, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBUseDiceShopNpcSpecialItem(oWarrior, oEventCB, 1008)


class CPerform(CCustomPerform):
    m_SID = 13607
    m_Name = '神观星'
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
    m_Career = None

