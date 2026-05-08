# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5742.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5742.pyc
# Source Generated with Decompyle++
# File: p5742.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_HP, NWARRIOR_DROP_BULLET, NWARRIOR_DROP_CASH, OBJ_SELF, PICK_BULLET, PICK_CASH, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_CASH, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_BULLET, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 4, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1379, 0, { }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_BULLET, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_CASH, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 4, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1379, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oWarrior, oEventCB, 100, CURE_TYPE_PERFORM | DAM_USE_HP, 1, None, None)
    if oWarrior.QueryAttr('HPMax') == oWarrior.HP():
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1379, 1, 0, 0, 1000)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckPickType(oWarrior, oEventCB, NWARRIOR_DROP_CASH) or cl_evcon.CheckPickType(oWarrior, oEventCB, NWARRIOR_DROP_BULLET):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, 100, CURE_TYPE_PERFORM | DAM_USE_HP, 1, None, None)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1379, 1, 0, 0, 1000)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1379, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 5742
    m_Name = '生命之源'
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
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

