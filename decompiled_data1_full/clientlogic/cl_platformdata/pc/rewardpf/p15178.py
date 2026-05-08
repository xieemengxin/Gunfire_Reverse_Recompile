# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15178.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15178.pyc
# Source Generated with Decompyle++
# File: p15178.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DAM_USE_ALL, DEFEND_TREND_ARMOR, DEFEND_TREND_SHIELD, OBJ_SELF
from cl_newformula import Func558, Func589

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 0, 0, 0)
    cl_action.CommonAddNeedSubCDState(oWarrior, oLifeCycle, 33475)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func558(*a))) < 50 and cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33475) == 0 and oWarrior.HP() > 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func589(*a) * 0.25), 0 | DAM_USE_ALL, 0, 1, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33475, 1500, { }, 1, 0, 0)
        if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
            cl_action.CommonAddExcessAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Shield', 10000, 0, 0)
        elif cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
            cl_action.CommonAddExcessAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Armor', 10000, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 15178
    m_Name = '应急防护'
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

