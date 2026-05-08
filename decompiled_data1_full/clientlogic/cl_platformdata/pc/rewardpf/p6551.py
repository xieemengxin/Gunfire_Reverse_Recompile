# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p6551.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p6551.pyc
# Source Generated with Decompyle++
# File: p6551.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, MG_SOURCE_KILLMONSTER, OBJ_VICTIM, WARRIOR_BOSS, WARRIOR_ELITE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if (cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE)) and cl_evcon.CheackTargetFightTypeIsRealit(oWarrior, oEventCB):
        cl_evact.CommonCBTargetDropReward(oWarrior, oEventCB, {
            1001: 1 }, {
            1001: 10000 }, 0, MG_SOURCE_KILLMONSTER, 1, None)


class CPerform(CCustomPerform):
    m_SID = 6551
    m_Name = '武器猎人'
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

