# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15116.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15116.pyc
# Source Generated with Decompyle++
# File: p15116.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import LEVEL_TYPE_HALL, LEVEL_TYPE_HIDE, NWARRIOR_NPC_EVENT, NWARRIOR_NPC_REFRESH, OBJ_SELF, RELIC_SUBMSG_GENERATE_CHOOSE, RELIC_SUBMSG_GENERATE_DROP
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_DROP, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_EVENTNPC_REWARD_RELIC, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_CHOOSE, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_EVENTNPC_CHOOSE_RELIC, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHOPREFRESH, -1, 1, 0, -10)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_INITGOODS, -1, 1, 0, -10)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33442, 0, { }, 1)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, -1, 3)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_EVENT) == 0 and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 33442 }))):
        if not cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_REFRESH):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33442, -1, 0)
        cl_evact.EventReplaceRelicReward(oWarrior, oEventCB, {
            5823: 1 }, 1, 1, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_EVENT) == 0 and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 33442 }))):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33442, (lambda *a: -cl_evact.EventCBChangeShowShopRelic(oWarrior, oEventCB, 5823, Func410(*a, **{
'sid': 33442 }))), 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CheckHasRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5868):
        cl_action.CommonSetRelicDisable(oWarrior, oEventCB.GetCBLifeCycle(), 5868)


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HALL) or cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HIDE):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33442, 1, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_EVENT) == 0 and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 33442 }))):
        cl_evact.EventReplaceRelicReward(oWarrior, oEventCB, {
            5823: 1 }, 1, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 15116
    m_Name = '顺其自然套装'
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

