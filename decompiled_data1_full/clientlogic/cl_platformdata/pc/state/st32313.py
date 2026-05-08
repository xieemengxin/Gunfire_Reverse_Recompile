# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32313.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32313.pyc
# Source Generated with Decompyle++
# File: st32313.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_SHIELD, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 27)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if oTarget.Shield() > 0 and cl_evcon.CheckBreakShieldPredictDam(oTarget, oEventCB) and cl_evcon.CheckHasState(oTarget, oEventCB, 32297) == 0:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventChangeDefValue(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }) + 0), DAM_USE_SHIELD, 0)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32297, 12000, 0, { }, 0, None, None)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32296, 200, 0, { }, 0, None, None)
        cl_evact.EventSetLimitDamage(oTarget, oEventCB, 0)
        cl_evact.EventCBHaltFlow(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 32313
    m_Name = '#NT#天赋异禀'
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

