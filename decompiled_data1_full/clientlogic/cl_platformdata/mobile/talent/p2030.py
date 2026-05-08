# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2030.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2030.pyc
# Source Generated with Decompyle++
# File: p2030.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import DUAL_STATE_BEGIN, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 0, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 0, 2000, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 0, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 0, 4000, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 0, 6000, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 32045, 32004, { }, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32004, 1, None, None):
        cl_evact.PassiveCureByFinalDam(oWarrior, oEventCB, 10000, { }, 0)
        cl_evact.EventClientBehavior(oWarrior, oEventCB, 1007, 0)


class CPerform(CCustomPerform):
    m_SID = 2030
    m_Name = '生存本能'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 101

