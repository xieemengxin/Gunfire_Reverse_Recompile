# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4192.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4192.pyc
# Source Generated with Decompyle++
# File: p4192.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1648)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1321, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1648, 0, { })


class CPerform(CCustomPerform):
    m_SID = 4192
    m_Name = '精英召唤怪法球被动'
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

