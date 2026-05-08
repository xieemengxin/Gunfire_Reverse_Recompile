# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25769.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25769.pyc
# Source Generated with Decompyle++
# File: p25769.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import MONSTERPF_TYPE_ATTACK, OBJ_SELF, PF_TYPE_MONSTERACT, QUALITY_TYPE_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_MONSTERACT, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.CheckMonsterPFAttackType(oWarrior, oEventCB, MONSTERPF_TYPE_ATTACK) and cl_evcon.CheckHasState(oWarrior, oEventCB, 1745) == 0:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1670, 50, { }, 1, -1, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1745, 200, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 25769
    m_Name = '中场休息'
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
    m_RelicType = 0
    m_HeroRelic = 5769
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

