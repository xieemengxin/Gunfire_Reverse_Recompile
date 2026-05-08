# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1404.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1404.pyc
# Source Generated with Decompyle++
# File: s1404.pyc (Python 3.6)

from cl_commondefines import ACHIEVEMENT_TYPE_EMOTION, ATTACKERSUBMSG_NORMAL
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1404
    m_Name = '#NT#破千军'
    m_Type = ACHIEVEMENT_TYPE_EMOTION
    m_TargetValue = 1000
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

