# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33682.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33682.pyc
# Source Generated with Decompyle++
# File: st33682.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_THROW, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from math import ceil
from cl_newformula import Func343

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if not cl_condition.StateGetSelfCount(oTarget, oLifeCycle):
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromThrowPerform(oTarget, oEventCB, None):
        cl_evact.PassiveExtBulletUse(oTarget, oEventCB, (lambda *a: ceil(Func343(*a, **{
'sid': 4508 }) * cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) / 100)))


class CState(cl_state.CState):
    m_SID = 33682
    m_Name = '破空'
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

