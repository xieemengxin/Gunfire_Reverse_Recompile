# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51364.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51364.pyc
# Source Generated with Decompyle++
# File: p51364.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, DICETAG_OTHER, DICE_PUTOUT_POLL_ONE, OBJ_VICTIM
from cl_newformula import Func531, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BloodThres', 25)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BloodThres', 25)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 3000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BloodThres', 25)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BloodThres', 25)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 2000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BloodThres', 25)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, (lambda *a: ((100 - Func531(*a)) // Func717(*a, **{
'sArg': 'BloodThres' })) * Func717(*a, **{
'sArg': 'AddDam' })), 0, DAM_MASK_ELEMENT, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, (lambda *a: ((100 - Func531(*a)) // Func717(*a, **{
'sArg': 'BloodThres' })) * Func717(*a, **{
'sArg': 'AddDam' })), DAM_MASK_ELEMENT, '')


class CPerform(CCustomPerform):
    m_SID = 51364
    m_Name = '乘胜追击'
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
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

