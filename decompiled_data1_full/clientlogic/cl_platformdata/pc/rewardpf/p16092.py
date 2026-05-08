# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16092.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16092.pyc
# Source Generated with Decompyle++
# File: p16092.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import JUMPFIGURE_BUYGOODS
from cl_newformula import Func207

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMSG_PHASESTART, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: Func207(*a) * 10 / 100), 0, JUMPFIGURE_BUYGOODS, 0, 1)


class CPerform(CCustomPerform):
    m_SID = 16092
    m_Name = '利滚利'
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

