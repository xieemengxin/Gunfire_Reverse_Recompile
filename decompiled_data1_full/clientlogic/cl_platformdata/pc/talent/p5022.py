# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p5022.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p5022.pyc
# Source Generated with Decompyle++
# File: p5022.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF
from cl_newformula import Func340

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 20, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonRecordMoveDis(oWarrior, oEventCB.GetCBLifeCycle(), '5022')
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func340(*a, **{
'sKey': 5022 }))) >= 10:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1712, { }, None)
        cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, '5022', None, None, None)


class CPerform(CCustomPerform):
    m_SID = 5022
    m_Name = '心灵之火'
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
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 1
    m_Career = 112

