# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3511.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3511.pyc
# Source Generated with Decompyle++
# File: p3511.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_ATTACK
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33066, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 33066 }))) == 30 and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1429, 1, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33067, 750, { }, 1, -1, 0)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33066, 0)


class CPerform(CCustomPerform):
    m_SID = 3511
    m_Name = '捕风弄月'
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
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 116

