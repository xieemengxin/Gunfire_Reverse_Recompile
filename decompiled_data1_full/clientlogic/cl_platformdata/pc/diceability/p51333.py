# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51333.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51333.pyc
# Source Generated with Decompyle++
# File: p51333.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DICETAG_WEAPON, DICE_PUTOUT_POLL_TWO, OBJ_VICTIM
from cl_newformula import Func555, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDTime', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCD', 5)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 45)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDTime', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCD', 5)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 60)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDTime', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCD', 10)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 120)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDTime', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCD', 10)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDTime', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCD', 20)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'CDTime' })))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1977, {
            'Dam': (lambda *a: int(Func555(*a, **{
'sAttr': 'Att' }) * Func717(*a, **{
'sArg': 'AttRatio' }) / 100)),
            'Trajectory': (lambda *a: Func555(*a, **{
'sAttr': 'Trajectory' }) // 100 + cl_action.CommonGetRandomResult(oWarrior, oEventCB.GetCBLifeCycle(), 100, Func555(*a, **{
'sAttr': 'Trajectory' }) % 100, 1)) }, None)
    cl_evact.PassiveCBModifyLiteCD(oWarrior, oEventCB, (lambda *a: -Func717(*a, **{
'sArg': 'SubCD' })))


class CPerform(CCustomPerform):
    m_SID = 51333
    m_Name = '灵气附武'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

