# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5038.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5038.pyc
# Source Generated with Decompyle++
# File: p5038.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import CREATE_SEED
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_SEED, CREATE_SEED, 0, 0, 0)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1436, 'ParasiticMul', 20000, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetTargetByID(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'SeedID' })))
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33847, 0, { }, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5038
    m_Name = '遍地生花'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 1
    m_IsRareTalent = 1
    m_Career = 119

