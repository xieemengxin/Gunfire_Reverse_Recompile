# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1213.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1213.pyc
# Source Generated with Decompyle++
# File: s1213.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL, WARRIOR_NORMAL
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 217):
        cl_action.CommonListenServantMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckFromPointPerform(oListener, oEventCB, 7153, 1, 0) and cl_evcon.CheckVictimFightType(oListener, oEventCB, WARRIOR_NORMAL):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1213
    m_Name = '遮风挡雨'
    m_TargetValue = 500
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

