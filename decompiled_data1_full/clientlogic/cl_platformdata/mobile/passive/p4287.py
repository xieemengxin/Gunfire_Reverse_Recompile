# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4287.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4287.pyc
# Source Generated with Decompyle++
# File: p4287.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import QUALITY_TYPE_HIGH, QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL
from cl_newformula import Func222, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32748, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32749, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32750, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32763, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 0, 1, 0)
    cl_action.CommonChangeQualityProb(oWarrior, oLifeCycle, QUALITY_TYPE_LOW, 150000)
    cl_action.CommonChangeQualityProb(oWarrior, oLifeCycle, QUALITY_TYPE_NORMAL, 90000)
    cl_action.CommonChangeQualityProb(oWarrior, oLifeCycle, QUALITY_TYPE_HIGH, 10000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 4, 0, -1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32917, 0, { }, 1)
    cl_action.CommonChangeMaxRelicRollNum(oWarrior, oLifeCycle, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func222(*a))) < 20:
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32763, (lambda *a: 10 + Func222(*a) * 2))
    elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func222(*a))) < 50:
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32763, (lambda *a: 30 + Func222(*a) * 1))
    elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func222(*a))) < 90:
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32763, (lambda *a: 55 + Func222(*a) * 0.5))
    else:
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32763, 100)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1317, 1, 0):
        cl_evact.EventSetSkillCache(oWarrior, oEventCB, 'DamFactor', (lambda *a: Func410(*a, **{
'sid': 32757 })))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CareerFlag', 0)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12007, 1, 0):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CareerFlag', 1)


class CPerform(CCustomPerform):
    m_SID = 4287
    m_Name = '赌侠被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

