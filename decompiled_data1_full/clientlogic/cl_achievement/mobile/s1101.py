# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1101.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1101.pyc
# Source Generated with Decompyle++
# File: s1101.pyc (Python 3.6)

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
    cl_evact.AchieveCBAddStat(oListener, oEventCB, (lambda *a: Func364(*a)))


class CAchieveStat(CCustom):
    m_SID = 1101
    m_Name = '勤俭节约'
    m_TargetValue = 10000
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

