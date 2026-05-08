# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3801.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3801.pyc
# Source Generated with Decompyle++
# File: p3801.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import CREATE_PLANT, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPlantAttrMul(oWarrior, oLifeCycle, 'PlantAttMul', 12000)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPlantAttrMul(oWarrior, oLifeCycle, 'PlantAttMul', 24000)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPlantAttrMul(oWarrior, oLifeCycle, 'PlantAttMul', 36000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33731, 0, { }, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 3801
    m_Name = '灵植强化'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 119

