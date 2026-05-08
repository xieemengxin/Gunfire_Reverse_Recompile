# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4326.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4326.pyc
# Source Generated with Decompyle++
# File: p4326.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import PHASE_CHALLENGE_END

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, PHASE_CHALLENGE_END, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonSetDieRemoveDelay(oWarrior, oEventCB.GetCBLifeCycle(), 500)
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 23411, 0, { })


class CPerform(CCustomPerform):
    m_SID = 4326
    m_Name = '【幸存者】宝箱怪逃跑'
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
    m_DieDisable = 1

