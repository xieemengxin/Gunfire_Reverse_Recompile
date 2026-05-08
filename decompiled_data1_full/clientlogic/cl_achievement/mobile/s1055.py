# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1055.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1055.pyc
# Source Generated with Decompyle++
# File: s1055.pyc (Python 3.6)

from cl_commondefines import GAMETYPE_MACHINE, NWARRIOR_NPC_ITEMBOX, NWARRIOR_NPC_MAGICBOX, NWARRIOR_NPC_PASSBOX, NWARRIOR_NPC_ROOMCHALLENGE
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 1, 0, 0)
    cl_action.AchieveListenGlobalMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_NPCINTERACT, -1, 2)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckLevelGameType(oListener, oEventCB, GAMETYPE_MACHINE):
        cl_evact.AchieveCBAddWarStat(oListener, oEventCB, 1)
    else:
        cl_evact.AchieveCBResetWarStat(oListener, oEventCB)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1) and cl_evcon.GetSingleDamageNum(oListener, oEventCB) > 0 and cl_evcon.CheckDamFromSelf(oListener, oEventCB, None) == False:
        cl_evact.AchieveCBResetWarStat(oListener, oEventCB)


def DoCallBackAction2(oEventCB, oListener):
    if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1) and cl_evcon.CheckSceneNPCInteracted(oListener, oEventCB, NWARRIOR_NPC_ITEMBOX) and cl_evcon.CheckSceneNPCInteracted(oListener, oEventCB, NWARRIOR_NPC_PASSBOX) and cl_evcon.CheckSceneNPCInteracted(oListener, oEventCB, NWARRIOR_NPC_ROOMCHALLENGE) and cl_evcon.CheckSceneNPCInteracted(oListener, oEventCB, NWARRIOR_NPC_MAGICBOX):
        if cl_evcon.CheckNPCType(oListener, oEventCB, NWARRIOR_NPC_ITEMBOX) or cl_evcon.CheckNPCType(oListener, oEventCB, NWARRIOR_NPC_PASSBOX) or cl_evcon.CheckNPCType(oListener, oEventCB, NWARRIOR_NPC_MAGICBOX) or cl_evcon.CheckNPCType(oListener, oEventCB, NWARRIOR_NPC_ROOMCHALLENGE):
            cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1055
    m_Name = '凌波微步'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }

