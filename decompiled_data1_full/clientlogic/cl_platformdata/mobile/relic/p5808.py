# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5808.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5808.pyc
# Source Generated with Decompyle++
# File: p5808.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_BUILD, MG_SOURCE_SMASHOBSTACLE, OBJ_VICTIM, OBSTACLE_JAR, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_BUILD, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_BUILD, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsPointClasses(oWarrior, oEventCB, OBSTACLE_JAR):
        cl_evact.CommonCBTargetDropReward(oWarrior, oEventCB, {
            102: 1,
            502: 1,
            401: 1 }, {
            102: 10000,
            502: 3000,
            401: 200 }, 0, MG_SOURCE_SMASHOBSTACLE, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsPointClasses(oWarrior, oEventCB, OBSTACLE_JAR):
        cl_evact.CommonCBTargetDropReward(oWarrior, oEventCB, {
            102: 1,
            502: 1,
            401: 1 }, {
            102: 10000,
            502: 5000,
            401: 500 }, 0, MG_SOURCE_SMASHOBSTACLE, None, None)


class CPerform(CCustomPerform):
    m_SID = 5808
    m_Name = '刮地三尺'
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
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 20
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

