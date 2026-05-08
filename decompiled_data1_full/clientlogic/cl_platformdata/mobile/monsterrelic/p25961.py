# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25961.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25961.pyc
# Source Generated with Decompyle++
# File: p25961.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import OBJ_ATTACK, QUALITY_TYPE_CURSE, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.EventCBAddDeadPunishmentTimes(oWarrior, oEventCB, -1)


class CPerform(CCustomPerform):
    m_SID = 25961
    m_Name = '误人庸医'
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
    m_HeroRelic = 5961
    m_Quality = QUALITY_TYPE_CURSE
    m_ExcludeRelic = ()

