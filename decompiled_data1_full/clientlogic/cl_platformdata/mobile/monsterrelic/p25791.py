# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25791.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25791.pyc
# Source Generated with Decompyle++
# File: p25791.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, QUALITY_TYPE_HIGH, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO) and cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 20026) == 0 and cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 1689) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 1673, 0, 0, None, None) or cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1673, 0, 0) < 10:
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1673, 1, 0, 0, 800)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1673, 804, { }, 1, 0, None)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1673, 1, 0, 0, 800)


class CPerform(CCustomPerform):
    m_SID = 25791
    m_Name = '无情连击'
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
    m_HeroRelic = 5791
    m_Quality = QUALITY_TYPE_HIGH
    m_ExcludeRelic = ()

