# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relictalent/p50022.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relictalent/p50022.pyc
# Source Generated with Decompyle++
# File: p50022.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1914)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50022, 'ThunderNum', (0, None, ((361, 50022, 'BaseThunderNum'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50022, 'TargetCount', (0, None, ((361, 50022, 'BaseTargetCount'), (lambda a0: a0))))
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33017, 0, { }, 1)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAGICPOWERCHANGE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (0, None, ((340, 'pf50007'), (lambda a0: a0)))) >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (0, None, ((361, 50022, 'MoveDistance'), (lambda a0: a0)))):
        cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'pf50007')
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33018, 0, { }, 1, -1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 1914, 'Att', (0, None, ((600,), (lambda a0: 1000 * a0))))


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, (0, None, ((361, 50022, 'EnemySearchRange'), (lambda a0: a0))), WARRIOR_MONSTER, 1, 0, (0, None, ((361, 50022, 'TargetCount'), (361, 50022, 'ExtraTargetCount'), (lambda a0, a1: a0 + a1))), 0, 1)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 3)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBUsePerform(oWarrior, oEventCB, 1914, -1)


class CPerform(CCustomPerform):
    m_SID = 50022
    m_Name = '步步惊雷迭代版本基础效果'
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
    m_BaseArgData = {
        'MoveDistance': 32,
        'EnemySearchRange': 30,
        'ExtraThunderNum': 0,
        'ExtraTargetCount': 0,
        'BaseTargetCount': 1,
        'BaseThunderNum': 1 }
    m_DieDisable = 0
    m_GrowPF = []

