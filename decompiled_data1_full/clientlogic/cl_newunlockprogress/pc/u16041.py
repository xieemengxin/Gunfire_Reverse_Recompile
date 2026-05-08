# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_newunlockprogress/pc/u16041.pyc
# RelativePath: clientlogic/cl_newunlockprogress/pc/u16041.pyc
# Source Generated with Decompyle++
# File: u16041.pyc (Python 3.6)

from cl_commondefines import DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, REWARD_UNLOCK_MODULE
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CUnlockProgress as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckTotalCureSource(oListener, oEventCB, 1069, DAM_USE_SHIELD) or cl_evcon.CheckTotalCureSource(oListener, oEventCB, 1069, DAM_USE_ARMOR) or cl_evcon.CheckTotalCureSource(oListener, oEventCB, 1069, DAM_USE_HP):
        cl_evact.CBAddUnlockProgress(oListener, oEventCB, 1)


class CUnlockProgress(CCustom):
    m_SID = 16041
    m_TargetValue = 100
    m_RewardType = REWARD_UNLOCK_MODULE
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

