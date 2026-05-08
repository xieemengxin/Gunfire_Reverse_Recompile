# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51711.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51711.pyc
# Source Generated with Decompyle++
# File: p51711.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_FILLBULLET, PF_SUBMSG_S8THIRDACTIVE
from cl_newformula import Func717, Func764

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDReduce', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CritRate', 15)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_S8THIRDACTIVE, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDReduce', 40)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CritRate', 30)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_S8THIRDACTIVE, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDReduce', 80)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CritRate', 60)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_S8THIRDACTIVE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 39743, 1, 0, 0):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 39743, 0, {
            'CDReduce': (lambda *a: Func717(*a, **{
'sArg': 'CDReduce' })) }, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 1, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 39743, 1)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39744, 3000, {
        'CritRate': (lambda *a: Func717(*a, **{
'sArg': 'CritRate' })),
        'WeaponID': (lambda *a: Func764(*a)) }, 1, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 51711
    m_Name = '伤害换弹'
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
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

