# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33401.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33401.pyc
# Source Generated with Decompyle++
# File: st33401.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ACTIVE_SENDMESSAGE, ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, LEVEL_TYPE_BOSS, NORMAL_DAMAGE, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func223, Func374, Func437, Func589, Func744

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, ACTIVE_SENDMESSAGE, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 6, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 6, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 33503, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CDComplete', 0)
    cl_evact.DelayTriggerGroup(oTarget, oEventCB, 7, 1, 300, 0, 1, { })
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func374(*a) * 0.08), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 1, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'IsDam'):
        if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 33401):
            cl_evact.StateCBSelfAttackerUsePerform(oTarget, oEventCB, 8604, {
                'Att': (lambda *a: cl_evact.EventCBGetTotalHPChangeByCureRatio(oTarget, oEventCB, 1) * 40 + Func223(*a) * 25000 + 100000),
                'Radius': 16 }, 0)
        elif cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()) == 0:
            cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: 50 / (10000 + Func744(*a, **{
'iType': 2 })) / 10000))
            cl_evact.StateCBSelfAttackerUsePerform(oTarget, oEventCB, 8604, {
                'Att': (lambda *a: (cl_evact.EventCBGetTotalHPChangeByCureRatio(oTarget, oEventCB, 1) + Func437(*a, **{
'sKey': 'StoreDamage' })) * 40 + Func223(*a) * 25000 + 100000),
                'Radius': 16 }, 0)
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'StoreDamage', 0)
        else:
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, cl_evact.EventCBGetTotalHPChangeByCureRatio(oTarget, oEventCB, 1), 'StoreDamage')


def CallBack4(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 33401) and cl_evcon.CheckDamFromSelf(oTarget, oEventCB, 0):
        cl_evact.EventCBAddMessageInfo(oTarget, oEventCB, 'HaltShieldRecovry', 0)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 8604, 1, 0):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func589(*a) * 2 / 100), CURE_TYPE_PERFORM | DAM_USE_HP | DAM_USE_SHIELD | DAM_USE_ARMOR, 0, 1, None)


def CallBack6(oEventCB, oTarget):
    if cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_BOSS):
        cl_evact.StateCBAddSelfState(oTarget, oEventCB, 33503, 0, {
            'Radius': 48,
            'StatusEffect': 33401 }, 0, 0, 0)
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 7, 1, 300, 0, 1, { })
    else:
        cl_evact.StateCBAddSelfState(oTarget, oEventCB, 33503, 0, {
            'Radius': 16,
            'StatusEffect': 33401 }, 0, 0, 0)
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 7, 1, 300, 0, 1, { })


def CallBack7(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 33503, 0, 0) > 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CDComplete', 0)
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 7, 1, 300, 0, 1, { })
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func374(*a) * 0.08), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 1, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)
    else:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CDComplete', 1)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33401
    m_Name = '电闪雷鸣套装三级效果'
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
        6: CallBack6,
        7: CallBack7 }

