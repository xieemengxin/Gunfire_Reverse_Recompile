# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5775.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5775.pyc
# Source Generated with Decompyle++
# File: p5775.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import LEVEL_TYPE_HIDE, OBJ_SELF, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func304, Func553

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALCURE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 3, 0, -1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveState(oWarrior, oLifeCycle, 1803)
    cl_action.CommonRemoveState(oWarrior, oLifeCycle, 1485)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 4, 0, -1)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemoveState(oWarrior, oLifeCycle, 1802)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1486, 0, { }, 1, 0, None)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1803, None, None, None)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1485, None, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1803, (lambda *a: Func553(*a, **{
'sAttr': 'HP' }) * 100 // Func304(*a, **{
'sAttr': 'HPMax' })), 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1486, 0, { }, 1, 0, None)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1802, None, None, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckEnterNewSecne(oWarrior, oEventCB) and cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HIDE) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1486, 0, { }, 1, 0, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1803, None, None, None)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1485, None, None, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckEnterNewSecne(oWarrior, oEventCB) and cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HIDE) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1486, 0, { }, 1, 0, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1802, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 5775
    m_Name = '复原灵龛'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2 }
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
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

