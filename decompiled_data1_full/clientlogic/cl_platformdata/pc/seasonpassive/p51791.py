# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51791.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51791.pyc
# Source Generated with Decompyle++
# File: p51791.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import FUNCMODE_TYPE_AUTOS8THIRDACTIVE, S8THIRDACTIVE_ENERGY_CHANGE_ADD
from cl_newformula import Func859, Func862, Func863

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonSwitchMode(oWarrior, oLifeCycle, FUNCMODE_TYPE_AUTOS8THIRDACTIVE, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_STHIRDACTIVE_ENERGY_CHANGE, S8THIRDACTIVE_ENERGY_CHANGE_ADD, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonSwitchMode(oWarrior, oLifeCycle, FUNCMODE_TYPE_AUTOS8THIRDACTIVE, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_STHIRDACTIVE_ENERGY_CHANGE, S8THIRDACTIVE_ENERGY_CHANGE_ADD, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonSwitchMode(oWarrior, oLifeCycle, FUNCMODE_TYPE_AUTOS8THIRDACTIVE, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_STHIRDACTIVE_ENERGY_CHANGE, S8THIRDACTIVE_ENERGY_CHANGE_ADD, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBModifyS8ThirdItemAttr(oWarrior, oEventCB, 'EnergyCost', (lambda *a: -Func859(*a, **{
'sAttr': 'ReduceRatio' })), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func863(*a) - Func862(*a, **{
'sAttr': 'EnergyCost' }))) >= 0:
        cl_action.CommonRefreshMode(oWarrior, oEventCB.GetCBLifeCycle(), FUNCMODE_TYPE_AUTOS8THIRDACTIVE, 1, { })


class CPerform(CCustomPerform):
    m_SID = 51791
    m_Name = '自动使用'
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
    m_BaseLevelArgData = {
        1: {
            'ReduceRatio': 500 },
        2: {
            'ReduceRatio': 1000 },
        3: {
            'ReduceRatio': 2000 } }

