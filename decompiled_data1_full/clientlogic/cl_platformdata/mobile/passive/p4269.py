# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4269.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4269.pyc
# Source Generated with Decompyle++
# File: p4269.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8031, 1365, { }, 1)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_CG_END, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheekFormPointBehavior(oWarrior, oEventCB, 100):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 8031, 0)
    elif cl_evcon.EventCBCheekFormPointBehavior(oWarrior, oEventCB, 99):
        cl_evact.EventGetHeroTarget(oWarrior, oEventCB, 0, 1, 0, None)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1009, 1, None, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 8028, 1, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonSetSceneAIData(oWarrior, oEventCB.GetCBLifeCycle(), 'EnterFight', 1)


class CPerform(CCustomPerform):
    m_SID = 4269
    m_Name = '妖王boss开场和胜利动画'
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
    m_DieDisable = 1

