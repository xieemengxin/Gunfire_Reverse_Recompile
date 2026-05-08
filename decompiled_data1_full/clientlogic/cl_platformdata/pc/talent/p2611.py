# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2611.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2611.pyc
# Source Generated with Decompyle++
# File: p2611.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import BIGLION_STATE_BEGIN, BIGLION_STATE_END
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 0, 2000, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraHPMax', 10000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33760, 0, {
        'TalentAffection': 2,
        'CostEnergyMax': 12000 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_BEGIN, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_END, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 0, 4000, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraHPMax', 25000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33760, 0, {
        'TalentAffection': 2,
        'CostEnergyMax': 9000 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_BEGIN, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_END, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 0, 6000, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraHPMax', 40000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33760, 0, {
        'TalentAffection': 3,
        'CostEnergyMax': 9000 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_BEGIN, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_END, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeAttrFixedAddition(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', (lambda *a: Func717(*a, **{
'sArg': 'ExtraHPMax' })))
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 33760, { }, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeAttrFixedAddition(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33604):
        cl_action.CommonChangeAttrFixedAddition(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', (lambda *a: Func717(*a, **{
'sArg': 'ExtraHPMax' })))


class CPerform(CCustomPerform):
    m_SID = 2611
    m_Name = '#NT#觉醒占位'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 121

