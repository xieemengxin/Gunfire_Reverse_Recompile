# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1044.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1044.pyc
# Source Generated with Decompyle++
# File: s1044.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEMIXDEBUFF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckTargetAddState(oListener, oEventCB, 1070):
        cl_evact.AchieveCBAddWarStat(oListener, oEventCB, 1)
        if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 50):
            cl_evact.AchieveCBAddStat(oListener, oEventCB, 50)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 50):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 50)


class CAchieveStat(CCustom):
    m_SID = 1044
    m_Name = '致幻毒药'
    m_TargetValue = 50
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }

