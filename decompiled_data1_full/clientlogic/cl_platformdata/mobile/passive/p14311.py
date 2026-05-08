# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14311.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14311.pyc
# Source Generated with Decompyle++
# File: p14311.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 30878)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATEMONSTER, -1, 1, 1, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 30878)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        30871: 1,
        30872: 1,
        30873: 1,
        30874: 1,
        30875: 1,
        30876: 1,
        30877: 1 }, 1, 0) and cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'SkillVID'):
        cl_evact.EventCBSetTargetByID(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'SkillVID' })))
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 30878, { }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonSetMonsterAttrPlus(oWarrior, oEventCB.GetCBLifeCycle(), {
        6203: 1,
        6202: 1 })
    cl_action.CommonAddMonsterBanAF(oWarrior, oEventCB.GetCBLifeCycle(), {
        6114: 1 })


class CPerform(CCustomPerform):
    m_SID = 14311
    m_Name = '轮回10-精英鲶人武士'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

