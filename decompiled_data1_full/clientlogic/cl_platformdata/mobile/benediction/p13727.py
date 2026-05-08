# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13727.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13727.pyc
# Source Generated with Decompyle++
# File: p13727.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_newformula import Func598, Func735
from cl_commondefines import DEFEND_TREND_ARMOR, DEFEND_TREND_SHIELD, PERFORMCDRATE_TYPE_CAREER, PERFORMCDRATE_TYPE_PASSIVE, PERFORMCDRATE_TYPE_SHIFT

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'PF13727' }))) == 0:
        cl_action.CommonSetSavedData(oWarrior, oLifeCycle, 'PF13727', 1)
        cl_action.CommonAddBlankRelic(oWarrior, oLifeCycle, 3)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33478, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ACTIVE_SEASONSUIT, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVE_SEASONSUIT, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonAddPerformCDTimer(oWarrior, oLifeCycle, 50, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33478, (lambda *a: Func735(*a)))
    cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: Func735(*a) * 2000), 0, 1)
    cl_action.CommonChangePerformCDRate(oWarrior, oEventCB.GetCBLifeCycle(), PERFORMCDRATE_TYPE_CAREER | PERFORMCDRATE_TYPE_PASSIVE | PERFORMCDRATE_TYPE_SHIFT, (lambda *a: Func735(*a) * 500), 0)
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: Func735(*a) * 1000), 0)
    if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func735(*a) * 1000), 0)
    elif cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: Func735(*a) * 1000), 0)


class CPerform(CCustomPerform):
    m_SID = 13727
    m_Name = '积少成多'
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

