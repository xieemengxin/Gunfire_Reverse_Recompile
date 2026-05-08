# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season5/t1020.pyc
# RelativePath: clientlogic/cl_season/pc/season5/t1020.pyc
# Source Generated with Decompyle++
# File: t1020.pyc (Python 3.6)

from cl_commondefines import WAND_SUBMSG_FINISHCONDITION, WAND_SUBMSG_WANDCDEND
from cl_newformula import Func774
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_FINISHCONDITION, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_WANDCDEND, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_condition.CommonCheckCurWandIsInCD(oListener, oEventCB.GetCBLifeCycle()):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_condition.CheckSceneFightMonster(oListener, oEventCB.GetCBLifeCycle()) and cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func774(*a, **{
'iCompSID': 1019 }))):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1020
    m_TargetValue = 1000
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

