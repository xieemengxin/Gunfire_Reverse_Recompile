# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16103.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16103.pyc
# Source Generated with Decompyle++
# File: p16103.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import MG_TALENT

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPGRADEREWARD_CREATE, -1, 0, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_TALENT):
        cl_evact.EventCBSetMiniGameChooseCnt(oWarrior, oEventCB, 4)


class CPerform(CCustomPerform):
    m_SID = 16103
    m_Name = '深度觉醒'
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

