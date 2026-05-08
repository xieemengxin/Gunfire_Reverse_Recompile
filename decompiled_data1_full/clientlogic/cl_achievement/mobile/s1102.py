# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1102.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1102.pyc
# Source Generated with Decompyle++
# File: s1102.pyc (Python 3.6)

from cl_newformula import Func364
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_RECYCLEDROP, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.AchieveCBAddWarStat(oListener, oEventCB, (lambda *a: Func364(*a)))
    if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1000):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1102
    m_Name = '吃干抹净'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

