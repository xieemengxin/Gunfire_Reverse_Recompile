# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2412.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2412.pyc
# Source Generated with Decompyle++
# File: p2412.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_USE_HP, OBJ_ATTACK, OBJ_VICTIM
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1414, 0, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32330, 200, { }, 1, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1414, 0, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 32330, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
            if cl_evcon.CheckHasState(oWarrior, oEventCB, 32473):
                cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 0.25), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)
            else:
                cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 0.125), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)


class CPerform(CCustomPerform):
    m_SID = 2412
    m_Name = '恐怖余震'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 105

