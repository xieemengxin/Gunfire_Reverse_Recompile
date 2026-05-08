# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1149.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1149.pyc
# Source Generated with Decompyle++
# File: st1149.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_FILLBULLET, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func505, Func506, Func511

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'Att', 0, (lambda *a: (Func511(*a) / Func505(*a)) * 10000))
    cl_action.StateChangeSourceWeaponForceAttr(oTarget, oLifeCycle, 'MaxBullet', (lambda *a: min(Func511(*a), Func506(*a)) + Func506(*a)))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        if cl_evcon.CheckStateSameItemSource(oTarget, oEventCB, 1148):
            cl_evact.EventCBDoEnableFunc(oTarget, oEventCB)
        else:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1149
    m_Name = '#NT#铭刻4859换弹重置'
    m_DieRemove = 1
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

