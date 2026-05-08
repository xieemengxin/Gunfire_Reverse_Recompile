# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14401.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14401.pyc
# Source Generated with Decompyle++
# File: p14401.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 10000, 0, -1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATEMONSTER, -1, 1, 1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CBCheckCastingSkill(oWarrior, oEventCB, 39014):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, -9000, 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetPhase(oWarrior, oEventCB, 3)
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 7088, 0)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7137, 0, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 14401
    m_Name = '轮回9-陆吾'
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
    m_DieDisable = 0

