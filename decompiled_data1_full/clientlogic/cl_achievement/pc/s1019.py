# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1019.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1019.pyc
# Source Generated with Decompyle++
# File: s1019.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL, LEVEL_TYPE_BOSS, OBJ_VICTIM, WARRIOR_BOSS
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.AchieveListenTeamMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1) and cl_evcon.GetSingleDamageNum(oListener, oEventCB) > 0 and cl_evcon.CheckDamFromSelf(oListener, oEventCB, None) == False:
        cl_evact.AchieveCBAddWarStat(oListener, oEventCB, -1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1):
        cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oListener, oEventCB, WARRIOR_BOSS) and cl_evcon.CheackTargetFightTypeIsRealit(oListener, oEventCB):
            cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


def DoCallBackAction2(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oListener, oEventCB, WARRIOR_BOSS) and cl_evcon.CheackTargetFightTypeIsRealit(oListener, oEventCB):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


def DoCallBackAction3(oEventCB, oListener):
    if cl_evcon.CheckLevelType(oListener, oEventCB, LEVEL_TYPE_BOSS):
        cl_evact.AchieveCBAddWarStat(oListener, oEventCB, 1)
    else:
        cl_evact.AchieveCBResetWarStat(oListener, oEventCB)


class CAchieveStat(CCustom):
    m_SID = 1019
    m_Name = '灵巧身法'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }

