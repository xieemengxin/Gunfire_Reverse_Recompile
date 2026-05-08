# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3505.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3505.pyc
# Source Generated with Decompyle++
# File: p3505.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import FLAW_HITTIMES, OBJ_VICTIM
from cl_newformula import Func590

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'Att', 20000, 0, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'Att', 40000, 0, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'Att', 60000, 0, None)
    cl_action.CommonAddFlawAddition(oWarrior, oLifeCycle, FLAW_HITTIMES, 0, -5000, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0) and cl_evcon.EventCBCheckBreakFlaw(oWarrior, oEventCB, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1854, 0, 0, 0):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1854, (lambda *a: Func590(*a)), { }, 0, 1, None)


class CPerform(CCustomPerform):
    m_SID = 3505
    m_Name = '骤降霜威'
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
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 116

