# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p6723.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p6723.pyc
# Source Generated with Decompyle++
# File: p6723.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.daytrialpf.customaction import CustonAction6723 as CustomAction
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, OBJ_SELF, TYPE_RELIFE_PASSIVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetRelifeAttr(oWarrior, oLifeCycle, TYPE_RELIFE_PASSIVE, 300, 1, 1, { }, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTRELIFES, -1, 0, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRelifeTimesKey(oWarrior, oEventCB):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1262, -1, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CheckHasPerform(oWarrior, oEventCB.GetCBLifeCycle(), 6797) and cl_evcon.CheckHasState(oWarrior, oEventCB, 1262) == 0:
        if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS) or cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
            CustomAction(oWarrior, oEventCB, { })
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1262, 0, { }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1262, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 6723
    m_Name = '玩家复活1次'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

