# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season7/t1025.pyc
# RelativePath: clientlogic/cl_season/pc/season7/t1025.pyc
# Source Generated with Decompyle++
# File: t1025.pyc (Python 3.6)

from cl_commondefines import COST_BAGBULLET_WEAPON
from cl_newformula import Func208, Func215
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckEventWeaponBulletType(oListener, oEventCB, 4502) or cl_evcon.CheckEventWeaponBulletType(oListener, oEventCB, 4503) or cl_evcon.CheckEventWeaponBulletType(oListener, oEventCB, 4504):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, (lambda *a: Func208(*a)))


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.CheckCostBulletType(oListener, oEventCB, 4502) or cl_evcon.CheckCostBulletType(oListener, oEventCB, 4503) or cl_evcon.CheckCostBulletType(oListener, oEventCB, 4504):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, (lambda *a: Func215(*a)))


class CSeasonTask(CCustom):
    m_SID = 1025
    m_TargetValue = 20000
    m_TaskValue = 500
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

