# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15303.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15303.pyc
# Source Generated with Decompyle++
# File: p15303.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func537, Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRecordLimitedTimeInfo(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'AID' })), (lambda *a: Func537(*a)))
    if cl_evcon.EventCBGetLimitedTimeInfo(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'AID' })), 200) >= 2000:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33797, 600, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 15303
    m_Name = '气涌强攻'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

