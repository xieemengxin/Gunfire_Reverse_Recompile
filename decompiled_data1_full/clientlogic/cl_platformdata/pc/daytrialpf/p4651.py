# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p4651.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p4651.pyc
# Source Generated with Decompyle++
# File: p4651.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import RELIC_SUBMSG_GENERATE_CHOOSE, RELIC_SUBMSG_GENERATE_DROP, RELIC_SUBMSG_GENERATE_GOOD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_DROP, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_GOOD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_CHOOSE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHOOSE_RELIC_START, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventReplaceRelicReward(oWarrior, oEventCB, {
        5822: 1,
        5823: 1 }, None, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventSetChooseRelicCnt(oWarrior, oEventCB, 2)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        3: 5000,
        4: 5000 }, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventReplaceRelicReward(oWarrior, oEventCB, {
        5822: 1 }, None, None, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventReplaceRelicReward(oWarrior, oEventCB, {
        5823: 1 }, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4651
    m_Name = '各安天命'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

