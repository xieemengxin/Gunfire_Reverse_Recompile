# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1096.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1096.pyc
# Source Generated with Decompyle++
# File: s1096.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_BLOCK, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1096
    m_Name = '绝对防御'
    m_TargetValue = 500
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

