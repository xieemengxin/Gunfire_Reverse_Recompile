# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14420.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14420.pyc
# Source Generated with Decompyle++
# File: p14420.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_THUNDER, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_THUNDER, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, -5000, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 33586):
        cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 33809, 33586, { }, 1, 0, 1)


class CPerform(CCustomPerform):
    m_SID = 14420
    m_Name = '轮回9-鲨鱼怪被动'
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

