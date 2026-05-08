# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p6712.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p6712.pyc
# Source Generated with Decompyle++
# File: p6712.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF, TYPE_RELIFE_PASSIVE, WARRIOR_BOSS, WARRIOR_ELIPART, WARRIOR_ELIRIDE, WARRIOR_NORBOX, WARRIOR_NORLARGESUMMON, WARRIOR_NORPART, WARRIOR_NORRIDE
from cl_newformula import Func201

def Action1(oWarrior, oLifeCycle):
    if cl_condition.RandomTrigger(oWarrior, oLifeCycle, 10, 3) and cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_BOSS) == 0 and cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORBOX) == 0 and cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORPART) == 0 and cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_ELIPART) == 0 and cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORRIDE) == 0 and cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_ELIRIDE) == 0 and cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORLARGESUMMON) == 0:
        cl_action.CommonSetRelifeAttr(oWarrior, oLifeCycle, TYPE_RELIFE_PASSIVE, 300, 1, 0, {
            'Elite': 50,
            'Normal': 150 }, None, None)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTRELIFES, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRelifeTimesKey(oWarrior, oEventCB):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS):
        cl_action.CommonDirectEventCBFunc(oWarrior, oEventCB.GetCBLifeCycle(), 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func201(*a))) == 1:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1256, 200, { }, 1, 0, None)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func201(*a))) == 2:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1256, 250, { }, 1, 0, None)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func201(*a))) == 3:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1256, 250, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 6712
    m_Name = '怪物复活'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

