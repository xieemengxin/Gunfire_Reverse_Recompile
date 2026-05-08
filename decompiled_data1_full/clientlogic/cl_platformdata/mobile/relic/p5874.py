# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5874.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5874.pyc
# Source Generated with Decompyle++
# File: p5874.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func598

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIC_CHOOSE_END, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHOOSE_RELIC, -1, 4, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIC_CHOOSE_END, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHOOSE_RELIC, -1, 4, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckChooseAll(oWarrior, oEventCB):
        cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'AllChooseRelicCnt', (lambda *a: Func598(*a, **{
'sKey': 'AllChooseRelicCnt' }) - 1))
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'AllChooseRelicCnt' }))) <= 0:
            cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5874, 1)
            cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DESTROY_RELIC, -1, { })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckLoading(oWarrior, oEventCB) == 0:
        cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'AllChooseRelicCnt', 1)
        cl_action.CommonChangeRelicChooseAllCnt(oWarrior, oEventCB.GetCBLifeCycle(), 1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonChangeRelicChooseAllCnt(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: -Func598(*a, **{
'sKey': 'AllChooseRelicCnt' })))
    cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'AllChooseRelicCnt', 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckChooseAll(oWarrior, oEventCB):
        cl_evact.EventCBChangeRelicValidRemove(oWarrior, oEventCB, 0, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckLoading(oWarrior, oEventCB) == 0:
        cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'AllChooseRelicCnt', 2)
        cl_action.CommonChangeRelicChooseAllCnt(oWarrior, oEventCB.GetCBLifeCycle(), 2)


class CPerform(CCustomPerform):
    m_SID = 5874
    m_Name = '顺手牵羊'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 0
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

