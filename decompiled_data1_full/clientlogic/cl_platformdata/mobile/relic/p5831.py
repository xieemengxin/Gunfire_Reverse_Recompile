# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5831.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5831.pyc
# Source Generated with Decompyle++
# File: p5831.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1419, 0, { }, 1)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'RShield', -5000, 0, -1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1419, 0, { }, 1)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'RShield', -2500, 0, -1)


class CPerform(CCustomPerform):
    m_SID = 5831
    m_Name = '涌能护盾'
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
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

