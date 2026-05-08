# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51296.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51296.pyc
# Source Generated with Decompyle++
# File: p51296.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.wandability.customaction import CustomAction51271 as CustomAction
from cl_platformdata.custom.wandability.customaction import CustomAction51271_Recory
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_EXCLUSIVE
from cl_newformula import Func361, Func364

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTWARCASH, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostCoin', (lambda *a: -Func364(*a)))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostCoin') >= 2000:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CycleNum', (lambda *a: Func361(*a, **{
'sid': 51296,
'sArgs': 'CostCoin' }) // 2000))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RecordCost', (lambda *a: Func361(*a, **{
'sid': 51296,
'sArgs': 'CycleNum' })))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostCoin', (lambda *a: -Func361(*a, **{
'sid': 51296,
'sArgs': 'CycleNum' }) * 2000))
        CustomAction(oWarrior, oEventCB, {
            'CycleNum': (lambda *a: Func361(*a, **{
'sid': 51296,
'sArgs': 'CycleNum' })),
            'StateList': (33665, 33666, 33667),
            'ContinueTime': 0,
            'MaxStateCount': 3,
            'ThresholdNum': 9 })
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RecordCost') >= 9:
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_COSTWARCASH, -1)


def DoCallBackAction1(oEventCB, oWarrior):
    CustomAction51271_Recory(oWarrior, oEventCB, {
        'ContinueTime': 0 })


class CPerform(CCustomPerform):
    m_SID = 51296
    m_Name = '钱龙令牌专属词条'
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
    m_QualityValue = { }
    m_AbilityType = ABILITY_TYPE_EXCLUSIVE
    m_BaseValue = 0
    m_IsReverseFloting = 0

