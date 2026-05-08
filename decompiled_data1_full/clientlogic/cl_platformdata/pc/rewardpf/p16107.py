# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16107.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16107.pyc
# Source Generated with Decompyle++
# File: p16107.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import OBJ_VICTIM, SIDE_TYPE_MONSTER, SIDE_TYPE_VERTIGO, WARRIOR_ELITE, WARRIOR_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, SIDE_TYPE_MONSTER, 0)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, SIDE_TYPE_VERTIGO, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetDist(oWarrior, oEventCB, 25, 0, 0):
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
            cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), 3000, 0)
        elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAL):
            cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), 100, 0)


class CPerform(CCustomPerform):
    m_SID = 16107
    m_Name = '气元汲取'
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

