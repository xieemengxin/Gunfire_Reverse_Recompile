# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51596.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51596.pyc
# Source Generated with Decompyle++
# File: p51596.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import S7_ALL_PERFORM_ENABLE
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF-1991DamMul', 8000)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF-1991DamMul', 14000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExplodeAreaAdd', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'KeepTimeAdd', 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF-1991DamMul', 20000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExplodeAreaAdd', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'KeepTimeAdd', 2)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBGetEquipS7ModuleNum(oWarrior, oEventCB, 2044, 0, 0, 0, 0, 0):
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1991, 'Radius', 0, (lambda *a: Func717(*a, **{
'sArg': 'ExplodeAreaAdd' })))
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1991, 'KeepTime', 0, (lambda *a: Func717(*a, **{
'sArg': 'KeepTimeAdd' })))


class CPerform(CCustomPerform):
    m_SID = 51596
    m_Name = '#NT#流星-伤害2'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

