# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5333.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5333.pyc
# Source Generated with Decompyle++
# File: p5333.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT3_KEY_IGNELBEEXECUTED, FIGHT3_KEY_IGNOREIMMOBILIZE, FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, FIGHT3_KEY_IGNOREUNBALANCE, FIGHT_KEY_IGNOREEXECTORCHOOSE, STATE_CLS_ABNORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1009, 0, { }, 1)
    cl_action.CommonRemoveAllStateByType(oWarrior, oLifeCycle, STATE_CLS_ABNORMAL)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNELBEEXECUTED)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREIMMOBILIZE)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREUNBALANCE)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNORETHUMP)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.CommonAddSpecialKey(oWarrior, oLifeCycle, FIGHT_KEY_IGNOREEXECTORCHOOSE, 0)
    cl_action.CommonSetNavMeshSize(oWarrior, oLifeCycle, 1, 0)
    cl_action.CommonForbid(oWarrior, oLifeCycle, 1111)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetNavMeshSize(oWarrior, oLifeCycle, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5333
    m_Name = '精英蟹先锋三阶段'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

