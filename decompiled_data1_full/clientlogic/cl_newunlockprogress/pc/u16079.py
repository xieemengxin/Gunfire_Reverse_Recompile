# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_newunlockprogress/pc/u16079.pyc
# RelativePath: clientlogic/cl_newunlockprogress/pc/u16079.pyc
# Source Generated with Decompyle++
# File: u16079.pyc (Python 3.6)

from cl_commondefines import LEVEL_TYPE_HIDE, VIRTUAL_ITEM_EMOTION
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CUnlockProgress as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckLevelType(oListener, oEventCB, LEVEL_TYPE_HIDE):
        cl_evact.CBAddUnlockProgress(oListener, oEventCB, 1)


class CUnlockProgress(CCustom):
    m_SID = 16079
    m_TargetValue = 1
    m_RewardType = VIRTUAL_ITEM_EMOTION
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

