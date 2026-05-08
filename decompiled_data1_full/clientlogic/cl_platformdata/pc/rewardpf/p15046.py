# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15046.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15046.pyc
# Source Generated with Decompyle++
# File: p15046.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import FIGHT3_KEY_IGNELECORRISION, FIGHT3_KEY_IGNELEFIRE, FIGHT3_KEY_IGNELETHUNDER

def Action1(oWarrior, oLifeCycle):
    cl_action.ImmunitySubSpdState(oWarrior, oLifeCycle)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNELECORRISION)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNELEFIRE)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNELETHUNDER)


class CPerform(CCustomPerform):
    m_SID = 15046
    m_Name = '神圣之躯（已弃置）'
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

