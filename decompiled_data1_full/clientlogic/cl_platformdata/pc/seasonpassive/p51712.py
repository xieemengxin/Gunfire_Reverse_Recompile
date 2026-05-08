# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51712.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51712.pyc
# Source Generated with Decompyle++
# File: p51712.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, PF_TYPE_CAREERPF, S8THIRDACTIVE_STATE_ALLEND
from cl_newformula import Func717, Func858

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 7)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxAddDam', 70)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_ALLEND, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 14)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxAddDam', 140)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_ALLEND, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 28)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxAddDam', 280)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_ALLEND, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: min((Func858(*a) // 100) * Func717(*a, **{
'sArg': 'AddDam' }), Func717(*a, **{
'sArg': 'MaxAddDam' })) * 100), 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39749, 300, {
        'StateCount': (lambda *a: min((Func858(*a) // 100) * Func717(*a, **{
'sArg': 'AddDam' }), Func717(*a, **{
'sArg': 'MaxAddDam' }))) }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51712
    m_Name = '持续伤害'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

