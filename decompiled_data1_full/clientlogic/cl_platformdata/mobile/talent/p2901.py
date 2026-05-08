# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2901.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2901.pyc
# Source Generated with Decompyle++
# File: p2901.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_ATTACK
from cl_newformula import Func331, Func360, Func407

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'AddStateTime', 0, 200, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'AddStateTime', 0, 400, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'AddStateTime', 0, 600, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_BLOCK, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1323, 1, 0):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32814, 0, { }, -1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32814, 6)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32774) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, None):
        cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32774, 100, (lambda *a: Func407(*a, **{
'sid': 32774 })))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32774, 100, (lambda *a: Func407(*a, **{
'sid': 32774 })))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1310: 1,
        1696: 1 }, 1, -1):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: (5 * Func331(*a, **{
'sid': 2901 }) + 5) * Func360(*a, **{
'sid': 1323,
'sAttr': 'AddStateTime' })), 0, DAM_TYPE_PERFORM, '')


class CPerform(CCustomPerform):
    m_SID = 2901
    m_Name = '江河之力'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 110

