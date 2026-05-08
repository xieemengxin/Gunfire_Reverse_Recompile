# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14604.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14604.pyc
# Source Generated with Decompyle++
# File: p14604.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeSubAttackMsgType(oWarrior, oLifeCycle, ATTACKERSUBMSG_NORMAL)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 1200, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 1961, { })


class CPerform(CCustomPerform):
    m_SID = 14604
    m_Name = '首领秘卷妖王装置'
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

