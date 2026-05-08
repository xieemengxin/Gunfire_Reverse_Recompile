# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51594.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51594.pyc
# Source Generated with Decompyle++
# File: p51594.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import OBJ_SELF, S7MODULE_TAG_FIRESTONE, S7_ALL_PERFORM_ENABLE
from cl_newformula import Func308, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ModulePointLimit', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReduceCDPer', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxReduceCD', 50)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ModulePointLimit', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReduceCDPer', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxReduceCD', 100)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ModulePointLimit', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReduceCDPer', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxReduceCD', 200)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 1, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ModulePointLimit', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReduceCDPer', 50)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxReduceCD', 300)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ModuleSumPoint', cl_evcon.EventCBGetEquipS7ModulePoint(oWarrior, oEventCB, {
        S7MODULE_TAG_FIRESTONE: 1 }, 1))
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ModuleFullPointNum', cl_evcon.EventCBGetEquipS7ModuleNum(oWarrior, oEventCB, 0, S7MODULE_TAG_FIRESTONE, 1, 0, 0, 0))
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33928):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBChangeTargetStateDelayTime(oWarrior, oEventCB, 33928, (lambda *a: -min(Func717(*a, **{
'sArg': 'MaxReduceCD' }), 10 * Func308(*a) * (Func717(*a, **{
'sArg': 'ModuleSumPoint' }) // Func717(*a, **{
'sArg': 'ModulePointLimit' })) + Func717(*a, **{
'sArg': 'ModuleFullPointNum' }) * Func717(*a, **{
'sArg': 'ReduceCDPer' }))), 0)


class CPerform(CCustomPerform):
    m_SID = 51594
    m_Name = '#NT#流星-上限'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

