# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1010.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1010.pyc
# Source Generated with Decompyle++
# File: s1010.pyc (Python 3.6)

from cl_newformula import Func207
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.GetFormula(oListener, oEventCB, (lambda *a: Func207(*a) * 100 / 100 + 0)) >= 4000:
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1010
    m_Name = '含恨而终'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

