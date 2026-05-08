# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13551.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13551.pyc
# Source Generated with Decompyle++
# File: p13551.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import FLAW_COLDTIME, FLAW_MAXCOUNT, FLAW_UNBALANCE_PROB, OBJ_VICTIM
from cl_newformula import Func659

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, -1, 0, 0, 0)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 13551, 2, None, None)
    cl_action.CommonAddFlawAddition(oWarrior, oLifeCycle, FLAW_MAXCOUNT, 10000, 0, 1)
    cl_action.CommonAddFlawAddition(oWarrior, oLifeCycle, FLAW_COLDTIME, 0, -5000, 1)
    cl_action.CommonAddFlawAddition(oWarrior, oLifeCycle, FLAW_UNBALANCE_PROB, 0, -6000, 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveClientBehavior(oWarrior, oLifeCycle, 13551)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1915, 1, 0) == 0 and cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.EventCBGetTargetFlawCount(oWarrior, oEventCB) > 1:
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1915, {
                'Flaw': (lambda *a: Func659(*a)) }, None)


class CPerform(CCustomPerform):
    m_SID = 13551
    m_Name = '雪上加霜'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 116

