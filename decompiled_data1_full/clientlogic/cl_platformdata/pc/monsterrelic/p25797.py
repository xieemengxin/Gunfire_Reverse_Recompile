# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25797.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25797.pyc
# Source Generated with Decompyle++
# File: p25797.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1679, 0, { }, -1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 20028, 0, { }, -1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1822, 0, { }, -1)


class CPerform(CCustomPerform):
    m_SID = 25797
    m_Name = '雷电狂热'
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
    m_HeroRelic = 5797
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

