# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51309.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51309.pyc
# Source Generated with Decompyle++
# File: p51309.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_PERFORM, DICE_PUTOUT_POLL_TWO, OBJ_SELF
from cl_newformula import Func804

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33674, 0, {
        'AddDam': 1000,
        'StateCount': 4 }, 1)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 500, 500, 1)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33674, 0, {
        'AddDam': 1250,
        'StateCount': 4 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DebuffCount', 5)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 500, 500, 1)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33674, 0, {
        'AddDam': 1500,
        'StateCount': 5,
        'StatusEffect': 500 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DebuffCount', 4)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 500, 500, 1)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33674, 0, {
        'AddDam': 2000,
        'StateCount': 5,
        'StatusEffect': 400 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DebuffCount', 3)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 400, 400, 1)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33674, 0, {
        'AddDam': 3000,
        'StateCount': 5,
        'StatusEffect': 300 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DebuffCount', 2)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 300, 300, 1)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, '51309CauseDebuff', 1)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, '51309CauseDebuff') >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'DebuffCount'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '51309CauseDebuff', 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33674, 1, 1, 1, None)
        cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
            'pfid': 51309,
            'Item': (lambda *a: Func804(*a)) })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33674, 1, 1, 1, None)
    cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
        'pfid': 51309,
        'Item': (lambda *a: Func804(*a)) })


class CPerform(CCustomPerform):
    m_SID = 51309
    m_Name = '强力打击'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

