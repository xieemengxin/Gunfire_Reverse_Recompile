# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season5/t1048.pyc
# RelativePath: clientlogic/cl_season/pc/season5/t1048.pyc
# Source Generated with Decompyle++
# File: t1048.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD
from cl_newformula import Func589
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
    cl_action.CommonListenMsgCallBackByAttr(oListener, oLifeCycle, 'HPMax', -1, 0, 0, 0)
    if cl_condition.CheckTargetDefendTrend(oListener, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonListenMsgCallBackByAttr(oListener, oLifeCycle, 'ShieldMax', -1, 0, 0, 0)
    else:
        cl_action.CommonListenMsgCallBackByAttr(oListener, oLifeCycle, 'ArmorMax', -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.CBSetWarSeasonTaskValue(oListener, oEventCB, (lambda *a: Func589(*a) // 100))
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 1000):
        cl_evact.CBSetSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1048
    m_TargetValue = 1
    m_TaskValue = 1500
    m_ShowTotalValue = 1000
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

