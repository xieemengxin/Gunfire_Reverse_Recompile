# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season4/t1032.pyc
# RelativePath: clientlogic/cl_season/pc/season4/t1032.pyc
# Source Generated with Decompyle++
# File: t1032.pyc (Python 3.6)

from cl_commondefines import BENE_SOURCE_LAYER, SEASONSUBTASK_TYPE_ADD, SEASONTASK_EXTINFO_TYPE_BENE, SETTLE_FINISHWAR
from cl_newformula import Func201, Func202, Func598, Func724
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADDBENED, -1, 0, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 1)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERSETTLE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckInPointBene(oListener, oEventCB, {
        13725: 1,
        13726: 1,
        13727: 1 }) and cl_evcon.EventCBCheckTargetBeneSource(oListener, oEventCB, BENE_SOURCE_LAYER):
        cl_evact.EventCBSetSavedData(oListener, oEventCB, 'season4_t1032', (lambda *a: Func724(*a)), 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.GetFormula(oListener, oEventCB, (lambda *a: Func201(*a))) >= 2 or cl_evcon.GetFormula(oListener, oEventCB, (lambda *a: Func202(*a))) >= 1:
        cl_action.CommonDoneEvent(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADDBENED, -1)


def DoCallBackAction2(oEventCB, oListener):
    if cl_evcon.CheckSettleType(oListener, oEventCB, SETTLE_FINISHWAR) and cl_condition.CheckHasSavedData(oListener, oEventCB.GetCBLifeCycle(), 'season4_t1032'):
        cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_BENE, (lambda *a: Func598(*a, **{
'sKey': 'season4_t1032' })), 1, SEASONSUBTASK_TYPE_ADD, 0)


class CSeasonTask(CCustom):
    m_SID = 1032
    m_TargetValue = 3
    m_TaskValue = 1000
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_WarExtInfoType = [
        SEASONTASK_EXTINFO_TYPE_BENE]
    m_SubTaskInfo = {
        SEASONTASK_EXTINFO_TYPE_BENE: {
            13725: 1,
            13726: 1,
            13727: 1 } }

