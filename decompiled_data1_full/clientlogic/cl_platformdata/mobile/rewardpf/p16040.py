# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16040.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16040.pyc
# Source Generated with Decompyle++
# File: p16040.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF, TYPE_RELIFE_GSCASH
from cl_newformula import Func441

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1578, 0, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1663, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRelifeType(oWarrior, oEventCB, TYPE_RELIFE_GSCASH) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func441(*a))) >= 6:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1663, 1, -1)


class CPerform(CCustomPerform):
    m_SID = 16040
    m_Name = '轮回转生'
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

