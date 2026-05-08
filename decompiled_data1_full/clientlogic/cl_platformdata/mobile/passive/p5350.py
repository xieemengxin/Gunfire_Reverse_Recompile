# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5350.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5350.pyc
# Source Generated with Decompyle++
# File: p5350.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func369, Func717, Func832

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1990)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33923, 0, { }, 1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33914, 1, 1, 0, 0):
            cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 40, WARRIOR_MONSTER, 0, 0, 99, 0, 0, 0, (lambda *a: Func832(*a, **{
'iState': 33914,
'iFromMsgAID': 1,
'iFromSameItem': 1 })))
            if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MarkDam', (lambda *a: Func369(*a) * 50 / 100))
                cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 1990, {
                    'TargetList': cl_evact.EventCBGetTargeList(oWarrior, oEventCB),
                    'Att': (lambda *a: Func717(*a, **{
'sArg': 'MarkDam' })) })
            else:
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33914, 0, { }, 0, 0, 0)
        None.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 40, WARRIOR_MONSTER, 1, 0, 1, 0, 1, 0, (lambda *a: Func832(*a, **{
'iState': 33914,
'iFromMsgAID': 1,
'iFromSameItem': 1 }) == 0))
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33914, 0, { }, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5350
    m_Name = '#NT#新苍鹰被动'
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

