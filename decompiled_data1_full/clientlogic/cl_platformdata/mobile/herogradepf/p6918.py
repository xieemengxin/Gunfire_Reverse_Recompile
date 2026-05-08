# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6918.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6918.pyc
# Source Generated with Decompyle++
# File: p6918.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import OBJ_VICTIM
from cl_newformula import Func343, Func361, Func812, Func813

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeThrowPerformUse(oWarrior, oLifeCycle, 0, 1439)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, -1, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckAffectedByLion(oWarrior, oEventCB, 1, 1, 1):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Source', cl_evact.EventGetTargeID(oWarrior, oEventCB))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateTime', cl_evact.EventCBGetTargetStateRemainingTime(oWarrior, oEventCB, 8156, 1))
        cl_evact.EventCBLionLockStateSearchEnemy(oWarrior, oEventCB, 50, 0, 1, 1, 1, 1, {
            cl_evact.EventGetTargeID(oWarrior, oEventCB): 1 }, 1)
        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) > 0:
            cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 8020, 0, {
                'Source': (lambda *a: Func361(*a, **{
'sid': 6918,
'sArgs': 'Source' })),
                'StateTime': (lambda *a: 50 + Func361(*a, **{
'sid': 6918,
'sArgs': 'StateTime' })),
                'LockStateKeepTime': (lambda *a: Func812(*a, **{
'iState': 8156 }) + Func813(*a, **{
'sid': 8156,
'sAttr': 'LockStateKeepTime' })) }, None)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBSetTargetStateStatistics(oWarrior, oEventCB, 8156, 'TransFlag', 1, 1, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckCostBulletType(oWarrior, oEventCB, 4508):
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func343(*a, **{
'sid': 4508 }))) < 3 or cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Stage') != 1:
            cl_action.CommonChangeThrowPerformUse(oWarrior, oEventCB.GetCBLifeCycle(), 0, 1435)
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33812, 0)
            cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Stage', 1)
        elif cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Stage') != 2:
            cl_action.CommonChangeThrowPerformUse(oWarrior, oEventCB.GetCBLifeCycle(), 3, 1435)
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33812, 0, { }, 1, 0, 1)
            cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Stage', 2)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func343(*a, **{
'sid': 4508 }))) < 3 or cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Stage') != 1:
        cl_action.CommonChangeThrowPerformUse(oWarrior, oEventCB.GetCBLifeCycle(), 0, 1435)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33812, 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Stage', 1)
    elif cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Stage') != 2:
        cl_action.CommonChangeThrowPerformUse(oWarrior, oEventCB.GetCBLifeCycle(), 3, 1435)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33812, 0, { }, 1, 0, 1)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Stage', 2)


class CPerform(CCustomPerform):
    m_SID = 6918
    m_Name = '苍玦lv.3'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

