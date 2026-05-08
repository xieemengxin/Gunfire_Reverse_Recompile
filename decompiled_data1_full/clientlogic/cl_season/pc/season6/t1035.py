# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season6/t1035.pyc
# RelativePath: clientlogic/cl_season/pc/season6/t1035.pyc
# Source Generated with Decompyle++
# File: t1035.pyc (Python 3.6)

from cl_commondefines import DICE_SUBMSG_ADD, SEASONSUBTASK_TYPE_ADD, SEASONTASK_EXTINFO_TYPE_DICEPOINT
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_AFTER_CONSETDICEPOINT, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DICECHANGE, DICE_SUBMSG_ADD, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_DICEPOINT, 0, 1, SEASONSUBTASK_TYPE_ADD, 1)


class CSeasonTask(CCustom):
    m_SID = 1035
    m_TargetValue = 12
    m_TaskValue = 1000
    m_ShowTotalValue = 0
    m_ShowAccuracy = 12
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 1
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = [
        SEASONTASK_EXTINFO_TYPE_DICEPOINT]
    m_SubTaskInfo = {
        SEASONTASK_EXTINFO_TYPE_DICEPOINT: {
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 1,
            8: 1,
            9: 1,
            10: 1,
            11: 1,
            12: 1,
            13: 1,
            14: 1,
            15: 1,
            16: 1,
            17: 1,
            18: 1 } }

