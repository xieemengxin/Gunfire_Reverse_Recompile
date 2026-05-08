# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5719.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5719.pyc
# Source Generated with Decompyle++
# File: p5719.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func327

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func327(*a) * 1 + 0)) >= 20:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 1373, 0, 0, None, None):
            cl_evact.PassiveSubPerformCD(oWarrior, oEventCB, 1310, 10000)
            if cl_evcon.CheckHasState(oWarrior, oEventCB, 32774) or cl_evcon.CheckHasState(oWarrior, oEventCB, 32004) or cl_evcon.CheckHasState(oWarrior, oEventCB, 32006) or cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33700) == 0:
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1797, 0, { }, 1, 1, None)
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1538, 0, { }, 1, 1, None)
            else:
                cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 0, 100)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1373, 200, { }, 1, 0, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func327(*a) * 1 + 0)) >= 20:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 1373, 0, 0, None, None):
            cl_evact.PassiveSubPerformCD(oWarrior, oEventCB, 1310, 10000)
            if cl_evcon.CheckHasState(oWarrior, oEventCB, 32774) or cl_evcon.CheckHasState(oWarrior, oEventCB, 32004) or cl_evcon.CheckHasState(oWarrior, oEventCB, 32006) or cl_evcon.CheckHasState(oWarrior, oEventCB, 33044) or cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33700) == 0:
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1539, 0, { }, 1, 1, None)
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1538, 0, { }, 1, 1, None)
            else:
                cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 0, 100)
                cl_action.CommonAddCareerPfTempUseTimes(oWarrior, oEventCB.GetCBLifeCycle(), 1, 0, 1, 1)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1373, 200, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 5719
    m_Name = '回光返照'
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
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

