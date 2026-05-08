# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season4/t1013.pyc
# RelativePath: clientlogic/cl_season/pc/season4/t1013.pyc
# Source Generated with Decompyle++
# File: t1013.pyc (Python 3.6)

from cl_commondefines import STATUS_DASH
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_MOVESTATUSCHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckMoveStatus(oListener, oEventCB, STATUS_DASH):
        cl_evact.EventCBRecordCurPos(oListener, oEventCB, 'seasontask_1013')
    elif cl_evcon.CheckLastMoveStatus(oListener, oEventCB, STATUS_DASH):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, cl_evact.EventCBGetDistance(oListener, oEventCB, 'seasontask_1013'))


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.CheckLastMoveStatus(oListener, oEventCB, STATUS_DASH):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, cl_evact.EventCBGetDistance(oListener, oEventCB, 'seasontask_1013'))


def DoCallBackAction2(oEventCB, oListener):
    if cl_evcon.CheckMoveStatus(oListener, oEventCB, STATUS_DASH):
        cl_evact.EventCBRecordCurPos(oListener, oEventCB, 'seasontask_1013')


class CSeasonTask(CCustom):
    m_SID = 1013
    m_TargetValue = 10000
    m_TaskValue = 500
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

