# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33015.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33015.pyc
# Source Generated with Decompyle++
# File: st33015.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('StateCount'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CLIENTACTIVEUSECOUNTCHANGE, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'StatusEffect' }))):
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, (lambda *a: -Func429(*a, **{
'sArg': 'StatusEffect' })), None)
        cl_action.StateAddState(oTarget, oLifeCycle, 33016, 0, { }, None)
        cl_action.CommonAddThrowBagBullet(oTarget, oLifeCycle, 6, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSetPerformArgs(oTarget, oLifeCycle, 50020, 'StateCount6', cl_action.StateGetSelfCount(oTarget, oLifeCycle), None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 12019, 0, 0):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


class CState(cl_state.CState):
    m_SID = 33015
    m_Name = '种豆得瓜'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

