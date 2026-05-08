# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2914.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2914.pyc
# Source Generated with Decompyle++
# File: p2914.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECEIVE, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32674, 0, { }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECEIVE, -1, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32674, 0, { }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECEIVE, -1, 2, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32674, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32674, (lambda *a: 10 + 4 * Func410(*a, **{
'sid': 32775 }) // 10))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32674, (lambda *a: 20 + 6 * Func410(*a, **{
'sid': 32775 }) // 10))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32674, (lambda *a: 30 + 8 * Func410(*a, **{
'sid': 32775 }) // 10))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12013, -1, -1):
        cl_evact.EventChangeDamCrazyEff(oWarrior, oEventCB, (lambda *a: (Func410(*a, **{
'sid': 32775 }) // 10) * 5000), 0)


class CPerform(CCustomPerform):
    m_SID = 2914
    m_Name = '海纳百川'
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
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 110

