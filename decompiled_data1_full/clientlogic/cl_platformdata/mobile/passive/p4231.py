# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4231.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4231.pyc
# Source Generated with Decompyle++
# File: p4231.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, HP_RADIO_SUB, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1009, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7991, 0, { }, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 70, HP_RADIO_SUB, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 30, HP_RADIO_SUB, 1)
    cl_action.CommonChangeSubAttackMsgType(oWarrior, oLifeCycle, ATTACKERSUBMSG_NORMAL)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 1, 0)
    cl_action.CommonSetDieRemoveDelay(oWarrior, oLifeCycle, 434)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 3, 1, 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'SpecialParasiticTarget', 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventClientBehavior(oWarrior, oEventCB, 92, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventClientBehavior(oWarrior, oEventCB, 93, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonSetSkillCheckArgs(oWarrior, oEventCB.GetCBLifeCycle(), 20, 20)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8011, 0, { }, 0, 1, None)


class CPerform(CCustomPerform):
    m_SID = 4231
    m_Name = '妖王建筑'
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

