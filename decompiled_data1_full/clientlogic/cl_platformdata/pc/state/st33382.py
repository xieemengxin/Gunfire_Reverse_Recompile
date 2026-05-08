# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33382.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33382.pyc
# Source Generated with Decompyle++
# File: st33382.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, LEVEL_TYPE_BOSS, NORMAL_DAMAGE, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func223, Func374, Func437, Func744

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 5, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 33503, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CDComplete', 0)
    cl_evact.DelayTriggerGroup(oTarget, oEventCB, 6, 1, 300, 0, 1, { })
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func374(*a) * 0.08), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 1, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'IsDam'):
        if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 33382):
            cl_evact.StateCBSelfAttackerUsePerform(oTarget, oEventCB, 8604, {
                'Att': (lambda *a: cl_evact.EventCBGetTotalHPChangeByCureRatio(oTarget, oEventCB, 1) * 40 + Func223(*a) * 25000 + 100000),
                'Radius': 12 }, 0)
        elif cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()) == 0:
            cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: 50 / (10000 + Func744(*a, **{
'iType': 2 })) / 10000))
            cl_evact.StateCBSelfAttackerUsePerform(oTarget, oEventCB, 8604, {
                'Att': (lambda *a: (cl_evact.EventCBGetTotalHPChangeByCureRatio(oTarget, oEventCB, 1) + Func437(*a, **{
'sKey': 'StoreDamage' })) * 40 + Func223(*a) * 25000 + 100000),
                'Radius': 12 }, 0)
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'StoreDamage', 0)
        else:
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, cl_evact.EventCBGetTotalHPChangeByCureRatio(oTarget, oEventCB, 1), 'StoreDamage')


def CallBack4(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 33382) and cl_evcon.CheckDamFromSelf(oTarget, oEventCB, 0):
        cl_evact.EventCBAddMessageInfo(oTarget, oEventCB, 'HaltShieldRecovry', 0)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_BOSS):
        cl_evact.StateCBAddSelfState(oTarget, oEventCB, 33503, 0, {
            'Radius': 36,
            'StatusEffect': 33382 }, 0, 0, 0)
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 6, 1, 300, 0, 1, { })
    else:
        cl_evact.StateCBAddSelfState(oTarget, oEventCB, 33503, 0, {
            'Radius': 12,
            'StatusEffect': 33382 }, 0, 0, 0)
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 6, 1, 300, 0, 1, { })


def CallBack6(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 33503, 0, 0) > 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CDComplete', 0)
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 6, 1, 300, 0, 1, { })
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func374(*a) * 0.08), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 1, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)
    else:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CDComplete', 1)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33382
    m_Name = '电闪雷鸣二级(套装)'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6 }

