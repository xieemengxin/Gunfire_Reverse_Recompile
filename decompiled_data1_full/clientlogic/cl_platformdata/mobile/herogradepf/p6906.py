# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6906.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6906.pyc
# Source Generated with Decompyle++
# File: p6906.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, FLAW_KILLLINE, OBJ_VICTIM
from cl_newformula import Func611

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEUNBALANCE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventCBAddTargetFlawAddition(oWarrior, oEventCB, FLAW_KILLLINE, 2000, 0, 0, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckHitFlaw(oWarrior, oEventCB) and cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0):
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: Func611(*a) // 200))


class CPerform(CCustomPerform):
    m_SID = 6906
    m_Name = '#NT#处决大师lv.1'
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

