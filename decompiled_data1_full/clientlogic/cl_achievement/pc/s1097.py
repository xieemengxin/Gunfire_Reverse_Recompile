# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1097.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1097.pyc
# Source Generated with Decompyle++
# File: s1097.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.AchieveListenWarMgrMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckLayerAndLevel(oListener, oEventCB, 4, 3):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1097
    m_Name = '破晓黎明'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

