# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5868.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5868.pyc
# Source Generated with Decompyle++
# File: p5868.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import NWARRIOR_NPC_EVENT, NWARRIOR_NPC_REFRESH, OBJ_SELF, QUALITY_TYPE_NORMAL, RELIC_SUBMSG_GENERATE_CHOOSE, RELIC_SUBMSG_GENERATE_DROP, RELIC_SUBMSG_GENERATE_GOOD, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddFilterRelic(oWarrior, oLifeCycle, 5868)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1879, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_DROP, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_GOOD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_CHOOSE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddFilterRelic(oWarrior, oLifeCycle, 5868)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1879, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_DROP, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_GOOD, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_CHOOSE, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_REFRESH) or cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_EVENT):
        cl_evact.EventReplaceRelicReward(oWarrior, oEventCB, {
            5823: 1 }, 1, 1, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckPointRelic(oWarrior, oEventCB, 5823):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1879, 1, 0)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1879, 1, 0) >= 4:
            cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5868, 1)
            cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DESTROY_RELIC, -1, { })


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckPointRelic(oWarrior, oEventCB, 5823):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1879, 1, 0)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1879, 1, 0) >= 6:
            cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5868, 1)
            cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DESTROY_RELIC, -1, { })


def DoCallBackAction6(oEventCB, oWarrior):
    if not cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_REFRESH) or cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_EVENT):
        if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
            cl_evact.EventReplaceRelicReward(oWarrior, oEventCB, {
                5823: 2 }, 1, 0, 1)
        else:
            cl_evact.EventReplaceRelicReward(oWarrior, oEventCB, {
                5823: 1 }, 1, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 5868
    m_Name = '富贵在天'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        4: DoCallBackAction4,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 0
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

