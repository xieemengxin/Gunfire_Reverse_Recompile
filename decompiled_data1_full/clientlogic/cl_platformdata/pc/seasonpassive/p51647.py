# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51647.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51647.pyc
# Source Generated with Decompyle++
# File: p51647.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import MAIN_SKILL_DURATION_BEGIN
from cl_newformula import Func651, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PerDamAdd', 500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_BEGIN, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PerDamAdd', 1000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_BEGIN, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PerDamAdd', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxAddCount', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PerPoint', 8)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCount', 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_BEGIN, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 39696, (lambda *a: Func651(*a, **{
'sKey': 'StateSID' })), {
        'PerDamAdd': (lambda *a: Func717(*a, **{
'sArg': 'PerDamAdd' })),
        'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })),
        'PerPoint': (lambda *a: Func717(*a, **{
'sArg': 'PerPoint' })),
        'MaxAddCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxAddCount' })),
        'AddCount': (lambda *a: Func717(*a, **{
'sArg': 'AddCount' })) }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51647
    m_Name = '主场作战'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

