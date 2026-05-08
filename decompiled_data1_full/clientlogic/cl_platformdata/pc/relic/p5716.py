# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5716.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5716.pyc
# Source Generated with Decompyle++
# File: p5716.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL, TYPE_RELIFE_RELIC
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'RShield', -5000, 0, -1)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldRecoverTime', 10000, 0, -1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 1227):
        cl_action.CommonSetRelifeAttr(oWarrior, oLifeCycle, TYPE_RELIFE_RELIC, 300, (lambda *a: Func410(*a, **{
'sid': 1227 })), 1, { }, 0, None)
    else:
        cl_action.CommonSetRelifeAttr(oWarrior, oLifeCycle, TYPE_RELIFE_RELIC, 300, 2, 1, { }, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTRELIFES, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1227, 0, { }, 0)


def Action2(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 1227):
        cl_action.CommonSetRelifeAttr(oWarrior, oLifeCycle, TYPE_RELIFE_RELIC, 300, (lambda *a: Func410(*a, **{
'sid': 1227 })), 1, { }, 0, None)
    else:
        cl_action.CommonSetRelifeAttr(oWarrior, oLifeCycle, TYPE_RELIFE_RELIC, 300, 2, 1, { }, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTRELIFES, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1227, 0, { }, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRelifeTimesKey(oWarrior, oEventCB):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1227, -1, 0)
    cl_evact.PassiveCBCalPFRelifeTimes(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 5716
    m_Name = '三重轮回'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 0
    m_BasePrice = 160
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

