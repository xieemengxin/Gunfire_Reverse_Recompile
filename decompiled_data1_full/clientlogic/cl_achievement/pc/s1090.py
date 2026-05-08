# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1090.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1090.pyc
# Source Generated with Decompyle++
# File: s1090.pyc (Python 3.6)

from cl_commondefines import PF_SUBMSG_CAREERPF, PLAYMODE_ROGUELIKE
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 201) and cl_condition.CheckWarPlayMode(oListener, oLifeCycle, PLAYMODE_ROGUELIKE):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckFromPointPerform(oListener, oEventCB, 1301, 0, 0):
        cl_evact.AchieveAddFollowState(oListener, oEventCB, 32608, 32004, { }, 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.EventCBCheckFromPointState(oListener, oEventCB, 32608):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
        cl_evact.AchieveRewardCheek(oListener, oEventCB, 1005)


class CAchieveStat(CCustom):
    m_SID = 1090
    m_Name = '火力全开'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }

