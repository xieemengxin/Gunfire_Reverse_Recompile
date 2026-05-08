# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p40070.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p40070.pyc
# Source Generated with Decompyle++
# File: p40070.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import NWARRIOR_NPC_TASKNPC, TASK_TYPE_HIDE, TASK_TYPE_LEGENDARY, TASK_TYPE_NORMAL, TASK_TYPE_RARE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_NPCCREATEOVER, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_TASKNPC):
        cl_evact.EventCBLimitNPCChooseTask(oWarrior, oEventCB, 3, {
            TASK_TYPE_HIDE: 1,
            TASK_TYPE_LEGENDARY: 1,
            TASK_TYPE_RARE: 1,
            TASK_TYPE_NORMAL: 1 })
        cl_action.PassiveRemoveSelfOnTask(oWarrior, oEventCB.GetCBLifeCycle())


class CPerform(CCustomPerform):
    m_SID = 40070
    m_Name = '天降大任-犹豫不决1特殊效果'
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

