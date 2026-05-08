# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33807.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33807.pyc
# Source Generated with Decompyle++
# File: st33807.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import COST_BAGBULLET_THROW, JUMPFIGURE_BUYGOODS, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func529

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBAddCash(oTarget, oEventCB, (lambda *a: Func529(*a) * Func404(*a)), 0, JUMPFIGURE_BUYGOODS, 0, 0)


class CState(cl_state.CState):
    m_SID = 33807
    m_Name = '聚灵生财'
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
    m_CBFuncAction = {
        0: CallBack0 }

