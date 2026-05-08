# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51731.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51731.pyc
# Source Generated with Decompyle++
# File: p51731.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, PF_TYPE_S8THIRDACTIVE
from cl_newformula import Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_S8THIRDACTIVE, 0) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func859(*a, **{
'sAttr': 'DrawingProbability' }))):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            4: 3400,
            5: 3300,
            6: 3300 }, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_S8THIRDACTIVE, 0) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 30):
        cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_CORRISION, 10000, 0)
        cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_FIRE, 10000, 0)
        cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_THUNDER, 10000, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func859(*a, **{
'sAttr': 'DrawingProbability' }))):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            4: 3400,
            5: 3300,
            6: 3300 }, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 30):
        cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_CORRISION, 10000, 0)
        cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_FIRE, 10000, 0)
        cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_THUNDER, 10000, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_THUNDER, 10000, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_CORRISION, 10000, 0)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_FIRE, 10000, 0)


class CPerform(CCustomPerform):
    m_SID = 51731
    m_Name = '施加元素异常'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'DrawingProbability': 10 },
        2: {
            'DrawingProbability': 30 } }

