# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6075.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6075.pyc
# Source Generated with Decompyle++
# File: p6075.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32511, 300, { }, 1, 0, None)
    CustomAction(oWarrior, oEventCB, { })
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1065, 300, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 6075
    m_Name = '改版桃lv.5'
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


def CustomAction(oWarrior, oEventCB, dArgs):
    oWarrior.StartShieldRecover('Halt')

