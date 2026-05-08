# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1215.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1215.pyc
# Source Generated with Decompyle++
# File: s1215.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, PLAYMODE_ROGUELIKE, PLAY_TYPE_SINGLE
from cl_newformula import Func205
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 217) and cl_condition.CheckWarPlayMode(oListener, oLifeCycle, PLAYMODE_ROGUELIKE) and cl_condition.CalFormula(oListener, oLifeCycle, (lambda *a: Func205(*a))) >= 3 and cl_condition.CheckWarPlayType(oListener, oLifeCycle, PLAY_TYPE_SINGLE) and cl_condition.CheckHasSavedData(oListener, oLifeCycle, 'Achi1215_Fail') == 0:
        cl_action.CommonListenServantMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DIEDIST, -1, 0)
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
        cl_action.CommonDirectEventCBFunc(oListener, oLifeCycle, 2, 0, None)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.EventCBCheckAtiveExplosion(oListener, oEventCB) == 0:
        cl_action.CommonRemoveOwnerState(oListener, oEventCB.GetCBLifeCycle(), 1792, 0)
        cl_action.CommonDoneServantAttention(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DIEDIST, -1)
        cl_action.CommonDoneEvent(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL)
        cl_action.CommonSetSavedData(oListener, oEventCB.GetCBLifeCycle(), 'Achi1215_Fail', 1)


def DoCallBackAction1(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetPointBaseMonster(oListener, oEventCB, 3924) or cl_evcon.CheckTargetPointBaseMonster(oListener, oEventCB, 3925) or cl_evcon.CheckTargetPointBaseMonster(oListener, oEventCB, 3902) or cl_evcon.CheckTargetPointBaseMonster(oListener, oEventCB, 3904):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
        cl_evact.AchieveRewardCheek(oListener, oEventCB, 1014)


def DoCallBackAction2(oEventCB, oListener):
    if not cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1):
        cl_evact.AchieveCBAddState(oListener, oEventCB, 1792, 0, { }, None)


class CAchieveStat(CCustom):
    m_SID = 1215
    m_Name = '未尝一败'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }

