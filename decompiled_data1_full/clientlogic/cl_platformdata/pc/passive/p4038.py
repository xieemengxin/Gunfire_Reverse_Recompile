# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4038.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4038.pyc
# Source Generated with Decompyle++
# File: p4038.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT3_KEY_IGNOREKNOCKBACK
from cl_newformula import Func235

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 3000, 0, None)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.CommonSetMonsterAgentConfig(oWarrior, oLifeCycle, 'RangedPosR', 7)
    cl_action.CommonSetMonsterAgentConfig(oWarrior, oLifeCycle, 'RangedPosMinDis', 2)
    cl_action.CommonSetMonsterAgentConfig(oWarrior, oLifeCycle, 'RangedPosMaxDis', 4)
    cl_action.CommonSetMonsterAgentConfig(oWarrior, oLifeCycle, 'RangedPosMinAngle', 60)
    cl_action.CommonSetMonsterAgentConfig(oWarrior, oLifeCycle, 'RangedPosMaxAngle', 80)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func235(*a, **{
'sType': 'RidingAlone' }))) >= 2:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 7088, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 4038
    m_Name = '首层BOSS-阶段3'
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

