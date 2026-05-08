# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p50261.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p50261.pyc
# Source Generated with Decompyle++
# File: p50261.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1312: 1,
        1302: 1,
        1304: 1,
        1317: 1,
        1305: 1,
        1301: 1 }, 1, 0):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33134, (lambda *a: Func361(*a, **{
'sid': 50106,
'sArgs': 'StateTime' })), { }, 0)


class CPerform(CCustomPerform):
    m_SID = 50261
    m_Name = '#NT#毒气专属7-通用主动技能开始监听'
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

