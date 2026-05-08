# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15117.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15117.pyc
# Source Generated with Decompyle++
# File: p15117.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func598, Func651
from cl_commondefines import MG_SOURCE_RELIC, SUIT_HANDLE_MYSTERYSUITREWARD, SUIT_HANDLE_SETTLEACCOUNTSSUIT

def Action1(oWarrior, oLifeCycle):
    if not cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'rwpf15117' }))):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, SUIT_HANDLE_SETTLEACCOUNTSSUIT, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckTargetSuit(oWarrior, oEventCB, 15123) and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 'rwpf15117' }))) == 0:
        cl_evact.EventCBSetSavedData(oWarrior, oEventCB, 'rwpf15117', 1, 0)
        cl_action.CommonSettleAccountsSeasonSuit(oWarrior, oEventCB.GetCBLifeCycle(), 15123)
        cl_action.CommonClearRecordInfoList(oWarrior, oEventCB.GetCBLifeCycle(), '15117RewardRelic')
        cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2412, {
            3: 100 }, MG_SOURCE_RELIC, 1, 1, 2, None)
        cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2413, {
            2: 100 }, MG_SOURCE_RELIC, 1, 1, 2, None)
        cl_action.CommonSendSuitHandleInfo(oWarrior, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_MYSTERYSUITREWARD, { }, cl_action.CommonGetRecordInfoList(oWarrior, oEventCB.GetCBLifeCycle(), '15117RewardRelic'))
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADDRELIC, -1)
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, SUIT_HANDLE_SETTLEACCOUNTSSUIT)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckKeyInReason(oWarrior, oEventCB, 'MiniGame2412') or cl_evcon.CheckKeyInReason(oWarrior, oEventCB, 'MiniGame2413'):
        cl_evact.EventCBRecordValueToInfoList(oWarrior, oEventCB, '15117RewardRelic', (lambda *a: Func651(*a, **{
'sKey': 'iPerform' })))


class CPerform(CCustomPerform):
    m_SID = 15117
    m_Name = '#NT#神秘连接套装'
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

