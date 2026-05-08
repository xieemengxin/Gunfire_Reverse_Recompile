# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33620.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33620.pyc
# Source Generated with Decompyle++
# File: st33620.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CREATE_SEED, DAM_TYPE_PERFORM, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func518

def StateActAction(oTarget, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('StatusEffect') == 1:
        cl_action.CommonAddStateCount(oTarget, oLifeCycle, 33620, (lambda *a: Func518(*a, **{
'sAttr': 'GradenerCount' })), 600)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    if oLifeCycle.m_Owner.GetArgValue('StatusEffect') == 2:
        cl_action.CommonAddStateCount(oTarget, oLifeCycle, 33620, (lambda *a: Func518(*a, **{
'sAttr': 'GradenerCount' })), 600)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    if oLifeCycle.m_Owner.GetArgValue('StatusEffect') == 3:
        cl_action.CommonAddStateCount(oTarget, oLifeCycle, 33620, (lambda *a: Func518(*a, **{
'sAttr': 'GradenerCount' })), 800)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_SEED, CREATE_SEED, 7, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'GradenerCount', (lambda *a: Func404(*a)))


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckSrcDamType(oTarget, oEventCB, DAM_TYPE_WEAPON):
        cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33620, 1, 600)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 50), 0, 0, '')
    elif cl_evcon.CheckSrcDamType(oTarget, oEventCB, DAM_TYPE_PERFORM):
        cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33620, 3, 600)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 50), 0, 0, '')


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckSrcDamType(oTarget, oEventCB, DAM_TYPE_WEAPON):
        cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33620, 2, 600)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 50), 0, 0, '')
    elif cl_evcon.CheckSrcDamType(oTarget, oEventCB, DAM_TYPE_PERFORM):
        cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33620, 6, 600)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 50), 0, 0, '')


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckSrcDamType(oTarget, oEventCB, DAM_TYPE_WEAPON):
        cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33620, 2, 800)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 50), 0, 0, '')
    elif cl_evcon.CheckSrcDamType(oTarget, oEventCB, DAM_TYPE_PERFORM):
        cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33620, 6, 800)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 50), 0, 0, '')


def CallBack7(oEventCB, oTarget):
    cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33620, 10, 800)


class CState(cl_state.CState):
    m_SID = 33620
    m_Name = '#NT#园丁天赋W4'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3,
        5: CallBack5,
        7: CallBack7 }

