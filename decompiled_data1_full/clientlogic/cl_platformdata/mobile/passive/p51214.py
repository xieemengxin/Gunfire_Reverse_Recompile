# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p51214.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p51214.pyc
# Source Generated with Decompyle++
# File: p51214.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import WAND_SUBMSG_FINISHCONDITION, WAND_SUBMSG_WANDCDEND
from cl_newformula import Func308, Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonWandForbidCasting(oWarrior, oLifeCycle, 1)
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 5)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_FINISHCONDITION, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_WANDCDEND, 3, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetSourceItemTmpData(oWarrior, oLifeCycle, 'ForbidCompCount', 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonWandForbidCasting(oWarrior, oLifeCycle, 1)
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 5)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_FINISHCONDITION, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_WANDCDEND, 3, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonSetSourceItemTmpData(oWarrior, oLifeCycle, 'ForbidCompCount', 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonWandForbidCasting(oWarrior, oLifeCycle, 1)
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 5)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_FINISHCONDITION, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_WANDCDEND, 3, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonSetSourceItemTmpData(oWarrior, oLifeCycle, 'ForbidCompCount', 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.PassiveGetSourceWandRemainCD(oWarrior, oEventCB.GetCBLifeCycle()) == 0 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LastFinishWC') != cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'CompSID' }))):
        cl_evact.PassiveCBResetWandComp(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LastFinishWC'), 0, 0)
        cl_evact.PassiveCBResetWandComp(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'CompSID' })), 1, 1)
        cl_evact.EventCBAddWandCount(oWarrior, oEventCB, 1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'LastFinishWC', (lambda *a: Func651(*a, **{
'sKey': 'CompSID' })))
        if cl_condition.CommonGetSourceWandCount(oWarrior, oEventCB.GetCBLifeCycle()) >= 5:
            cl_action.CommonSetSourceItemTmpData(oWarrior, oEventCB.GetCBLifeCycle(), 'ForbidCompCount', 1)
            cl_evact.PassiveCBResetWandComp(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LastFinishWC'), 0, 1)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'LastFinishWC', 0)
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33560, (lambda *a: 32 * (3 + Func308(*a) * 5)), { }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBResetWandComp(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LastFinishWC'), 0, 1)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'LastFinishWC', 0)
    cl_evact.EventCBSetWandCount(oWarrior, oEventCB, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonSetSourceItemTmpData(oWarrior, oEventCB.GetCBLifeCycle(), 'ForbidCompCount', 0)


class CPerform(CCustomPerform):
    m_SID = 51214
    m_Name = '#NT#评分法杖被动'
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
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

