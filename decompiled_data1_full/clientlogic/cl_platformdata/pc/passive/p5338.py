# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5338.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5338.pyc
# Source Generated with Decompyle++
# File: p5338.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import STATE_EFF_CONTROL
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckStateEffType(oWarrior, oEventCB, STATE_EFF_CONTROL):
        cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 33781, (lambda *a: Func651(*a, **{
'sKey': 'StateSID' })), { }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5338
    m_Name = '#NT#控制骰子光环'
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

