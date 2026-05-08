# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50219.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50219.pyc
# Source Generated with Decompyle++
# File: p50219.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33095, 800, { }, 0)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33095, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 50219
    m_Name = '英雄核心'
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
    m_ExclusiveDevice = (1002,)
    m_ExclusiveHero = (214,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

