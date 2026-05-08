# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15136.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15136.pyc
# Source Generated with Decompyle++
# File: p15136.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, SUIT_HANDLE_REDUCESUITNUM, SUIT_REDUCENUM_UI

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, SUIT_HANDLE_REDUCESUITNUM, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 3000 + cl_action.CommonGetSuitConditionNum(oWarrior, oEventCB.GetCBLifeCycle(), 15136) * 1000, 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckSuitReduceSource(oWarrior, oEventCB, 15136):
        cl_action.CommonTriggerReduceSuitTakeEffectAmount(oWarrior, oEventCB.GetCBLifeCycle(), {
            'UIType': SUIT_REDUCENUM_UI,
            'Key': 'Seasonsuit15136',
            'ChooseNum': 1,
            'ReduceNum': 1,
            'CheckSuitNum': 3,
            'FromSuit': 15136 })


class CPerform(CCustomPerform):
    m_SID = 15136
    m_Name = '武器增幅'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 1

