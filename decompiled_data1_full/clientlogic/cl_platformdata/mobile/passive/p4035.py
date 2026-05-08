# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4035.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4035.pyc
# Source Generated with Decompyle++
# File: p4035.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7903, 100, { }, 1, None, None)
    if cl_evcon.GetVictimHPRatio(oWarrior, oEventCB) <= 50:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7902, 0, { }, 1, None, None)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7900, 0, { }, 1, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'CanBreakHideBuild', None) > 0:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, -10000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 4035
    m_Name = '隐藏门受击'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

