# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33171.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33171.pyc
# Source Generated with Decompyle++
# File: st33171.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CURE_TYPE_SCENE, DAM_USE_HP, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALCURE, -1, 1, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33172, 0, { }, 0)


def CallBack1(oEventCB, oTarget):
    if oTarget.HP() < oTarget.QueryAttr('HPMax'):
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1207, 0, { }, 0)
    else:
        cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 1207, 0)


def CallBack2(oEventCB, oTarget):
    if oTarget.HP() < oTarget.QueryAttr('HPMax'):
        cl_evact.EventGetAllMonsterByTargetScene(oTarget, oEventCB, 1, 1, 1)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 9 / 100), CURE_TYPE_SCENE | DAM_USE_HP, 1, 1, 0)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1230, 50, 1, { }, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33171
    m_Name = '#NT#妖化增幅-琉璃花木'
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
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50,
        'firsttime': 50 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

