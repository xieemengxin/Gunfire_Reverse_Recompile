# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39738.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39738.pyc
# Source Generated with Decompyle++
# File: st39738.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func369, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'StateCount' })))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckSrcDamType(oTarget, oEventCB, DAM_TYPE_WEAPON) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st39738', 0) == 0:
        if not cl_evcon.CheckEventWeapon(oTarget, oEventCB, {
            1415: 0 }):
            cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'st39738', 1, 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 2005, {
            'Radius': (lambda *a: Func429(*a, **{
'sArg': 'Radius' })),
            'Att': (lambda *a: Func369(*a) * Func429(*a, **{
'sArg': 'DamRatio' }) // 100) }, 0)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, 0)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) <= 0:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 39738
    m_Name = '武器-眩光爆破'
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
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

