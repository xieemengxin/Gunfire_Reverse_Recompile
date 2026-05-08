# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season5/t1015.pyc
# RelativePath: clientlogic/cl_season/pc/season5/t1015.pyc
# Source Generated with Decompyle++
# File: t1015.pyc (Python 3.6)

from cl_newformula import Func597
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
    cl_action.CommonDirectEventCBFunc(oListener, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oListener, oLifeCycle, 'MoveSpeed', -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.CBSetWarSeasonTaskValue(oListener, oEventCB, (lambda *a: Func597(*a)))
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 300):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 300):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1015
    m_TargetValue = 1
    m_TaskValue = 500
    m_ShowTotalValue = 300
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

