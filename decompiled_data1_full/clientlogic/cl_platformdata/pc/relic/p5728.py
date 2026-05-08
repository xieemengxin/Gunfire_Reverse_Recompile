# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5728.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5728.pyc
# Source Generated with Decompyle++
# File: p5728.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, 10000, 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4503, 10000, 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4502, 10000, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, 15000, 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4503, 15000, 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4502, 15000, 0)


class CPerform(CCustomPerform):
    m_SID = 5728
    m_Name = '弹药腰带'
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
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 20
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

