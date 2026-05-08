# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25833.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25833.pyc
# Source Generated with Decompyle++
# File: p25833.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM, QUALITY_TYPE_NORMAL, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1674, 0, 0, None) == 0 and cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 20026) == 0 and cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 1689) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
            if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 1744, 0, 0, None, None) or cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1744, 0, 0) < 8:
                cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1744, 2, 0, 0, 1000)
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1674, 100, { }, 0, 0, None)
            else:
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1744, 1004, { }, 0, 0, None)
                cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1744, 2, 0, 0, 1000)
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1674, 100, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 25833
    m_Name = '幕后交易'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5833
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

