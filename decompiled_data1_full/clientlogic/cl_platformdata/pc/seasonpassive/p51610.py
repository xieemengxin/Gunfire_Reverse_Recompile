# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51610.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51610.pyc
# Source Generated with Decompyle++
# File: p51610.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, PF_TYPE_THROW, WARRIOR_MONSTER
from cl_newformula import Func604, Func651, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RemainTransTimes', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransDamRadius', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransDamRatio', 20)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RemainTransTimes', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransDamRadius', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransDamRatio', 30)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RemainTransTimes', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransDamRadius', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransDamRatio', 45)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RemainTransTimes', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransDamRadius', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransDamRatio', 50)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RemainTransTimes', 99)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransDamRadius', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransDamRatio', 70)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'TransDamRadius' })), WARRIOR_MONSTER, 1, 0, 1, 0, 1, 0, None, None)
        cl_evact.EventCBUsePerform(oWarrior, oEventCB, 1985, 1, {
            'TransDamRatio': (lambda *a: Func717(*a, **{
'sArg': 'TransDamRatio' })),
            'RemainTransTimes': (lambda *a: Func717(*a, **{
'sArg': 'RemainTransTimes' }) - 1),
            'Att': (lambda *a: Func651(*a, **{
'sKey': 'FinalDam' })) })
    elif cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1985, 1, 0) and cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'RemainTransTimes'):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'TransDamRadius' })), WARRIOR_MONSTER, 1, 0, 1, 0, 1, 0, None, None)
        cl_evact.EventCBUsePerform(oWarrior, oEventCB, 1985, 1, {
            'TransDamRatio': (lambda *a: Func717(*a, **{
'sArg': 'TransDamRatio' })),
            'RemainTransTimes': (lambda *a: Func604(*a, **{
'sKey': 'RemainTransTimes' }) - 1),
            'Att': (lambda *a: Func651(*a, **{
'sKey': 'FinalDam' })) })


class CPerform(CCustomPerform):
    m_SID = 51610
    m_Name = '株连'
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

