# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51381.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51381.pyc
# Source Generated with Decompyle++
# File: p51381.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_PERFORM, DICE_PUTOUT_POLL_TWO, MAIN_SKILL_DURATION_BEGIN
from cl_newformula import Func651, Func717

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MoveSpeedMul', 600)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StateEffect', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_BEGIN, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MoveSpeedMul', 700)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 300)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StateEffect', 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_BEGIN, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 15)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MoveSpeedMul', 800)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 600)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StateEffect', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_BEGIN, 0, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 15)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MoveSpeedMul', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 900)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StateEffect', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_BEGIN, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 33856, (lambda *a: Func651(*a, **{
'sKey': 'StateSID' })), {
        'MoveSpeedMul': (lambda *a: Func717(*a, **{
'sArg': 'MoveSpeedMul' })),
        'DamRatio': (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })),
        'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })),
        'Distance': (lambda *a: Func717(*a, **{
'sArg': 'Distance' })),
        'StateEffect': (lambda *a: Func717(*a, **{
'sArg': 'StateEffect' })) }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51381
    m_Name = '大步流星'
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

