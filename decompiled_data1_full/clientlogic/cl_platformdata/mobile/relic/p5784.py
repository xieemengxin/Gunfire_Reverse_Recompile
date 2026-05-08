# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5784.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5784.pyc
# Source Generated with Decompyle++
# File: p5784.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_ATTACK, OBJ_VICTIM, QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL, WARRIOR_BOSS, WARRIOR_ELITE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 3, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1525, 1000, { }, 1, 0, None)
    cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 1003, 1525, {
        'MoveSpeedMul': -1000 }, 1, 1, 1)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 25):
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)
    elif cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 40):
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 30):
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)
    elif cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 5784
    m_Name = '门板重盾'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

