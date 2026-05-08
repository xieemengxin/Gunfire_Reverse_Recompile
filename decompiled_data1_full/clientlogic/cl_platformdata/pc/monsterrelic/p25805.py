# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25805.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25805.pyc
# Source Generated with Decompyle++
# File: p25805.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_LOW, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1678, 0, { }, -1)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 10, 50, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 20, WARRIOR_MONSTER, 0, 0, 0, 0, 0, { }, 0, None, None, None, None)
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1678, cl_evact.EventCBGetHasStateTargetNum(oWarrior, oEventCB, 1678))


class CPerform(CCustomPerform):
    m_SID = 25805
    m_Name = '惺惺相惜'
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
    m_HeroRelic = 5805
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

