# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51628.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51628.pyc
# Source Generated with Decompyle++
# File: p51628.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import S7_MODULE_POINT_CHANGE
from cl_newformula import Func746, Func839

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 200, 200, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 150, 150, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39730, 0, { }, 1)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 2)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddWeaponPFBulletByHoldType(oWarrior, oEventCB, 0, 1000, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39730, (lambda *a: Func839(*a)), 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func746(*a, **{
'iStateSID': 39730 }))):
        cl_evact.EventCBAddWeaponPFBulletByHoldType(oWarrior, oEventCB, 0, 2000, 0)
    else:
        cl_evact.EventCBAddWeaponPFBulletByHoldType(oWarrior, oEventCB, 0, 1000, 0)


class CPerform(CCustomPerform):
    m_SID = 51628
    m_Name = '武器充能'
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

