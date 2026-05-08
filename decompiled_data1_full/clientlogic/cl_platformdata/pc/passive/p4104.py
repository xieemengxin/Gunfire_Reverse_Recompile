# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4104.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4104.pyc
# Source Generated with Decompyle++
# File: p4104.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 7933, 0, 0, None):
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1634, 0, { })
        cl_evact.PassiveCBDisableSelf(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 4104
    m_Name = '挑战事件死亡毒气爆炸'
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

