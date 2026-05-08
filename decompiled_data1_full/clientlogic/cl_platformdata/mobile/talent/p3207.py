# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3207.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3207.pyc
# Source Generated with Decompyle++
# File: p3207.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK
from cl_newformula import Func559, Func560

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'Att', 25000, 0, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'Att', 40000, 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'Att', 60000, 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1317, -1, -1) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func559(*a, **{
'idx': 0 }))) > 0:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 4500, 0, 0, '')


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1317, -1, -1) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func559(*a, **{
'idx': 0 }))) > 0:
        if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func560(*a))):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 15000, 0, 0, '')
        else:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 9000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 3207
    m_Name = '贯穿星辰'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 113

