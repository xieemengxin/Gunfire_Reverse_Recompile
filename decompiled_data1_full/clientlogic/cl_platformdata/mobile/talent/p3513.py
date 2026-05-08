# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3513.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3513.pyc
# Source Generated with Decompyle++
# File: p3513.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func361, Func612
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1429, 'Att', 20000, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3513, 'NowDam', (lambda *a: Func361(*a, **{
'sid': 3513,
'sArgs': 'Level1Dam' })), None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1429, 'Att', 40000, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3513, 'NowDam', (lambda *a: Func361(*a, **{
'sid': 3513,
'sArgs': 'Level2Dam' })), None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1429, 'Att', 60000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3513, 'NowDam', (lambda *a: Func361(*a, **{
'sid': 3513,
'sArgs': 'Level3Dam' })), None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1429: 1,
        8010: 1,
        8016: 1,
        1433: 1,
        1432: 1 }, 1, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func612(*a) * 5000), DAM_TYPE_PERFORM, '')


class CPerform(CCustomPerform):
    m_SID = 3513
    m_Name = '霜华满天'
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
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 116

