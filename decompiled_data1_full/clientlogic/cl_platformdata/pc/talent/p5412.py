# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p5412.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p5412.pyc
# Source Generated with Decompyle++
# File: p5412.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, PF_TYPE_CONSHOOT
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None):
        if cl_evcon.CheckFixedTimeDamCnt(oWarrior, oEventCB, PF_TYPE_CONSHOOT, 500, (lambda *a: 10 - 2 * Func308(*a)), 0):
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func308(*a))) == 3:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32848, 1000, { }, 0, -1, None)
            else:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32848, 500, { }, 0, -1, None)
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32847, 1, None, None)
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32846, 1, None, None)
        elif cl_evcon.CheckFixedTimeDamCnt(oWarrior, oEventCB, PF_TYPE_CONSHOOT, 500, (lambda *a: 5 - Func308(*a)), 1) or cl_evcon.CheckHasState(oWarrior, oEventCB, 32848) == 0:
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func308(*a))) == 3:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32847, 1000, { }, 0, -1, None)
            else:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32847, 500, { }, 0, -1, None)
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32846, 1, None, None)
        elif cl_evcon.CheckFixedTimeDamCnt(oWarrior, oEventCB, PF_TYPE_CONSHOOT, 500, 1, 1) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32848) == 0 and cl_evcon.CheckHasState(oWarrior, oEventCB, 32847) == 0:
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func308(*a))) == 3:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32846, 1000, { }, 0, -1, None)
            else:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32846, 500, { }, 0, -1, None)
    else:
        cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 0)
        if (cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', None) >= 1 and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', None) < cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: 5 - Func308(*a))) or cl_evcon.CheckHasState(oWarrior, oEventCB, 32848) == 0) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32847) == 0:
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func308(*a))) == 3:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32846, 1000, { }, 0, -1, None)
            else:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32846, 500, { }, 0, -1, None)
        elif cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', None) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: 5 - Func308(*a))) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', None) < cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: 10 - 2 * Func308(*a))) or cl_evcon.CheckHasState(oWarrior, oEventCB, 32848) == 0:
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func308(*a))) == 3:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32847, 1000, { }, 0, -1, None)
            else:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32847, 500, { }, 0, -1, None)
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32846, 1, None, None)
        elif cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', None) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: 10 - 2 * Func308(*a))):
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func308(*a))) == 3:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32848, 1000, { }, 0, -1, None)
            else:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32848, 500, { }, 0, -1, None)
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32847, 1, None, None)
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32846, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 5412
    m_Name = '乘势追击'
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
    m_Career = 103

