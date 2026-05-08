# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51597.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51597.pyc
# Source Generated with Decompyle++
# File: p51597.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import OBJ_SELF
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomIntData(oWarrior, oLifeCycle, '51597ExtraLeiRenNum', 1, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomIntData(oWarrior, oLifeCycle, '51597ExtraLeiRenNum', 2, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomIntData(oWarrior, oLifeCycle, '51597ExtraLeiRenNum', 2, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraTriggerLeiRenNum', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomIntData(oWarrior, oLifeCycle, '51597ExtraLeiRenNum', 3, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraTriggerLeiRenNum', 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 33934):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateStatistics(oWarrior, oEventCB, 33934, '51597ExtraNum', (lambda *a: Func717(*a, **{
'sArg': 'ExtraTriggerLeiRenNum' })), 1)
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 33934, { }, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 51597
    m_Name = '#NT#雷刃数量'
    m_MaxLevel = 4
    m_MaxStack = 2
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

