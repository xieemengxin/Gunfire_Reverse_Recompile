# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p50259.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p50259.pyc
# Source Generated with Decompyle++
# File: p50259.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DEVICE_CONTROL_ACTIVE, DEVICE_CONTROL_UNACTIVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_ACTIVE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_UNACTIVE, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SkillInterval'), 2)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonDeviceUsePF(oWarrior, oEventCB.GetCBLifeCycle(), 7204, {
        'FromDevice': 1 })


class CPerform(CCustomPerform):
    m_SID = 50259
    m_Name = '#NT#毒雾技能释放控制'
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
    m_BaseArgData = {
        'SkillInterval': 200 }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'SkillInterval': 200 } }

