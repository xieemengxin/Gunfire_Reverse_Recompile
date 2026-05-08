# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51341.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51341.pyc
# Source Generated with Decompyle++
# File: p51341.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_SEASONOUTPUT, DICE_PUTOUT_POLL_THREE
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCDRatio', 2000)
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33793):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33793, 0, { }, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33793, (lambda *a: Func717(*a, **{
'sArg': 'SubCDRatio' })), 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33793, (lambda *a: -Func717(*a, **{
'sArg': 'SubCDRatio' })), 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCDRatio', 4000)
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33793):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33793, 0, { }, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33793, (lambda *a: Func717(*a, **{
'sArg': 'SubCDRatio' })), 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33793, (lambda *a: -Func717(*a, **{
'sArg': 'SubCDRatio' })), 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCDRatio', 6000)
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33793):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33793, 0, { }, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33793, (lambda *a: Func717(*a, **{
'sArg': 'SubCDRatio' })), 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33793, (lambda *a: -Func717(*a, **{
'sArg': 'SubCDRatio' })), 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCDRatio', 8000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCDTime', 10)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, 0, 0, 0)
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33793):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33793, 0, { }, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33793, (lambda *a: Func717(*a, **{
'sArg': 'SubCDRatio' })), 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33793, (lambda *a: -Func717(*a, **{
'sArg': 'SubCDRatio' })), 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCDRatio', 10000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCDTime', 65)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, 0, 0, 0)
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33793):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33793, 0, { }, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33793, (lambda *a: Func717(*a, **{
'sArg': 'SubCDRatio' })), 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33793, (lambda *a: -Func717(*a, **{
'sArg': 'SubCDRatio' })), 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        51336: 1,
        51340: 1,
        51328: 1,
        51309: 1,
        51308: 1,
        51352: 1,
        51363: 1,
        51389: 1,
        51388: 1 }, 1, 0):
        cl_evact.EventCBModifySubCDPerformColdTime(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'SubCDTime' })), 1, 10)


class CPerform(CCustomPerform):
    m_SID = 51341
    m_Name = '自动核心'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_SEASONOUTPUT,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_THREE

