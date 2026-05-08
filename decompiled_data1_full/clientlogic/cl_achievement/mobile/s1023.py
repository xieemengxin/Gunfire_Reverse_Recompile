# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1023.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1023.pyc
# Source Generated with Decompyle++
# File: s1023.pyc (Python 3.6)

from cl_item.defines import QUALITY_TYPE_HIGH
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.GetRelicNumByQuality(oListener, oEventCB, QUALITY_TYPE_HIGH) >= 5:
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1023
    m_Name = '出神入化'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

