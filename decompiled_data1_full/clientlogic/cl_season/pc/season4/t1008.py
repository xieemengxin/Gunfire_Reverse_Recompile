# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season4/t1008.pyc
# RelativePath: clientlogic/cl_season/pc/season4/t1008.pyc
# Source Generated with Decompyle++
# File: t1008.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ENEMY, OBJ_VICTIM, PF_SUBMSG_THROW, PF_TYPE_THROW
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from branch import *
from ...mobject import CSeasonTask as CCustom

def RewardAction(oTarget, sReason):
    pass


def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 217) == 0 and cl_condition.CheckHero(oListener, oLifeCycle, 205) == 0 and cl_condition.CheckHero(oListener, oLifeCycle, 218) == 0:
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 1, 0, 0)
    if cl_condition.CheckHero(oListener, oLifeCycle, 217):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 1, 0, 0)
    if cl_condition.CheckHero(oListener, oLifeCycle, 218):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_EXPLOSION, -1, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 1, 0, 0)
    if cl_condition.CheckHero(oListener, oLifeCycle, 205):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckPerformType(oListener, oEventCB, PF_TYPE_THROW, 0) and cl_evcon.CheckTargetSideType(oListener, oEventCB, OBJ_ENEMY):
        cl_evact.EventCBRecordSkillCollectTarget(oListener, oEventCB, 's4task1008', 0)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evact.EventCBGetSkillCollectTargetNum(oListener, oEventCB, 's4task1008', 0) > cl_evcon.SeasonTaskCBGetWarValue(oListener, oEventCB):
        cl_evact.CBSetWarSeasonTaskValue(oListener, oEventCB, cl_evact.EventCBGetSkillCollectTargetNum(oListener, oEventCB, 's4task1008', None))
        if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 8):
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)
    cl_evact.EventCBClearCollectInfo(oListener, oEventCB, 's4task1008', 0)


def DoCallBackAction2(oEventCB, oListener):
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 8):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction3(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckDamFromSelf(oListener, oEventCB, 1):
        cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckPerformType(oListener, oEventCB, PF_TYPE_THROW, 0) and cl_evcon.CheckTargetSideType(oListener, oEventCB, OBJ_ENEMY):
            cl_evact.EventCBRecordSkillCollectTarget(oListener, oEventCB, 's4task1008', 0)


def DoCallBackAction4(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckPerformType(oListener, oEventCB, PF_TYPE_THROW, 0) and cl_evcon.CheckTargetSideType(oListener, oEventCB, OBJ_ENEMY):
        cl_evact.EventCBRecordSkillCollectTarget(oListener, oEventCB, 's4task1008', 1)
        if cl_evact.EventCBGetSkillCollectTargetNum(oListener, oEventCB, 's4task1008', 1) > cl_evcon.SeasonTaskCBGetWarValue(oListener, oEventCB):
            cl_evact.CBSetWarSeasonTaskValue(oListener, oEventCB, cl_evact.EventCBGetSkillCollectTargetNum(oListener, oEventCB, 's4task1008', 1))
            if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 8):
                cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction5(oEventCB, oListener):
    if cl_evact.EventCBGetSkillCollectTargetNum(oListener, oEventCB, 's4task1008', 1) > cl_evcon.SeasonTaskCBGetWarValue(oListener, oEventCB):
        cl_evact.CBSetWarSeasonTaskValue(oListener, oEventCB, cl_evact.EventCBGetSkillCollectTargetNum(oListener, oEventCB, 's4task1008', 1))
        if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 8):
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1008
    m_TargetValue = 1
    m_TaskValue = 500
    m_ShowTotalValue = 8
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

