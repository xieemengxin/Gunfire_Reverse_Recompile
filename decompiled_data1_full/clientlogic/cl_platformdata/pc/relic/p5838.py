# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5838.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5838.pyc
# Source Generated with Decompyle++
# File: p5838.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKED, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKED, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1418, 1000, { }, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1495, 1000, { }, 1)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if not cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, None):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8040, 1000, { }, 1, -1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1495):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 8040, 0, 0, None):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 8000, 0, 0, '')
        else:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 4000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 5838
    m_Name = '睚眦必报'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

