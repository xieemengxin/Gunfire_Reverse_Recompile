# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3701.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3701.pyc
# Source Generated with Decompyle++
# File: p3701.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, OBJ_ATTACK
from cl_newformula import Func453

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1434, 'Att', 18000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1439, 'Att', 18000, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1434, 'Att', 36000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1434, 'Radius', 0, 1)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1439, 'Att', 36000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1439, 'Radius', 0, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1434, 'Att', 54000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1434, 'Radius', 0, 2)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1439, 'Att', 54000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1439, 'Radius', 0, 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1434: 1,
        1439: 1 }, 1, 0) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func453(*a))) == 1:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 10000, DAM_MASK_ELEMENT, '')


class CPerform(CCustomPerform):
    m_SID = 3701
    m_Name = '摧岳劲诀'
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
    m_Career = 118

