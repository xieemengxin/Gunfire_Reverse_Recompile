# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5859.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5859.pyc
# Source Generated with Decompyle++
# File: p5859.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL, TALENT_CHOOSE_NOMAL, TALENT_CHOOSE_PHASE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetTalentChooseAllTimes(oWarrior, oLifeCycle, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TALENT_CHOOSE_BEFORE, TALENT_CHOOSE_NOMAL, 0, 0, 5)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TALENT_CHOOSE_BEFORE, TALENT_CHOOSE_PHASE, 0, 0, 5)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1865, 0, { }, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetTalentChooseAllTimes(oWarrior, oLifeCycle, 5)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TALENT_CHOOSE_BEFORE, TALENT_CHOOSE_NOMAL, 1, 0, 5)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TALENT_CHOOSE_BEFORE, TALENT_CHOOSE_PHASE, 1, 0, 5)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1865, 0, { }, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetNumTalentGen(oWarrior, oEventCB, 2)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetNumTalentGen(oWarrior, oEventCB, 2)


class CPerform(CCustomPerform):
    m_SID = 5859
    m_Name = '塞翁失马'
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
    m_DropShape = 5524
    m_ValidRemove = 0
    m_BasePrice = 120
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

