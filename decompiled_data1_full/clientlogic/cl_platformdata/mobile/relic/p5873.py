# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5873.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5873.pyc
# Source Generated with Decompyle++
# File: p5873.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import NWARRIOR_DROP_RELIC, QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL
from cl_newformula import Func210, Func219, Func222, Func361, Func410, Func575, Func614

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1886, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECYCLEDROP, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    if not cl_condition.CheckHasPerform(oWarrior, oLifeCycle, 6544) or cl_condition.CheckHasPerform(oWarrior, oLifeCycle, 16051):
        cl_action.CommonAddRecycleDropReward(oWarrior, oLifeCycle, NWARRIOR_DROP_RELIC, (lambda *a: Func219(*a) * 10 / 100), None)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1886, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECYCLEDROP, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    if not cl_condition.CheckHasPerform(oWarrior, oLifeCycle, 6544) or cl_condition.CheckHasPerform(oWarrior, oLifeCycle, 16051):
        cl_action.CommonAddRecycleDropReward(oWarrior, oLifeCycle, NWARRIOR_DROP_RELIC, (lambda *a: Func219(*a) * 10 / 100), None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1886, (lambda *a: min(100, (100 - min((Func222(*a) - Func575(*a) - Func210(*a)) * 10, 90)) + Func361(*a, **{
'sid': 5873,
'sArgs': 'Count' }) * 20)))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckEventRecycleDropType(oWarrior, oEventCB, NWARRIOR_DROP_RELIC) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func614(*a))) > 0 and cl_evcon.EventCBCheckAutoRecycle(oWarrior, oEventCB) == 0:
        cl_action.CommonUpgradeRelic(oWarrior, oEventCB.GetCBLifeCycle(), 0, 1)
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            4: (lambda *a: Func410(*a, **{
'sid': 1886 }) * 100) }, 1)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'Count', 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1886, (lambda *a: min(100, (100 - min((Func222(*a) - Func575(*a) - Func210(*a)) * 10, 90)) + Func361(*a, **{
'sid': 5873,
'sArgs': 'Count' }) * 20)))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1886, (lambda *a: min(100, (100 - min((Func222(*a) - Func575(*a) - Func210(*a)) * 10, 100)) + Func361(*a, **{
'sid': 5873,
'sArgs': 'Count' }) * 15)))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckEventRecycleDropType(oWarrior, oEventCB, NWARRIOR_DROP_RELIC) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func614(*a))) > 0:
        cl_action.CommonUpgradeRelic(oWarrior, oEventCB.GetCBLifeCycle(), 0, 1)
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            4: (lambda *a: Func410(*a, **{
'sid': 1886 }) * 100) }, 1)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'Count', 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1886, (lambda *a: min(100, (100 - min((Func222(*a) - Func575(*a) - Func210(*a)) * 10, 100)) + Func361(*a, **{
'sid': 5873,
'sArgs': 'Count' }) * 15)))


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5873, 1)
    cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DESTROY_RELIC, -1, { })


class CPerform(CCustomPerform):
    m_SID = 5873
    m_Name = '华章天求'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 0
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

