# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1008.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1008.pyc
# Source Generated with Decompyle++
# File: s1008.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 1, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckHasState(oListener, oEventCB, 20027):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1008
    m_Name = '致命毒气'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

