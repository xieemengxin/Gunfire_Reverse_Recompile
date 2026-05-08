# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season2/gst1018.pyc
# RelativePath: clientlogic/cl_season/pc/season2/gst1018.pyc
# Source Generated with Decompyle++
# File: gst1018.pyc (Python 3.6)

from cl_commondefines import SEASONSUBTASK_TYPE_MAX, SEASONTASK_EXTINFO_TYPE_DEVICE, SETTLE_FINISHWAR

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
    if eventcondi.CommonCBCheckWarEndType(oTarget, oEventCB, SETTLE_FINISHWAR) and eventcondi.CommonCBGetSeasonNum(oTarget, oEventCB) == 2:
        eventact.CBAddSeasonSonTaskValue(oTarget, oEventCB, 'Device', 1, SEASONSUBTASK_TYPE_MAX)


class CSeasonTask(CCustom):
    m_SID = 1018
    m_TargetValue = 3
    m_TaskValue = 1
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = []
    m_SubTaskInfo = {
        SEASONTASK_EXTINFO_TYPE_DEVICE: {
            1001: 3,
            1002: 3,
            1003: 3 } }

