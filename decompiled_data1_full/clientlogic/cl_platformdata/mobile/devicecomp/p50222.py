# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50222.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50222.pyc
# Source Generated with Decompyle++
# File: p50222.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_HERO, FROM_OWNER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BARRIER_THROUGH, FROM_OWNER, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1425, 0, 0):
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33144) == 0:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33144, 400, { }, 1, 0, None)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33144, 1, 400)


class CPerform(CCustomPerform):
    m_SID = 50222
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
    m_ExclusiveDevice = (1003,)
    m_ExclusiveHero = (216,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

