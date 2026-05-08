# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1403.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1403.pyc
# Source Generated with Decompyle++
# File: s1403.pyc (Python 3.6)

from cl_commondefines import ACHIEVEMENT_TYPE_EMOTION, RESCUE_SUBMSG_SUCCESS
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_RESCUE, RESCUE_SUBMSG_SUCCESS, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1403
    m_Name = '#NT#感谢'
    m_Type = ACHIEVEMENT_TYPE_EMOTION
    m_TargetValue = 3
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

