# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p51204.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p51204.pyc
# Source Generated with Decompyle++
# File: p51204.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import LEVEL_TYPE_HIDE, PF_SUBMSG_COMMON
from cl_newformula import Func223, Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1970)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1970, 'Att', (lambda *a: Func223(*a) * 30000 + 80000))
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1970, 'Count', 2, 1)
    cl_action.CommonUsePerform(oWarrior, oLifeCycle, 1970, { })
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 2, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, 4, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 1970)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1970)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1970, 'Att', (lambda *a: Func223(*a) * 40000 + 150000))
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1970, 'Count', 3, 1)
    cl_action.CommonUsePerform(oWarrior, oLifeCycle, 1970, { })
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 2, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, 4, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 1970)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1970)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1970, 'Att', (lambda *a: Func223(*a) * 60000 + 350000))
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1970, 'Count', 4, 1)
    cl_action.CommonUsePerform(oWarrior, oLifeCycle, 1970, { })
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 2, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, 4, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 1970)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1970: 1 }, 0, 0):
        cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 1970, { })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 1970, { })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func308(*a))) >= 3:
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1970, 'Att', 0, (lambda *a: Func223(*a) * 60000 + 350000))
    else:
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1970, 'Att', 0, (lambda *a: Func223(*a) * (20000 + 10000 * Func308(*a)) + 70000 * Func308(*a) + 10000))


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_HIDE):
        cl_action.CommonHaltPointPerform(oWarrior, oEventCB.GetCBLifeCycle(), 1970)
        cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 1970, { })


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1970, 1, 0):
        cl_action.CommonHaltPointPerform(oWarrior, oEventCB.GetCBLifeCycle(), 1970)
        cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 1970, { })


class CPerform(CCustomPerform):
    m_SID = 51204
    m_Name = '#NT#星系法杖被动'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 1

