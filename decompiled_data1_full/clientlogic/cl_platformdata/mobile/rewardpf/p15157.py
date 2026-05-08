# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15157.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15157.pyc
# Source Generated with Decompyle++
# File: p15157.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import PF_SUBMSG_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'ColdTime', -1500, 0, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 20):
        cl_evact.EventReduceBulletUse(oWarrior, oEventCB, 1011)


class CPerform(CCustomPerform):
    m_SID = 15157
    m_Name = '法力充沛'
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

