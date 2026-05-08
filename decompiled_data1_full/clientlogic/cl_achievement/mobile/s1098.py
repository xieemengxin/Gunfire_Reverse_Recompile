# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1098.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1098.pyc
# Source Generated with Decompyle++
# File: s1098.pyc (Python 3.6)

from cl_commondefines import OBJ_VICTIM
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.AchieveListenGlobalMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckTargetAddState(oListener, oEventCB, 8005):
        cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
        if (cl_evcon.CheckTargetPointBaseMonster(oListener, oEventCB, 3924) or cl_evcon.CheckTargetPointBaseMonster(oListener, oEventCB, 3925)) and cl_evcon.EventCBGetTargetStateRemainingTime(oListener, oEventCB, 7985, 0) > 0 and cl_evcon.EventCBGetTargetStateRemainingTime(oListener, oEventCB, 7985, 0) <= 300:
            cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if (cl_evcon.CheckTargetPointBaseMonster(oListener, oEventCB, 3924) or cl_evcon.CheckTargetPointBaseMonster(oListener, oEventCB, 3925)) and cl_evcon.EventCBGetTargetStateRemainingTime(oListener, oEventCB, 7985, 0) > 0 and cl_evcon.EventCBGetTargetStateRemainingTime(oListener, oEventCB, 7985, 0) <= 300:
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1098
    m_Name = '屏住呼吸'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }

