# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16105.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16105.pyc
# Source Generated with Decompyle++
# File: p16105.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION, FUNCMODE_TYPE_AIMCORRISIONMONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 4000, DAM_TYPE_CORRISION, 1)
    cl_action.CommonSwitchMode(oWarrior, oLifeCycle, FUNCMODE_TYPE_AIMCORRISIONMONSTER, 1, { }, None)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1436, 'ExtraMonsterBoom', 1, 1)


class CPerform(CCustomPerform):
    m_SID = 16105
    m_Name = '园丁灵气模块2'
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

