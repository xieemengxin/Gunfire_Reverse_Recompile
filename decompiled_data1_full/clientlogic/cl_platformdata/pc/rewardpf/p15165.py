# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15165.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15165.pyc
# Source Generated with Decompyle++
# File: p15165.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import PF_SUBMSG_THROW, SUIT_HANDLE_TRIGGERSKILL
from cl_newformula import Func451

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddSuitPerform(oWarrior, oLifeCycle, 8601)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8601, 'MaxCover', 0, 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, SUIT_HANDLE_TRIGGERSKILL, 1, 0, 0)
    cl_action.CommonAddPerformCDTimer(oWarrior, oLifeCycle, 25, 1)
    cl_action.CommonAddNeedSubCDActivePerform(oWarrior, oLifeCycle, 8601)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 2, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 6, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33489, 0, {
        'GainEffect': 1250 }, 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33397, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddSuitPerform(oWarrior, oLifeCycle, 8601)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8601, 'MaxCover', 0, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, SUIT_HANDLE_TRIGGERSKILL, 1, 0, 0)
    cl_action.CommonAddNeedSubCDActivePerform(oWarrior, oLifeCycle, 8601)
    cl_action.CommonAddPerformCDTimer(oWarrior, oLifeCycle, 25, 1)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8601, 'ColdTime', 0, -100)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 2, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 6, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33489, 0, {
        'GainEffect': 1250 }, 1)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33397, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddSuitPerform(oWarrior, oLifeCycle, 8601)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8601, 'MaxCover', 0, 4)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8601, 'ColdTime', 0, -200)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, SUIT_HANDLE_TRIGGERSKILL, 1, 0, 0)
    cl_action.CommonAddPerformCDTimer(oWarrior, oLifeCycle, 25, 1)
    cl_action.CommonAddNeedSubCDActivePerform(oWarrior, oLifeCycle, 8601)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 2, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 6, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33489, 0, {
        'GainEffect': 1250 }, 1)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33397, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func451(*a, **{
'sid': 33397,
'sAttr': 'AddDam' }))):
        cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 8601, { })


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33397):
        cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33489, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33397):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33489, 1250, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33397) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33489, 0, None)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction6(oEventCB, oWarrior):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 50, 50, 3)


class CPerform(CCustomPerform):
    m_SID = 15165
    m_Name = '破隐一击'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0

