# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4399.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4399.pyc
# Source Generated with Decompyle++
# File: p4399.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MG_SOURCE_KILLMONSTER, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckIsEndless(oWarrior, oLifeCycle):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.CommonCBDropReward(oWarrior, oEventCB, {
        2404: 1,
        4101: 1 }, {
        2404: 10000,
        4101: 10000 }, 0, MG_SOURCE_KILLMONSTER, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 4399
    m_Name = '无尽旅途四幕boss额外掉落'
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

