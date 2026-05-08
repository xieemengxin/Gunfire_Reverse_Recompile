# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15181.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15181.pyc
# Source Generated with Decompyle++
# File: p15181.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import OBJECT_OWNER, OBJ_ATTACK, OBJ_SELF, PF_SUBMSG_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33482, 0, { }, 1)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 1)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0) == 0 and cl_evcon.CheckTargetDist(oWarrior, oEventCB, 15, 0, OBJECT_OWNER):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33482, 1, 1, 1, 300)


class CPerform(CCustomPerform):
    m_SID = 15181
    m_Name = '狐假虎威'
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

