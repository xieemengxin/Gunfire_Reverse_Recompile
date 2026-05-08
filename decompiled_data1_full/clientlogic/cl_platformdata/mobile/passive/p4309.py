# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4309.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4309.pyc
# Source Generated with Decompyle++
# File: p4309.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction4309 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT_KEY_WUDI, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 1, 1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 2, 1, 0)
    cl_action.CommonAddSpecialKey(oWarrior, oLifeCycle, FIGHT_KEY_WUDI, None)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB.GetCBLifeCycle(), {
        'SceneCenter': (0, 0, 0),
        'Dis': 4,
        'Size': (7, 4, 7),
        'UsePerformStateSID': 8098,
        'AttractSID': 8080,
        'NoAttractSID': 8082 })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 39023, 0, 0) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 39029, 0, 0):
        cl_action.CommonRemoveSpecialKey(oWarrior, oEventCB.GetCBLifeCycle(), FIGHT_KEY_WUDI)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1445, 100, { }, 0, 0, None)
        cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 1713, None, { }, None)
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 4309, 0, None, None)


class CPerform(CCustomPerform):
    m_SID = 4309
    m_Name = '罗睺-石柱被动'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

