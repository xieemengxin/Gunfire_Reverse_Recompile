# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s7specialpassive/p51501.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s7specialpassive/p51501.pyc
# Source Generated with Decompyle++
# File: p51501.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.s7specialpassive import CSpecialPassive as CCustomPerform
from cl_newformula import Func598, Func846
from cl_commondefines import S7_MODULE_POINT_CHANGE

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': '50501reward' }))) < 2:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MeetModuleNum', (lambda *a: Func846(*a, **{
'iTarget': 4 })))
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': '51501reward' }))) < 1 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MeetModuleNum') >= 1:
        cl_evact.EventCBSetSavedData(oWarrior, oEventCB, '51501reward', 1, 0)
        cl_action.CommonRewardS7Crystal(oWarrior, oEventCB.GetCBLifeCycle(), 0, {
            1001: 1 }, 2)
        cl_evact.EventCBSendNotify(oWarrior, oEventCB, 1, 2551, { })
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': '51501reward' }))) < 2 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MeetModuleNum') >= 2:
        cl_evact.EventCBSetSavedData(oWarrior, oEventCB, '51501reward', 2, 0)
        cl_action.CommonRewardS7Crystal(oWarrior, oEventCB.GetCBLifeCycle(), 0, {
            1001: 1 }, 2)
        cl_evact.EventCBSendNotify(oWarrior, oEventCB, 1, 2551, { })
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE)


class CPerform(CCustomPerform):
    m_SID = 51501
    m_Name = '#NT#玄符阵'
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

