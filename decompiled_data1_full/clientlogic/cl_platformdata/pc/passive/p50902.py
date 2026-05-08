# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p50902.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p50902.pyc
# Source Generated with Decompyle++
# File: p50902.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DROP_REASON_GAMBLER_ROLLRELIC, DROP_REASON_MONSTERRELIC, NWARRIOR_NPC_EVENT, NWARRIOR_NPC_REFRESH, RELIC_SUBMSG_GENERATE_CHOOSE, RELIC_SUBMSG_GENERATE_DROP

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_DROP, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_CHOOSE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventReplaceRelicReward(oWarrior, oEventCB, {
        5823: 1 }, 1, 1, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckDropReason(oWarrior, oEventCB, DROP_REASON_MONSTERRELIC) or cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_EVENT) or cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_REFRESH) or cl_evcon.CheckDropReason(oWarrior, oEventCB, DROP_REASON_GAMBLER_ROLLRELIC):
        cl_evact.EventReplaceRelicReward(oWarrior, oEventCB, {
            5823: 1 }, 1, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 50902
    m_Name = '#NT#卡包-星光使改动'
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

