# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p6544.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p6544.pyc
# Source Generated with Decompyle++
# File: p6544.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import NWARRIOR_DROP_EQUIP, NWARRIOR_DROP_RELIC
from cl_newformula import Func16, Func201, Func202, Func203

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddRecycleDropReward(oWarrior, oLifeCycle, NWARRIOR_DROP_EQUIP, (lambda *a: 4 + Func201(*a) * 12 + Func202(*a) * 3), 1)
    if cl_condition.CheckOpenElement(oWarrior, oLifeCycle, {
        'EndlessElement': 1,
        'RealEndlessElement': 1 }):
        cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTENDLESS, -1, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddRecycleDropReward(oWarrior, oLifeCycle, NWARRIOR_DROP_EQUIP, (lambda *a: 8 + Func201(*a) * 24 + Func202(*a) * 6), 1)
    cl_action.CommonAddRecycleDropReward(oWarrior, oLifeCycle, NWARRIOR_DROP_RELIC, (lambda *a: (Func201(*a) * 24 + Func202(*a) * 6 + 8) * Func203(*a) * Func16(*a, **{
'a': 0.9,
'b': 1 })), 1)
    if cl_condition.CheckOpenElement(oWarrior, oLifeCycle, {
        'EndlessElement': 1,
        'RealEndlessElement': 1 }):
        cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTENDLESS, -1, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddRecycleDropReward(oWarrior, oEventCB.GetCBLifeCycle(), NWARRIOR_DROP_EQUIP, 44, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonAddRecycleDropReward(oWarrior, oEventCB.GetCBLifeCycle(), NWARRIOR_DROP_EQUIP, 92, 1)
    cl_action.CommonAddRecycleDropReward(oWarrior, oEventCB.GetCBLifeCycle(), NWARRIOR_DROP_RELIC, (lambda *a: 91.5 * Func203(*a) * Func16(*a, **{
'a': 0.9,
'b': 1 })), 1)


class CPerform(CCustomPerform):
    m_SID = 6544
    m_Name = '物品回收'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

