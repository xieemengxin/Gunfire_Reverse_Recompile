# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13536.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13536.pyc
# Source Generated with Decompyle++
# File: p13536.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM
from cl_newformula import Func303, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32673, 0, 1, None) == 0:
        cl_evact.EventTargetSputterDamage(oWarrior, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'Trajectory' })), 1, 1, 0, 1, None, None, None, None, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32673, (lambda *a: 30 - Func410(*a, **{
'sid': 1573 })), { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 13536
    m_Name = '避无可避'
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
    m_Career = 103

