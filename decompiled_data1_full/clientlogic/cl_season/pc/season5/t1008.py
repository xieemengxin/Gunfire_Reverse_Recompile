# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season5/t1008.pyc
# RelativePath: clientlogic/cl_season/pc/season5/t1008.pyc
# Source Generated with Decompyle++
# File: t1008.pyc (Python 3.6)

from cl_commondefines import LEVEL_TYPE_HIDE, OBJ_ENEMY, OBJ_SELF, OBJ_VICTIM
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_INTERACT_PERFORM_HIT_TARGET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetSideType(oListener, oEventCB, OBJ_ENEMY) and cl_evcon.EventCBCheckInteractReHit(oListener, oEventCB, 'S5Task_1008') == 0:
        cl_evact.EventCBSetInteractHitFlag(oListener, oEventCB, 'S5Task_1008')
        cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, 1)
        if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 10):
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.CheckTargetSideType(oListener, oEventCB, OBJ_ENEMY) and cl_evcon.EventCBCheckInteractReHit(oListener, oEventCB, 'S5Task_1008') == 0:
        cl_evact.EventCBSetInteractHitFlag(oListener, oEventCB, 'S5Task_1008')
        cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, 1)
        if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 10):
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction2(oEventCB, oListener):
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 10):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction3(oEventCB, oListener):
    if not cl_evcon.CheckLevelType(oListener, oEventCB, LEVEL_TYPE_HIDE):
        cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_SELF)
        cl_evact.EventCBDelTargetCustomData(oListener, oEventCB, 'S5Task_1008')


class CSeasonTask(CCustom):
    m_SID = 1008
    m_TargetValue = 1
    m_TaskValue = 500
    m_ShowTotalValue = 10
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

