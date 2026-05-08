# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13606.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13606.pyc
# Source Generated with Decompyle++
# File: p13606.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddDiceShopNpcEnergy(oWarrior, oLifeCycle, 0, 2)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33696, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 13606
    m_Name = '废骰点金'
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
    m_Career = None

