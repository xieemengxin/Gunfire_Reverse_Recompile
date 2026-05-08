# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/survivormonsteraf/p6164.pyc
# RelativePath: clientlogic/cl_perform/survivormonsteraf/p6164.pyc
# Source Generated with Decompyle++
# File: p6164.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.survivormonsteraf import CPerform as CCustomPerform
from cl_commondefines import MAF_TYPE_FIRE, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 1, 0)
    cl_action.CommonAttentionOwnerRoomGoalCallBack(oWarrior, oLifeCycle, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.CheckTargetPointBaseMonsters(oWarrior, oEventCB, {
        3165: 1 }):
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 50, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBCreateRandomNumMonster(oWarrior, oEventCB, 3, {
        2: 10 }, 0, 6166, 0, 0, { }, { }, { }, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBDisableSelf(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 6164
    m_Name = '分裂的'
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
    m_MonsterAfType = MAF_TYPE_FIRE

