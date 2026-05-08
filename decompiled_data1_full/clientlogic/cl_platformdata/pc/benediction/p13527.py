# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13527.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13527.pyc
# Source Generated with Decompyle++
# File: p13527.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import OBJ_VICTIM
from cl_newformula import Func410, Func428

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20026):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32954, 1000, { }, 1, 0, None)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32954, 1, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32700, 1000, { }, 1, 0, None)
        cl_evact.EventCBSetTargetStateMaxCount(oWarrior, oEventCB, 32700, (lambda *a: Func428(*a, **{
'sid': 32954 })), 1, None)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 32700, 0, 0) < cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 32954 }))):
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32700, 1, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 13527
    m_Name = '与火共舞'
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
    m_Career = 112

