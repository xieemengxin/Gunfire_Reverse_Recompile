# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4396.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4396.pyc
# Source Generated with Decompyle++
# File: p4396.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckOpenElement(oWarrior, oLifeCycle, {
        'EndlessElement': 1 }):
        cl_action.CommonSetLimitRelicNum(oWarrior, oLifeCycle, 60)
    else:
        cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTENDLESS, -1, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1858, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonSetRelicUnFilterHasRatio(oWarrior, oEventCB.GetCBLifeCycle(), 7500, 10000)


class CPerform(CCustomPerform):
    m_SID = 4396
    m_Name = '无尽模式初始被动'
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

