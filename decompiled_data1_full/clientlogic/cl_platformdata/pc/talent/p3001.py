# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3001.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3001.pyc
# Source Generated with Decompyle++
# File: p3001.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import PF_SUBMSG_CAREERPF
from cl_newformula import Func336

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1315, 'DamInterval', 0, 2)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1315, 'DamInterval', 0, 4)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1315, 'DamInterval', 0, 6)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1315, 1, 0):
        cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 0, (lambda *a: 5 * Func336(*a, **{
'sKey': 'RemainTimes' })))


class CPerform(CCustomPerform):
    m_SID = 3001
    m_Name = '狂澜棒法'
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
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 111

