# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/monsteraf/p6119.pyc
# RelativePath: clientlogic/cl_perform/monsteraf/p6119.pyc
# Source Generated with Decompyle++
# File: p6119.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsteraf import CPerform as CCustomPerform
from cl_commondefines import MAF_TYPE_SEASONWAND, TYPE_PASSIVE_TIME_CYCLE

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckHasLockEnemy(oWarrior, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_END_HATE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 200, 500, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1740, 0, { })


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonHaltPointPerform(oWarrior, oEventCB.GetCBLifeCycle(), 1740)


class CPerform(CCustomPerform):
    m_SID = 6119
    m_Name = '剑气'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_MonsterAfType = MAF_TYPE_SEASONWAND

