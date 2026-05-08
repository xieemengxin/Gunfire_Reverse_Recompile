# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season3/t1039.pyc
# RelativePath: clientlogic/cl_season/pc/season3/t1039.pyc
# Source Generated with Decompyle++
# File: t1039.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, PET_ENTER_BATTLE, PET_LEAVE_BATTLE, WARRIOR_MONSTER
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from branch import *
from ...mobject import CSeasonTask as CCustom

def RewardAction(oTarget, sReason):
    pass


def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PFNODEKILL, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_EXECUTE, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oListener, oLifeCycle, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_SET_CURPET, PET_ENTER_BATTLE, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_SET_CURPET, PET_LEAVE_BATTLE, 8, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckVictimFightType(oListener, oEventCB, WARRIOR_MONSTER):
        cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFromPointPerform(oListener, oEventCB, 13509, 0, 0) and cl_evcon.CheckTargetHasMark(oListener, oEventCB, 'SeasonTask1039', 0) == 0:
            cl_evact.EventSetTargetMark(oListener, oEventCB, 'SeasonTask1039', None)
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.CheckVictimFightType(oListener, oEventCB, WARRIOR_MONSTER):
        cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetHasMark(oListener, oEventCB, 'SeasonTask1039', 0) == 0:
            cl_evact.EventSetTargetMark(oListener, oEventCB, 'SeasonTask1039', None)
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction2(oEventCB, oListener):
    if cl_evcon.CheckVictimFightType(oListener, oEventCB, WARRIOR_MONSTER):
        cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetHasMark(oListener, oEventCB, 'SeasonTask1039', 0) == 0:
            cl_evact.EventSetTargetMark(oListener, oEventCB, 'SeasonTask1039', None)
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction3(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFromPointPerform(oListener, oEventCB, 13509, 0, 0) and cl_evcon.CheckTargetHasMark(oListener, oEventCB, 'SeasonTask1039', 0) == 0:
        cl_evact.EventSetTargetMark(oListener, oEventCB, 'SeasonTask1039', None)
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction4(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasMark(oListener, oEventCB, 'SeasonTask1039', 0) == 0:
        cl_evact.EventSetTargetMark(oListener, oEventCB, 'SeasonTask1039', None)
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction5(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasMark(oListener, oEventCB, 'SeasonTask1039', 0) == 0:
        cl_evact.EventSetTargetMark(oListener, oEventCB, 'SeasonTask1039', None)
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction6(oEventCB, oListener):
    cl_evact.EventSetTargetMark(oListener, oEventCB, 'SeasonTask1039', None)
    cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction7(oEventCB, oListener):
    cl_action.CommonListenCurPetMsgCallBack(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_EXECUTE, -1, 2)


def DoCallBackAction8(oEventCB, oListener):
    cl_action.CommonDoneCurPetEvent(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_EXECUTE, -1)


class CSeasonTask(CCustom):
    m_SID = 1039
    m_TargetValue = 500
    m_TaskValue = 1000
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

