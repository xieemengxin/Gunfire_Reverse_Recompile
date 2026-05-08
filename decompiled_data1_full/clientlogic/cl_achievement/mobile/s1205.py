# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1205.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1205.pyc
# Source Generated with Decompyle++
# File: s1205.pyc (Python 3.6)

from cl_object.logging import CheekLog
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, PLAYMODE_ROGUELIKE, PLAY_TYPE_SINGLE, WARRIOR_BOSS
from cl_newformula import Func205
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 215) and cl_condition.CheckWarPlayMode(oListener, oLifeCycle, PLAYMODE_ROGUELIKE) and cl_condition.CheckWarPlayType(oListener, oLifeCycle, PLAY_TYPE_SINGLE) and cl_condition.CalFormula(oListener, oLifeCycle, (lambda *a: Func205(*a))) >= 3:
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oListener, oEventCB, WARRIOR_BOSS) and cl_evcon.CheckFromPointPerform(oListener, oEventCB, 1423, 1, -1) and not cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1):
        cl_evact.AchieveCBAddWarStat(oListener, oEventCB, 1)
        CustomCBAction(oListener, oEventCB, { })


def DoCallBackAction1(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oListener, oEventCB, WARRIOR_BOSS) and not cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1):
        cl_evact.AchieveCBAddWarStat(oListener, oEventCB, 1)
        CustomCBAction(oListener, oEventCB, { })


def DoCallBackAction2(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oListener, oEventCB, WARRIOR_BOSS) and cl_evcon.CheackTargetFightTypeIsRealit(oListener, oEventCB):
        if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1):
            cl_evact.AchieveCBResetWarStat(oListener, oEventCB)
        else:
            cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
            cl_evact.AchieveRewardCheek(oListener, oEventCB, 1010)


def DoCallBackAction3(oEventCB, oListener):
    if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1):
        cl_evact.AchieveCBResetWarStat(oListener, oEventCB)
    else:
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
        cl_evact.AchieveRewardCheek(oListener, oEventCB, 1010)


class CAchieveStat(CCustom):
    m_SID = 1205
    m_Name = '赤狐传说'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }


def CustomCBAction(oListener, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dTransInfo = oEventCB.GetCBTransInfo()
    oGame = oListener.m_Game
    iSkillSID = 0
    lstTargetSID = []
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iSkillSID = oSkill.m_Base['pfid']
    if 'TargetList' in dTransInfo:
        for iTargetID in dTransInfo['TargetList']:
            oTarget = oGame.GetObject(iTargetID)
            if not oTarget:
                continue
            lstTargetSID.append(oTarget.m_SID)
        
    CheekLog.Info(f'''achievement1205 fail skillSID:{iSkillSID} target{lstTargetSID}''')

