# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25850.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25850.pyc
# Source Generated with Decompyle++
# File: p25850.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM, QUALITY_TYPE_HIGH
from cl_newformula import Func369

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1654, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 1623) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func369(*a))) > 0 and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.CommonCBDropReward(oWarrior, oEventCB, {
            101: 1 }, {
            101: 10000 }, 0, 0, 0, 1)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1654, 1, -1)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1623, 300, { }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 1654, 1) * 2000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 25850
    m_Name = '挥金如土'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5850
    m_Quality = QUALITY_TYPE_HIGH
    m_ExcludeRelic = ()

