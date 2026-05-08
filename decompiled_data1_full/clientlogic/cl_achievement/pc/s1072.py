# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1072.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1072.pyc
# Source Generated with Decompyle++
# File: s1072.pyc (Python 3.6)

from cl_only import Frame2Time
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckTargetAddState(oListener, oEventCB, 32006):
        CustomCBAction(oListener, oEventCB, { })


class CAchieveStat(CCustom):
    m_SID = 1072
    m_Name = '雷神附体'
    m_TargetValue = 100000
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }


def CustomCBAction(oListener, oEventCB, dArgs):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'LastFrame' not in dMsgInfo:
        return None
    iTime = Frame2Time(dMsgInfo['LastFrame'])
    cl_evact.AchieveCBAddStat(oListener, oEventCB, iTime)

