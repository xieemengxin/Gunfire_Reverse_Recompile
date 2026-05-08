# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13701.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13701.pyc
# Source Generated with Decompyle++
# File: p13701.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckHasSavedData(oWarrior, oLifeCycle, 'pf13701') == 0:
        cl_action.CommonSetSavedData(oWarrior, oLifeCycle, 'pf13701', 1)
        cl_action.CommonAddWarCash(oWarrior, oLifeCycle, 2000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETWARCASH, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBChangeGetCash(oWarrior, oEventCB, 5000, 0)


class CPerform(CCustomPerform):
    m_SID = 13701
    m_Name = '公平交易'
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
    m_Career = None

