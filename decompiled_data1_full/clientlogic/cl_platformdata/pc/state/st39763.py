# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39763.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39763.pyc
# Source Generated with Decompyle++
# File: st39763.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_FILLBULLET, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREREMOVEWEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 2, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveState(oTarget, oLifeCycle, 33562)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBClearWeaponForceAttr(oTarget, oEventCB, 'MaxBullet')


def CallBack2(oEventCB, oTarget):
    cl_action.CommonSetWeaponForceAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MaxBullet', (lambda *a: max(1, Func404(*a))), 0, 0, 998)
    cl_evact.StateCBAddSelfState(oTarget, oEventCB, 33562, 0, { }, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 39763
    m_Name = '#NT#S7爆射'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        1: CallBack1,
        2: CallBack2 }

