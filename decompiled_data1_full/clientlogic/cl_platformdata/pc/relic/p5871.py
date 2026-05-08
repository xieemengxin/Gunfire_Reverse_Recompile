# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5871.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5871.pyc
# Source Generated with Decompyle++
# File: p5871.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import PF_SUBMSG_THROW, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33036, 300, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33037, 300, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33036, 1, 'SkillOver')
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33037, 1, 'SkillOver')
    cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33034)
    cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33035)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33071, 300, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33072, 300, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 3, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33071, 1, 'SkillOver')
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33072, 1, 'SkillOver')
    cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33069)
    cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33070)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33034, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33035, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33069, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33070, 0)


class CPerform(CCustomPerform):
    m_SID = 5871
    m_Name = '心无二用'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

