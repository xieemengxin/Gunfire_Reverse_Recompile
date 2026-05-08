# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14608.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14608.pyc
# Source Generated with Decompyle++
# File: p14608.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import WARRIOR_ELITE, WARRIOR_NORMAL

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORMAL):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.GetSceneData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF-4691Head') < 3 and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('EffectVal')):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33717, 0, { }, 1)
    else:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33716, 0, { }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELITE):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33716, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 14608
    m_Name = '骰子挑战3技能'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 1

