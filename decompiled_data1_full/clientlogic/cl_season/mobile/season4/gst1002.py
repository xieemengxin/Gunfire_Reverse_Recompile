# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/mobile/season4/gst1002.pyc
# RelativePath: clientlogic/cl_season/mobile/season4/gst1002.pyc
# Source Generated with Decompyle++
# File: gst1002.pyc (Python 3.6)

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
    pass


def EnableAction(oTarget, oLifeCycle):
    commonact.CommonListenMsgCallBack(oTarget, oLifeCycle, tools.msgcenter.MSG_PLAYER_WARENDBEFORE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oTarget):
    if eventcondi.CommonCBCheckWarEndType(oTarget, oEventCB, SETTLE_FINISHWAR) and eventcondi.CommonCBGetSeasonNum(oTarget, oEventCB) == 3 and eventcondi.CommonCBSeasonDamageProportionFromReport(oTarget, oEventCB) > 80:
        eventact.CBAddSeasonTaskValue(oTarget, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1002
    m_TargetValue = 10
    m_TaskValue = 500
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

