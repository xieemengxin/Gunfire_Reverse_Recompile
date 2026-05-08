# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p50114.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p50114.pyc
# Source Generated with Decompyle++
# File: p50114.pyc (Python 3.6)

from cl_platformdata.custom.passive.customaction import CustomAction50102 as CustomAction1
from cl_platformdata.custom.passive.customaction import ClearAddToxicNumInfo as CustomAction3
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTER_ADD_TOXICSTATECOUNT, -1, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction1(oWarrior, oEventCB, {
        'TriggerNum': 4 })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventCBStartThrowSkill(oWarrior, oEventCB, 1413, 1, { })


def DoCallBackAction2(oEventCB, oWarrior):
    CustomAction3(oWarrior, oEventCB, { })


class CPerform(CCustomPerform):
    m_SID = 50114
    m_Name = '#NT#毒气组件连环闪电被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

