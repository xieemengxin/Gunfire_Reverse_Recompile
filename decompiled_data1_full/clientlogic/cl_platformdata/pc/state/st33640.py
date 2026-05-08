# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33640.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33640.pyc
# Source Generated with Decompyle++
# File: st33640.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckCurLevel(oTarget, oEventCB.GetCBLifeCycle(), 1301003):
        cl_evact.StateCBChangeSourceWeaponAttr(oTarget, oEventCB, 'AttDis', 0, 15000)
        cl_evact.StateCBChangeSourceWeaponAttr(oTarget, oEventCB, 'BulletSpeed', 0, 15000)
    else:
        cl_evact.StateCBChangeSourceWeaponAttr(oTarget, oEventCB, 'AttDis', 0, 0)
        cl_evact.StateCBChangeSourceWeaponAttr(oTarget, oEventCB, 'BulletSpeed', 0, 0)


class CState(cl_state.CState):
    m_SID = 33640
    m_Name = '#NT#火焰狂龙'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

