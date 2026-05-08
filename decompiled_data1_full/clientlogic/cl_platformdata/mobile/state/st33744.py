# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33744.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33744.pyc
# Source Generated with Decompyle++
# File: st33744.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE, TYPE_RELIFE_GSCASH
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTRELIFES, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSetRelifeAttr(oTarget, oLifeCycle, TYPE_RELIFE_GSCASH, 0, (lambda *a: Func404(*a)), 3, { }, 0, None)


def CallBack0(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
        'iDiceSID': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('iDiceSID') })


class CState(cl_state.CState):
    m_SID = 33744
    m_Name = '近战大师'
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

