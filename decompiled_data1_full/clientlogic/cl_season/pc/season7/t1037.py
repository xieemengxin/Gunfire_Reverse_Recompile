# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season7/t1037.pyc
# RelativePath: clientlogic/cl_season/pc/season7/t1037.pyc
# Source Generated with Decompyle++
# File: t1037.pyc (Python 3.6)

from cl_commondefines import S7MODULE_ADD, SEASONTASK_EXTINFO_TYPE_S7MODULE
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, S7MODULE_ADD, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.CBAddWarSeasonTaskValueByDifferentID(oListener, oEventCB, 'ModuleSID', 1)


class CSeasonTask(CCustom):
    m_SID = 1037
    m_TargetValue = 20
    m_TaskValue = 1000
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = [
        SEASONTASK_EXTINFO_TYPE_S7MODULE]
    m_SubTaskInfo = { }

