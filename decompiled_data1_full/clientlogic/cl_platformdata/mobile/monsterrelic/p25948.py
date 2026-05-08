# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25948.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25948.pyc
# Source Generated with Decompyle++
# File: p25948.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_CURSE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        1: 1000 }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByAttackHero(oWarrior, oEventCB)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1764, 0, 0, None):
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1764, 1, 0, 0, None)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1764, 0, { }, 0, 0, None)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1764, 1, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 25948
    m_Name = '军火黑商'
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
    m_HeroRelic = 5948
    m_Quality = QUALITY_TYPE_CURSE
    m_ExcludeRelic = ()

