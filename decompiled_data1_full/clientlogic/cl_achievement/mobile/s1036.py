# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1036.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1036.pyc
# Source Generated with Decompyle++
# File: s1036.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_BUILD
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_BUILD, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1036
    m_Name = '闲情逸致'
    m_TargetValue = 3000
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

