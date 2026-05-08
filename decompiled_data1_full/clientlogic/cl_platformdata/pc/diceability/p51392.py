# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51392.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51392.pyc
# Source Generated with Decompyle++
# File: p51392.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_OTHER, DICE_PUTOUT_POLL_TWO, OBJ_ENEMY, PF_SUBMSG_CAREERPF, WARRIOR_BOSS, WARRIOR_ELITE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'WithTargetCnt', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddHpMax', 2000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Range', 6)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'WithTargetCnt', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddHpMax', 3000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Range', 6)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'WithTargetCnt', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddHpMax', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Range', 6)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'WithTargetCnt', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddHpMax', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Range', 6)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'WithTargetCnt', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddHpMax', 2500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Range', 8)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 0, 0):
        cl_evact.EventGetRangeTargetByTargetType(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Range'), OBJ_ENEMY, 0)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'WithTargetCnt') or cl_evcon.GetThisTargetNum(oWarrior, oEventCB) > 0:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33888, 300, {
                'AddHpMax': cl_evcon.GetThisTargetNum(oWarrior, oEventCB) * cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddHpMax') }, 1, -1, 0)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33888, 300, {
                'AddHpMax': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddHpMax') }, 1, -1, 0)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20039, 150, { }, 1, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 51392
    m_Name = '英勇冲锋'
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
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

