# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1219.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1219.pyc
# Source Generated with Decompyle++
# File: s1219.pyc (Python 3.6)

from cl_commondefines import PF_SUBMSG_CAREERPF
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 219):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckFromPointPerform(oListener, oEventCB, 1325, 1, 0):
        cl_evact.AchieveCBAddState(oListener, oEventCB, 33302, 0, { }, 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.EventCBCheckFromPointState(oListener, oEventCB, 33040):
        cl_evact.AchieveAddFollowState(oListener, oEventCB, 33302, 33040, { }, 1)


class CAchieveStat(CCustom):
    m_SID = 1219
    m_Name = '玄灵墨影'
    m_TargetValue = 2000
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }

