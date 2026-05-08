# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33915.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33915.pyc
# Source Generated with Decompyle++
# File: st33915.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_FRIEND, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonTriggerClientBehavior(oTarget, oLifeCycle, 1515, 2, None, 0)
    cl_action.StateTriggerClientBehavior(oTarget, oLifeCycle, 1516)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 1)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveClientBehavior(oTarget, oLifeCycle, 1515)
    cl_action.CommonRemoveClientBehavior(oTarget, oLifeCycle, 1516)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, (lambda *a: -3000 - Func429(*a, **{
'sArg': 'PF13130_HardEff' })), 0, '')
    if not cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()):
        cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 10)
        cl_evact.EventGetHeroTarget(oTarget, oEventCB, 1, 1, 0, 0)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 2)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 33957, 0, 0, 0, 0):
        cl_evact.EventCBTarget2UsePerform(oTarget, oEventCB, 1945, {
            'StateOwner': cl_evact.EventGetTargeIDtByType(oTarget, oEventCB, OBJ_SELF) })


class CState(cl_state.CState):
    m_SID = 33915
    m_Name = '#NT#雷刹护盾'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_FRIEND
    m_MinCount = 0
    m_MaxCount = 15
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_GameBroadcast = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

