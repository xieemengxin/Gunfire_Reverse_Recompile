# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51373.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51373.pyc
# Source Generated with Decompyle++
# File: p51373.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_OTHER, DICE_PUTOUT_POLL_TWO, PF_SUBMSG_CAREERPF
from cl_newformula import Func717

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedAddRatio', 700)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedAddRatio', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedAddRatio', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedAddRatio', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33823, (lambda *a: Func717(*a, **{
'sArg': 'EffectTime' })), {
            'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })),
            'SpeedAddRatio': (lambda *a: Func717(*a, **{
'sArg': 'SpeedAddRatio' })),
            'EffectTime': (lambda *a: Func717(*a, **{
'sArg': 'EffectTime' })),
            'Distance': (lambda *a: Func717(*a, **{
'sArg': 'Distance' })) }, 1, -1, 0)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33823, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 51373
    m_Name = '疾步如飞'
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
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

