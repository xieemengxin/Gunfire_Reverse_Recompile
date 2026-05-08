# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5839.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5839.pyc
# Source Generated with Decompyle++
# File: p5839.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenCareerPerformCD(oWarrior, oLifeCycle, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 12, WARRIOR_HERO, 1, 1, 0, 1, 1, { }, None, None, None, None, None)
    cl_evact.EventCBSubTargetCareerPerformColdTime(oWarrior, oEventCB, 0, 100)


class CPerform(CCustomPerform):
    m_SID = 5839
    m_Name = '顺水推舟'
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
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 0
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

