# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1034.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1034.pyc
# Source Generated with Decompyle++
# File: s1034.pyc (Python 3.6)

from cl_commondefines import DUAL_STATE_BEGIN
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.AchieveAddFollowState(oListener, oEventCB, 32238, 32004, { }, 0)


class CAchieveStat(CCustom):
    m_SID = 1034
    m_Name = '双持精英'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

