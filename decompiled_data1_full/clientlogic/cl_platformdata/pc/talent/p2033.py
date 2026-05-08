# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2033.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2033.pyc
# Source Generated with Decompyle++
# File: p2033.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import COST_BAGBULLET_WEAPON, OBJ_SELF
from cl_newformula import Func208, Func215, Func308, Func407

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1301, 'AddStateTime', 5000, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1301, 'AddStateTime', 7500, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1301, 'AddStateTime', 10000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32004):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32040):
            cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 32040, 32004, { }, 1, None, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32040, (lambda *a: Func208(*a) * 100 / 100 + 0), None)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 32040, None, None) >= 20:
            cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32004, (lambda *a: Func308(*a) * 50 + 50), (lambda *a: Func407(*a, **{
'sid': 32004 })))
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32040, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32004):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32040):
            cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 32040, 32004, { }, 1, None, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32040, (lambda *a: Func215(*a) * 100 / 100 + 0), 0)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 32040, None, None) >= 20:
            cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32004, (lambda *a: Func308(*a) * 50 + 50), (lambda *a: Func407(*a, **{
'sid': 32004 })))
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32040, 0)


class CPerform(CCustomPerform):
    m_SID = 2033
    m_Name = '越战越勇'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 101

