# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season2/gst1045.pyc
# RelativePath: clientlogic/cl_season/pc/season2/gst1045.pyc
# Source Generated with Decompyle++
# File: gst1045.pyc (Python 3.6)

from cl_commondefines import SETTLE_FINISHWAR

try:
    from season import action
    from season.mobject import CSeasonTask as CCustom
    import commonact
    import eventact
    import eventcondi
except:
    
    class CCustom(object):
        pass


import tools.msgcenter

def RewardAction(oTarget, sReason):
    action.SeasonTaskRewardGSCash(oTarget, sReason, 150)


def EnableAction(oTarget, oLifeCycle):
    commonact.CommonListenMsgCallBack(oTarget, oLifeCycle, tools.msgcenter.MSG_PLAYER_WAREND, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oTarget):
    if eventcondi.CommonCBCheckWarEndType(oTarget, oEventCB, SETTLE_FINISHWAR) and eventcondi.CommonCBHPMax(oTarget, oEventCB) > 49900 and eventcondi.CommonCBGetSeasonNum(oTarget, oEventCB) == 2:
        eventact.CBAddSeasonTaskValue(oTarget, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1045
    m_TargetValue = 1
    m_TaskValue = 1
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

