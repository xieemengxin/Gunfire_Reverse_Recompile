# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1209.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1209.pyc
# Source Generated with Decompyle++
# File: s1209.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, PLAYMODE_ROGUELIKE, WARRIOR_ELITE
from cl_newformula import Func221
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckWarPlayMode(oListener, oLifeCycle, PLAYMODE_ROGUELIKE) and cl_condition.CalFormula(oListener, oLifeCycle, (lambda *a: Func221(*a))) >= 1:
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckMonsterType(oListener, oEventCB) and cl_evcon.CheckFightType(oListener, oEventCB, WARRIOR_ELITE):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1209
    m_Name = '地狱猎手'
    m_TargetValue = 30
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

