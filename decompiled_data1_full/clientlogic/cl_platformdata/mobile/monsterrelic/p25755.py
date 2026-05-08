# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25755.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25755.pyc
# Source Generated with Decompyle++
# File: p25755.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import OBJ_ATTACK, QUALITY_TYPE_NORMAL, WARRIOR_HERO, WARRIOR_SERVANT

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if (cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_SERVANT)) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1830, 0, 0, 0) == 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20027, 400, { }, -1, -1, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1830, 800, { }, -1, -1, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1829, 400, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 25755
    m_Name = '荆棘外壳'
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
    m_HeroRelic = 5755
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

