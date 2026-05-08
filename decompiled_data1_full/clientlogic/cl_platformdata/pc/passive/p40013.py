# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p40013.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p40013.pyc
# Source Generated with Decompyle++
# File: p40013.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_PERSISTENCE, LEVEL_TYPE_FIGHT, OBJ_ATTACK, TASK_CHANGESTATUS, TASK_STATUS_SUCCESS, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetTaskSaveInfo(oWarrior, oLifeCycle, 'Shield', 1600)
    cl_action.PassiveSetTaskSaveInfo(oWarrior, oLifeCycle, 'HP', 1400)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 0, cl_action.PassiveGetTaskSaveInfo(oWarrior, oLifeCycle, 'Shield'), 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, cl_action.PassiveGetTaskSaveInfo(oWarrior, oLifeCycle, 'Shield'), 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 0, cl_action.PassiveGetTaskSaveInfo(oWarrior, oLifeCycle, 'HP'), 0)
    if not cl_condition.PassiveCheckTaskStatus(oWarrior, oLifeCycle, TASK_STATUS_SUCCESS):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 5, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TASK, TASK_CHANGESTATUS, 4, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 50)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER) and cl_evcon.CheckTargetDist(oWarrior, oEventCB, 10, 0, None) and cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERSISTENCE) == 0:
            if cl_evcon.PassiveCBGetTaskSaveInfo(oWarrior, oEventCB, 'Shield') > 0:
                cl_action.PassiveAddTaskSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), 'Shield', -200)
                cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, cl_action.PassiveGetTaskSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), 'Shield'), 0)
                cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, cl_action.PassiveGetTaskSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), 'Shield'), 0)
            elif cl_evcon.PassiveCBGetTaskSaveInfo(oWarrior, oEventCB, 'HP') > 0:
                cl_action.PassiveAddTaskSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), 'HP', -200)
                cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 0, cl_action.PassiveGetTaskSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), 'HP'), 0)
            else:
                cl_action.PassiveRemoveSelfOnTask(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_condition.PassiveCheckTaskStatus(oWarrior, oEventCB.GetCBLifeCycle(), TASK_STATUS_SUCCESS):
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_TASK, TASK_CHANGESTATUS)
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ENTERSCENE, -1)
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    else:
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1)


class CPerform(CCustomPerform):
    m_SID = 40013
    m_Name = '天降大任-避其锋芒2奖励'
    m_MaxLevel = 1
    m_MaxStack = 0
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

