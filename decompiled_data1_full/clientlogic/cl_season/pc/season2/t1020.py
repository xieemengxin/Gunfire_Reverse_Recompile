# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season2/t1020.pyc
# RelativePath: clientlogic/cl_season/pc/season2/t1020.pyc
# Source Generated with Decompyle++
# File: t1020.pyc (Python 3.6)

from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from branch import *
from ...mobject import CSeasonTask as CCustom

def RewardAction(oTarget, sReason):
    action.SeasonTaskRewardGSCash(oTarget, sReason, 150)


def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADDWEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_RECAST_INSCRIPTION, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_UPGRADE_INSCRIPTION, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_APPEND_INSCRIPTION, -1, 0, 0, 0)
    if cl_condition.CheckHero(oListener, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_condition.GetWeaponInscriptionNumByTypeAndLevel(oListener, oEventCB.GetCBLifeCycle(), INSCRIPTION_TYPE_EXCLUSIVE, cl_evcon.CheckTalentLevel(oListener, oEventCB, 3014)) >= 5:
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.EventCBCheckTalent(oListener, oEventCB, 3014) and cl_condition.GetWeaponInscriptionNumByTypeAndLevel(oListener, oEventCB.GetCBLifeCycle(), INSCRIPTION_TYPE_EXCLUSIVE, cl_evcon.CheckTalentLevel(oListener, oEventCB, 3014)) >= 5:
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1020
    m_TargetValue = 1
    m_TaskValue = 1
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

