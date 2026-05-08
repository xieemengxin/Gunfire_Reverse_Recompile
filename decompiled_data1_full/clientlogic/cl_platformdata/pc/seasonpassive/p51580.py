# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51580.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51580.pyc
# Source Generated with Decompyle++
# File: p51580.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_ENEMY, WARRIOR_BUILD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLevel', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxLevel', 6)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 500, 500, 3)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLevel', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxLevel', 6)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 400, 400, 3)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLevel', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxLevel', 6)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 400, 400, 3)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLevel', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxLevel', 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraEffLimit', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddAttSpeed', 2400)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletChangeLv', 1)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 300, 300, 3)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLevel', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxLevel', 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraEffLimit', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddAttSpeed', 4800)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletChangeLv', 2)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 300, 300, 3)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33965, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckTargetSideType(oWarrior, oEventCB, OBJ_ENEMY) and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BUILD) == 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ReceiveHit', 1)
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 33965):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33965, -1, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ReceiveHit'):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33965, 1, 0)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ReceiveHit', 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33965, 0, {
        'AddLevel': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddLevel'),
        'MaxLevel': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxLevel'),
        'AddAttSpeed': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAttSpeed'),
        'BulletChangeLv': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BulletChangeLv'),
        'ExtraEffLimit': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraEffLimit') }, 1, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 51580
    m_Name = '#NT#等级增幅'
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
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

