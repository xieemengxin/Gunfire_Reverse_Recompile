# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13565.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13565.pyc
# Source Generated with Decompyle++
# File: p13565.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import OBJ_SELF
from cl_newformula import Func360, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33772, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 2, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 400, 400, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBLionLockStateSearchEnemy(oWarrior, oEventCB, 50, 0, 3, 0, 0, 1, { }, 0)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 3)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddLockStateNum') < 3:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeEnergy(oWarrior, oEventCB, (lambda *a: 800 * (3 - Func717(*a, **{
'sArg': 'AddLockStateNum' }))))
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddLockStateNum', 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 8155) or cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 8156):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33772, 1, 800)


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_evcon.EventCBCheckAffectedByLion(oWarrior, oEventCB, 0, 1, 1):
        cl_evact.EventCBAddLionLockStateToTarget(oWarrior, oEventCB, (lambda *a: Func360(*a, **{
'sid': 1434,
'sAttr': 'AddStateTime' })), 0, { })
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AddLockStateNum', 1)


class CPerform(CCustomPerform):
    m_SID = 13565
    m_Name = '万影归元'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 118

