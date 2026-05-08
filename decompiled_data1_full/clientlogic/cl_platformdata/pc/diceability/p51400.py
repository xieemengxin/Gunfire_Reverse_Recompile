# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51400.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51400.pyc
# Source Generated with Decompyle++
# File: p51400.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DICETAG_OTHER, DICE_PUTOUT_POLL_TWO, OBJ_VICTIM, WARRIOR_BOSS, WARRIOR_ELIBATTERY, WARRIOR_ELITE, WARRIOR_MONSTER, WARRIOR_NODURABILITY, WARRIOR_NORBATTERY, WARRIOR_NORBOX, WARRIOR_NORFLY, WARRIOR_NORLARGESUMMON
from cl_newformula import Func308

def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER) and cl_evcon.CheckFightTypeInRange(oWarrior, oEventCB, {
        WARRIOR_NODURABILITY: 1,
        WARRIOR_NORBOX: 1,
        WARRIOR_NORBATTERY: 1,
        WARRIOR_NORLARGESUMMON: 1,
        WARRIOR_NORFLY: 1,
        WARRIOR_ELIBATTERY: 1,
        WARRIOR_BOSS: 1,
        WARRIOR_ELITE: 1 }) == 0:
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func308(*a))) > 3 or cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 10):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33917, 800, { }, 1, 0, 0)
        elif cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 5):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33917, 800, { }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51400
    m_Name = '变形魔法'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

