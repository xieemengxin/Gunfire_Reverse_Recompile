# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p15801.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p15801.pyc
# Source Generated with Decompyle++
# File: p15801.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_HIGH, RELIC_TYPE_BOSS

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33424, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33425, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 15801
    m_Name = '连城秘卷'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_BOSS
    m_DropShape = 5568
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_HIGH

