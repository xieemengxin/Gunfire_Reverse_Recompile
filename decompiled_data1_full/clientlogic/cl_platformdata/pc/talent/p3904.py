# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3904.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3904.pyc
# Source Generated with Decompyle++
# File: p3904.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPlantAttrMul(oWarrior, oLifeCycle, 'PlantHpAdd', 2000)
    cl_action.CommonAddPlantAttrMul(oWarrior, oLifeCycle, 'PlantAttDisAdd', 5)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPlantAttrMul(oWarrior, oLifeCycle, 'PlantHpAdd', 3000)
    cl_action.CommonAddPlantAttrMul(oWarrior, oLifeCycle, 'PlantAttDisAdd', 10)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPlantAttrMul(oWarrior, oLifeCycle, 'PlantHpAdd', 4000)
    cl_action.CommonAddPlantAttrMul(oWarrior, oLifeCycle, 'PlantAttDisAdd', 84)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1333, 0, 0) and cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'HitMonster') == 0:
        cl_evact.EventCBGetTargetBySkillCustomData(oWarrior, oEventCB, 'CreatePlant')
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33745, 0, { }, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 3904
    m_Name = '#NT#觉醒占位'
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
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 120

