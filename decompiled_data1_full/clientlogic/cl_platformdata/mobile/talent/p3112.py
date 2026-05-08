# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3112.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3112.pyc
# Source Generated with Decompyle++
# File: p3112.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import MAIN_DEBUFF, OBJ_ATTACK, WARRIOR_MONSTER, WARRIOR_SUMMON
from cl_newformula import Func308, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, MAIN_DEBUFF, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32627, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 4, 0, 13)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, MAIN_DEBUFF, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32627, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 4, 0, 13)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, MAIN_DEBUFF, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32627, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 4, 0, 13)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20026):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32627, 1, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_SUMMON):
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 32627 }))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: 3 - Func308(*a) // 3)):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32627, (lambda *a: Func308(*a) // 3 - 3), 0)
            if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33419) == 0:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33419, (lambda *a: 1400 - Func308(*a) * 400), { }, 0, 0, 0)
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32695, 200, { }, 0, 0, 0)
                cl_evact.EventSetLimitDamage(oWarrior, oEventCB, 0)
            else:
                cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32627, (lambda *a: Func308(*a) // 3 - 3), 0)


class CPerform(CCustomPerform):
    m_SID = 3112
    m_Name = '浴火护符'
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
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 112

