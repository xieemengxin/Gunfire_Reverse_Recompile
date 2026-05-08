# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33248.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33248.pyc
# Source Generated with Decompyle++
# File: st33248.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oTarget, oLifeCycle, 0, 0, 0, 1)
    cl_action.CommonChangeOwnerBaseDamRatio(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, (lambda *a: Func404(*a)), 0, 1)
    cl_action.CommonChangeOwnerBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a)), 0, 0)


class CState(cl_state.CState):
    m_SID = 33248
    m_Name = '#NT#灵佑13602'
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
    m_Action = (None, StateRemoveAction)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

