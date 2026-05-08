# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1061.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1061.pyc
# Source Generated with Decompyle++
# File: s1061.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckFromPointPerform(oListener, oEventCB, 1304, 0, None):
        cl_evact.PassiveCBSetCollectInfo(oListener, oEventCB, 'KillCnt', 1, 0)
        if cl_evcon.CheckSkillCollectInfo(oListener, oEventCB, 'KillCnt', None) == 5:
            cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.CheckSkillCollectInfo(oListener, oEventCB, 'KillCnt', None) == 5:
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1061
    m_Name = '凌空一击'
    m_TargetValue = 50
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }

