# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_newunlockprogress/pc/u16033.pyc
# RelativePath: clientlogic/cl_newunlockprogress/pc/u16033.pyc
# Source Generated with Decompyle++
# File: u16033.pyc (Python 3.6)

from cl_commondefines import RESCUE_SUBMSG_SUCCESS, REWARD_UNLOCK_MODULE
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CUnlockProgress as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_RESCUE, RESCUE_SUBMSG_SUCCESS, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.CBAddUnlockProgress(oListener, oEventCB, 1)


class CUnlockProgress(CCustom):
    m_SID = 16033
    m_TargetValue = 10
    m_RewardType = REWARD_UNLOCK_MODULE
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

