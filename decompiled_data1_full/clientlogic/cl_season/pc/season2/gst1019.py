# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season2/gst1019.pyc
# RelativePath: clientlogic/cl_season/pc/season2/gst1019.pyc
# Source Generated with Decompyle++
# File: gst1019.pyc (Python 3.6)

from season import action
from season.mobject import CSeasonTask as CCustom
import tools.msgcenter
import commonact
import eventact
import eventcondi

def RewardAction(oTarget, sReason):
    action.SeasonTaskRewardGSCash(oTarget, sReason, 50)


def EnableAction(oTarget, oLifeCycle):
    commonact.CommonListenMsgCallBack(oTarget, oLifeCycle, tools.msgcenter.MSG_PLAYER_CONSUMECASH, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oTarget):
    eventact.CBAddSeasonTaskValueByConsumeCash(oTarget, oEventCB)


class CSeasonTask(CCustom):
    m_SID = 1019
    m_TargetValue = 3000
    m_TaskValue = 1
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = []

