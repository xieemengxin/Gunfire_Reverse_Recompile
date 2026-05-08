# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5818.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5818.pyc
# Source Generated with Decompyle++
# File: p5818.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_ATTACK, PF_SUBMSG_CAREERPF, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 0, None):
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1669, 0, { })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 0, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 25, WARRIOR_MONSTER, 1, 1, 3, 0, 1, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 2)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBUsePerform(oWarrior, oEventCB, 1698, 0, { })


class CPerform(CCustomPerform):
    m_SID = 5818
    m_Name = '步步惊雷'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

