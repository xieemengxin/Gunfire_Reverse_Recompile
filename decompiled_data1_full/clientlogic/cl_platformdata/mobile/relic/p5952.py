# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5952.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5952.pyc
# Source Generated with Decompyle++
# File: p5952.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_CURSE, RELIC_TYPE_CURSE

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11046, 1)


class CPerform(CCustomPerform):
    m_SID = 5952
    m_Name = '弹夹克星'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'StateSID': 33359 }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_CURSE
    m_DropShape = 5531
    m_ValidRemove = 0
    m_BasePrice = 0
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_CURSE

