# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/monsteraf/p6121.pyc
# RelativePath: clientlogic/cl_perform/monsteraf/p6121.pyc
# Source Generated with Decompyle++
# File: p6121.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsteraf import CPerform as CCustomPerform
from cl_commondefines import MAF_TYPE_SEASONWAND, WARRIOR_ELIBADGER, WARRIOR_ELIDART, WARRIOR_ELIFOOT, WARRIOR_ELIHEVFAR, WARRIOR_ELIHEVNEAR, WARRIOR_ELIMAGIC, WARRIOR_ELIMEDFAR, WARRIOR_ELIMEDNEAR, WARRIOR_ELIRIDE, WARRIOR_ELISMAFAR, WARRIOR_ELISMANEAR, WARRIOR_ELISNIPE, WARRIOR_ELITHROW, WARRIOR_NORBADGER, WARRIOR_NORFOOT, WARRIOR_NORHEVFAR, WARRIOR_NORHEVNEAR, WARRIOR_NORSMAFAR, WARRIOR_NORSMANEAR
from math import ceil
from cl_newformula import Func361, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 500, 500, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'p6121', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, 1742, { }, {
        'count': (lambda *a: max(1, min(4, ceil(Func717(*a, **{
'sArg': 'p6121' }) / Func361(*a, **{
'sid': 6121,
'sArgs': 'EveryDam' }))))) }, 0)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'p6121', 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_NORSMANEAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_NORFOOT) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_NORSMAFAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_NORSMAFAR):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EveryDam', 7)
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1742, 'Radius', 500, 1)
    elif cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_NORBADGER):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EveryDam', 5)
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1742, 'Radius', 300, 1)
    elif cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIBADGER) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIDART) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIFOOT) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIHEVFAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIHEVNEAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIMAGIC) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIMEDFAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIMEDNEAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIRIDE) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELISMAFAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELISMANEAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELISNIPE) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELITHROW):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EveryDam', 15)
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1742, 'Radius', 700, 1)
    elif not cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_NORHEVFAR):
        pass
    if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_NORHEVNEAR):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EveryDam', 10)
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1742, 'Radius', 550, 1)
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EveryDam', 7)
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1742, 'Radius', 400, 1)


class CPerform(CCustomPerform):
    m_SID = 6121
    m_Name = '电弧'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = (1742,)
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_MonsterAfType = MAF_TYPE_SEASONWAND

