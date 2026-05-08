# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_newunlockprogress/mobile/u16032.pyc
# RelativePath: clientlogic/cl_newunlockprogress/mobile/u16032.pyc
# Source Generated with Decompyle++
# File: u16032.pyc (Python 3.6)

from cl_commondefines import REWARD_UNLOCK_MODULE, TYPE_RELIFE_RESCUE
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CUnlockProgress as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckRelifeType(oListener, oEventCB, TYPE_RELIFE_RESCUE):
        cl_evact.CBAddUnlockProgress(oListener, oEventCB, 1)


class CUnlockProgress(CCustom):
    m_SID = 16032
    m_TargetValue = 5
    m_RewardType = REWARD_UNLOCK_MODULE
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

