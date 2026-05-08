# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14044.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14044.pyc
# Source Generated with Decompyle++
# File: p14044.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MONSTER_PFAI_CATCH

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4060, 'NeverShow', 1, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4061, 'NeverShow', 1, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 0, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 5000, 0, -1)
    cl_action.CommonSetPFAIGroupWeightByType(oWarrior, oLifeCycle, MONSTER_PFAI_CATCH, 21421, 30)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldRecoverTime', -5000, 0, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 7942, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 14044
    m_Name = '轮回9-马贼隐士'
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

