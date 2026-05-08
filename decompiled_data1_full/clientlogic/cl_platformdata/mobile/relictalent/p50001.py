# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relictalent/p50001.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relictalent/p50001.pyc
# Source Generated with Decompyle++
# File: p50001.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_commondefines import PF_SUBMSG_COMMON

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50007, 'TargetCount', 3, None)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'ColdTime', -2000, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50007, 'TargetCount', 4, None)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'ColdTime', -4000, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50007, 'TargetCount', 5, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50001, 'ThunderCount', 20, None)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'ColdTime', -6000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1914: 1,
        1911: 1 }, 1, 0) and cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33032) == 0:
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33024):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33024, 1, 0)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33024, 0, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 50001
    m_Name = '驱雷策电'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_GrowPF = []
    m_DamagePF = []

