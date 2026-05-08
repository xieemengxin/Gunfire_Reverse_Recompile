# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p4691.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p4691.pyc
# Source Generated with Decompyle++
# File: p4691.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF, WARRIOR_NORBATTERY, WARRIOR_NORDART, WARRIOR_NORHEVFAR, WARRIOR_NORMAGIC, WARRIOR_NORMEDFAR, WARRIOR_NORSMAFAR, WARRIOR_NORSNIPE, WARRIOR_NORTHROW

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORSMAFAR) or cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORMEDFAR) or cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORHEVFAR) or cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORTHROW) or cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORSNIPE) or cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORBATTERY) or cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORMAGIC) or cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORDART):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 1316, 0, { }, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.GetSceneData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF-4691Head') >= 1 and cl_condition.GetSceneData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF-4691Head') < 2 or cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 10, 1) or cl_condition.GetSceneData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF-4691Head') < 1:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1314, 0, { }, 0)
        cl_evact.PassiveCBChangeSceneData(oWarrior, oEventCB, 'PF-4691Head', 1, 0)
        cl_evact.EventGetAllMonsterByTargetScene(oWarrior, oEventCB, 1, None, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1316, 0, { }, 0, 0, None)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1316, 0, { }, 0, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1314, 0, 0, None):
        cl_evact.PassiveCBChangeSceneData(oWarrior, oEventCB, 'PF-4691Head', -1, 0)
        cl_evact.EventGetAllMonsterByTargetScene(oWarrior, oEventCB, 1, None, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1316, 0, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4691
    m_Name = '远程怪有10%的概率获得【头目】buff'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

