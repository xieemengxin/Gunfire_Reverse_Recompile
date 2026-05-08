# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13569.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13569.pyc
# Source Generated with Decompyle++
# File: p13569.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import OBJECT_SERVANT
from cl_newformula import Func304, Func332, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    CustomAction(oWarrior, oLifeCycle, { })
    CustomAction3(oWarrior, oLifeCycle, { })
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVETALENT, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'HPMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackFromOwnByAttr(oWarrior, oLifeCycle, 'HPMax', 1, OBJECT_SERVANT)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33885, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExtraHPMax', (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 2))
    cl_action.CommonChangeServantAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: Func332(*a) * 6000 + Func717(*a, **{
'sArg': 'ExtraHPMax' })), 1)


def DoCallBackAction1(oEventCB, oWarrior):
    CustomAction4(oWarrior, oEventCB, { })


def DoCallBackAction2(oEventCB, oWarrior):
    CustomAction2(oWarrior, oEventCB, { })


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33885):
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 2, 1, 100, 0, 0, { })


def DoCallBackAction5(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, { })
    CustomAction3(oWarrior, oEventCB, { })


class CPerform(CCustomPerform):
    m_SID = 13569
    m_Name = '战斗核心'
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
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = {
        'CanUpgradeTimes': 2,
        'CanModifyTimes': -1,
        'ExtraHPMax': 0,
        'RewardModifyTimes': 0,
        'RewardUpgradeTimes': 0,
        'ModifyPerHP': 50000,
        'UpgradePerHP': 300000,
        'FirstModifyTimes': 1,
        'FirstUpgradeTimes': 1,
        'FirstUpgradeHP': 0,
        'FirstModifyHP': 50000,
        'HadUpgradeTimes': 0 }
    m_DieDisable = 0
    m_Career = None

