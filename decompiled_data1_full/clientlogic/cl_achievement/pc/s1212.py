# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1212.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1212.pyc
# Source Generated with Decompyle++
# File: s1212.pyc (Python 3.6)

from cl_commondefines import PF_SUBMSG_CAREERPF
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckFromPointPerform(oListener, oEventCB, 1317, 1, 1) and cl_evcon.EventCBCheckPerformMode(oListener, oEventCB) == 4:
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1212
    m_Name = '天命之选'
    m_TargetValue = 200
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

