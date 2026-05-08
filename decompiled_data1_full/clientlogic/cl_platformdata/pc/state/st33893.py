# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33893.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33893.pyc
# Source Generated with Decompyle++
# File: st33893.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, OBJ_SELF, OBJ_VICTIM, PF_SUBMSG_CAREERPF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func598

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0)
    cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 3)
    cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_CAREERPF, 3)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 7153, 1, 0):
        cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, 'ScanNum', 1, 1)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func598(*a, **{
'sKey': '217StoreDamage' })), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP | DAM_USE_SHIELD | DAM_USE_ARMOR | DAM_USE_ALL, 1, -1, 0, 1, 0, 0, 1, 1, 0, 0, None)


def CallBack1(oEventCB, oTarget):
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func598(*a, **{
'sKey': '217StoreDamage' }) // 100) })


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'ScanNum', 1) > 0:
        if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'ScanNum', 1) < 3:
            cl_evact.EventCBSetSavedData(oTarget, oEventCB, '217StoreDamage', (lambda *a: Func598(*a, **{
'sKey': '217StoreDamage' }) * 3 // 10), 1)
        else:
            cl_evact.EventCBSetSavedData(oTarget, oEventCB, '217StoreDamage', 0, 1)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 7153, 1, 0) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 7152, 1, 0):
        if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'ScanNum', 1) > 0:
            if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'ScanNum', 1) < 3:
                cl_evact.EventCBSetSavedData(oTarget, oEventCB, '217StoreDamage', (lambda *a: Func598(*a, **{
'sKey': '217StoreDamage' }) * 3 // 10), 1)
            else:
                cl_evact.EventCBSetSavedData(oTarget, oEventCB, '217StoreDamage', 0, 1)
        cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'ScanNum', 0, 1)
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': (lambda *a: Func598(*a, **{
'sKey': '217StoreDamage' }) // 100) })


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


class CState(cl_state.CState):
    m_SID = 33893
    m_Name = '蓄能弹夹'
    m_IsShow = 1
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

