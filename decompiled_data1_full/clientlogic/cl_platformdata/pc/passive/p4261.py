# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4261.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4261.pyc
# Source Generated with Decompyle++
# File: p4261.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_ATTACK, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKED, -1, 0, 1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, -1, 0)
    cl_action.CommonSetSkillCheckArgs(oWarrior, oLifeCycle, 30, 30)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 105, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonSetSkillCheckArgs(oWarrior, oEventCB.GetCBLifeCycle(), 30, 30)


class CPerform(CCustomPerform):
    m_SID = 4261
    m_Name = '四幕boss被动3'
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

