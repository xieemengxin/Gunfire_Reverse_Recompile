# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season8/t1015.pyc
# RelativePath: clientlogic/cl_season/pc/season8/t1015.pyc
# Source Generated with Decompyle++
# File: t1015.pyc (Python 3.6)

from cl_commondefines import S7_MODULE_POINT_CHANGE
from cl_newformula import Func854
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func854(*a, **{
'iTarget': 10 }))) >= 1:
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1015
    m_TargetValue = 1
    m_TaskValue = 500
    m_ShowTotalValue = 1
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

