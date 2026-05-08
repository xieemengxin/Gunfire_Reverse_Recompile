# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13554.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13554.pyc
# Source Generated with Decompyle++
# File: p13554.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_ENEMY, OBJ_VICTIM
from cl_newformula import Func361, Func638

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 13554, 'Trigger', 1, None)
    cl_action.CommonChangeMaxInkValue(oWarrior, oLifeCycle, 30)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33044):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func638(*a) * 25), 0, '')
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: Func638(*a) * Func361(*a, **{
'sid': 15100,
'sArgs': 'ExtraMul' }) * 0.25))
    else:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func638(*a) * 100), 0, '')
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: Func638(*a) * Func361(*a, **{
'sid': 15100,
'sArgs': 'ExtraMul' })))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33097):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33125, 0, { }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33097):
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 33125)
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 1045):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Trigger', 1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Trigger') and cl_evcon.CheckTargetSideType(oWarrior, oEventCB, OBJ_ENEMY):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Trigger', 0)
        cl_action.CommonModifyInkValue(oWarrior, oEventCB.GetCBLifeCycle(), 20, '', { })


class CPerform(CCustomPerform):
    m_SID = 13554
    m_Name = '韵影交融'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 117

