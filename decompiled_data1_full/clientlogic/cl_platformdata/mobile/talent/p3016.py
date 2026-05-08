# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3016.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3016.pyc
# Source Generated with Decompyle++
# File: p3016.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import STATE_COUNT_MIN
from cl_newformula import Func332

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33639, 4, 0, 1, 0)
    cl_action.CommonChangeStateAttr(oWarrior, oLifeCycle, 33639, 1, STATE_COUNT_MIN, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33639, 8, 0, 1, 0)
    cl_action.CommonChangeStateAttr(oWarrior, oLifeCycle, 33639, 3, STATE_COUNT_MIN, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33639, (lambda *a: 12 + Func332(*a) // 3), 0, 1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 0, 0, 0)
    cl_action.CommonChangeStateAttr(oWarrior, oLifeCycle, 33639, 5, STATE_COUNT_MIN, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeStateMaxCount(oWarrior, oEventCB.GetCBLifeCycle(), 33639, (lambda *a: 12 + Func332(*a) // 3), 0, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 3016
    m_Name = '斗转星移'
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
    m_Career = 111

