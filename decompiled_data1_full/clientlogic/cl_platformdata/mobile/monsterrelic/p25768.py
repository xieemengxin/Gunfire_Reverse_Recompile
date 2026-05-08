# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25768.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25768.pyc
# Source Generated with Decompyle++
# File: p25768.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, QUALITY_TYPE_LOW, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 10, 5) and cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 20026) == 0 and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 34):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20026, 600, {
                'AbnormalSourceDam': 2500 }, 1, -1, None)
        elif cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 10, 5):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20027, 600, { }, 0, -1, None)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20028, 600, { }, 0, -1, None)


class CPerform(CCustomPerform):
    m_SID = 25768
    m_Name = '元素折磨'
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
    m_HeroRelic = 5768
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

