# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p6740.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p6740.pyc
# Source Generated with Decompyle++
# File: p6740.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, JUMPFIGURE_KILLMONSTER, OBJ_VICTIM
from cl_newformula import Func207, Func220

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasMark(oWarrior, oEventCB, 'DCHitAddMoney', 1) == 0 and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func207(*a))) >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: (80 - Func220(*a)) // 6 + 1)) and cl_evcon.CheckHitWeakness(oWarrior, oEventCB, -1):
        cl_evact.EventSetTargetMark(oWarrior, oEventCB, 'DCHitAddMoney', None)
        cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -1 - (80 - Func220(*a)) // 6), 1, JUMPFIGURE_KILLMONSTER, (lambda *a: -1 - (80 - Func220(*a)) // 6), None)


class CPerform(CCustomPerform):
    m_SID = 6740
    m_Name = '暴击时扣除铜币'
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

