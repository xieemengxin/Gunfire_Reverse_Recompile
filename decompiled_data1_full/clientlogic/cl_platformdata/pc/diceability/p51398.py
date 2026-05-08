# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51398.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51398.pyc
# Source Generated with Decompyle++
# File: p51398.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DICETAG_WEAPON, DICE_PUTOUT_POLL_TWO

def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLevel', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxLevel', 5)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLevel', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxLevel', 8)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLevel', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxLevel', 8)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33913):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33913, 1, 0)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33913, 0, {
            'AddLevel': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddLevel'),
            'MaxLevel': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxLevel') }, 1, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33913) and cl_evcon.CheckAttackIsVictim(oWarrior, oEventCB) == 0:
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33913, -1, 0)


class CPerform(CCustomPerform):
    m_SID = 51398
    m_Name = '等级增幅'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
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
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

