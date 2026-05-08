# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5806.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5806.pyc
# Source Generated with Decompyle++
# File: p5806.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, OBJ_SELF, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func357

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, None, None)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 10, 50, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckTotalCureSource(oWarrior, oEventCB, 1069, DAM_USE_SHIELD) or cl_evcon.CheckTotalCureSource(oWarrior, oEventCB, 1069, DAM_USE_ARMOR) or cl_evcon.CheckTotalCureSource(oWarrior, oEventCB, 1069, DAM_USE_HP):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventGetHeroTarget(oWarrior, oEventCB, 1, 1, 1, 0)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1225, 50, {
        'Cure': (lambda *a: Func357(*a) * 25 / 100) }, 1, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if oWarrior.HP() >= oWarrior.QueryAttr('HPMax') and cl_condition.CheckHasPerform(oWarrior, oEventCB.GetCBLifeCycle(), 6540):
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1442, 0)
        cl_evact.EventGetHeroTarget(oWarrior, oEventCB, 1, 1, 1, 0)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 3)
    else:
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1442, 1)
        cl_evact.EventGetHeroTarget(oWarrior, oEventCB, 1, 1, 1, 0)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 3)


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1441, 0, 0, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1442, 0, 0, None):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1441, 0, { }, 1, 0, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1441, 0, None, None)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1442, 0, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 5806
    m_Name = '有福同享'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

