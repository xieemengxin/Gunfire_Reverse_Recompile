# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5013.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5013.pyc
# Source Generated with Decompyle++
# File: p5013.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, PF_SUBMSG_CAREERPF
from cl_newformula import Func428

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_CAREERPF, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1313, 1, 1) and cl_evcon.EventCBCheckPerformMode(oWarrior, oEventCB) == 1:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.CheckTargetHasMark(oWarrior, oEventCB, 'Talent5013', -1):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32505, (lambda *a: Func428(*a, **{
'sid': 32505 })), -1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32504, 0)
            cl_evact.EventCBRefreshPerformColdTime(oWarrior, oEventCB, 1312)
            cl_evact.EventClearTargetMark(oWarrior, oEventCB, 'Talent5013', None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1313, 1, 1):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventSetTargetMark(oWarrior, oEventCB, 'Talent5013', None)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 8503, 1, 1) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 8504, 1, 1):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32505, (lambda *a: Func428(*a, **{
'sid': 32505 })), -1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32504, 0)
        cl_evact.EventCBRefreshPerformColdTime(oWarrior, oEventCB, 1312)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32505, (lambda *a: Func428(*a, **{
'sid': 32505 })), -1)
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32504, 0)
    cl_evact.EventCBRefreshPerformColdTime(oWarrior, oEventCB, 1312)
    cl_evact.EventClearTargetMark(oWarrior, oEventCB, 'Talent5013', None, None)


class CPerform(CCustomPerform):
    m_SID = 5013
    m_Name = '重回巅峰'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 1
    m_Career = 109

