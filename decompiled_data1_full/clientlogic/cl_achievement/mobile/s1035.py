# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1035.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1035.pyc
# Source Generated with Decompyle++
# File: s1035.pyc (Python 3.6)

from cl_achievement.customaction import CustomCBAction1035 as CustomCBAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckTargetAddState(oListener, oEventCB, 32101):
        CustomCBAction(oListener, oEventCB, { })


class CAchieveStat(CCustom):
    m_SID = 1035
    m_Name = '源力大师'
    m_TargetValue = 100000
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

