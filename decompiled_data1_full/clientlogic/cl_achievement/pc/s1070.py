# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1070.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1070.pyc
# Source Generated with Decompyle++
# File: s1070.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ENEMY, OBJ_VICTIM
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.AchieveListenGlobalMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetSideType(oListener, oEventCB, OBJ_ENEMY) and cl_evcon.CheckInPointPerform(oListener, oEventCB, {
        1605: 1,
        1609: 1,
        1658: 1 }, 0, 0):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1070
    m_Name = '爆桶艺术'
    m_TargetValue = 100
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

