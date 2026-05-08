# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25711.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25711.pyc
# Source Generated with Decompyle++
# File: p25711.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, QUALITY_TYPE_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 100, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if oWarrior.QueryAttr('HPMax') == oWarrior.HP():
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 2500, 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if oWarrior.QueryAttr('HPMax') == oWarrior.HP():
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1822, 100, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 25711
    m_Name = '虚张声势'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5711
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

