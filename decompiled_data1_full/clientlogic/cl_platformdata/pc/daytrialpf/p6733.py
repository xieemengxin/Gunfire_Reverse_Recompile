# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p6733.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p6733.pyc
# Source Generated with Decompyle++
# File: p6733.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, JUMPFIGURE_KILLMONSTER, OBJ_VICTIM, WARRIOR_ELITE, WARRIOR_NORHEVFAR, WARRIOR_NORHEVNEAR, WARRIOR_NORMEDNEAR, WARRIOR_NORSNIPE, WARRIOR_SUMMON
from cl_newformula import Func207

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_SUMMON):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_ELITE):
            if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 0 + Func207(*a))) >= 600:
                cl_evact.EventCBAddCash(oWarrior, oEventCB, -600, 1, JUMPFIGURE_KILLMONSTER, -600, None)
            else:
                cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -Func207(*a)), 1, JUMPFIGURE_KILLMONSTER, -600, None)
        elif cl_evcon.GetMonsterSuperLevel(oWarrior, oEventCB) > 0:
            if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 0 + Func207(*a))) >= 100:
                cl_evact.EventCBAddCash(oWarrior, oEventCB, -100, 1, JUMPFIGURE_KILLMONSTER, -100, None)
            else:
                cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -Func207(*a)), 1, JUMPFIGURE_KILLMONSTER, -100, None)
        elif cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORHEVNEAR) or cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORHEVFAR) or cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORSNIPE) or cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORMEDNEAR):
            if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 0 + Func207(*a))) >= 100:
                cl_evact.EventCBAddCash(oWarrior, oEventCB, -100, 1, JUMPFIGURE_KILLMONSTER, -100, None)
            else:
                cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -Func207(*a)), 1, JUMPFIGURE_KILLMONSTER, -100, None)
        elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 0 + Func207(*a))) >= 30:
            cl_evact.EventCBAddCash(oWarrior, oEventCB, -30, 1, JUMPFIGURE_KILLMONSTER, -30, None)
        else:
            cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -Func207(*a)), 1, JUMPFIGURE_KILLMONSTER, -30, None)


class CPerform(CCustomPerform):
    m_SID = 6733
    m_Name = '击杀怪物扣铜币'
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

