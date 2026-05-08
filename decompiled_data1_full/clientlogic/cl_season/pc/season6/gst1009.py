# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season6/gst1009.pyc
# RelativePath: clientlogic/cl_season/pc/season6/gst1009.pyc
# Source Generated with Decompyle++
# File: gst1009.pyc (Python 3.6)


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
    commonact.CommonListenMsgCallBack(oTarget, oLifeCycle, tools.msgcenter.MSG_PLAYER_CONSUMECASH, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oTarget):
    eventact.CBAddSeasonTaskValueByConsumeCash(oTarget, oEventCB)


class CSeasonTask(CCustom):
    m_SID = 1009
    m_TargetValue = 1000
    m_TaskValue = 500
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

