# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32265.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32265.pyc
# Source Generated with Decompyle++
# File: st32265.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func410, Func425

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromWeapon(oTarget, oEventCB, None):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventGetAllMonsterByStateMark(oTarget, oEventCB, 32264, 'dMonster')
        cl_evact.StateCBRemoveState(oTarget, oEventCB, 32264)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func425(*a) * 0.3 * Func410(*a, **{
'sid': 32266 }) + 0.1 * Func425(*a)), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, None, None, None, None, None, None, None, None)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.StateCBRemoveState(oTarget, oEventCB, 32264)


class CState(cl_state.CState):
    m_SID = 32265
    m_Name = '#NT#静电链接(玩家)'
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

