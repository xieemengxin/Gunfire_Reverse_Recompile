# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33706.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33706.pyc
# Source Generated with Decompyle++
# File: st33706.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CREATE_PLANT, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func598

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 'CreatePlantNum' })))
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect'):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33707, 0, 1, {
            'Att': (lambda *a: (Func404(*a) // Func429(*a, **{
'sArg': 'StatusEffect' })) * Func429(*a, **{
'sArg': 'Att' })) }, 0, 0, None)


class CState(cl_state.CState):
    m_SID = 33706
    m_Name = '#NT#园丁E灵佑显示'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 1000
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

