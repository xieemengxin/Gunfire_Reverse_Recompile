# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1088.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1088.pyc
# Source Generated with Decompyle++
# File: s1088.pyc (Python 3.6)

from cl_commondefines import PLAYMODE_ROGUELIKE, SETTLE_FINISHWAR, TYPE_RELIFE_GSCASH
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERSETTLE, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oListener, oLifeCycle, 2, None, None)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1) and cl_evcon.CheckRelifeType(oListener, oEventCB, TYPE_RELIFE_GSCASH):
        cl_evact.AchieveCBAddWarStat(oListener, oEventCB, -1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1) and cl_evcon.CheckSettleType(oListener, oEventCB, SETTLE_FINISHWAR):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


def DoCallBackAction2(oEventCB, oListener):
    if cl_evcon.CheckWarPlayMode(oListener, oEventCB, PLAYMODE_ROGUELIKE):
        cl_evact.AchieveCBAddWarStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1088
    m_Name = '一命通关'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }

