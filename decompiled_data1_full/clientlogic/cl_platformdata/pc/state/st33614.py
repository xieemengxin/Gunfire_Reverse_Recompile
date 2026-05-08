# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33614.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33614.pyc
# Source Generated with Decompyle++
# File: st33614.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CREATE_SEED, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func361, Func404, Func429, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_SEED, CREATE_SEED, 0, 0, 0)
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func361(*a, **{
'sid': 3811,
'sArgs': '33614Cnt' })))


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= oLifeCycle.m_Owner.GetArgValue('StatusEffect'):
        cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33614, (lambda *a: Func404(*a) // Func429(*a, **{
'sArg': 'StatusEffect' })), 'TriCnt')
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, (lambda *a: -oLifeCycle.m_Owner.GetArgValue('StatusEffect') * Func437(*a, **{
'sKey': 'TriCnt' })), None)
        cl_action.CommonAddThrowBagBullet(oTarget, oLifeCycle, (lambda *a: Func437(*a, **{
'sKey': 'TriCnt' })), 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSetPerformArgs(oTarget, oLifeCycle, 3811, '33614Cnt', (lambda *a: Func404(*a)), 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)


class CState(cl_state.CState):
    m_SID = 33614
    m_Name = '#NT#园丁Q5'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

