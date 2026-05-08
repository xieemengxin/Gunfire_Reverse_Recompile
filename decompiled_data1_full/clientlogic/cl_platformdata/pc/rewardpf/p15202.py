# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15202.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15202.pyc
# Source Generated with Decompyle++
# File: p15202.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import PERFORMCDRATE_TYPE_CAREER, PERFORMCDRATE_TYPE_PASSIVE, PERFORMCDRATE_TYPE_SHIFT

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1011, 0, {
        'MoveSpeedMul': -2000 }, 1)
    cl_action.CommonAddPerformCDTimer(oWarrior, oLifeCycle, 50, None)
    cl_action.CommonChangePerformCDRate(oWarrior, oLifeCycle, PERFORMCDRATE_TYPE_CAREER | PERFORMCDRATE_TYPE_PASSIVE | PERFORMCDRATE_TYPE_SHIFT, 3000, 0)


class CPerform(CCustomPerform):
    m_SID = 15202
    m_Name = '稳健步伐'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 1

