# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7103.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7103.pyc
# Source Generated with Decompyle++
# File: st7103.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_SHIELD, MONSTER_PART_LEFTGUN, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func403

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 0.01 * cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' }) * 5 / 100 + 1)):
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.StateAddState(oTarget, oLifeCycle, 7105, 500, { }, None)
    if not cl_condition.HasState(oTarget, oLifeCycle, 7104):
        cl_action.CommonHaltPointPerform(oTarget, oLifeCycle, 32031)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHitPart(oTarget, oEventCB, MONSTER_PART_LEFTGUN):
        cl_evact.StateAddSelfCountByPredictPartDamage(oTarget, oEventCB, DAM_TYPE_SHIELD, 1)


class CState(cl_state.CState):
    m_SID = 7103
    m_Name = '#NT#精英火箭炮兵-左炮筒-可用'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 60000
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

