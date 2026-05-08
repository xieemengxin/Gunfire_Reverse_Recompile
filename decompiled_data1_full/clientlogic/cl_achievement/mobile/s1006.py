# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1006.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1006.pyc
# Source Generated with Decompyle++
# File: s1006.pyc (Python 3.6)

from cl_commondefines import OBJ_ATTACK, WARRIOR_BUILD_TRAP
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oListener, oEventCB, WARRIOR_BUILD_TRAP):
        cl_evact.AchieveCBAddWarStat(oListener, oEventCB, 1)
    if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 2):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1006
    m_Name = '手抖驾校'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

