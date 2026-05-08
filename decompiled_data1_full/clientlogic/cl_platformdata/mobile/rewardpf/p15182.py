# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15182.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15182.pyc
# Source Generated with Decompyle++
# File: p15182.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import SUIT_HANDLE_NOCOSTREROLL
from cl_newformula import Func210, Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CursorRelicNum', (lambda *a: Func210(*a)))
    cl_action.CommonAddLotteryRelicBackProb(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: min(int(5 + Func361(*a, **{
'sid': 15182,
'sArgs': 'CursorRelicNum' }) * 5), 50)))
    cl_action.CommonSendSuitHandleInfo(oWarrior, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_NOCOSTREROLL, {
        1: (lambda *a: min(int(5 + Func361(*a, **{
'sid': 15182,
'sArgs': 'CursorRelicNum' }) * 5), 50)) }, None)


class CPerform(CCustomPerform):
    m_SID = 15182
    m_Name = '苦尽甘来'
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

