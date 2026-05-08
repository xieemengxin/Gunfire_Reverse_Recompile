# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_newunlockprogress/mobile/u16065.pyc
# RelativePath: clientlogic/cl_newunlockprogress/mobile/u16065.pyc
# Source Generated with Decompyle++
# File: u16065.pyc (Python 3.6)

from cl_commondefines import PF_SUBMSG_THROW, REWARD_UNLOCK_MODULE
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CUnlockProgress as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 213):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckFromPointPerform(oListener, oEventCB, 1427, -1, -1):
        cl_evact.CBAddUnlockProgress(oListener, oEventCB, 1)


class CUnlockProgress(CCustom):
    m_SID = 16065
    m_TargetValue = 100
    m_RewardType = REWARD_UNLOCK_MODULE
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

