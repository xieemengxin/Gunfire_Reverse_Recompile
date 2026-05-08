# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3601.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3601.pyc
# Source Generated with Decompyle++
# File: p3601.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM
from cl_newformula import Func360, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1431, 'Att', 20000, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1431, 'Att', 40000, 0)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1431, 'ExplodeDelay', 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1431, 'Att', 60000, 0)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1431, 'ExplodeDelay', 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1431: 1,
        12030: 1 }, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if (cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 33068 }))) or cl_evcon.CheckTargetDist(oWarrior, oEventCB, (lambda *a: Func360(*a, **{
'sid': 1918,
'sAttr': 'Radius' })), 1, None) or cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 33068 }))) == 0) and cl_evcon.CheckTargetDist(oWarrior, oEventCB, 8, 0, None) == 0 and cl_evcon.CheckTargetDist(oWarrior, oEventCB, (lambda *a: Func360(*a, **{
'sid': 1921,
'sAttr': 'Radius' })), 1, None):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 7500, 0, '')


class CPerform(CCustomPerform):
    m_SID = 3601
    m_Name = '笔力遒劲'
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
    m_Career = 117

