# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2228.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2228.pyc
# Source Generated with Decompyle++
# File: p2228.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKARMOR, -1, 2, 0, 1)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12003)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32844, 900, { }, 1, 0, 0)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32844, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1411, 1, 0) and cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32844) >= 99:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeArmor(oWarrior, oEventCB, (lambda *a: -Func304(*a, **{
'sAttr': 'Armor' })))
        cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32844, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12003, '', None, None, { })


class CPerform(CCustomPerform):
    m_SID = 2228
    m_Name = '破盾新星'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 103

