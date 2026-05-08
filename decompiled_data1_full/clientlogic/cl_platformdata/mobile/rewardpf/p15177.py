# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15177.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15177.pyc
# Source Generated with Decompyle++
# File: p15177.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func589

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, (lambda *a: (Func589(*a) / 5) * 1), 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'HPMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'ShieldMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'ArmorMax', -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: (Func589(*a) / 5) * 1), 0, 0)


class CPerform(CCustomPerform):
    m_SID = 15177
    m_Name = '重装之力'
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

