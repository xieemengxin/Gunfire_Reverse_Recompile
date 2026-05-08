# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1050.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1050.pyc
# Source Generated with Decompyle++
# File: s1050.pyc (Python 3.6)

from cl_commondefines import SETTLE_FINISHWAR
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.AchieveListenTeamMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERSETTLE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.AchieveCBAddWarStat(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 10) and cl_evcon.CheckSettleType(oListener, oEventCB, SETTLE_FINISHWAR):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1050
    m_Name = '艰难困苦'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }

