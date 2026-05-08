# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14416.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14416.pyc
# Source Generated with Decompyle++
# File: p14416.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, MONSTER_PFAI_CATCH, OBJ_VICTIM
from cl_newformula import Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 39045)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 39046)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 39044)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 39047)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectSetPFAIGroupWeight(oWarrior, oLifeCycle, MONSTER_PFAI_CATCH, {
        1001: 0,
        1002: 0,
        2002: 20,
        5003: 0,
        5004: 10,
        5002: 0,
        5005: 10,
        3002: 0,
        3003: 10,
        2001: 0 })


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 8080):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, '14416Cnt', 1)
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 14416,
'sArgs': '14416Cnt' }) // Func361(*a, **{
'sid': 14416,
'sArgs': '14416Interval' }))):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '14416Cnt', 0)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 39045, 0, { }, None)


class CPerform(CCustomPerform):
    m_SID = 14416
    m_Name = '轮回10-吞天'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = {
        '14416Interval': 2 }
    m_DieDisable = 0

