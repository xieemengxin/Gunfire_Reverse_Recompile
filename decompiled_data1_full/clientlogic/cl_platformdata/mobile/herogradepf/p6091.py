# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6091.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6091.pyc
# Source Generated with Decompyle++
# File: p6091.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeRollRelicCnt(oWarrior, oLifeCycle, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckReason(oWarrior, oEventCB, 'load', 0) == 0 and cl_evcon.CheckReason(oWarrior, oEventCB, 'ExchangeRewardChooseTalentGame', 1) == 0 and cl_evcon.CheckNPCSID(oWarrior, oEventCB, 30011067) == 0:
        cl_action.CommonChangeUpgradeRelicCnt(oWarrior, oEventCB.GetCBLifeCycle(), 2)
        cl_action.CommonChangeRollRelicCnt(oWarrior, oEventCB.GetCBLifeCycle(), 1)


class CPerform(CCustomPerform):
    m_SID = 6091
    m_Name = '赌侠lv.1'
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

