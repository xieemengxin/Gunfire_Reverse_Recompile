# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3608.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3608.pyc
# Source Generated with Decompyle++
# File: p3608.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3608, 'State_Time', 600, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3608, 'State_Time', 600, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3608, 'State_Time', 1000, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1326: 1 }, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
            if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33272, 0, 1, 0):
                cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33272, 1, 1, 0, (lambda *a: Func361(*a, **{
'sid': 3608,
'sArgs': 'State_Time' })))
            else:
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33272, (lambda *a: Func361(*a, **{
'sid': 3608,
'sArgs': 'State_Time' })), {
                    '1920Enhance': cl_action.CommonGetPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1920, 'Att') // 10000 }, 1, 1, 0)
                if cl_evcon.CBGetPFArgs(oWarrior, oEventCB, 5031, '5031have'):
                    cl_evact.EventCBChangeTargetStateDelayTime(oWarrior, oEventCB, 33272, 0, -3300)
                cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33272, 1, 1, 0, (lambda *a: Func361(*a, **{
'sid': 3608,
'sArgs': 'State_Time' })))


class CPerform(CCustomPerform):
    m_SID = 3608
    m_Name = '蚀墨残痕'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = {
        'State_Time': 0 }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 117

