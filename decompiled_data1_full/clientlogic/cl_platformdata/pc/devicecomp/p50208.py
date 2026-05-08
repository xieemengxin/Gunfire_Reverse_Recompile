# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50208.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50208.pyc
# Source Generated with Decompyle++
# File: p50208.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_HERO
from cl_newformula import Func645

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12025)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8012)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1411, 0, 0):
        if cl_condition.CheckDeciveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 0, 1):
            cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12025, '', 0, None, { })
        elif (cl_condition.CheckDeciveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 1, 1) or cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func645(*a))) > 0) and cl_evcon.CheckSelfDeviceInRaycastRange(oWarrior, oEventCB, 7):
            cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12025, '', 0, None, { })


class CPerform(CCustomPerform):
    m_SID = 50208
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
    m_ExclusiveHero = (206,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

