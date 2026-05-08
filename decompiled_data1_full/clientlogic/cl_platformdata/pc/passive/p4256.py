# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4256.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4256.pyc
# Source Generated with Decompyle++
# File: p4256.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7983, 1, None, None)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1009, 100, { }, -1)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1500, 0, -1)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 1070, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 32101, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7085, 200, { }, -1)
    cl_action.CommonSwitchMonsterAtt(oWarrior, oLifeCycle, 23814)


class CPerform(CCustomPerform):
    m_SID = 4256
    m_Name = '测试版骑乘怪阶段二-切换为主体模型'
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

