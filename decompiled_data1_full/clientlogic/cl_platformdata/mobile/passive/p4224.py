# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4224.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4224.pyc
# Source Generated with Decompyle++
# File: p4224.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import STATE_CLS_ABNORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7983, 1, None, None)
    cl_action.CommonSwitchMonsterAtt(oWarrior, oLifeCycle, 23814)
    cl_action.CommonRemoveAllStateByType(oWarrior, oLifeCycle, STATE_CLS_ABNORMAL)


class CPerform(CCustomPerform):
    m_SID = 4224
    m_Name = '骑乘怪阶段二-切换为主体模型'
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

