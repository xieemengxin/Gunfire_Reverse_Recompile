# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3402.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3402.pyc
# Source Generated with Decompyle++
# File: p3402.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_HOLD, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, -1, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_HOLD, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, -1, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_HOLD, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 32815, 32774, { }, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1101009) or cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1301002) or cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1101007):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Radius', 20)
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Radius', 7)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1310: 1,
        1696: 1 }, 1, -1):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (0, None, ((304, 'ShieldMax'), (lambda a0: a0))), 0, DAM_TYPE_PERFORM)


class CPerform(CCustomPerform):
    m_SID = 3402
    m_Name = '反击之潮'
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
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 115

