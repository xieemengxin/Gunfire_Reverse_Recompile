# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25834.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25834.pyc
# Source Generated with Decompyle++
# File: p25834.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'AttSpeed', -3000, 0, -1)
    cl_action.CommonChangeAllAtivePerformAttr(oWarrior, oLifeCycle, 'ColdTime', -3000, 0)


class CPerform(CCustomPerform):
    m_SID = 25834
    m_Name = '交叉火力'
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
    m_RelicType = 0
    m_HeroRelic = 5834
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

