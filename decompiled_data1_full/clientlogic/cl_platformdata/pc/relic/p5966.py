# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5966.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5966.pyc
# Source Generated with Decompyle++
# File: p5966.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_CURSE, RELIC_TYPE_CURSE, RELIC_TYPE_NORMAL
from cl_newformula import Func598, Func651

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'PF5966' }))) < 3:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREADDRELIC, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRelicType(oWarrior, oEventCB, RELIC_TYPE_NORMAL) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 10) and cl_evcon.EventCBCheckFirstGetRelic(oWarrior, oEventCB) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'RollNum' }))) <= 0 and cl_evcon.CheckKeyInReason(oWarrior, oEventCB, 'NpcMode') == 0:
        cl_evact.EventCBAddSavedData(oWarrior, oEventCB, 'PF5966', 1, 0)
        cl_evact.EventCBRandomReplaceRelicBySourceRelic(oWarrior, oEventCB, { }, 2421)
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 'PF5966' }))) >= 3:
            cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_PREADDRELIC, -1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckPointRelic(oWarrior, oEventCB, 5966):
        cl_evact.EventCBSetSavedData(oWarrior, oEventCB, 'PF5966', 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5966
    m_Name = '货不对板'
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
    m_RelicType = RELIC_TYPE_CURSE
    m_DropShape = 5531
    m_ValidRemove = 0
    m_BasePrice = 0
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_CURSE

