# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4249.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4249.pyc
# Source Generated with Decompyle++
# File: p4249.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import LEVEL_TYPE_BOSS

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1404, 0, { }, 1)
    if cl_condition.CheckOpenElement(oWarrior, oLifeCycle, {
        'WandElement': 1 }):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33618, 0, { }, 1)
    if cl_condition.CheckOpenCycle(oWarrior, oLifeCycle) and cl_condition.CheckWarCycle(oWarrior, oLifeCycle) == 10:
        cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_ROOMGOAL, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.CommonAddDeadPunishmentTimes(oWarrior, oEventCB.GetCBLifeCycle(), -1)


class CPerform(CCustomPerform):
    m_SID = 4249
    m_Name = '英雄通用被动技能'
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

