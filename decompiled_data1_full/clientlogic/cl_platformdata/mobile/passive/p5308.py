# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5308.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5308.pyc
# Source Generated with Decompyle++
# File: p5308.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM
from cl_newformula import Func444

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func444(*a))) > 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32269, 800, { }, 0, 1, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32269, 1, 0, 1, 800)
        cl_evact.EventCBSetTargetStateStatistics(oWarrior, oEventCB, 32269, 'TotalDamageValue', (lambda *a: Func444(*a)), 0, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 5308
    m_Name = '#NT逐风流血状态'
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

