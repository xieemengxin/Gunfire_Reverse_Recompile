# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1026.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1026.pyc
# Source Generated with Decompyle++
# File: s1026.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckHitWeakness(oListener, oEventCB, None):
        cl_evact.AchieveCBAddWarStat(oListener, oEventCB, 1)
    else:
        cl_evact.AchieveCBResetWarStat(oListener, oEventCB)
    if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 100):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1026
    m_Name = '精准射手'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

