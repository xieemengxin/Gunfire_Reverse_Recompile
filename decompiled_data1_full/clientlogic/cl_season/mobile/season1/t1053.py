# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/mobile/season1/t1053.pyc
# RelativePath: clientlogic/cl_season/mobile/season1/t1053.pyc
# Source Generated with Decompyle++
# File: t1053.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL, LEVEL_TYPE_BOSS, OBJ_VICTIM
from cl_newformula import Func598
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from branch import *
from ...mobject import CSeasonTask as CCustom

def RewardAction(oTarget, sReason):
    action.SeasonTaskRewardGSCash(oTarget, sReason, 100)


def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckOpenElement(oListener, oLifeCycle, {
        'EndlessElement': 1 }):
        cl_action.CommonListenWarMgrMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckLevelType(oListener, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.CommonListenAllHeroMsgCallBack(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0)
    else:
        cl_action.CommonClearListenAllHeroMsgCallBack(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL)


def DoCallBackAction1(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetPointBaseMonsters(oListener, oEventCB, {
        3902: 1,
        3904: 1 }) and cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 's1053luohou' }))) == 0:
        cl_evact.EventCBSetSavedData(oListener, oEventCB, 's1053luohou', 1, 0)
    if cl_evcon.CheckTargetPointBaseMonsters(oListener, oEventCB, {
        3925: 1,
        3924: 1 }) and cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 's1053yaowan' }))) == 0:
        cl_evact.EventCBSetSavedData(oListener, oEventCB, 's1053yaowan', 1, 0)
    if cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 's1053luohou' }))) and cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 's1053yaowan' }))):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1053
    m_TargetValue = 1
    m_TaskValue = 1
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

