# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14060.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14060.pyc
# Source Generated with Decompyle++
# File: p14060.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MONSTER_PFAI_CATCH

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPFAIGroupWeightByType(oWarrior, oLifeCycle, MONSTER_PFAI_CATCH, 21124, 10)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 8135):
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 21123, 0, { })


class CPerform(CCustomPerform):
    m_SID = 14060
    m_Name = '轮回9-剧毒鲶兵'
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

