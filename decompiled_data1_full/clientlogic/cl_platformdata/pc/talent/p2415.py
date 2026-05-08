# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2415.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2415.pyc
# Source Generated with Decompyle++
# File: p2415.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import DAM_MASK_ELEMENT
from cl_newformula import Func333

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, (lambda *a: Func333(*a) * -4000), DAM_MASK_ELEMENT, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, (lambda *a: Func333(*a) * -6000), DAM_MASK_ELEMENT, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, (lambda *a: Func333(*a) * -8000), DAM_MASK_ELEMENT, None, None)


class CPerform(CCustomPerform):
    m_SID = 2415
    m_Name = '坚韧不屈'
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
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 105

