# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13545.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13545.pyc
# Source Generated with Decompyle++
# File: p13545.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import QUALITY_TYPE_CURSE, QUALITY_TYPE_HIGH, QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_GROOVE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_REPLACE_QUALITY, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33409):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33409, 500, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33409, 1, 500)
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'ClearCnt', 1)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ClearCnt') >= 6:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ClearCnt', 0)
        cl_evact.EventCBDirectEventCBFuncByNum(oWarrior, oEventCB, cl_action.CommonSimulationChooseQuality(oWarrior, oEventCB.GetCBLifeCycle()), {
            QUALITY_TYPE_CURSE: 4,
            QUALITY_TYPE_HIGH: 3,
            QUALITY_TYPE_NORMAL: 2,
            QUALITY_TYPE_LOW: 1 })


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33410):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33410, 1000, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33410, 1, 1000)
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 134, 0, QUALITY_TYPE_LOW, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33411):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33411, 1000, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33411, 1, 1000)
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 134, 0, QUALITY_TYPE_NORMAL, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33412):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33412, 1000, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33412, 1, 1000)
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 134, 0, QUALITY_TYPE_HIGH, 1)


def DoCallBackAction4(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33410):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33410, 1000, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33410, 1, 1000)
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33411):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33411, 1000, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33411, 1, 1000)
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33412):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33412, 1000, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33412, 1, 1000)
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 134, 0, QUALITY_TYPE_CURSE, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33410):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33410, 1000, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33410, 1, 1000)


def DoCallBackAction6(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33411):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33411, 1000, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33411, 1, 1000)


def DoCallBackAction7(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33412):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33412, 1000, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33412, 1, 1000)


class CPerform(CCustomPerform):
    m_SID = 13545
    m_Name = '万用套牌'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 113

