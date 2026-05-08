# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1220.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1220.pyc
# Source Generated with Decompyle++
# File: s1220.pyc (Python 3.6)

from cl_object.logging import AchievementLog
from cl_commondefines import LEVEL_TYPE_BOSS, OBJ_SELF, OBJ_VICTIM, PLAYMODE_ROGUELIKE, PLAY_TYPE_SINGLE, WARRIOR_BOSS
from cl_newformula import Func205, Func598
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 218) and cl_condition.CheckWarPlayMode(oListener, oLifeCycle, PLAYMODE_ROGUELIKE) and cl_condition.CalFormula(oListener, oLifeCycle, (lambda *a: Func205(*a))) >= 3 and cl_condition.CheckWarPlayType(oListener, oLifeCycle, PLAY_TYPE_SINGLE) and cl_condition.CheckHasSavedData(oListener, oLifeCycle, 'Achi1220_Fail') == 0:
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)
        cl_action.AchieveListenWarMgrMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 3)
        cl_action.CommonDirectEventCBFunc(oListener, oLifeCycle, 4, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckLevelType(oListener, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.CommonListenMsgCallBack(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PFNODEKILL, -1, 1, 0, 0)
        cl_action.CommonSetSavedData(oListener, oEventCB.GetCBLifeCycle(), 'a1220KillBoos', 0)


def DoCallBackAction1(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckVictimFightType(oListener, oEventCB, WARRIOR_BOSS) and cl_evcon.CheckInPointPerform(oListener, oEventCB, {
        1324: 1,
        1328: 1 }, 1, 0) and cl_evcon.CheckTargetPointBaseMonster(oListener, oEventCB, 3926) == 0:
        if cl_evcon.CheckTargetPointBaseMonster(oListener, oEventCB, 3921) or cl_evcon.CheackTargetFightTypeIsRealit(oListener, oEventCB):
            cl_action.CommonAddStateCount(oListener, oEventCB.GetCBLifeCycle(), 33305, 1, 0)
            cl_action.CommonSetSavedData(oListener, oEventCB.GetCBLifeCycle(), 'a1220KillBoos', 1)
            cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_SELF)
            if cl_evcon.GetTargetStateCount(oListener, oEventCB, 33305, 0, 0) >= 4:
                cl_evact.AchieveRewardCheek(oListener, oEventCB, 1018)
                cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


def DoCallBackAction2(oEventCB, oListener):
    if cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 'a1220KillBoos' }))) == 0:
        CustomAction(oListener, oEventCB, { })
        cl_action.CommonSetSavedData(oListener, oEventCB.GetCBLifeCycle(), 'Achi1220_Fail', 1)
        cl_action.CommonRemoveState(oListener, oEventCB.GetCBLifeCycle(), 33305)
        cl_evact.EventCBDoneEvent(oListener, oEventCB, cl_msgcenter.MSG_WAR_ENTERSCENE, -1)


def DoCallBackAction3(oEventCB, oListener):
    if cl_evcon.CheckLevelType(oListener, oEventCB, LEVEL_TYPE_BOSS):
        cl_evact.EventCBDoneEvent(oListener, oEventCB, cl_msgcenter.MSG_WAR_PFNODEKILL, -1)
        if cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 'a1220KillBoos' }))) == 0:
            CustomAction(oListener, oEventCB, { })
            cl_action.CommonSetSavedData(oListener, oEventCB.GetCBLifeCycle(), 'Achi1220_Fail', 1)
            cl_action.CommonRemoveState(oListener, oEventCB.GetCBLifeCycle(), 33305)
            cl_evact.EventCBDoneEvent(oListener, oEventCB, cl_msgcenter.MSG_WAR_ENTERSCENE, -1)


def DoCallBackAction4(oEventCB, oListener):
    cl_evact.AchieveCBAddState(oListener, oEventCB, 33305, 0, { }, 1)


def DoCallBackAction5(oEventCB, oListener):
    if cl_evcon.GetTargetStateCount(oListener, oEventCB, 33305, 0, 0) >= 4:
        cl_evact.AchieveRewardCheek(oListener, oEventCB, 1018)
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1220
    m_Name = '凛冽打击'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }


def CustomAction(oListener, oEventCB, dInfo):
    oGame = oListener.m_Game
    if not oGame:
        return None
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return None
    AchievementLog.Debug('%d playerid:%d level:%d a1220fail' % (oGame.m_ID, oListener.m_PlayerID, oScene.m_Level))

