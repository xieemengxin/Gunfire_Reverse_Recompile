# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51657.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51657.pyc
# Source Generated with Decompyle++
# File: p51657.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import S7_MODULE_POINT_CHANGE
from cl_newformula import Func839

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214) or cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.CommonChangeThrowPerformAttr(oWarrior, oLifeCycle, 'DamInterval', 1000, 0, 0)
    else:
        cl_action.CommonChangeThrowPerformAttr(oWarrior, oLifeCycle, 'Radius', 1000, 0, 0)


def Action2(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214) or cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.CommonChangeThrowPerformAttr(oWarrior, oLifeCycle, 'DamInterval', 2000, 0, 0)
    else:
        cl_action.CommonChangeThrowPerformAttr(oWarrior, oLifeCycle, 'Radius', 2000, 0, 0)


def Action3(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214) or cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeThrowPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'DamInterval', (lambda *a: 3000 + min(Func839(*a) * 50, 1500)), 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeThrowPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', (lambda *a: 3000 + min(Func839(*a) * 50, 1500)), 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51657
    m_Name = 'Q范围'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

