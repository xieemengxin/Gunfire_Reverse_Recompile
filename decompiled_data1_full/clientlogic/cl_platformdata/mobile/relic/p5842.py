# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5842.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5842.pyc
# Source Generated with Decompyle++
# File: p5842.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import BUYRULE_CASHREFRESHFREE, BUYRULE_REFRESHFREE, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddHeroBuyRule(oWarrior, oLifeCycle, BUYRULE_REFRESHFREE, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddHeroBuyRule(oWarrior, oLifeCycle, BUYRULE_CASHREFRESHFREE, 1)
    cl_action.CommonAddHeroBuyRule(oWarrior, oLifeCycle, BUYRULE_REFRESHFREE, 1)


class CPerform(CCustomPerform):
    m_SID = 5842
    m_Name = '货如轮转'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

