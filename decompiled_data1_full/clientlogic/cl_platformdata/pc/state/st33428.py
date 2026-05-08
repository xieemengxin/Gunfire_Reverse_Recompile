# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33428.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33428.pyc
# Source Generated with Decompyle++
# File: st33428.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction33428 as CustomAction
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func619

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 21, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 11, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, -1, None)
    else:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack1(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB.GetCBLifeCycle(), { })


def CallBack11(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func619(*a, **{
'sAttr': 'Count' })))


def CallBack21(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33428
    m_Name = '#NT#损余奉缺桃/璃/小玖持续释放Q技能'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 4
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
        'delay': 20,
        'firsttime': 20 }
    m_CBFuncAction = {
        1: CallBack1,
        11: CallBack11,
        21: CallBack21 }

