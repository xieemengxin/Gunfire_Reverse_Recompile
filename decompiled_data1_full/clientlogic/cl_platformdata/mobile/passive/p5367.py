# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5367.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5367.pyc
# Source Generated with Decompyle++
# File: p5367.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction5367 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func247, Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1009, 0, { }, 1)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DYING, -1, 1)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 1)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 6)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 11)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 10, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDoneOwnerEvent(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB.GetCBLifeCycle(), {
        'SearchRange': 30,
        'AddTime': 500,
        'RandomDeviation': 2,
        'FollowHeroRandomDeviation': 5,
        'Behavior': 39724 })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonRemoveSelf(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBDirectEventCBFuncByNum(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'LevelID' })), {
        1101009: 3,
        1301003: 4,
        1403003: 5,
        1403004: 5 })


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'PF5367Boss', 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 7)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'PF5367Boss', 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 8)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'PF5367Boss', 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 9)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_condition.CheckInPointLevel(oWarrior, oEventCB.GetCBLifeCycle(), {
        1101009: 1,
        1301003: 1,
        1403003: 1,
        1403004: 1 }):
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 0)


def DoCallBackAction7(oEventCB, oWarrior):
    CustomAction2(oWarrior, oEventCB.GetCBLifeCycle(), {
        'AddTime': 500,
        'BossX': -11,
        'BossY': 1,
        'BossZ': 28.5,
        'RandomDeviation': 1,
        'FollowHeroRandomDeviation': 5,
        'Behavior': 39724 })


def DoCallBackAction8(oEventCB, oWarrior):
    CustomAction3(oWarrior, oEventCB.GetCBLifeCycle(), {
        'AddTime': 500,
        'ExtraRadius': 3,
        'RandomDeviation': 1,
        'FollowHeroRandomDeviation': 5,
        'Behavior': 39724 })


def DoCallBackAction9(oEventCB, oWarrior):
    CustomAction4(oWarrior, oEventCB.GetCBLifeCycle(), {
        'SearchRange': 30,
        'AddTime': 500,
        'Angle': 60,
        'BossY': 2.5,
        'RandomDeviation': 2,
        'FollowHeroRandomDeviation': 5,
        'Behavior': 39724 })


def DoCallBackAction10(oEventCB, oWarrior):
    if cl_condition.CheckInPointLevel(oWarrior, oEventCB.GetCBLifeCycle(), {
        1101009: 1,
        1301003: 1,
        1403003: 1,
        1403004: 1 }):
        cl_evact.EventCBDirectEventCBFuncByNum(oWarrior, oEventCB, (lambda *a: Func247(*a)), {
            1101009: 3,
            1301003: 4,
            1403003: 5,
            1403004: 5 })
    else:
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 0)


def DoCallBackAction11(oEventCB, oWarrior):
    CustomAction5(oWarrior, oEventCB.GetCBLifeCycle(), {
        'Behavior': 39724 })


class CPerform(CCustomPerform):
    m_SID = 5367
    m_Name = '#NT#毒雾装置被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8,
        9: DoCallBackAction9,
        10: DoCallBackAction10,
        11: DoCallBackAction11 }
    m_BaseArgData = { }
    m_DieDisable = 0

