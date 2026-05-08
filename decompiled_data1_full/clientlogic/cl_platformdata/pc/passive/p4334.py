# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4334.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4334.pyc
# Source Generated with Decompyle++
# File: p4334.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT3_KEY_IGNELECORRISION, FIGHT3_KEY_IGNELEFIRE, FIGHT3_KEY_IGNELETHUNDER, FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, STATE_EFF_DEBAR, STATE_EFF_SUBSPD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 0, 400, -1)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'Att', 5000, 0, -1)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'AttSpeed', -3000, 0, -1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1210, 0, { }, -1)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNORETHUMP)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.CommonIgnoreStateEffectAdd(oWarrior, oLifeCycle, STATE_EFF_DEBAR, None)
    cl_action.CommonIgnoreStateEffectAdd(oWarrior, oLifeCycle, STATE_EFF_SUBSPD, None)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNELECORRISION)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNELEFIRE)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNELETHUNDER)


class CPerform(CCustomPerform):
    m_SID = 4334
    m_Name = '黄金精英怪-二阶段'
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

