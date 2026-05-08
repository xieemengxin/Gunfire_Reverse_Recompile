# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5313.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5313.pyc
# Source Generated with Decompyle++
# File: p5313.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func204

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckHasLockEnemy(oWarrior, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_END_HATE, -1, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    if cl_condition.CheckHasLockEnemy(oWarrior, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_END_HATE, -1, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    if cl_condition.CheckHasLockEnemy(oWarrior, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_END_HATE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 4, (lambda *a: (56 - Func204(*a) * 6) * (Func204(*a) * 3 - 1) + 1300), 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1678, 0, { })


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


class CPerform(CCustomPerform):
    m_SID = 5313
    m_Name = '雷霆强化预警-怪物秘卷'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

