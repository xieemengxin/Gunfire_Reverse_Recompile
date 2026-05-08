# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51355.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51355.pyc
# Source Generated with Decompyle++
# File: p51355.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import CHANGEWARCASHSUBMSG_COST, DICETAG_PERFORM, DICE_PUTOUT_POLL_TWO, JUMPFIGURE_UPGRADEWEAPON
from cl_newformula import Func364

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33834, 0, {
        'CostRatio': 0.1,
        'Delay': 500,
        'AddDam': 3 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33834, 0, {
        'CostRatio': 0.1,
        'Delay': 500,
        'AddDam': 4 }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33834, 0, {
        'CostRatio': 0.1,
        'Delay': 500,
        'AddDam': 5 }, 1)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33834, 0, {
        'CostRatio': 0.1,
        'Delay': 700,
        'AddDam': 5 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDCASH, CHANGEWARCASHSUBMSG_COST, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 30):
        cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -Func364(*a)), 0, JUMPFIGURE_UPGRADEWEAPON, 0, 1)


class CPerform(CCustomPerform):
    m_SID = 51355
    m_Name = '铜币注灵'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

