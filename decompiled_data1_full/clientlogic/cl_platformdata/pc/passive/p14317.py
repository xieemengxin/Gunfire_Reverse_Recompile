# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14317.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14317.pyc
# Source Generated with Decompyle++
# File: p14317.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 2, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'Toughness', 0, 30000, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 31835, 1, 0):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 5000, 0, 1)
    elif cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 31840, 1, 0):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 0, 0, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -4000, 0, '')


class CPerform(CCustomPerform):
    m_SID = 14317
    m_Name = '轮回9-精英蟹先锋'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

