# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51310.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51310.pyc
# Source Generated with Decompyle++
# File: p51310.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_PERFORM, DICE_PUTOUT_POLL_ONE, PF_SUBMSG_THROW
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 10)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 10)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 10)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 10)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 8)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 10)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, (lambda *a: 15 + (Func308(*a) - 1) * 5)) and cl_evcon.CheckFromThrowPerform(oWarrior, oEventCB, None):
        cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, (lambda *a: 35 + (Func308(*a) - 4) * 15)) and cl_evcon.CheckFromThrowPerform(oWarrior, oEventCB, None):
        cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 51310
    m_Name = '#NT#灵力回复'
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
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

