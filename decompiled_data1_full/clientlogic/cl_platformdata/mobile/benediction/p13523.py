# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13523.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13523.pyc
# Source Generated with Decompyle++
# File: p13523.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, WARRIOR_BOSS, WARRIOR_ELITE
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32668, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 2, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 32668, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 32669, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 32670, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 32671, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 20026, 0, 0, None, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20027, 0, 0, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20028, 0, 0, None):
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 32671):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32671, (lambda *a: 1000 + Func410(*a, **{
'sid': 1565 })), (lambda *a: 1000 + Func410(*a, **{
'sid': 1565 })))
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32671, 1, 0)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32671, (lambda *a: 1000 + Func410(*a, **{
'sid': 1565 })), { }, 1, 0, None)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32671, 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 32671):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32671, (lambda *a: 1000 + Func410(*a, **{
'sid': 1565 })), (lambda *a: 1000 + Func410(*a, **{
'sid': 1565 })))
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32671, 1, 0)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32671, (lambda *a: 1000 + Func410(*a, **{
'sid': 1565 })), { }, 1, 0, None)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32671, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 13523
    m_Name = '元素之球'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 102

