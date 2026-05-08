# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39674.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39674.pyc
# Source Generated with Decompyle++
# File: st39674.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, BOX_DOUBLE_DAMAGE, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_SELF, OBJ_VICTIM, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func529, Func604, Func717

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxCount'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': (lambda *a: oLifeCycle.m_Owner.GetArgValue('DamRatio') * Func404(*a)) })
    if oLifeCycle.m_Owner.GetArgValue('AbsorbThress'):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('EnableAbsorb'):
        cl_action.CommonAddPerformArgsValue(oTarget, oLifeCycle, 1998, 'EnableAbsorb', -1, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckCostBulletType(oTarget, oEventCB, 4508):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func529(*a)), (lambda *a: Func429(*a, **{
'sArg': 'Duration' })))


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1998: 1 }, 1, 0):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func604(*a, **{
'sKey': 'TriggerFinalDam' }) * cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) * Func717(*a, **{
'sArg': 'DamRatio' }) / 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, BOX_DOUBLE_DAMAGE, 0, None)


def CallBack2(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AbsorbThress') or oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('EnableAbsorb') == 0:
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'EnableAbsorb', 1)
        cl_action.CommonAddPerformArgsValue(oTarget, oEventCB.GetCBLifeCycle(), 1998, 'EnableAbsorb', 1, 0)
    elif oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('EnableAbsorb') == 1:
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'EnableAbsorb', 0)
        cl_action.CommonAddPerformArgsValue(oTarget, oEventCB.GetCBLifeCycle(), 1998, 'EnableAbsorb', -1, 0)


class CState(cl_state.CState):
    m_SID = 39674
    m_Name = '莲花-真灵绽放'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

