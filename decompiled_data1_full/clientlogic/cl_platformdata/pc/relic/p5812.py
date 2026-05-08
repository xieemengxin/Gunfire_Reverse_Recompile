# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5812.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5812.pyc
# Source Generated with Decompyle++
# File: p5812.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'MaxCover', 0, 1, None)
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'ColdTime', 3000, 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'MaxCover', 0, 2, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MaxCover', 0, 1, None)
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ColdTime', 3000, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MaxCover', 0, 2, None)


class CPerform(CCustomPerform):
    m_SID = 5812
    m_Name = '储能核心'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

