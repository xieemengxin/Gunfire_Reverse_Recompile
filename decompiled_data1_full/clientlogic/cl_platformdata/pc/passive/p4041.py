# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4041.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4041.pyc
# Source Generated with Decompyle++
# File: p4041.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_USE_HP

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 1, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 0, -5000000, None)
    cl_action.CommonChangeDefValue(oWarrior, oLifeCycle, 3000000, DAM_USE_HP)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7023, 600, { }, 1)
    cl_action.HaltAllCasting(oWarrior, oLifeCycle.Key())
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7024, 1, None, None)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7027, 1, None, None)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7032, 1, None, None)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7030, 1, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetPhase(oWarrior, oEventCB, 4)


class CPerform(CCustomPerform):
    m_SID = 4041
    m_Name = '组队BOSS-阶段3'
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

